<!--: V4 ves.map (DASH.027) — the track: primary evidence, not yet recorded (REQ.037-01/02). No endpoint. -->
<cfinclude template="/test/cos/shared/open.cfm">
<section data-component="ves.map"></section>
<script>
COS.component('ves.map', {
    code: 'V4', title: 'Track', hint: 'Where the vessel sailed. Not recorded yet, so the line is made up.', vessel: true,
    mockReason: 'position is not recorded yet (REQ.037-01/02)',
    mock: function () {
        var r = COS.mock.rng('V4'), pts = [], x = 100, y = 900, zone = 0;
        for (var i = 0; i < 120; i++) {
            x += 6 + r() * 4; y -= 5 + r() * 3;
            if (i === 30 || i === 70 || i === 105) zone++;
            pts.push([x, y, zone]);
        }
        return { rows: pts };
    },
    render: function (ctx, data) {
        if (!ctx.body.querySelector('.cos-chart')) {
            ctx.body.innerHTML = '<p class="cos-notice cos-placeholder">Position is not recorded yet (REQ.037-01/02). This line is made up.</p><div class="cos-chart"></div>';
        }
        var Z = COS.enc.zones;
        COS.chart(ctx, 'map', ctx.body.querySelector('.cos-chart'), {
            grid: { left: 48, right: 16, top: 12, bottom: 40 },
            tooltip: { show: false },
            legend: { bottom: 0, data: Z.map(function (z) { return z.label; }), textStyle: { color: COS.token('--text-secondary') } },
            xAxis: COS.axis('Map x', { type: 'value', scale: true, nameGap: 24 }),
            yAxis: COS.axis('Map y', { type: 'value', scale: true, nameGap: 36 }),
            series: Z.map(function (z, i) {
                return { name: z.label, type: 'line', showSymbol: false, lineStyle: { width: 3, color: COS.enc.color(z) },
                    itemStyle: { color: COS.enc.color(z) },
                    data: data.rows.filter(function (p) { return p[2] === i; }).map(function (p) { return [p[0], p[1]]; }) };
            })
        }, { height: 300 });
    },
    caption: function () { return 'No position is recorded for any vessel.'; }
});
</script>
<cfinclude template="/test/cos/shared/close.cfm">
