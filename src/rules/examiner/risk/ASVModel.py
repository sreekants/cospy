#!/usr/bin/python
# Filename: ASVModel.py
# Description: ASV risk model

from cos.math.risk.ConditionalProbabilityTable import apply_all, read
from rules.examiner.risk.ASVCPT import read as read_model
from rules.examiner.risk.RiskModel import CURRENCY, LossMatrix

import xml.etree.ElementTree as ET
import numpy as np
import pyagrum as gum
import os, json, argparse, yaml



# Skeleton of the ASV risk model, Fig. 2 of:
# 
#     Kristensen, Maidana, Utne & Bremnes (2025),
#     "Evaluating the effect of risk metrics for supporting operational
#     decision-making by autonomous surface vehicles",
#     Ocean Engineering 338, 121937.
# 
# Structure and states are transcribed from Fig. 2 and Tables A.4/A.5, and live
# here. The conditional probability tables are NOT published, and are held in
# config/risk/asv.model.yaml rather than in code: apart from the four static
# priors of Table A.6 and the uniform priors the paper specifies for the dynamic
# inputs, every one of them is a placeholder. Node colours in Fig. 2 map onto the
# node kinds below.
# 
# Running this module rebuilds config/risk/risk.model.xdsl from that
# configuration, prints a model report, and writes the risk.model.labels.json
# sidecar holding the paper's node captions for xdsl2md.py. Pass a path to write
# the network somewhere else.



# Node kinds, matching the colour legend of Fig. 2. The names are declared in
# the model file; these constants exist so that the colour map and the report
# below can refer to them without spelling them out again.
HE = "HE"                    # light blue: hazardous event
DYNAMIC = "dynamic"          # blue:   probability-influencing, updated in operation
STATIC = "static"            # grey:   probability-influencing, static
CONSEQUENCE = "consequence"  # orange: consequence / end node

KINDS = (CONSEQUENCE, HE, DYNAMIC, STATIC)

# Valuation is NOT declared here. What a consequence is worth is specific to a
# domain and to a territory, so it lives in $(SIMULATION)/risk.yaml under
# risk.cost and is read through RiskModel.LossMatrix. A copy in code could only
# ever drift from the territory that governs it - and would drift silently,
# because nothing compares the two.
#
# This module needs a territory only to print an illustrative expected loss in
# its report; the network it builds carries no costs at all.
TERRITORY = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), *([os.pardir] * 4),
    "config", "simulation", "no", "trondheim", "risk.yaml"))


def build(model=None):
    """Assemble the network described by config/risk/asv.model.yaml.

    Nothing about the model is declared in this module: inference.network gives
    the nodes, their states and the arcs, and the tables give the conditional
    probabilities. apply_all reports every mismatched shape and every
    unnormalised row at once rather than failing on the first, so an edited
    configuration is correctable in one pass.

    Arguments
        model -- (network, tables) as returned by ASVCPT.read(); read from the
            default configuration when omitted.
    Returns
        (bn, network, tables)
    """
    network, tables = model if model is not None else read_model()

    bn = gum.BayesNet("ASV risk model (Kristensen et al. 2025, Fig. 2)")
    for node in network.nodes:
        bn.add(gum.LabelizedVariable(node, network.label(node), network.states(node)))
    for parent, child in network.edges:
        bn.addArc(parent, child)

    problems = apply_all(bn, tables)
    if problems:
        raise ValueError("conditional probability tables rejected:\n  " +
                         "\n  ".join(problems))
    return bn, network, tables


# GeNIe interior colours, matching the legend of Fig. 2.
GENIE_COLOUR = {
    CONSEQUENCE: "ff8000",   # orange
    HE: "e0ffff",            # light blue
    DYNAMIC: "99ccff",       # blue
    STATIC: "c0c0c0",        # grey
}


def write_network(bn, path, network):
    """Save the network, then add the Fig. 2 node colours that pyAgrum omits.

    The colours make the file render like Fig. 2 in GeNIe, and let xdsl2md.py
    group the generated diagram by the paper's own legend rather than guessing
    from graph structure.

    The paper's node captions are deliberately NOT written into the GeNIe
    <name> element, even though that is where a caption belongs. pyAgrum reads
    <name> back as the VARIABLE name, so a captioned file reloads with every
    variable renamed - "Failure of communication system" instead of
    comms_system_failure - which breaks the faculty bindings and HAZARDS.
    Colours carry no such penalty.
    """
    gum.saveBN(bn, path)

    tree = ET.parse(path)
    for element in tree.getroot().iterfind("./extensions/genie/node"):
        kind = network.kind(element.get("id"))

        interior = element.find("interior")
        if interior is None:
            interior = ET.SubElement(element, "interior")
        interior.set("color", GENIE_COLOUR[kind])

    tree.write(path, encoding="utf-8", xml_declaration=True)

    # The captions go in a sidecar instead, which xdsl2md.py picks up by name.
    sidecar = os.path.splitext(path)[0] + ".labels.json"
    with open(sidecar, "w", encoding="utf-8") as handle:
        json.dump(network.labels(), handle, indent=2)

    return path


