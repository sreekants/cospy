<!--: V4 ves.map (DASH.027) — the track: the vessel's position at each risk assessment (REQ-048-07 to -11). -->
<cfparam name="composed" default="0">
<cfif composed EQ 0><cfinclude template="../shared/open.cfm"></cfif>
<cfoutput><section data-component="ves.map" data-endpoint="#cos_root#/data/ves.map.data.cfm"></section></cfoutput>
<script>
COS.component('ves.map', {
    code: 'V4', title: 'Track', hint: 'Where the vessel sailed: its position at each risk assessment.', vessel: true,
    mockReason: 'no position recorded for this vessel',
    mock: function () {
        var r = COS.mock.rng('V4'), pts = [], lat = 1.20, lon = 103.70, zone = 0;
        for (var i = 0; i < 120; i++) {
            lon += 0.0015 + r() * 0.001; lat += 0.0008 + r() * 0.0006;
            if (i === 30 || i === 70 || i === 105) zone++;
            pts.push([lon, lat, i * 20, zone]);
        }
        return { pts: pts };
    },
    render: function (ctx, data) {
        var Z = COS.enc.zones;
        /* Morton code (60 bits, longitude on the upper bit of each pair) to the centre of its cell */
        function axis(v) {
            var out = 0n;
            for (var i = 0n; i < 30n; i++) out += ((v >> (2n * i)) & 1n) * 2n ** i;	/* no left shift: the engine rewrites it */
            return Number(out);
        }
        function decode(row) {
            var v = BigInt(row[0]), cell = Math.pow(2, 30);
            var z = Z.findIndex(function (q) { return q.key === row[2]; });
            return [-180 + (axis(v >> 1n) + 0.5) * 360 / cell, -90 + (axis(v) + 0.5) * 180 / cell, row[1], z < 0 ? 0 : z];
        }
        var pts = data.pts || data.rows.map(decode);

        if (!ctx.body.querySelector('.cos-chart')) {
            ctx.body.innerHTML = '<p class="cos-notice">Position at each risk assessment. Course and speed are not recorded yet (REQ.037-01).</p><div class="cos-chart"></div>';
        }
        var el = ctx.body.querySelector('.cos-chart');

        function draw() {
            if (!el.clientWidth) return;		/* hidden tab: drawn when shown (COS.mapWatch) */
            var f = COS.mapFrame(el, pts), py = (f.y[1] - f.y[0]) / 2;
            var dp = Math.min(6, Math.max(2, Math.ceil(-Math.log10(py)) + 1)), deg = function (v) { return v.toFixed(dp) + '°'; };
            var inst = COS.chart(ctx, 'map', el, {
                grid: f.grid,
                tooltip: { trigger: 'item', backgroundColor: COS.token('--surface-2'), borderColor: COS.token('--line'), textStyle: { color: COS.token('--text-primary') }, formatter: function (q) {
                    return 'Tick ' + COS.fmt.int(q.data[2]) + '<br>' + q.data[1].toFixed(5) + '° N, ' + q.data[0].toFixed(5) + '° E<br>' + Z[q.data[3]].label; } },
                legend: { top: 0, data: Z.map(function (z) { return z.label; }), textStyle: { color: COS.token('--text-secondary') } },
                xAxis: COS.axis('Longitude', { type: 'value', min: f.x[0], max: f.x[1], nameGap: 24, axisLabel: { formatter: deg, showMinLabel: false, showMaxLabel: false, color: COS.token('--text-secondary') } }),
                yAxis: COS.axis('Latitude', { type: 'value', min: f.y[0], max: f.y[1], nameGap: 76, axisLabel: { formatter: deg, showMinLabel: false, showMaxLabel: false, color: COS.token('--text-secondary') } }),
                dataZoom: [{ type: 'inside', xAxisIndex: 0, filterMode: 'none' }, { type: 'inside', yAxisIndex: 0, filterMode: 'none' }],
                series: Z.map(function (z, i) {
                    return { name: z.label, type: 'line', showSymbol: true, symbolSize: 5, lineStyle: { width: 3, color: COS.enc.color(z) },
                        itemStyle: { color: COS.enc.color(z) },
                        data: pts.filter(function (p) { return p[3] === i; }) };
                })
            }, { height: f.height });
            COS.mapHeight(inst, el, f.height);
        }
        COS.mapWatch(el, draw);
        draw();
    },
    caption: function (ctx, data) {
        var n = (data.pts || data.rows).length;
        return n + ' position' + (n === 1 ? '' : 's') + ', one per risk assessment.';
    }
});
</script>
<cfif composed EQ 0><cfinclude template="../shared/close.cfm"></cfif>
