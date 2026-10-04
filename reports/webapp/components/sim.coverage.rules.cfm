<!--: S7 sim.coverage.rules (DASH.009) — breaches beside the encounters where each rule could apply. -->
<cfinclude template="shared/open.cfm">
<cfoutput><section data-component="sim.coverage.rules" data-endpoint="#cos_root#/data/sim.coverage.rules.data.cfm"></section></cfoutput>
<script>
COS.component('sim.coverage.rules', {
    code: 'S7', title: 'COLREG rules and encounters', hint: 'How often each rule could apply, and how often it was broken.',
    mock: function () {
        return { rows: [{ rule: 13, enc: 'overtaking', n: 40, b: 0 }, { rule: 14, enc: 'head-on', n: 12, b: 3 },
                        { rule: 15, enc: 'crossing', n: 60, b: 5 }, { rule: 16, enc: 'give-way', n: 50, b: 0 },
                        { rule: 17, enc: 'crossing (stand-on)', n: 60, b: 0 }, { rule: 0, enc: 'all', n: 162, b: 90 }] };
    },
    render: function (ctx, data) {
        COS.ui.table(ctx.body, [
            { key: 'rule', label: 'Rule', fmt: function (v, r) { return 'COLREG ' + v + ' — ' + r.enc; } },
            { key: 'n', label: 'Encounters', num: true, fmt: COS.fmt.int },
            { key: 'b', label: 'Breaches', num: true, fmt: COS.fmt.int },
            { key: 'm', label: 'Met or not checked', html: true, sort: false,
              fmt: function () { return '<span class="cos-missing">not recorded — REQ.037-06</span>'; } }
        ], data.rows.filter(function (r) { return r.rule > 0; }), { ctx: ctx });
    },
    flags: function () { return [{ ticket: 'COS.044', text: 'One encounter can be counted many times (§2)' }]; },
    caption: function (ctx, data) {
        var all = data.rows.filter(function (r) { return r.rule === 0; })[0];
        return all ? COS.fmt.pct(all.n ? all.b / all.n : null) + ' of ' + COS.fmt.int(all.n) +
            ' encounters were seen only once, so the counts are too high.' : '';
    }
});
</script>
<cfinclude template="shared/close.cfm">
