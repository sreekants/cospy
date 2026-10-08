<!--: V36 ves.map.violations (DASH.075, REQ.052) — where this vessel broke rules: one marker per violation at its recorded position. -->
<cfparam name="composed" default="0">
<cfif composed EQ 0><cfinclude template="../shared/open.cfm"></cfif>
<cfoutput><section data-component="ves.map.violations" data-endpoint="#cos_root#/data/ves.map.violations.data.cfm"></section></cfoutput>
<script>
(function () {
    var S = COS.enc.sources, picked = null;		/* clause filter: null shows every clause */

    /* Morton code (60 bits, longitude on the upper bit of each pair) to the centre of its cell */
    function axis(v) {
        var out = 0n;
        for (var i = 0n; i < 30n; i++) out += ((v >> (2n * i)) & 1n) * 2n ** i;	/* no left shift: the engine rewrites it */
        return Number(out);
    }
    function decode(code) {
        var v = BigInt(code), cell = Math.pow(2, 30);
        return [-180 + (axis(v >> 1n) + 0.5) * 360 / cell, -90 + (axis(v) + 0.5) * 180 / cell];
    }

    /* Base map (DASH.065): polygons in map units, styled after the map generator's render table */
    var DEPTH = [[500, '#143E78'], [200, '#225CA0'], [100, '#3C7EC4'], [50, '#5C9EDB'], [20, '#80BAEA'], [10, '#A0CEF2'], [5, '#BADEF7'], [0, '#D6ECFA']];
    var ZONES = { 301000: ['Harbour', '#2896AA'], 302000: ['Waterway', '#78D2EB'], 303000: ['TSS', '#5A64DC'], 304000: ['TSS', '#5A64DC'],
        305000: ['TSS', '#3C32A0'], 306000: ['TSS', '#3C32A0'] };
    var LAYERS = ['Depth', 'Land', 'Jurisdiction', 'Exclusion', 'Waterway', 'Harbour', 'TSS', 'Other zones', 'Sky'];
    var SWATCH = { 'Depth': '#5C9EDB', 'Land': '#D9CFAE', 'Jurisdiction': '#5A6E96', 'Exclusion': '#788CAA', 'Waterway': '#78D2EB',
        'Harbour': '#2896AA', 'TSS': '#5A64DC', 'Other zones': '#8CAADC', 'Sky': '#B4BAC4' };

    function rgba(hex, a) {
        var n = parseInt(hex.slice(1), 16);
        return 'rgba(' + Math.floor(n / 65536) + ',' + (Math.floor(n / 256) % 256) + ',' + (n % 256) + ',' + a + ')';	/* no bit shifts: the engine rewrites them */
    }
    function style(p) {
        var t = p.t;
        if (p.db === 'land') return { group: 'Land', fill: '#EDE6D3', stroke: '#B9AE8E', width: 0.6 };
        if (p.db === 'sky') return { group: 'Sky', fill: 'rgba(180,186,196,0.2)', stroke: '#B4BAC4', width: 0.8 };
        if (t === 100000 || (t >= 111000 && t <= 117000)) {
            var d = p.l || 0, c = DEPTH[DEPTH.length - 1][1];
            for (var i = 0; i < DEPTH.length; i++) { if (d >= DEPTH[i][0]) { c = DEPTH[i][1]; break; } }
            return { group: 'Depth', fill: c, stroke: c, width: 0.3 };
        }
        if (t >= 201000 && t <= 204000) return { group: 'Jurisdiction', fill: 'none', stroke: '#5A6E96', width: 1, dash: [4, 3] };
        if (t === 205000) return { group: 'Exclusion', fill: 'rgba(120,140,170,0.25)', stroke: '#788CAA', width: 1 };
        var z = ZONES[t] || ['Other zones', '#8CAADC'];
        return { group: z[0], fill: rgba(z[1], 0.35), stroke: z[1], width: 1 };
    }

    /* Latitude/longitude to map units through the run's georeference; null for a CRS other than UTM */
    function projector(g) {
        var m = /^EPSG:32([67])(\d\d)$/.exec(g.crs || '');
        if (!m || !window.proj4) return null;
        var def = '+proj=utm +zone=' + (+m[2]) + (m[1] === '7' ? ' +south' : '') + ' +datum=WGS84 +units=m +no_defs';
        var south = g.axis !== 'north';
        return function (lon, lat) {
            var en = proj4('WGS84', def, [lon, lat]);
            return [(en[0] - g.e0) / g.mx, south ? (g.n0 - en[1]) / g.my : (en[1] - g.n0) / g.my];
        };
    }

    /* Fetched once per run; null when the run names no usable map */
    function basemap(ctx, done) {
        var key = ctx.meta.case;
        if (ctx.mode !== 'live' || !key) return null;
        if (ctx.map && ctx.map.key === key) return ctx.map.ready ? ctx.map : null;
        ctx.map = { key: key, ready: false };
        COS.fetch(COS.root + '/data/map.layers.data.cfm?case=' + encodeURIComponent(key)).then(function (res) {
            var d = res.data, layers = (d.rows || []).filter(Boolean), b = String(d.georef.bounds || '').split(',').map(Number);
            var groups = {};
            layers.forEach(function (p) {
                p.s = style(p);
                p.pts = String(p.p).split(' ').filter(Boolean).map(function (xy) { return xy.split(',').map(Number); });
                (groups[p.s.group] = groups[p.s.group] || []).push(p);
            });
            ctx.map = { key: key, ready: true, found: layers.length > 0 && b.length === 4 && b.every(isFinite),
                        bounds: b, groups: groups, project: projector(d.georef), south: d.georef.axis !== 'north', refused: d.refused || 0,
                        my: (+d.georef.my || 1) / (+d.georef.mx || 1) };
            done();
        }).catch(function () { ctx.map = { key: key, ready: true, found: false, refused: 0 }; done(); });
        return null;
    }

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
                var p = decode(r[0]);
                return { gps: r[0], lon: p[0], lat: p[1], tick: r[1], source: r[2], clause: r[3], zone: r[4], concern: r[5], penalty: r[6] };
            });
            ctx.pts = pts;

            /* Clause list with counts; the reader's selection survives polls */
            var counts = {};
            pts.forEach(function (p) { counts[p.clause] = (counts[p.clause] || 0) + 1; });
            var clauses = Object.keys(counts).sort(function (a, b) { return counts[b] - counts[a]; });
            if (picked) Object.keys(picked).forEach(function (c) { if (!(c in counts)) delete picked[c]; });

            var map = basemap(ctx, ctx.rerender), pending = ctx.mode === 'live' && ctx.map && !ctx.map.ready;
            var onmap = !!(map && map.found && map.project);
            if (!ctx.body.querySelector('.cos-chart')) {
                ctx.body.innerHTML = '<p class="cos-notice v36-notice"></p>' +
                    '<div class="v36-clauses" style="display:flex;flex-wrap:wrap;gap:4px 12px;margin:4px 0 8px;font-size:12px"></div><div class="cos-chart"></div>';
            }
            var notice = ctx.body.querySelector('.v36-notice'), why = '';
            if (ctx.mode !== 'live') why = '';
            else if (pending) why = 'Loading the map of this run…';
            else if (map && map.found && !map.project) why = 'This map has no GPS reference, so violations are drawn on latitude and longitude only.';
            else if (!onmap) why = 'The map of this run was not found, so violations are drawn on latitude and longitude only' +
                (map && map.refused ? ' (its recorded path was refused).' : '.');
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
                var b = map.bounds, w = el.clientWidth, top = 32, bottom = 8;
                var xs = pts.map(function (p) { return p.xy[0]; }), ys = pts.map(function (p) { return p.xy[1]; });
                var x0 = Math.min.apply(null, xs), x1 = Math.max.apply(null, xs), y0 = Math.min.apply(null, ys), y1 = Math.max.apply(null, ys);
                /* spans in ground units (x metres per unit taken as 1, y scaled by map.my); the plot height follows the width */
                var gx = Math.max(x1 - x0, 10) * 1.4, gy = Math.max(y1 - y0, 10) * 1.4 * map.my;
                var ph = Math.min(600, Math.max(320, w * gy / gx));
                if (gx / gy > w / ph) gy = gx * ph / w; else gx = gy * w / ph;
                /* ECharts clips a zoom window to the axis range, which would change the aspect: keep it inside the map and shorten the plot instead */
                var bw = b[2] - b[0], bh = (b[3] - b[1]) * map.my;
                if (gx > bw) { gx = bw; gy = gx * ph / w; }
                if (gy > bh) { gy = bh; gx = gy * w / ph; }
                ph = w * gy / gx;
                gy /= map.my;
                var h = Math.round(ph) + top + bottom;
                var cx = Math.min(Math.max((x0 + x1) / 2, b[0] + gx / 2), b[2] - gx / 2), cy = Math.min(Math.max((y0 + y1) / 2, b[1] + gy / 2), b[3] - gy / 2);

                var series = LAYERS.filter(function (g) { return map.groups[g]; }).map(function (g) {
                    var polys = map.groups[g];
                    return { name: g, type: 'custom', coordinateSystem: 'cartesian2d', clip: true, silent: g === 'Depth', z: 1,
                        itemStyle: { color: SWATCH[g] },
                        data: polys.map(function (p) { return { value: [p.pts[0][0], p.pts[0][1]], n: p.n }; }),
                        renderItem: function (params, api) {
                            var p = polys[params.dataIndex];
                            return { type: 'polygon', shape: { points: p.pts.map(function (q) { return api.coord(q); }) },
                                     style: { fill: p.s.fill, stroke: p.s.stroke, lineWidth: p.s.width, lineDash: p.s.dash || null } };
                        } };
                }).concat(markers(shown, function (p) { return p.xy; }));

                var inst = COS.chart(ctx, 'map', el, {
                    grid: { left: 0, right: 0, top: top, bottom: bottom },
                    legend: { top: 0, itemGap: 16, data: series.map(function (s) { return s.name; }), selected: ctx.state.hidden || {},
                              textStyle: { color: COS.token('--text-secondary') } },
                    tooltip: { trigger: 'item', confine: true, backgroundColor: COS.token('--surface-2'), borderColor: COS.token('--line'),
                               textStyle: { color: COS.token('--text-primary') }, formatter: tip },
                    xAxis: { type: 'value', min: b[0], max: b[2], show: false },
                    yAxis: { type: 'value', min: b[1], max: b[3], inverse: map.south, show: false },
                    dataZoom: [{ type: 'inside', xAxisIndex: 0, filterMode: 'none', startValue: cx - gx / 2, endValue: cx + gx / 2 },
                               { type: 'inside', yAxisIndex: 0, filterMode: 'none', startValue: cy - gy / 2, endValue: cy + gy / 2 }],
                    series: series
                }, { height: h, trigger: 'item', onClick: function (q) {
                    var g = q.data && q.data.group;
                    if (!g) return;
                    COS.state.set({ t: g[0].tick }); COS.emit('time-cursor', { t: g[0].tick });
                } });
                COS.mapHeight(inst, el, h);
                if (inst && !ctx.state.legendHooked) {
                    ctx.state.legendHooked = true;
                    inst.on('legendselectchanged', function (e) { ctx.state.hidden = e.selected; });
                }
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
