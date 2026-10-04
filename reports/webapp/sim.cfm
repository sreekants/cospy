<!--: sim.cfm — simulation page in three tabs (UX §1.3b, SIM-20), composed from components (CP-01). Each component also runs alone. -->
<cfset composed = 1>
<cfinclude template="../shared/config.cfm">
<!DOCTYPE html>
<html lang="en">
<head>
<cfinclude template="../shared/head.cfm">
<title>COS — Simulation</title>
</head>
<body>
<main class="cos-app cos-composed" id="sim-page">
<header class="cos-pagehead"><h1>Simulation</h1>
<cfoutput><nav><a href="#cos_root#/parts.cfm">Components</a></nav></cfoutput>
<span class="part-code">Material for debate, not conclusions.</span></header>
<div class="cos-tabs" role="tablist" aria-label="Simulation page">
  <button type="button" role="tab" data-tab="overview" aria-controls="tab-overview">Overview</button>
  <button type="button" role="tab" data-tab="fleet" aria-controls="tab-fleet">Fleet</button>
  <button type="button" role="tab" data-tab="record" aria-controls="tab-record">Record</button>
</div>

<div class="cos-tabpanel cos-grid" role="tabpanel" id="tab-overview" data-tabpanel="overview">
  <div class="span-12"><cfinclude template="components/sim.kpis.cfm"></div>
  <div class="span-6"><cfinclude template="components/sim.findings.bysource.cfm"></div>
  <div class="span-6"><cfinclude template="components/sim.rb.byconcern.cfm"></div>
  <div class="span-12"><cfinclude template="components/sim.runstrip.cfm"></div>
  <div class="span-12"><cfinclude template="components/sim.checks.cfm"></div>
  <div class="span-12"><cfinclude template="components/sim.coverage.rules.cfm"></div>
</div>

<div class="cos-tabpanel cos-grid" role="tabpanel" id="tab-fleet" data-tabpanel="fleet" hidden>
  <div class="span-6"><cfinclude template="components/sim.rb.cumulative.cfm"></div>
  <div class="span-6"><cfinclude template="components/sim.scatter.cfm"></div>
  <div class="span-12"><cfinclude template="components/sim.fleet.table.cfm"></div>
</div>

<div class="cos-tabpanel cos-grid" role="tabpanel" id="tab-record" data-tabpanel="record" hidden>
  <div class="span-12"><cfinclude template="components/sim.heat.zoneconcern.cfm"></div>
  <div class="span-12"><cfinclude template="components/sim.findings.tree.cfm"></div>
  <div class="span-12"><cfinclude template="components/sim.rev.cfm"></div>
  <div class="span-6"><cfinclude template="components/run.provenance.cfm"></div>
  <div class="span-6"><cfinclude template="components/run.picker.cfm"></div>
</div>
</main>
<script>COS.tabs(document.getElementById('sim-page'));</script>
</body>
</html>
