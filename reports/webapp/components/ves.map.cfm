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
        function decode(row) {
            var z = Z.findIndex(function (q) { return q.key === row[2]; });
            return COS.morton(row[0]).concat([row[1], z < 0 ? 0 : z]);
        }
        var pts = data.pts || data.rows.map(decode);
        var map = COS.basemap.load(ctx), onmap = COS.basemap.usable(map) && pts.length > 0;

        if (!ctx.body.querySelector('.cos-chart')) {
            ctx.body.innerHTML = '<p class="cos-notice">Position at each risk assessment. Course and speed are not recorded yet (REQ.037-01).</p>' +
                '<p class="cos-notice v4-notice"></p><div class="cos-chart"></div>';
        }
        var notice = ctx.body.querySelector('.v4-notice'), why = COS.basemap.notice(ctx, 'the track is');
        notice.textContent = why;
        notice.style.display = why ? '' : 'none';
        var el = ctx.body.querySelector('.cos-chart');

        /* One line per zone; each point is [x, y, tick, zone, lon, lat] with x, y in map units on the map, else longitude and latitude */
        function track(at) {
            return Z.map(function (z, i) {
                return { name: z.label, type: 'line', showSymbol: true, symbolSize: 5, z: 10, lineStyle: { width: 3, color: COS.enc.color(z) },
                    itemStyle: { color: COS.enc.color(z) },
                    data: pts.reduce(function (out, p, k) { if (p[3] === i) out.push(at(p, k).concat([p[2], p[3], p[0], p[1]])); return out; }, []) };
            });
        }
        var tooltip = { trigger: 'item', confine: true, backgroundColor: COS.token('--surface-2'), borderColor: COS.token('--line'), textStyle: { color: COS.token('--text-primary') }, formatter: function (q) {
            if (q.seriesType === 'custom') return q.seriesName + (q.data && q.data.n ? '<br>' + COS.esc(q.data.n) : '');
            return 'Tick ' + COS.fmt.int(q.data[2]) + '<br>' + q.data[5].toFixed(5) + '° N, ' + q.data[4].toFixed(5) + '° E<br>' + Z[q.data[3]].label; } };

        function draw() {
            if (!el.clientWidth) return;		/* hidden tab: drawn when shown (COS.mapWatch) */
            if (onmap) { drawMap(); return; }
            var f = COS.mapFrame(el, pts), py = (f.y[1] - f.y[0]) / 2;
            var dp = Math.min(6, Math.max(2, Math.ceil(-Math.log10(py)) + 1)), deg = function (v) { return v.toFixed(dp) + '°'; };
            var inst = COS.chart(ctx, 'map', el, {
                grid: f.grid,
                tooltip: tooltip,
                legend: { top: 0, data: Z.map(function (z) { return z.label; }), textStyle: { color: COS.token('--text-secondary') } },
                xAxis: COS.axis('Longitude', { type: 'value', min: f.x[0], max: f.x[1], nameGap: 24, axisLabel: { formatter: deg, showMinLabel: false, showMaxLabel: false, color: COS.token('--text-secondary') } }),
                yAxis: COS.axis('Latitude', { type: 'value', min: f.y[0], max: f.y[1], nameGap: 76, axisLabel: { formatter: deg, showMinLabel: false, showMaxLabel: false, color: COS.token('--text-secondary') } }),
                dataZoom: [{ type: 'inside', xAxisIndex: 0, filterMode: 'none' }, { type: 'inside', yAxisIndex: 0, filterMode: 'none' }],
                series: track(function (p) { return [p[0], p[1]]; })
            }, { height: f.height });
            COS.mapHeight(inst, el, f.height);
        }

        /* The run's map opened on the track; layers can be hidden from the legend */
        function drawMap() {
            var xy = pts.map(function (p) { return map.project(p[0], p[1]); });
            var f = COS.basemap.frame(map, el, xy);
            var series = COS.basemap.series(map).concat(track(function (p, k) { return xy[k]; }));
            var inst = COS.chart(ctx, 'map', el, {
                grid: f.grid,
                tooltip: tooltip,
                legend: { top: 0, itemGap: 16, data: series.map(function (s) { return s.name; }), selected: ctx.state.hidden || {},
                          textStyle: { color: COS.token('--text-secondary') } },
                xAxis: f.xAxis, yAxis: f.yAxis, dataZoom: f.dataZoom,
                series: series
            }, { height: f.height });
            COS.mapHeight(inst, el, f.height);
            COS.basemap.keepLegend(ctx, inst);
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
