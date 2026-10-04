<!--: S13 sim.fleet.table (DASH.015) — every vessel on equal terms; choose which voyage to examine. -->
<cfinclude template="../shared/open.cfm">
<cfoutput><section data-component="sim.fleet.table" data-endpoint="#cos_root#/data/sim.fleet.table.data.cfm"></section></cfoutput>
<script>
COS.component('sim.fleet.table', {
    code: 'S13', title: 'Fleet', hint: 'Every vessel side by side. Click one to open it.',
    mock: function () {
        var r = COS.mock.rng('S13');
        return { names: COS.mock.imos.map(function (m, i) { return [String(m), COS.mock.vessels[i]]; }),
            rows: COS.mock.imos.map(function (imo) {
                return { imo: imo, rb: 5000 + r() * 80000, surv: 0.1 + r() * 0.5, pc: r() * 0.2, pg: r() * 0.05,
                         pl0: 0.1724, pl1: 0.6, nc: Math.round(r() * 5), np: Math.round(100 + r() * 400), enc: Math.round(20 + r() * 150) };
            }) };
    },
    render: function (ctx, data) {
        var names = {};
        (data.names || []).forEach(function (n) { names[n[0]] = n[1]; });
        data.rows.forEach(function (r) { r.name = names[String(r.imo)] || null; });
        if (!ctx.state.sort) ctx.state.sort = { key: 'name', dir: 'asc' };
        COS.ui.table(ctx.body, [
            { key: 'name', label: 'Vessel', html: true, fmt: function (v, r) {
                return (v ? COS.esc(v) : '<span class="cos-missing">not in register</span>') + ' <span class="part-code">' + r.imo + '</span>'; } },
            { key: 'nc', label: 'COLREG findings', num: true, fmt: COS.fmt.int },
            { key: 'np', label: 'Seamanship findings', num: true, fmt: COS.fmt.int },
            { key: 'enc', label: 'Encounters', num: true, fmt: COS.fmt.int },
            { key: 'rb', label: 'Risk (USD)', num: true, fmt: function (v) { return COS.fmt.int(v); } },
            { key: 'surv', label: 'Survival', num: true, fmt: function (v) { return COS.fmt.num(v, 2); } },
            { key: 'pc', label: 'Highest P_C', num: true, fmt: COS.fmt.prob },
            { key: 'pg', label: 'Highest P_G', num: true, fmt: COS.fmt.prob }
        ], data.rows, { ctx: ctx, maxHeight: 440,
            onRow: function (r) { window.location.href = COS.link('vessel.cfm', { imo: r.imo }); } });
    },
    flags: function () { return [{ ticket: 'COS.044', text: 'Finding and encounter counts are too high (§2)' }]; },
    caption: function (ctx, data) {
        var lo = Infinity, hi = 0;
        data.rows.forEach(function (r) { lo = Math.min(lo, r.pl0); hi = Math.max(hi, r.pl1); });
        return data.rows.length + ' vessels. Chance of losing communications is left out: it is ' +
            COS.fmt.prob(lo) + ' or more everywhere (a placeholder value).';
    }
});
</script>
<cfinclude template="../shared/close.cfm">