def load_territory(path=None):
    """Read a territory's valuation as a LossMatrix.

    The territory file is the definitive source of cost. This returns the whole
    matrix rather than just the cost table so that a caller can also reach the
    concern mapping and the zone factors without reading the file twice.

    Arguments
        path -- Territory risk file; defaults to the location named in cos.ini
    """
    path = path or TERRITORY

    with open(path, encoding="utf-8") as handle:
        config = yaml.safe_load(handle) or {}

    matrix = LossMatrix(config.get("risk", {}) or {})
    if not matrix.cost:
        raise ValueError(f"{path}: declares no risk.cost")

    return matrix


def expected_loss(bn, evidence=None, matrix=None):
    """Expected loss summed over every consequence node, in RiskModel.CURRENCY.

    Costs come from the territory file, never from this module. Summing
    expectations across consequences is valid whatever the dependence between
    them, and is right physically: one collision may damage both vessels and
    harm a person.

    Arguments
        bn -- The network
        evidence -- Evidence to condition on
        matrix -- A LossMatrix; loaded from the default territory when omitted
    """
    matrix = matrix if matrix is not None else load_territory()

    engine = gum.LazyPropagation(bn)
    engine.setEvidence(evidence or {})
    engine.makeInference()

    return sum(matrix.base(engine).values())


def hazard_probability(bn, hazards, evidence=None):
    """Probability that any hazardous event occurs, two ways.

    'sum' is eq. (14) of the paper, P_C + P_G + P_L. That is Boole's inequality:
    an upper bound, not a probability, and it may exceed 1. 'any' is the exact
    joint, 1 - P(none of them), which the network answers directly with no
    independence assumption.

    Arguments
        bn -- The network
        hazards -- Hazardous event node names, from inference.network.hazards
        evidence -- Evidence to condition on
    """
    hazards = tuple(hazards)

    engine = gum.LazyPropagation(bn)
    engine.addAllTargets()   # a joint target alone would drop the other marginals
    engine.addJointTarget(set(hazards))
    engine.setEvidence(evidence or {})
    engine.makeInference()

    marginals = {h: float(engine.posterior(h)[{h: "yes"}]) for h in hazards}
    joint = engine.jointPosterior(set(hazards))
    none = float(joint[{h: "no" for h in hazards}])

    return marginals, sum(marginals.values()), 1.0 - none


def report(bn, network, tables):
    kinds = network.by_kind()
    print(f"nodes {bn.size()}   arcs {bn.sizeArcs()}   free parameters {bn.dim()}")
    for kind in KINDS:
        print(f"  {kind:<12} {len(kinds.get(kind, [])):>2}")
    roots = sorted(n for n in network.nodes if not list(bn.parents(n)))
    leaves = sorted(n for n in network.nodes if not list(bn.children(n)))
    print(f"\nroots  ({len(roots)}): \n {'\n '.join(roots)}")
    print(f"leaves ({len(leaves)}): \n {'\n '.join(leaves)}")

    sources = {}
    cells = 0
    for table in tables:
        sources[table.source] = sources.get(table.source, 0) + 1
        cells += table.shape[0] * table.shape[1]
    print(f"\ntables {len(tables)}, {cells} cells")
    for source, count in sorted(sources.items(), key=lambda kv: -kv[1]):
        print(f"  {count:>2}  {source}")


DEPLOYED = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), *([os.pardir] * 4),
    "config", "risk", "risk.model.xdsl"))


def parse(argv=None):
    """Command line for rebuilding the network.

    Defaulting the output to the deployed path is what makes this module the
    regenerable source of the network the examiners load, rather than a script
    whose output has to be copied across by hand.
    """
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--out", default=DEPLOYED,
                        help="where to write the network (default: %(default)s)")
    parser.add_argument("--model", default=None,
                        help="model file carrying inference.network and the "
                             "tables (default: config/risk/asv.model.yaml)")
    parser.add_argument("--territory", default=TERRITORY,
                        help="territory risk file supplying cost "
                             "(default: %(default)s)")
    return parser.parse_args(argv)


if __name__ == "__main__":
    args = parse()

    bn, network, tables = build(read_model(args.model) if args.model else None)
    report(bn, network, tables)

    matrix = load_territory(args.territory)
    print(f"\nexpected loss [{CURRENCY}], placeholder tables")
    print(f"  valuation from {args.territory}")
    print(f"  no evidence                      {expected_loss(bn, matrix=matrix):>14,.0f}")
    print(f"  target on collision course       "
          f"{expected_loss(bn, {'target_on_collision': 'yes'}, matrix):>14,.0f}")
    print(f"  ... and recovery has failed       "
          f"{expected_loss(bn, {'target_on_collision': 'yes', 'fail_recover_collision': 'yes'}, matrix):>13,.0f}")

    marginals, p_sum, p_any = hazard_probability(bn, network.hazards)
    print("\nprobability that any hazardous event occurs")
    for name, p in marginals.items():
        print(f"  P({name})".ljust(26) + f"{p:>8.3f}")
    print("  eq. (14), the sum".ljust(26) + f"{p_sum:>8.3f}")
    print("  exact joint".ljust(26) + f"{p_any:>8.3f}")

    # Round-trip: the tables must come back out of the network unchanged.
    drift = max(float(np.abs(read(bn, t.node, t.parents).table - t.table).max())
                for t in tables)
    print(f"\ntable round-trip, worst cell error {drift:.2e}")

    write_network(bn, args.out, network)
    print(f"\nwrote {args.out}")
    print("  (opens in GeNIe, coloured as Fig. 2; captions in the .labels.json sidecar)")
