<!--: S14 sim.heat.zoneconcern (DASH.016) — the run's observed-violation input to Ro. -->
<cfinclude template="../shared/open.cfm">
<cfoutput><section data-component="sim.heat.zoneconcern" data-endpoint="#cos_root#/data/sim.heat.zoneconcern.data.cfm"></section></cfoutput>
<script>
COS.component('sim.heat.zoneconcern', {
    code: 'S14', title: 'Penalty points by zone', hint: 'Where penalty points were given, by zone and concern.',
    mock: function () {
        var r = COS.mock.rng('S14'), rows = [];
        COS.enc.zones.forEach(function (z) { ['safety', 'traffic', 'operational'].forEach(function (c) {
            var n = Math.round(r() * 300); rows.push({ zone: z.key, concern: c, n: n, pts: n * 60 }); }); });
        return { rows: rows };
    },
    render: function (ctx, data) {
        var cell = function (z, c, k) {
            var m = data.rows.filter(function (r) { return r.zone === z && r.concern === c; })[0];
            return m ? m[k] : 0;
        };
        var Z = COS.enc.zones, C = COS.enc.concerns;
        COS.ui.matrix(ctx.body, {
            rows: Z.map(function (z) { return z.label; }), cols: C.map(function (c) { return c.label; }), corner: 'points',
            val: function (i, j) { return cell(Z[i].key, C[j].key, 'pts'); },
            sub: function (i, j) { return COS.fmt.int(cell(Z[i].key, C[j].key, 'n')) + ' findings'; },
            fmt: COS.fmt.int
        });
    },
    flags: function () { return [{ ticket: 'COS.013', text: 'Penalty points are not calibrated' }, { ticket: 'COS.044', text: 'Points are counted again at every check (§2)' }]; },
    caption: function (ctx, data) {
        var top = data.rows.slice().sort(function (a, b) { return b.pts - a.pts; })[0];
        return top ? 'Most points: ' + top.concern + ', ' + top.zone.replace('_', ' ') + '.' : '';
    }
});
</script>
<cfinclude template="../shared/close.cfm">
