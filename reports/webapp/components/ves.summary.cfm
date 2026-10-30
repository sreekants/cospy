<!--: V39 ves.summary (DASH.078) — what happened on this voyage, written from the store with fixed phrase templates; every sentence cites its rows. -->
<cfparam name="composed" default="0">
<cfif composed EQ 0><cfinclude template="../shared/open.cfm"></cfif>
<cfoutput><section data-component="ves.summary" data-endpoint="#cos_root#/data/ves.summary.data.cfm"></section></cfoutput>
<script>
(function () {
    var KINDS = ['crossing', 'give_way', 'head_on', 'overtaking', 'stand_on'];
    var TABLES = ['fact_crossing', 'fact_give_way', 'fact_head_on', 'fact_overtaking', 'fact_stand_on'];

    function fill(tpl, v) { return String(tpl).replace(/\{(\w+)\}/g, function (m, k) { return v[k] === undefined || v[k] === null ? 'not recorded' : v[k]; }); }
    function plural(n, w) { return COS.fmt.int(n) + ' ' + w + (n === 1 ? '' : 's'); }
    function sum(rows) { var s = 0; rows.forEach(function (r) { s += r.pts; }); return s; }

    /* Sentences are { text, refs: [{ t: table, ids: [] }] }; sections are [{ title, items: [sentence | scene] }] */
    function write(P, data) {
        var S = P.settings, m = data.meta || {}, name = {}, cfg = {};
        (data.names || []).forEach(function (n) { name[n[0]] = n[1]; });
        (data.cfg || []).forEach(function (c) { cfg[c[0]] = c[1]; });
        var imo = String(m.imo), me = name[imo] || 'Vessel ' + imo;
        function who(id) { return name[String(id)] || 'vessel ' + id; }
        function say(key, v, refs) { return { text: fill(P[key], Object.assign({ vessel: me }, v || {})), refs: refs || [] }; }
        var out = [];

        /* Setting */
        var zones = [];
        (data.zones || []).forEach(function (z) { if (z[1] && (!zones.length || zones[zones.length - 1] !== z[1])) zones.push(z[1]); });
        out.push({ title: 'Setting', items: [
            say('setting.run', { scenario: cfg['run.scenario'], map: cfg['map.key'], t0: COS.fmt.time(m.t0), t1: COS.fmt.time(m.t1), dur: COS.fmt.dur(m.t1 - m.t0) }, [{ t: 'configs', ids: ['run.scenario', 'map.key'] }]),
            zones.length ? say('setting.zones', { zones: zones.map(function (z) { return COS.enc.find(COS.enc.zones, z).label; }).join(' → ') }, [{ t: 'fact_risk_assessment', ids: ['zone, ' + (data.zones || []).length + ' rows'] }]) : null
        ] });

        /* Vessels */
        var ut = data.ut || [], tested = ut.filter(function (u) { return u[1] === 1; });
        var role = tested.length ? (tested.some(function (u) { return String(u[0]) === imo; }) ? P['vessel.role.tested'] : P['vessel.role.background']) : P['vessel.role.all'];
        var enc = (data.enc || []).map(function (e) { return { k: KINDS[e[0]], table: TABLES[e[0]], id: e[1], s: e[2], e: e[3], tg: e[4] }; });
        var met = {};
        enc.forEach(function (e) { met[e.tg] = true; });
        var metIds = Object.keys(met);
        out.push({ title: 'Vessels', items: [
            say('vessel.self', { imo: imo, role: role }, ut.length ? [{ t: 'fact_under_test', ids: ut.map(function (u) { return u[0]; }) }] : []),
            metIds.length ? say('vessel.met', { n: metIds.length, names: metIds.map(who).join(', ') }, refsOf(enc)) : say('vessel.met.none')
        ] });

        /* Scenes: a counterparty's encounter records closer than merge_s, plus the COLREG findings naming it */
        var scenes = [];
        enc.slice().sort(function (a, b) { return a.tg - b.tg || a.s - b.s; }).forEach(function (e) {
            var sc = scenes[scenes.length - 1];
            if (!sc || sc.tg !== e.tg || e.s > sc.t1 + S.merge_s) scenes.push(sc = { tg: e.tg, t0: e.s, t1: e.e, recs: [], finds: [] });
            sc.recs.push(e); sc.t1 = Math.max(sc.t1, e.e);
        });
        var colreg = (data.rows || []).filter(function (f) { return f.src === 'colreg'; });
        colreg.forEach(function (f) {
            var tg = (/target=(\d+)/.exec(f.sit || '') || [])[1];
            var sc = scenes.filter(function (s) { return String(s.tg) === tg && f.t >= s.t0 - S.attach_s && f.t <= s.t1 + S.attach_s; })[0];
            if (!sc) scenes.push(sc = { tg: tg ? +tg : null, t0: f.t, t1: f.t, recs: [], finds: [], outside: true });
            sc.finds.push(f);
        });
        var coll = (data.coll || []).map(function (c) { return { id: c[0], t: c[1], tg: c[2] }; });
        scenes.forEach(function (sc) {
            sc.coll = coll.filter(function (c) { return c.tg === sc.tg && c.t >= sc.t0 - S.attach_s && c.t <= sc.t1 + S.attach_s; });
            sc.pts = sum(sc.finds);
        });
        var ranked = scenes.filter(function (s) { return s.finds.length || s.coll.length; })
            .sort(function (a, b) { return (b.coll.length > 0) - (a.coll.length > 0) || b.pts - a.pts || a.t0 - b.t0; });
        var shown = ranked.slice(0, S.scenes).sort(function (a, b) { return a.t0 - b.t0; });
        var rest = scenes.filter(function (s) { return shown.indexOf(s) < 0; });
        var standOn = enc.some(function (e) { return e.k === 'stand_on'; });

        var items = shown.map(function (sc) {
            var kinds = {};
            sc.recs.forEach(function (r) { kinds[r.k] = (kinds[r.k] || []).concat([r]); });
            var main = ['head_on', 'overtaking', 'crossing', 'give_way', 'stand_on'].filter(function (k) { return kinds[k]; })[0] || 'finding';
            var target = sc.tg ? who(sc.tg) : 'an unnamed vessel', lines = [];
            if (sc.recs.length) lines.push(say('scene.met', { target: target, records: Object.keys(kinds).map(function (k) { return plural(kinds[k].length, P.kind[k].toLowerCase() + ' record'); }).join(', ') }, refsOf(sc.recs)));
            if (sc.outside) lines.push(say('scene.outside', { target: target }));
            if (kinds.give_way) lines.push(say('scene.role.give_way', {}, refsOf(kinds.give_way)));
            else if (kinds.stand_on) lines.push(say('scene.role.stand_on', {}, refsOf(kinds.stand_on)));
            else if (kinds.crossing || kinds.overtaking) lines.push(say('scene.role.unknown'));
            lines.push(say('scene.cpa', {}, [{ t: 'fact_dcpa', ids: ['no rows'] }]));
            var eps = COS.colreg.episodes(sc.finds);
            lines.push(eps.length ? say('scene.findings', { list: byRule(eps).map(function (g) { return 'Rule ' + g.rule + ' (' + plural(g.eps.length, 'episode') + ', ' + COS.fmt.pts(g.pts) + ')'; }).join(', ') }, [{ t: 'fact_ro', ids: sc.finds.map(function (f) { return f.id; }) }])
                                  : say('scene.findings.none'));
            if (kinds.give_way && !eps.some(function (e) { return /Rule16/.test(e.clause); })) lines.push(say('scene.unjudged.16', {}, refsOf(kinds.give_way)));
            if ((kinds.crossing || kinds.overtaking) && !standOn) lines.push(say('scene.unjudged.17', {}, [{ t: 'fact_stand_on', ids: ['no rows'] }]));
            sc.coll.forEach(function (c) { lines.push(say('scene.collision', { target: target, t: COS.fmt.time(c.t) }, [{ t: 'fact_collision', ids: [c.id] }])); });
            return { scene: true, head: fill(P['scene.head'], { kind: P.kind[main], target: target, t0: COS.fmt.time(sc.t0), t1: COS.fmt.time(sc.t1) }), t: sc.t0, lines: lines };
        });
        if (rest.length) {
            var rt = {};
            rest.forEach(function (s) { rt[s.tg] = true; });
            items.push(say('scene.rollup', { n: rest.length, m: Object.keys(rt).length }, refsOf([].concat.apply([], rest.map(function (s) { return s.recs; })))));
        }
        out.push({ title: 'What happened', items: items.length ? items : [say('vessel.met.none')] });

        /* What went wrong: COLREG by rule, then other findings by clause */
        var all = data.rows || [], wrong = [];
        byRule(COS.colreg.episodes(colreg)).forEach(function (g) {
            var cl = {};
            g.eps.forEach(function (e) { cl[e.clause] = (cl[e.clause] || 0) + 1; });
            wrong.push(Object.assign(say('wrong.rule', { rule: g.rule, episodes: plural(g.eps.length, 'episode'), pts: COS.fmt.pts(g.pts),
                clauses: Object.keys(cl).map(function (c) { return c.replace(/^COLREG\.Rule\d+[./]?/, '') + ' × ' + cl[c]; }).join(', ') }, [{ t: 'fact_ro', ids: g.ids }]), { t: g.t, rule: g.rule }));
        });
        var other = {};
        all.filter(function (f) { return f.src !== 'colreg'; }).forEach(function (f) { (other[f.clause] = other[f.clause] || []).push(f); });
        var groups = Object.keys(other).map(function (c) { return { clause: c, rows: other[c], pts: sum(other[c]), src: other[c][0].src }; })
            .sort(function (a, b) { return b.pts - a.pts; });
        groups.slice(0, S.clauses).forEach(function (g) {
            var eps = COS.colreg.episodes(g.rows);
            wrong.push(Object.assign(say('wrong.clause', { clause: g.clause, source: COS.enc.find(COS.enc.sources, COS.enc.sourceFamily(g.src)).label, episodes: plural(eps.length, 'episode'), pts: COS.fmt.pts(g.pts), t: COS.fmt.time(g.rows[0].t) },
                [{ t: 'fact_ro', ids: g.rows.map(function (f) { return f.id; }) }]), { t: g.rows[0].t }));
        });
        if (groups.length > S.clauses) {
            var more = groups.slice(S.clauses);
            wrong.push(say('wrong.more', { n: more.length, pts: COS.fmt.pts(more.reduce(function (s, g) { return s + g.pts; }, 0)) }));
        }
        out.push({ title: 'What went wrong', items: wrong.length ? wrong : [say('wrong.none')] });

        /* What was not judged */
        var gw = enc.filter(function (e) { return e.k === 'give_way'; }), cx = enc.filter(function (e) { return e.k === 'crossing' || e.k === 'overtaking'; }), nj = [];
        if (gw.length && !colreg.some(function (f) { return /Rule16/.test(f.clause); })) nj.push(Object.assign(say('notjudged.16', { n: gw.length }, refsOf(gw)), { rule: '16' }));
        if (cx.length && !standOn) nj.push(Object.assign(say('notjudged.17', { n: cx.length }, refsOf(cx)), { rule: '17' }));
        out.push({ title: 'What was not judged', items: nj.length ? nj : [say('notjudged.none')] });

        /* Result */
        var ground = all.filter(function (f) { return f.clause === 'grounding.contact'; }), res = [];
        res.push(coll.length ? say('result.collision', { n: coll.length, target: who(coll[0].tg), t: COS.fmt.time(coll[0].t) }, [{ t: 'fact_collision', ids: coll.map(function (c) { return c.id; }) }])
                             : say('result.collision.none', {}, [{ t: 'fact_collision', ids: ['no rows for this vessel'] }]));
        if (ground.length) res.push(say('result.grounding', { n: ground.length, t: COS.fmt.time(ground[0].t) }, [{ t: 'fact_ro', ids: ground.map(function (f) { return f.id; }) }]));
        res.push(say('result.cpa', {}, [{ t: 'fact_dcpa', ids: ['no rows'] }]));
        out.push({ title: 'Result', items: res });
        return out;
    }

    function refsOf(recs) {
        var by = {};
        recs.forEach(function (r) { (by[r.table] = by[r.table] || []).push(r.id); });
        return Object.keys(by).map(function (t) { return { t: t, ids: by[t] }; });
    }
    function byRule(eps) {
        var g = {}, order = [];
        eps.forEach(function (e) {
            var c = COS.colreg.parse(e.clause), r = c ? c.rule : '?';
            if (!g[r]) { g[r] = { rule: r, eps: [], pts: 0, ids: [], t: e.t0 }; order.push(r); }
            g[r].eps.push(e); g[r].pts += sum(e.rows); g[r].ids = g[r].ids.concat(e.rows.map(function (f) { return f.id; }));
        });
        return order.map(function (r) { return g[r]; });
    }

    function refText(refs) { return refs.map(function (r) { return r.t + ': ' + (r.ids.length > 20 ? r.ids.slice(0, 20).join(', ') + ' … (' + r.ids.length + ')' : r.ids.join(', ')); }).join('\n'); }

    function html(sections, refs) {
        function sentence(s) {
            if (!s) return '';
            var sup = '';
            if (s.refs && s.refs.length) { refs.push(s.refs); sup = '<sup class="ref" title="' + COS.esc(refText(s.refs)) + '">[' + refs.length + ']</sup>'; }
            return COS.esc(s.text) + sup;
        }
        return sections.map(function (sec) {
            return '<h3>' + COS.esc(sec.title) + '</h3>' + sec.items.map(function (it) {
                if (!it) return '';
                if (it.scene) return '<h4><button type="button" class="go" data-t="' + it.t + '">' + COS.esc(it.head) + '</button></h4><p>' + it.lines.map(sentence).join(' ') + '</p>';
                var attrs = it.rule ? ' class="go" data-rule="' + it.rule + '"' + (it.t !== undefined ? ' data-t="' + it.t + '"' : '') : it.t !== undefined ? ' class="go" data-t="' + it.t + '"' : '';
                return attrs ? '<p><button type="button"' + attrs + '>' + sentence(it) + '</button></p>' : '<p>' + sentence(it) + '</p>';
            }).join('');
        }).join('');
    }

    function markdown(sections) {
        var n = 0, notes = [];
        function s(x) { if (!x) return ''; var t = x.text; if (x.refs && x.refs.length) { n++; notes.push('[' + n + '] ' + refText(x.refs).replace(/\n/g, '; ')); t += ' [' + n + ']'; } return t; }
        var md = sections.map(function (sec) {
            return '## ' + sec.title + '\n\n' + sec.items.map(function (it) {
                if (!it) return '';
                return it.scene ? '**' + it.head + '.** ' + it.lines.map(s).join(' ') : s(it);
            }).filter(Boolean).join('\n\n');
        }).join('\n\n');
        return md + '\n\n' + notes.join('\n');
    }

    COS.component('ves.summary', {
        code: 'V39', title: 'What happened on this voyage',
        hint: 'Generated from the recorded data. Each sentence links to the rows it is based on.', vessel: true,
        controls: '<button type="button" class="part-cite" data-copy>Copy as Markdown</button>',
        empty: function (data) { return !(data.rows && data.rows.length) && !(data.enc && data.enc.length); },
        mockReason: 'no encounters or findings for this vessel',
        mock: function () {
            return { meta: { imo: 9000003, t0: 0, t1: 3600 },
                names: [['9000003', 'MOCK TRUE NORTH'], ['9000002', 'MOCK BERGE ODEL'], ['9000004', 'MOCK X100']],
                cfg: [['run.scenario', 'mock scenario'], ['map.key', 'mock/map']], ut: [[9000003, 1]],
                zones: [[0, 'territorial_waters'], [1800, 'internal_waters']],
                enc: [[0, 1, 600, 640, 9000002], [1, 2, 600, 640, 9000002], [3, 3, 2100, 2160, 9000004], [1, 4, 2100, 2160, 9000004]],
                rows: [{ id: 1, t: 645, src: 'colreg', clause: 'COLREG.Rule15/CrossAstern', zone: 'territorial_waters', pts: 50, sit: 'own=9000003 target=9000002' },
                       { id: 2, t: 2150, src: 'colreg', clause: 'COLREG.Rule13.a', zone: 'internal_waters', pts: 50, sit: 'own=9000003 target=9000004' },
                       { id: 3, t: 2900, src: 'examiner', clause: 'grounding.margin', zone: 'internal_waters', pts: 30, sit: '' }],
                coll: [] };
        },
        render: function (ctx, data) {
            if (!ctx.state.P) {
                if (!ctx.state.loading) {
                    ctx.state.loading = true;
                    COS.colreg.file('scene.phrases.json').then(function (p) { ctx.state.P = p; ctx.rerender(); })
                        .catch(function (e) { ctx.state.err = e.message; ctx.rerender(); });
                }
                COS.ui.notice(ctx.body, ctx.state.err ? 'The phrase file could not be loaded (' + ctx.state.err + ').' : 'Loading the phrase file…', ctx.state.err ? 'cos-error' : '');
                return;
            }
            var meta = ctx.mode === 'mock' ? data.meta : ctx.meta;
            var sections = write(ctx.state.P, Object.assign({}, data, { meta: meta }));
            ctx.state.sections = sections;
            var box = ctx.body.querySelector('.cos-story'), top = box ? box.scrollTop : 0, refs = [];
            ctx.body.innerHTML = '<div class="cos-story">' + html(sections, refs) + '</div>';
            box = ctx.body.querySelector('.cos-story');
            box.scrollTop = top;
            ctx.state.refs = refs.length;
            box.querySelectorAll('.go').forEach(function (b) {
                b.addEventListener('click', function () {
                    var t = b.getAttribute('data-t'), r = b.getAttribute('data-rule');
                    if (r) COS.emit('colreg-select', { rule: r });
                    if (t !== null) { COS.state.set({ t: Math.round(+t) }); COS.emit('time-cursor', { t: Math.round(+t) }); }
                });
            });
            var copy = ctx.controls && ctx.controls.querySelector('[data-copy]');
            if (copy && !copy.__hooked) {
                copy.__hooked = true;
                copy.addEventListener('click', function () {
                    if (navigator.clipboard && ctx.state.sections) navigator.clipboard.writeText(markdown(ctx.state.sections)).catch(function () {});
                    copy.textContent = 'Copied';
                    setTimeout(function () { copy.textContent = 'Copy as Markdown'; }, 1500);
                });
            }
        },
        flags: function () {
            return [{ ticket: 'REQ.067', text: 'Closest approach, course and speed are not recorded yet, so scenes cannot say how close the vessels came or what they did.' }];
        },
        caption: function (ctx) {
            var P = ctx.state.P;
            return 'Phrases v' + (P ? P.version : '?') + '; up to ' + (P ? P.settings.scenes : '?') + ' scenes with findings, ranked by collision, then points; ' +
                (ctx.state.refs || 0) + ' references. Hover a reference for the table and row ids.';
        }
    });
})();
</script>
<cfif composed EQ 0><cfinclude template="../shared/close.cfm"></cfif>
