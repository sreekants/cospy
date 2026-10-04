<!--: V19 ves.ro.matrix — the voyage by zone and concern. -->
<cfinclude template="../shared/open.cfm">
<cfoutput><section data-component="ves.ro.matrix" data-endpoint="#cos_root#/data/ves.ro.matrix.data.cfm"></section></cfoutput>
<script>
COS.component('ves.ro.matrix', {
    code: 'V19', title: 'Penalty points by zone', hint: 'Where this vessel got penalty points, by zone and concern.', vessel: true,
    mock: function () {
        var r = COS.mock.rng('V19'), rows = [], tot = 0;
        COS.enc.zones.forEach(function (z) { ['safety', 'traffic', 'operational'].forEach(function (c) {
            var n = Math.round(r() * 60); rows.push({ zone: z.key, concern: c, n: n, v: n * 70 }); tot += rows[rows.length - 1].v; }); });
        return { final: tot, rows: rows };
    },
    render: function (ctx, data) {
        var Z = COS.enc.zones, C = COS.enc.concerns;
        var cell = function (z, c, k) {
            var m = data.rows.filter(function (r) { return r.zone === z && r.concern === c; })[0];
            return m ? m[k] : 0;
        };
        COS.ui.matrix(ctx.body, {
            rows: Z.map(function (z) { return z.label; }), cols: C.map(function (c) { return c.label; }), corner: 'points',
            val: function (i, j) { return cell(Z[i].key, C[j].key, 'v'); }, sub: function (i, j) { return COS.fmt.int(cell(Z[i].key, C[j].key, 'n')) + ' findings'; }, fmt: COS.fmt.int
        });
    },
    flags: function () { return [{ ticket: 'COS.013', text: 'Penalty points are not calibrated' }, { ticket: 'COS.044', text: 'Points are counted again at every check (§2)' }]; },
    caption: function (ctx, data) { return 'Rule-based risk (R_ev) is not computed yet (REQ.031, COS.044 §1).'; }
});
</script>
<cfinclude template="../shared/close.cfm">
