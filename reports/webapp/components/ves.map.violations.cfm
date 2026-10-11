<!--: V36 ves.map.violations (DASH.075, REQ.052) — where this vessel broke rules: one marker per violation at its recorded position. -->
<cfparam name="composed" default="0">
<cfif composed EQ 0><cfinclude template="../shared/open.cfm"></cfif>
<cfoutput><section data-component="ves.map.violations" data-endpoint="#cos_root#/data/ves.map.violations.data.cfm"></section></cfoutput>
<script>
(function () {
    var S = COS.enc.sources, picked = null;		/* clause filter: null shows every clause */

    COS.component('ves.map.violations', {
        code: 'V36', title: 'Where this vessel broke rules', hint: 'Each violation where it happened. Shape shows who raised it.', vessel: true,
        mockReason: 'no positioned violations for this vessel',
        mock: function () {
            var r = COS.mock.rng('V36'), rows = [], lat = 1.20, lon = 103.75, src = ['examiner', 'colreg', 'local'];
            var cl = ['grounding.contact', 'COLREG.Rule15/KeepClear', 'COLREG.Rule13.a', 'speed.limit'];
            for (var i = 0; i < 40; i++) {
                lon += (r() - 0.3) * 0.004; lat += (r() - 0.4) * 0.003;
                var k = Math.floor(r() * 4);
                rows.push({ lon: lon, lat: lat, tick: i * 25, source: src[k % 3], clause: cl[k], zone: 'territorial_waters', concern: 'safety', penalty: 50 + Math.round(r() * 100) });
            }
            return { pts: rows, unpositioned: 0 };
        },
        render: function (ctx, data) {
            var pts = data.pts || data.rows.map(function (r) {
                var p = COS.morton(r[0]);
                return { gps: r[0], lon: p[0], lat: p[1], tick: r[1], source: r[2], clause: r[3], zone: r[4], concern: r[5], penalty: r[6] };
            });
            ctx.pts = pts;

            /* Clause list with counts; the reader's selection survives polls */
            var counts = {};
            pts.forEach(function (p) { counts[p.clause] = (counts[p.clause] || 0) + 1; });
            var clauses = Object.keys(counts).sort(function (a, b) { return counts[b] - counts[a]; });
            if (picked) Object.keys(picked).forEach(function (c) { if (!(c in counts)) delete picked[c]; });

            var map = COS.basemap.load(ctx), onmap = COS.basemap.usable(map);
            if (!ctx.body.querySelector('.cos-chart')) {
                ctx.body.innerHTML = '<p class="cos-notice v36-notice"></p>' +
                    '<div class="v36-clauses" style="display:flex;flex-wrap:wrap;gap:4px 12px;margin:4px 0 8px;font-size:12px"></div><div class="cos-chart"></div>';
            }
            var notice = ctx.body.querySelector('.v36-notice'), why = COS.basemap.notice(ctx, 'violations are');
            notice.textContent = why;
            notice.style.display = why ? '' : 'none';
            var list = ctx.body.querySelector('.v36-clauses');
            list.innerHTML = clauses.map(function (c) {
                var on = !picked || picked[c];
                return '<label style="cursor:pointer"><input type="checkbox" data-clause="' + COS.esc(c) + '"' + (on ? ' checked' : '') + '> ' +
                    COS.esc(c) + ' <span style="color:var(--text-secondary)">(' + counts[c] + ')</span></label>';
            }).join('');
            list.onchange = function (e) {
                var c = e.target.getAttribute('data-clause');
                if (!picked) { picked = {}; clauses.forEach(function (k) { picked[k] = true; }); }
                picked[c] = e.target.checked;
                draw();
            };

            function draw() {
                var shown = pts.filter(function (p) { return !picked || picked[p.clause]; });
                var el = ctx.body.querySelector('.cos-chart');
                if (!el.clientWidth) return;		/* hidden tab: drawn when shown (COS.mapWatch) */
                if (onmap) { drawMap(shown, el); return; }

                /* Equal ground scale over every violation, so filtering does not move the map */
                var f = COS.mapFrame(el, pts.map(function (p) { return [p.lon, p.lat]; }));
                var cx = (f.x[0] + f.x[1]) / 2, cy = (f.y[0] + f.y[1]) / 2, px = (f.x[1] - f.x[0]) / 2, py = (f.y[1] - f.y[0]) / 2;
                var dp = Math.min(6, Math.max(2, Math.ceil(-Math.log10(py)) + 1)), deg = function (v) { return v.toFixed(dp) + '°'; };

                /* One series per source; violations at the same position combine into one marker with a count */
                var series = S.map(function (s) {
                    var at = {};
                    shown.forEach(function (p) {
                        if (COS.enc.sourceFamily(p.source) !== s.key) return;
                        var key = p.gps || (p.lon.toFixed(6) + ',' + p.lat.toFixed(6));
                        (at[key] = at[key] || []).push(p);
                    });
                    var items = Object.keys(at).map(function (key) {
                        var g = at[key];
                        return { value: [g[0].lon, g[0].lat, g.length], group: g };
                    });
                    return { name: s.label, type: 'scatter', symbol: s.symbol, itemStyle: { color: COS.enc.color(s) },
                        symbolSize: function (v) { return 9 + Math.min(14, 3 * Math.log2(v[2])); },
                        label: { show: true, formatter: function (q) { return q.value[2] > 1 ? q.value[2] : ''; }, position: 'right', fontSize: 11,
                                 color: COS.token('--text-secondary') },
                        data: items };
                });

                var inst0 = COS.chart(ctx, 'map', el, {
                    grid: f.grid,
                    legend: { top: 0, itemGap: 24, data: S.map(function (s) { return s.label; }), textStyle: { color: COS.token('--text-secondary') } },
                    tooltip: { trigger: 'item', confine: true, backgroundColor: COS.token('--surface-2'), borderColor: COS.token('--line'), textStyle: { color: COS.token('--text-primary') }, formatter: function (q) {
                        var g = q.data.group, head = g.length > 1 ? g.length + ' violations here<br>' : '';
                        return head + g.slice(0, 6).map(function (p) {
                            return 'Tick ' + COS.fmt.int(p.tick) + ' · ' + COS.esc(p.clause) + ' · ' + COS.esc(COS.enc.find(S, COS.enc.sourceFamily(p.source)).label) +
                                '<br>' + (p.penalty === null ? 'unpriced' : COS.fmt.int(p.penalty) + ' points') + ' · ' + COS.esc(p.zone.replace('_', ' ')) + ' · ' + COS.esc(p.concern);
                        }).join('<br>') + (g.length > 6 ? '<br>… ' + (g.length - 6) + ' more' : '');
                    } },
                    xAxis: COS.axis('Longitude', { type: 'value', min: cx - px, max: cx + px, nameGap: 24,
                        axisLabel: { formatter: deg, showMinLabel: false, showMaxLabel: false, color: COS.token('--text-secondary') } }),
                    yAxis: COS.axis('Latitude', { type: 'value', min: cy - py, max: cy + py, nameGap: 76,
                        axisLabel: { formatter: deg, showMinLabel: false, showMaxLabel: false, color: COS.token('--text-secondary') } }),
                    dataZoom: [{ type: 'inside', xAxisIndex: 0, filterMode: 'none' }, { type: 'inside', yAxisIndex: 0, filterMode: 'none' }],
                    series: series
                }, { height: f.height, onClick: function (q) {
                    var g = q.data && q.data.group;
                    if (!g) return;
                    COS.state.set({ t: g[0].tick }); COS.emit('time-cursor', { t: g[0].tick });
                } });
                COS.mapHeight(inst0, el, f.height);
            }
            /* One series per source; violations at the same position combine into one marker with a count */
            function markers(shown, at2) {
                return S.map(function (s) {
                    var at = {};
                    shown.forEach(function (p) {
                        if (COS.enc.sourceFamily(p.source) !== s.key) return;
                        var key = p.gps || (p.lon.toFixed(6) + ',' + p.lat.toFixed(6));
                        (at[key] = at[key] || []).push(p);
                    });
                    return { name: s.label, type: 'scatter', symbol: s.symbol, itemStyle: { color: COS.enc.color(s), borderColor: '#ffffff', borderWidth: 1 }, z: 10,
                        symbolSize: function (v) { return 9 + Math.min(14, 3 * Math.log2(v[2])); },
                        label: { show: true, formatter: function (q) { return q.value[2] > 1 ? q.value[2] : ''; }, position: 'right', fontSize: 11,
                                 color: COS.token('--text-primary') },
                        labelLayout: { hideOverlap: true },
                        data: Object.keys(at).map(function (key) { var g = at[key], xy = at2(g[0]); return { value: [xy[0], xy[1], g.length], group: g }; }) };
                });
            }

            function tip(q) {
                var g = q.data && q.data.group;
                if (!g) return q.seriesName + (q.data && q.data.n ? '<br>' + COS.esc(q.data.n) : '');
                var head = g.length > 1 ? g.length + ' violations here<br>' : '';
                return head + g.slice(0, 6).map(function (p) {
                    return 'Tick ' + COS.fmt.int(p.tick) + ' · ' + COS.esc(p.clause) + ' · ' + COS.esc(COS.enc.find(S, COS.enc.sourceFamily(p.source)).label) +
                        '<br>' + (p.penalty === null ? 'unpriced' : COS.fmt.int(p.penalty) + ' points') + ' · ' + COS.esc(p.zone.replace('_', ' ')) + ' · ' + COS.esc(p.concern);
                }).join('<br>') + (g.length > 6 ? '<br>… ' + (g.length - 6) + ' more' : '');
            }

            /* The run's map in map units, opened on the violations at equal ground scale; layers can be hidden from the legend */
            function drawMap(shown, el) {
                pts.forEach(function (p) { if (!p.xy) p.xy = map.project(p.lon, p.lat); });
                var f = COS.basemap.frame(map, el, pts.map(function (p) { return p.xy; }));
                var series = COS.basemap.series(map).concat(markers(shown, function (p) { return p.xy; }));

                var inst = COS.chart(ctx, 'map', el, {
                    grid: f.grid,
                    legend: { top: 0, itemGap: 16, data: series.map(function (s) { return s.name; }), selected: ctx.state.hidden || {},
                              textStyle: { color: COS.token('--text-secondary') } },
                    tooltip: { trigger: 'item', confine: true, backgroundColor: COS.token('--surface-2'), borderColor: COS.token('--line'),
                               textStyle: { color: COS.token('--text-primary') }, formatter: tip },
                    xAxis: f.xAxis, yAxis: f.yAxis, dataZoom: f.dataZoom,
                    series: series
                }, { height: f.height, trigger: 'item', onClick: function (q) {
                    var g = q.data && q.data.group;
                    if (!g) return;
                    COS.state.set({ t: g[0].tick }); COS.emit('time-cursor', { t: g[0].tick });
                } });
                COS.mapHeight(inst, el, f.height);
                COS.basemap.keepLegend(ctx, inst);
            }

            COS.mapWatch(ctx.body.querySelector('.cos-chart'), draw);
            draw();
        },
        caption: function (ctx, data) {
            var n = (data.pts || data.rows).length, u = data.unpositioned || 0;
            return n + ' violation' + (n === 1 ? '' : 's') + ', ' + u + ' without a recorded position.';
        }
    });
})();
</script>
<cfif composed EQ 0><cfinclude template="../shared/close.cfm"></cfif>
