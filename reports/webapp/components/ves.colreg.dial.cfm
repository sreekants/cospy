<!--: V38 ves.colreg.dial (DASH.077, REQ.066) — which COLREG duties this voyage was judged on, on the coverage dial's geometry. -->
<cfparam name="composed" default="0">
<cfif composed EQ 0><cfinclude template="../shared/open.cfm"></cfif>
<cfoutput><section data-component="ves.colreg.dial" data-endpoint="#cos_root#/data/ves.colreg.dial.data.cfm"></section></cfoutput>
<script>
(function () {
    var STATES = [
        { key: 'finding', label: 'Finding', cls: '' },
        { key: 'not_recorded', label: 'Not recorded', cls: 'hatch hatch-heavy' },
        { key: 'applied_not_judged', label: 'Applied, not judged', cls: 'hatch' },
        { key: 'judged_clear', label: 'Judged, no finding', cls: '' },
        { key: 'not_applicable', label: 'Did not arise', cls: '' },
        { key: 'not_assessed', label: 'Not assessed', cls: 'outline' }
    ];
    var RANK = {}; STATES.forEach(function (s, i) { RANK[s.key] = i; });
    var KINDS = ['crossing', 'give_way', 'head_on', 'overtaking', 'stand_on'];
    /* Prototype applicability (REQ-066-03, proposal p1): encounter kind -> rules whose situation it is */
    var APPLY = { version: 'p1', crossing: ['15', '17'], give_way: ['16'], head_on: ['14'], overtaking: ['13', '17'], stand_on: ['17'] };
    var SCOPE = ['13', '14', '15', '16', '17'];				/* rules whose situation the store can tell */
    var JUDGED = ['12', '13', '14', '15', '18', '19', '35'];	/* L4 or above in COLREG.COVERAGE.md (2026-10-18) */

    function derive(geo, data) {
        var arose = {}, standOn = data.enc.some(function (e) { return e[0] === 4; });
        data.enc.forEach(function (e) {
            (APPLY[KINDS[e[0]]] || []).forEach(function (r) { (arose[r] = arose[r] || []).push({ t: e[2], t1: e[3], id: e[1], kind: KINDS[e[0]] }); });
        });
        var single = {};
        geo.paragraphs.forEach(function (p) { if (p.paragraph === '—') single[p.rule] = true; });
        var byPara = {}, byRule = {};
        data.rows.forEach(function (f) {
            var c = COS.colreg.parse(f.clause);
            if (!c) return;
            var k = c.para || (single[c.rule] ? c.rule : null);
            if (k) (byPara[k] = byPara[k] || []).push(f);
            else (byRule[c.rule] = byRule[c.rule] || []).push(f);
        });
        var rules = [], at = {};
        geo.paragraphs.forEach(function (p) {
            var key = p.paragraph === '—' ? p.rule : p.paragraph, f = byPara[key] || [], eps = COS.colreg.episodes(f), st, inferred = false;
            if (eps.length) st = 'finding';
            else if (arose[p.rule]) {
                if (p.rule === '17' && !standOn) st = 'not_recorded';
                else if (JUDGED.indexOf(p.rule) >= 0) { st = 'judged_clear'; inferred = true; }
                else st = 'applied_not_judged';
            } else st = SCOPE.indexOf(p.rule) >= 0 ? 'not_applicable' : 'not_assessed';
            var node = { key: key, p: p, state: st, inferred: inferred, eps: eps, rows: f, arose: arose[p.rule] || [] };
            var r = at[p.rule];
            if (!r) {
                var re = COS.colreg.episodes(byRule[p.rule] || []);
                r = at[p.rule] = { rule: p.rule, title: p.title, part: p.part, kids: [], eps: re, ruleOnly: re, state: re.length ? 'finding' : null, arose: arose[p.rule] || [] };
                rules.push(r);
            }
            r.kids.push(node);
            if (!r.state || RANK[st] < RANK[r.state]) r.state = st;
        });
        rules.forEach(function (r) { r.kids.forEach(function (k) { r.eps = r.eps.concat(k.eps); }); r.eps.sort(function (a, b) { return a.t0 - b.t0; }); });
        return rules;
    }

    function style(st, inferred, eps) {
        var tok = COS.token, hatch = { symbol: 'rect', dashArrayX: [1, 0], dashArrayY: [1, 3], rotation: -Math.PI / 4, color: tok('--state-hatch') };
        if (st === 'finding') return { color: tok('--state-finding-' + Math.min(4, Math.max(1, eps <= 2 ? eps : eps <= 4 ? 3 : 4))) };
        if (st === 'not_recorded') return { color: tok('--state-blank'), decal: hatch, borderWidth: 2.5, borderColor: tok('--state-hatch') };
        if (st === 'applied_not_judged') return { color: tok('--state-blank'), decal: hatch };
        if (st === 'judged_clear') return inferred ? { color: tok('--state-clear-inferred'), decal: { symbol: 'circle', symbolSize: 0.4, dashArrayX: 4, dashArrayY: 4, color: tok('--state-clear') } } : { color: tok('--state-clear') };
        if (st === 'not_applicable') return { color: tok('--state-na') };
        return { color: tok('--state-blank'), borderColor: tok('--line') };
    }

    function label(st) { return STATES[RANK[st]].label; }

    function tip(n) {
        var h = '<b>' + COS.esc(n.rule ? (/^Annex/.test(n.rule) ? n.rule : 'Rule ' + n.rule) : (n.p.paragraph === '—' ? 'Rule ' + n.p.rule : 'Rule ' + n.p.paragraph)) + '</b> ' +
            COS.esc(n.rule ? n.title : n.p.title);
        if (!n.rule && n.p.label !== n.p.title) h += '<br><span style="opacity:.8">' + COS.esc(n.p.label) + '</span>';
        h += '<br>State: ' + COS.esc(label(n.state)) + (n.inferred ? ' (inferred from coverage and encounters)' : '');
        if (n.eps.length) {
            var cl = {};
            n.eps.forEach(function (e) { cl[e.clause] = (cl[e.clause] || 0) + 1; });
            h += '<br>Finding episodes: ' + n.eps.length + ', first at ' + COS.fmt.time(n.eps[0].t0) +
                Object.keys(cl).map(function (c) { return '<br>&nbsp;· <code>' + COS.esc(c) + '</code> × ' + cl[c]; }).join('');
            var pts = 0; n.eps.forEach(function (e) { e.rows.forEach(function (r) { pts += r.pts; }); });
            h += '<br>Penalty: ' + COS.fmt.pts(pts);
        }
        if (n.ruleOnly && n.ruleOnly.length) h += '<br>' + n.ruleOnly.length + ' episode(s) not mapped to a paragraph';
        if (n.arose.length) h += '<br>Situation arose in ' + n.arose.length + ' encounter record(s)';
        return h;
    }

    COS.component('ves.colreg.dial', {
        code: 'V38', title: 'Which COLREG duties this voyage was judged on',
        hint: 'Each segment is one paragraph of COLREG. Hatched: the situation arose but was not judged.', vessel: true,
        empty: function (data) { return !(data.rows && data.rows.length) && !(data.enc && data.enc.length); },
        mockReason: 'no encounters or COLREG findings for this vessel',
        mock: function () {
            return { rows: [{ id: 1, t: 300, clause: 'COLREG.Rule14.a', pts: 50 }, { id: 2, t: 310, clause: 'COLREG.Rule14.a', pts: 50 },
                            { id: 3, t: 900, clause: 'COLREG.Rule15/CrossAstern', pts: 50 }, { id: 4, t: 1500, clause: 'COLREG.Rule13.b', pts: 50 }],
                     enc: [[0, 1, 880, 920, 9000002], [1, 2, 880, 920, 9000002], [3, 3, 1480, 1520, 9000003]] };
        },
        render: function (ctx, data) {
            data.enc = data.enc || [];
            if (!ctx.state.geo) {
                if (!ctx.state.loading) {
                    ctx.state.loading = true;
                    COS.colreg.file('colreg.paragraphs.json').then(function (g) { ctx.state.geo = g; ctx.rerender(); })
                        .catch(function (e) { ctx.state.geoError = e.message; ctx.rerender(); });
                }
                COS.ui.notice(ctx.body, ctx.state.geoError ? 'The paragraph list could not be loaded (' + ctx.state.geoError + ').' : 'Loading the paragraph list…', ctx.state.geoError ? 'cos-error' : '');
                return;
            }
            var geo = ctx.state.geo;
            if (String(geo.version) !== COS.colreg.GEOMETRY) {
                COS.ui.notice(ctx.body, 'Paragraph list version ' + geo.version + ' differs from the version this dial is drawn for (' + COS.colreg.GEOMETRY + '); no dial is drawn.', 'cos-error');
                return;
            }
            var rules = derive(geo, data);
            ctx.state.rules = rules;
            if (!ctx.body.querySelector('.cos-chart')) ctx.body.innerHTML = '<div class="cos-chart"></div><div class="cos-legend"></div>';
            var el = ctx.body.querySelector('.cos-chart');

            var count = {}, paras = [];
            STATES.forEach(function (s) { count[s.key] = 0; });
            rules.forEach(function (r) { r.kids.forEach(function (k) { count[k.state]++; paras.push(k); }); });
            var arose = paras.length - count.not_applicable - count.not_assessed;
            var inferred = paras.filter(function (k) { return k.inferred; }).length;
            var eps = COS.colreg.episodes(data.rows).length;
            ctx.state.summary = { arose: arose, judged: count.finding + count.judged_clear, inferred: inferred, eps: eps };

            ctx.body.querySelector('.cos-legend').innerHTML = STATES.map(function (s) {
                var c = s.key === 'finding' ? COS.token('--state-finding-3') : s.key === 'judged_clear' ? COS.token('--state-clear') : style(s.key, false, 0).color;
                return '<span class="' + (count[s.key] ? '' : 'dim') + '"><i class="swatch ' + s.cls + '" style="background-color:' + c + '"></i>' +
                    COS.esc(s.label) + ' (' + count[s.key] + ')</span>';
            }).join('') + '<span><i class="swatch dotted" style="background-color:' + COS.token('--state-clear-inferred') + '"></i>Judged, no finding — inferred (' + inferred + ')</span>';

            function draw() {
                if (!el.clientWidth) return;		/* hidden tab: drawn when shown (COS.mapWatch) */
                var side = Math.max(240, Math.min(480, el.clientWidth));
                var inst = ctx.charts.dial;
                if (inst && !inst.isDisposed() && inst.getHeight() !== side) { inst.dispose(); delete ctx.charts.dial; }
                var share = arose ? Math.round(100 * ctx.state.summary.judged / arose) : null;
                var centre = arose ? share + '%\n{s|of the duties that arose\nwere judged' + (inferred ? '\n(' + Math.round(100 * inferred / arose) + '% inferred)' : '') + '}\n{n|' + eps + ' finding episode' + (eps === 1 ? '' : 's') + '}'
                                   : '{s|No COLREG situation\nrecorded}';
                inst = COS.chart(ctx, 'dial', el, {
                    series: [{
                        type: 'sunburst', startAngle: 90, clockwise: true, sort: null, nodeClick: false, radius: ['30%', '96%'],
                        emphasis: { focus: 'ancestor' },
                        levels: [{}, { r0: '30%', r: '58%', label: { rotate: 'radial', fontSize: 9, minAngle: 5, color: COS.token('--text-primary') } },
                                     { r0: '58%', r: '96%', label: { show: false } }],
                        itemStyle: { borderColor: COS.token('--surface-1'), borderWidth: 0.5 },
                        tooltip: { formatter: function (p) { return p.data && p.data.n ? tip(p.data.n) : ''; } },
                        data: rules.map(function (r) {
                            return { name: /^Annex/.test(r.rule) ? r.rule.replace('Annex ', 'A') : r.rule, n: r,
                                itemStyle: style(r.state, r.kids.every(function (k) { return k.inferred || k.state !== 'judged_clear'; }) && r.state === 'judged_clear', r.eps.length),
                                children: r.kids.map(function (k) {
                                    return { name: k.key === r.rule ? 'Rule ' + r.rule : k.key, value: k.p.weight, n: k, itemStyle: style(k.state, k.inferred, k.eps.length) };
                                }) };
                        })
                    }],
                    graphic: [{ type: 'text', left: 'center', top: 'middle', silent: true, style: {
                        text: centre, align: 'center', fill: COS.token('--text-primary'), font: '600 20px system-ui, sans-serif',
                        rich: { s: { fontSize: 10, fontWeight: 400, fill: COS.token('--text-secondary'), lineHeight: 13 }, n: { fontSize: 11, fontWeight: 600, fill: COS.token('--text-primary'), lineHeight: 18 } } } }]
                }, { height: side, trigger: 'item', onClick: function (p) {
                    var n = p.data && p.data.n;
                    if (!n) return;
                    var stops = n.eps.length ? n.eps.map(function (e) { return e.t0; }) : n.arose.map(function (a) { return a.t; });
                    if (!stops.length) return;
                    var same = ctx.state.clicked === p.name;
                    ctx.state.step = same ? (ctx.state.step + 1) % stops.length : 0;
                    ctx.state.clicked = p.name;
                    var t = Math.round(stops[ctx.state.step]);
                    COS.state.set({ t: t }); COS.emit('time-cursor', { t: t, from: 'ves.colreg.dial' });
                } });
                if (inst) { inst.resize({ width: el.clientWidth, height: side }); mark(); }
            }
            COS.mapWatch(el, draw);
            draw();
        },
        flags: function (ctx) {
            var f = [{ ticket: 'REQ.037-06', text: 'Judged, no finding is inferred from the coverage levels and the encounters until clause states are recorded.' }];
            var s = ctx.state.summary;
            if (s && ctx.state.rules && ctx.state.rules.some(function (r) { return r.rule === '17' && r.state === 'not_recorded'; }))
                f.push({ ticket: 'REQ.067', text: 'The stand-on side of an encounter is not recorded, so Rule 17 cannot be judged.' });
            return f;
        },
        caption: function (ctx) {
            var g = ctx.state.geo;
            return 'Paragraph list v' + (g ? g.version : '?') + ' (' + (g ? g.paragraphs.length : '?') + ' segments); applicability ' + APPLY.version +
                ' (Rules 13–17 from the encounter records; other rules not assessed). Light green and dotted: judged with no finding, inferred until clause states are recorded.';
        }
    });

    /* A cursor set elsewhere, or a rule chosen in V39, highlights the matching segments */
    var ctx = COS.components['ves.colreg.dial'];
    function names(test) {
        var out = [];
        (ctx.state.rules || []).forEach(function (r) {
            if (test(r)) out.push(/^Annex/.test(r.rule) ? r.rule.replace('Annex ', 'A') : r.rule);
            r.kids.forEach(function (k) { if (test(k)) out.push(k.key === r.rule ? 'Rule ' + r.rule : k.key); });
        });
        return out;
    }
    function mark() {
        var inst = ctx && ctx.charts.dial, sel = ctx && ctx.state.sel;
        if (!inst || inst.isDisposed()) return;
        inst.dispatchAction({ type: 'downplay', seriesIndex: 0 });
        if (sel) inst.dispatchAction({ type: 'highlight', seriesIndex: 0, name: sel });
    }
    if (ctx) {
        COS.on('time-cursor', function (d) {
            if (d.from === 'ves.colreg.dial') return;
            var t = +d.t;
            ctx.state.sel = names(function (n) { return n.eps.some(function (e) { return t >= e.t0 - COS.colreg.GAP && t <= e.t1 + COS.colreg.GAP; }); });
            mark();
        });
        COS.on('colreg-select', function (d) { ctx.state.sel = names(function (n) { return n.rule === d.rule || (n.p && n.p.rule === d.rule); }); mark(); });
    }
})();
</script>
<cfif composed EQ 0><cfinclude template="../shared/close.cfm"></cfif>
