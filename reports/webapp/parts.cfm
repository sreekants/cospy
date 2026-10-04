<!--: parts.cfm — index of every component, standalone and mock, with its endpoint (CP-11). -->
<cfset composed = 1>
<cfinclude template="/test/cos/shared/config.cfm">
<!DOCTYPE html>
<html lang="en">
<head>
<cfinclude template="/test/cos/shared/head.cfm">
<title>COS — Components</title>
</head>
<body>
<main class="cos-app cos-composed">
<header class="cos-pagehead"><h1>Components</h1><nav><a href="/test/cos/sim.cfm">Simulation</a> <a href="/test/cos/vessel.cfm">Vessel</a></nav></header>
<section class="part"><p class="part-caption">Vessel components take <code>?imo=</code>; every page takes <code>?case=</code>, <code>?poll=</code> (milliseconds, never below 3000) and <code>?mock=1</code>.</p>
<div class="cos-tablewrap"><table class="cos-table"><thead><tr><th>Component</th><th>Open</th><th>Data</th></tr></thead><tbody>
<tr><td><code>run.picker</code></td><td><a href="/test/cos/components/run.picker.cfm">standalone</a> · <a href="/test/cos/components/run.picker.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/run.picker.data.cfm">endpoint</a></td></tr>
<tr><td><code>run.provenance</code></td><td><a href="/test/cos/components/run.provenance.cfm">standalone</a> · <a href="/test/cos/components/run.provenance.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/run.provenance.data.cfm">endpoint</a></td></tr>
<tr><td><code>sim.checks</code></td><td><a href="/test/cos/components/sim.checks.cfm">standalone</a> · <a href="/test/cos/components/sim.checks.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/sim.checks.data.cfm">endpoint</a></td></tr>
<tr><td><code>sim.coverage.rules</code></td><td><a href="/test/cos/components/sim.coverage.rules.cfm">standalone</a> · <a href="/test/cos/components/sim.coverage.rules.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/sim.coverage.rules.data.cfm">endpoint</a></td></tr>
<tr><td><code>sim.findings.bysource</code></td><td><a href="/test/cos/components/sim.findings.bysource.cfm">standalone</a> · <a href="/test/cos/components/sim.findings.bysource.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/sim.findings.bysource.data.cfm">endpoint</a></td></tr>
<tr><td><code>sim.findings.tree</code></td><td><a href="/test/cos/components/sim.findings.tree.cfm">standalone</a> · <a href="/test/cos/components/sim.findings.tree.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/sim.findings.tree.data.cfm">endpoint</a></td></tr>
<tr><td><code>sim.fleet.table</code></td><td><a href="/test/cos/components/sim.fleet.table.cfm">standalone</a> · <a href="/test/cos/components/sim.fleet.table.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/sim.fleet.table.data.cfm">endpoint</a></td></tr>
<tr><td><code>sim.heat.zoneconcern</code></td><td><a href="/test/cos/components/sim.heat.zoneconcern.cfm">standalone</a> · <a href="/test/cos/components/sim.heat.zoneconcern.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/sim.heat.zoneconcern.data.cfm">endpoint</a></td></tr>
<tr><td><code>sim.kpis</code></td><td><a href="/test/cos/components/sim.kpis.cfm">standalone</a> · <a href="/test/cos/components/sim.kpis.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/sim.kpis.data.cfm">endpoint</a></td></tr>
<tr><td><code>sim.rb.byconcern</code></td><td><a href="/test/cos/components/sim.rb.byconcern.cfm">standalone</a> · <a href="/test/cos/components/sim.rb.byconcern.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/sim.rb.byconcern.data.cfm">endpoint</a></td></tr>
<tr><td><code>sim.rb.cumulative</code></td><td><a href="/test/cos/components/sim.rb.cumulative.cfm">standalone</a> · <a href="/test/cos/components/sim.rb.cumulative.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/sim.rb.cumulative.data.cfm">endpoint</a></td></tr>
<tr><td><code>sim.rev</code></td><td><a href="/test/cos/components/sim.rev.cfm">standalone</a> · <a href="/test/cos/components/sim.rev.cfm?mock=1">mock</a></td><td>—</td></tr>
<tr><td><code>sim.runstrip</code></td><td><a href="/test/cos/components/sim.runstrip.cfm">standalone</a> · <a href="/test/cos/components/sim.runstrip.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/sim.runstrip.data.cfm">endpoint</a></td></tr>
<tr><td><code>sim.scatter</code></td><td><a href="/test/cos/components/sim.scatter.cfm">standalone</a> · <a href="/test/cos/components/sim.scatter.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/sim.scatter.data.cfm">endpoint</a></td></tr>
<tr><td><code>ves.baselines</code></td><td><a href="/test/cos/components/ves.baselines.cfm">standalone</a> · <a href="/test/cos/components/ves.baselines.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/ves.baselines.data.cfm">endpoint</a></td></tr>
<tr><td><code>ves.coupling</code></td><td><a href="/test/cos/components/ves.coupling.cfm">standalone</a> · <a href="/test/cos/components/ves.coupling.cfm?mock=1">mock</a></td><td>—</td></tr>
<tr><td><code>ves.episode.clauses</code></td><td><a href="/test/cos/components/ves.episode.clauses.cfm">standalone</a> · <a href="/test/cos/components/ves.episode.clauses.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/ves.episode.clauses.data.cfm">endpoint</a></td></tr>
<tr><td><code>ves.episodes</code></td><td><a href="/test/cos/components/ves.episodes.cfm">standalone</a> · <a href="/test/cos/components/ves.episodes.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/ves.episodes.data.cfm">endpoint</a></td></tr>
<tr><td><code>ves.findings.log</code></td><td><a href="/test/cos/components/ves.findings.log.cfm">standalone</a> · <a href="/test/cos/components/ves.findings.log.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/ves.findings.log.data.cfm">endpoint</a></td></tr>
<tr><td><code>ves.identity</code></td><td><a href="/test/cos/components/ves.identity.cfm">standalone</a> · <a href="/test/cos/components/ves.identity.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/ves.identity.data.cfm">endpoint</a></td></tr>
<tr><td><code>ves.kpis</code></td><td><a href="/test/cos/components/ves.kpis.cfm">standalone</a> · <a href="/test/cos/components/ves.kpis.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/ves.kpis.data.cfm">endpoint</a></td></tr>
<tr><td><code>ves.map</code></td><td><a href="/test/cos/components/ves.map.cfm">standalone</a> · <a href="/test/cos/components/ves.map.cfm?mock=1">mock</a></td><td>—</td></tr>
<tr><td><code>ves.rb.byconcern</code></td><td><a href="/test/cos/components/ves.rb.byconcern.cfm">standalone</a> · <a href="/test/cos/components/ves.rb.byconcern.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/ves.rb.byconcern.data.cfm">endpoint</a></td></tr>
<tr><td><code>ves.rb.matrix</code></td><td><a href="/test/cos/components/ves.rb.matrix.cfm">standalone</a> · <a href="/test/cos/components/ves.rb.matrix.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/ves.rb.matrix.data.cfm">endpoint</a></td></tr>
<tr><td><code>ves.ro.matrix</code></td><td><a href="/test/cos/components/ves.ro.matrix.cfm">standalone</a> · <a href="/test/cos/components/ves.ro.matrix.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/ves.ro.matrix.data.cfm">endpoint</a></td></tr>
<tr><td><code>ves.snapshot</code></td><td><a href="/test/cos/components/ves.snapshot.cfm">standalone</a> · <a href="/test/cos/components/ves.snapshot.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/ves.snapshot.data.cfm">endpoint</a></td></tr>
<tr><td><code>ves.tl.encounters</code></td><td><a href="/test/cos/components/ves.tl.encounters.cfm">standalone</a> · <a href="/test/cos/components/ves.tl.encounters.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/ves.tl.encounters.data.cfm">endpoint</a></td></tr>
<tr><td><code>ves.tl.environment</code></td><td><a href="/test/cos/components/ves.tl.environment.cfm">standalone</a> · <a href="/test/cos/components/ves.tl.environment.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/ves.tl.environment.data.cfm">endpoint</a></td></tr>
<tr><td><code>ves.tl.findings</code></td><td><a href="/test/cos/components/ves.tl.findings.cfm">standalone</a> · <a href="/test/cos/components/ves.tl.findings.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/ves.tl.findings.data.cfm">endpoint</a></td></tr>
<tr><td><code>ves.tl.hazards</code></td><td><a href="/test/cos/components/ves.tl.hazards.cfm">standalone</a> · <a href="/test/cos/components/ves.tl.hazards.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/ves.tl.hazards.data.cfm">endpoint</a></td></tr>
<tr><td><code>ves.tl.rb</code></td><td><a href="/test/cos/components/ves.tl.rb.cfm">standalone</a> · <a href="/test/cos/components/ves.tl.rb.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/ves.tl.rb.data.cfm">endpoint</a></td></tr>
<tr><td><code>ves.tl.zone</code></td><td><a href="/test/cos/components/ves.tl.zone.cfm">standalone</a> · <a href="/test/cos/components/ves.tl.zone.cfm?mock=1">mock</a></td><td><a href="/test/cos/data/ves.tl.zone.data.cfm">endpoint</a></td></tr>
</tbody></table></div></section>
</main>
</body>
</html>
