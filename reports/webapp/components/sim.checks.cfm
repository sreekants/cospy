<!--: S2 sim.checks (DASH.004) — what is wrong with the data, and what was verified (SIM-03, SIM-06). -->
<cfparam name="composed" default="0">
<cfif composed EQ 0><cfinclude template="../shared/open.cfm"></cfif>
<cfoutput><section data-component="sim.checks" data-endpoint="#cos_root#/data/sim.checks.data.cfm"></section></cfoutput>
<script>
COS.component('sim.checks', {
    code: 'S2', title: 'Data checks', hint: 'Problems found in the data, and the checks that passed.',
    mock: function () {
        return { rows: [
            { id: 'bound', label: 'Exact hazard probability above the summed bound', ticket: '', n: 0 },
            { id: 'cum', label: 'Cumulative risk decreases within a voyage', ticket: '', n: 0 },
            { id: 'rescore', label: 'Findings re-scored within two assessment intervals', ticket: 'COS.044', n: 120 },
            { id: 'dup', label: 'Duplicate findings (same vessel, tick, event)', ticket: 'COS.044', n: 8 }] };
    },
    render: function (ctx, data) {
        var bad = data.rows.filter(function (r) { return r.n > 0; });
        var good = data.rows.filter(function (r) { return r.n === 0; });
        ctx.body.innerHTML = '<div class="s2-t"></div><p class="s2-pass"></p>';
        COS.ui.table(ctx.body.querySelector('.s2-t'), [
            { key: 'label', label: 'Problem' },
            { key: 'n', label: 'Rows', num: true, fmt: COS.fmt.int },
            { key: 'ticket', label: 'Ticket', fmt: function (v) { return v || '—'; } }
        ], bad, { ctx: ctx, sortable: false, emptyText: 'No problems found.' });
        ctx.body.querySelector('.s2-pass').textContent = good.length
            ? 'No problem found: ' + good.map(function (r) { return r.label.charAt(0).toLowerCase() + r.label.slice(1); }).join('; ') + '.'
            : '';
    },
    flags: function (ctx, data) {
        var t = {};
        data.rows.forEach(function (r) { if (r.n > 0 && r.ticket) t[r.ticket] = 1; });
        return Object.keys(t).map(function (k) { return { ticket: k, text: 'Data problem, see ' + k }; });
    },
    caption: function (ctx, data) {
        var bad = data.rows.filter(function (r) { return r.n > 0; }).length;
        return bad + ' of ' + data.rows.length + ' checks found a problem.';
    }
});
</script>
<cfif composed EQ 0><cfinclude template="../shared/close.cfm"></cfif>
