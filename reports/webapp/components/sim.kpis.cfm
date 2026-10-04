<!--: S5 sim.kpis (DASH.007) — three figures, each opening into the component that explains it. -->
<cfinclude template="../shared/open.cfm">
<cfoutput><section data-component="sim.kpis" data-endpoint="#cos_root#/data/sim.kpis.data.cfm"></section></cfoutput>
<script>
COS.component('sim.kpis', {
    code: 'S5', title: 'Run figures', hint: 'Three numbers that sum up the run.',
    mock: function () {
        return { rows: [{ pc: 1900, nc: 38, pp: 539382, np: 6340, pl: 0, imo: 9000003, name: 'MOCK TRUE NORTH',
                          rb: 84873, surv: 0.074, enc: 2128, enc0: 1417 }] };
    },
    render: function (ctx, data) {
        var r = data.rows[0];
        COS.ui.tiles(ctx.body, [
            { key: 'f', label: 'Findings', href: '#part-sim.findings.bysource', html: true,
              value: COS.esc(COS.fmt.int(r.nc)) + ' <small>COLREG</small> · ' + COS.esc(COS.fmt.int(r.np)) + ' <small>seamanship</small>',
              sub: 'Penalty points: ' + COS.fmt.int(r.pc) + ' COLREG · ' + COS.fmt.int(r.pp) + ' seamanship' + (r.pl ? ' · ' + COS.fmt.pts(r.pl) + ' other' : '') },
            { key: 'r', label: 'Highest risk (Rb)', href: '#part-sim.fleet.table',
              value: COS.fmt.usd(r.rb), sub: (r.name || 'vessel ' + r.imo) + ' · survival ' + COS.fmt.num(r.surv, 2) + ' at the end' },
            { key: 'e', label: 'Encounters', href: '#part-sim.coverage.rules',
              value: COS.fmt.int(r.enc), sub: COS.fmt.pct(r.enc ? r.enc0 / r.enc : null) + ' seen only once' }
        ]);
    },
    flags: function (ctx, data) {
        return data.rows[0].enc0 ? [{ ticket: 'COS.044', text: 'Finding and encounter counts are too high (§2)' }] : [];
    },
    caption: function (ctx, data) {
        var r = data.rows[0], tot = r.nc + r.np;
        return COS.fmt.pct(tot ? r.nc / tot : null) + ' of findings come from COLREG rules.';
    }
});
</script>
<cfinclude template="../shared/close.cfm">
