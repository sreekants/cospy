<!--: V3 ves.kpis (DASH.026) — where the voyage ended up, and under which regimes. -->
<cfparam name="composed" default="0">
<cfif composed EQ 0><cfinclude template="../shared/open.cfm"></cfif>
<cfoutput><section data-component="ves.kpis" data-endpoint="#cos_root#/data/ves.kpis.data.cfm"></section></cfoutput>
<script>
COS.component('ves.kpis', {
    code: 'V3', title: 'Voyage figures', hint: 'Four numbers that sum up the voyage.', vessel: true,
    mock: function () { return { rows: [{ rb: 43300, surv: 0.31, nc: 3, np: 410, enc: 140, enc0: 90, z: [1200, 5400, 2300, 400] }] }; },
    render: function (ctx, data) {
        var r = data.rows[0], tot = r.z.reduce(function (a, b) { return a + b; }, 0);
        var zl = COS.enc.zones.map(function (z, i) {
            return '<span class="chip chip-z' + (i + 1) + '">' + COS.esc(z.short) + ' ' + Math.round(tot ? 100 * r.z[i] / tot : 0) + ' %</span>';
        }).join(' ');
        COS.ui.tiles(ctx.body, [
            { key: 'rb', label: 'Risk at the end (Rb)', value: COS.fmt.usd(r.rb), sub: 'survival ' + COS.fmt.num(r.surv, 2) },
            { key: 'f', label: 'Findings', html: true,
              value: COS.esc(COS.fmt.int(r.nc)) + ' <small>COLREG</small> · ' + COS.esc(COS.fmt.int(r.np)) + ' <small>seamanship</small>' },
            { key: 'e', label: 'Encounters', value: COS.fmt.int(r.enc), sub: COS.fmt.pct(r.enc ? r.enc0 / r.enc : null) + ' seen only once' },
            { key: 'z', label: 'Time per zone', html: true, value: '<span style="font-size:13px;font-weight:400">' + zl + '</span>',
              sub: COS.fmt.dur(tot) + ' in total' }
        ]);
    },
    flags: function (ctx, data) { return data.rows[0].enc0 ? [{ ticket: 'COS.044', text: 'Counts are too high (§2)' }] : []; },
    caption: function (ctx, data) {
        var r = data.rows[0];
        return 'The voyage ended with ' + COS.fmt.usd(r.rb) + ' of risk and ' + COS.fmt.int(r.nc) + (r.nc === 1 ? ' COLREG finding.' : ' COLREG findings.');
    }
});
</script>
<cfif composed EQ 0><cfinclude template="../shared/close.cfm"></cfif>
