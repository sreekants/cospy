<!--: S19 sim.scatter (DASH.021) — normative and consequential on one plane, undivided. -->
<cfinclude template="shared/open.cfm">
<cfoutput><section data-component="sim.scatter" data-endpoint="#cos_root#/data/sim.scatter.data.cfm"></section></cfoutput>
<script>
COS.component('sim.scatter', {
    code: 'S19', title: 'Penalty points and risk', hint: 'Each dot is a vessel. For exploring only: no lines or limits are drawn.',
    mock: function () {
        var r = COS.mock.rng('S19');
        return { names: COS.mock.imos.map(function (m, i) { return [String(m), COS.mock.vessels[i]]; }),
                 rows: COS.mock.imos.map(function (m) { return [m, Math.round(r() * 60000), Math.round(r() * 80000)]; }) };
    },
    render: function (ctx, data) {
        var names = {};
        (data.names || []).forEach(function (n) { names[n[0]] = n[1]; });
        if (!ctx.body.querySelector('.cos-chart')) ctx.body.innerHTML = '<div class="cos-chart"></div>';
        COS.chart(ctx, 'sc', ctx.body.firstChild, {
            grid: { left: 76, right: 24, top: 16, bottom: 48 },
            tooltip: { trigger: 'item', formatter: function (p) {
                return COS.esc(names[String(p.value[2])] || p.value[2]) + '<br>' + COS.fmt.pts(p.value[0]) + '<br>' + COS.fmt.usd(p.value[1]); } },
            xAxis: COS.axis('Penalty points (not calibrated)', { type: 'value', nameGap: 30 }),
            yAxis: COS.axis('Risk (USD)', { type: 'value', nameGap: 60 }),
            series: [{ type: 'scatter', symbolSize: 10,
                itemStyle: { color: COS.token('--text-primary'), opacity: 0.8, borderColor: COS.token('--surface-1'), borderWidth: 2 },
                data: data.rows.map(function (r) { return [r[1], r[2], r[0]]; }) }]
        }, { height: 300, onClick: function (p) { window.location.href = COS.link('vessel.cfm', { imo: p.value[2] }); } });
    },
    flags: function () { return [{ ticket: 'COS.013', text: 'Penalty points are not calibrated' }]; },
    caption: function (ctx, data) { return data.rows.length + ' vessels.'; }
});
</script>
<cfinclude template="shared/close.cfm">
