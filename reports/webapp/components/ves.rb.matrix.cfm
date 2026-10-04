<!--: V20 ves.rb.matrix — the voyage by zone and concern. -->
<cfinclude template="shared/open.cfm">
<cfoutput><section data-component="ves.rb.matrix" data-endpoint="#cos_root#/data/ves.rb.matrix.data.cfm"></section></cfoutput>
<script>
COS.component('ves.rb.matrix', {
    code: 'V20', title: 'Risk by zone', hint: 'Where the risk (Rb) of this vessel built up, by zone and concern.', vessel: true,
    mock: function () {
        var r = COS.mock.rng('V20'), rows = [], tot = 0;
        COS.enc.zones.forEach(function (z) { ['safety', 'traffic', 'operational'].forEach(function (c) {
            var n = Math.round(r() * 60); rows.push({ zone: z.key, concern: c, v: n * 40 }); tot += rows[rows.length - 1].v; }); });
        return { final: tot, rows: rows };
    },
    render: function (ctx, data) {
        var Z = COS.enc.zones, C = COS.enc.concerns;
        var cell = function (z, c, k) {
            var m = data.rows.filter(function (r) { return r.zone === z && r.concern === c; })[0];
            return m ? m[k] : 0;
        };
        COS.ui.matrix(ctx.body, {
            rows: Z.map(function (z) { return z.label; }), cols: C.map(function (c) { return c.label; }), corner: 'USD',
            val: function (i, j) { return cell(Z[i].key, C[j].key, 'v'); }, sub: null, fmt: COS.fmt.usd
        });
    },
    flags: function () { return [{ ticket: 'REQ.001', text: 'Risk network tables are placeholders' }]; },
    caption: function (ctx, data) { return (function () { var s = 0; data.rows.forEach(function (r) { s += r.v; }); return data.final && Math.abs(s - data.final) <= 1e-9 * Math.max(1, data.final) ? 'The cells add up to ' + COS.fmt.usd(s) + ', the voyage total.' : 'The cells add up to ' + COS.fmt.usd(s) + ', but the voyage total is ' + COS.fmt.usd(data.final) + '.'; })(); }
});
</script>
<cfinclude template="shared/close.cfm">
