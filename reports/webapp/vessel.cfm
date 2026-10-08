<!--: vessel.cfm — vessel page in three tabs (UX §2.3, VES-19), composed from components (CP-01). Each component also runs alone. -->
<cfset composed = 1>
<cfinclude template="shared/config.cfm">
<!DOCTYPE html>
<html lang="en">
<head>
<cfinclude template="shared/head.cfm">
<title>COS — Vessel</title>
</head>
<body>
<main class="cos-app cos-composed" id="vessel-page">
<header class="cos-pagehead"><h1>Vessel</h1>
<cfoutput><nav><a href="#cos_root#/sim.cfm">← Simulation</a> <a href="#cos_root#/parts.cfm">Components</a></nav></cfoutput>
<span class="part-code">Material for debate, not conclusions.</span></header>
<div class="cos-tabs" role="tablist" aria-label="Vessel page">
  <button type="button" role="tab" data-tab="overview" aria-controls="tab-overview">Overview</button>
  <button type="button" role="tab" data-tab="voyage" aria-controls="tab-voyage">Voyage</button>
  <button type="button" role="tab" data-tab="record" aria-controls="tab-record">Record</button>
</div>

<div class="cos-tabpanel cos-grid" role="tabpanel" id="tab-overview" data-tabpanel="overview">
  <div class="span-12"><cfinclude template="components/ves.kpis.cfm"></div>
  <div class="span-6"><cfinclude template="components/ves.rb.byconcern.cfm"></div>
  <div class="span-6"><cfinclude template="components/ves.map.cfm"></div>
  <div class="span-6"><cfinclude template="components/ves.ro.matrix.cfm"></div>
  <div class="span-6"><cfinclude template="components/ves.rb.matrix.cfm"></div>
  <div class="span-12"><cfinclude template="components/ves.identity.cfm"></div>
</div>

<div class="cos-tabpanel cos-grid" role="tabpanel" id="tab-voyage" data-tabpanel="voyage" hidden>
  <div class="span-12"><cfinclude template="components/ves.map.violations.cfm"></div>
  <div class="span-12"><cfinclude template="components/ves.tl.zone.cfm"></div>
  <div class="span-12"><cfinclude template="components/ves.tl.rb.cfm"></div>
  <div class="span-12"><cfinclude template="components/ves.tl.hazards.cfm"></div>
  <div class="span-12"><cfinclude template="components/ves.tl.findings.cfm"></div>
  <div class="span-12"><cfinclude template="components/ves.tl.encounters.cfm"></div>
  <div class="span-12"><cfinclude template="components/ves.tl.environment.cfm"></div>
  <div class="span-6"><cfinclude template="components/ves.snapshot.cfm"></div>
  <div class="span-6"><cfinclude template="components/ves.episode.clauses.cfm"></div>
</div>

<div class="cos-tabpanel cos-grid" role="tabpanel" id="tab-record" data-tabpanel="record" hidden>
  <div class="span-12"><cfinclude template="components/ves.baselines.cfm"></div>
  <div class="span-6"><cfinclude template="components/ves.episodes.cfm"></div>
  <div class="span-6"><cfinclude template="components/ves.findings.log.cfm"></div>
  <div class="span-6"><cfinclude template="components/ves.coupling.cfm"></div>
  <div class="span-6"><cfinclude template="components/run.provenance.cfm"></div>
</div>
</main>
<script>COS.tabs(document.getElementById('vessel-page'), { cursorTab: 'voyage' });</script>
</body>
</html>
