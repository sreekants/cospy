/* COS dashboards — shared client (REQUIREMENTS §2, §3; INVENTORY SW-8 to SW-17).
 * One global, COS. Components register with COS.component(name, spec); the framework fetches the
 * component's endpoint, falls back to labelled mock data when the store has no rows (SH-17), polls
 * every COS.pollMs (never below 3 000 ms, SH-13), and renders through spec.render(ctx, data).
 */
(function () {
    'use strict';

    var COS = window.COS = window.COS || {};
    var cfg = window.COS_CONFIG || {};

    COS.root = cfg.root || '/test/cos';
    COS.pollMs = Math.max(3000, parseInt(cfg.poll, 10) || 3000);
    COS.ENGINE_ERROR = 'Internal Application Error';

    /* ---------------------------------------------------------------- escaping, state, events */

    COS.esc = function (s) {
        return String(s === null || s === undefined ? '' : s).replace(/[&<>"']/g, function (c) {
            return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
        });
    };

    COS.state = {
        get: function (key, dflt) {
            var v = new URLSearchParams(window.location.search).get(key);
            return v === null ? dflt : v;
        },
        set: function (values, push) {
            var u = new URL(window.location.href);
            Object.keys(values).forEach(function (k) {
                var v = values[k];
                if (v === null || v === undefined || v === '') u.searchParams.delete(k);
                else u.searchParams.set(k, v);
            });
            window.history[push ? 'pushState' : 'replaceState']({}, '', u.toString());
        }
    };

    COS.on = function (name, fn) {
        document.addEventListener('cos:' + name, function (e) { fn(e.detail || {}); });
    };
    COS.emit = function (name, detail) {
        document.dispatchEvent(new CustomEvent('cos:' + name, { detail: detail || {} }));
    };

    /* ---------------------------------------------------------------- fetch and parse (TK-05) */

    function clean(v) {
        if (Array.isArray(v)) return v.filter(function (x) { return x !== null; }).map(clean);
        if (v && typeof v === 'object') {
            var o = {};
            Object.keys(v).forEach(function (k) { o[k] = clean(v[k]); });
            return o;
        }
        if (typeof v === 'string') {
            try { return decodeURIComponent(v); } catch (e) { return v; }
        }
        return v;
    }

    /* The engine may emit stray tags around the JSON; parse the outermost object only. */
    COS.parse = function (text) {
        if (text.indexOf(COS.ENGINE_ERROR) >= 0) throw new Error('server error in endpoint');
        var a = text.indexOf('{'), b = text.lastIndexOf('}');
        if (a < 0 || b < a) throw new Error('no JSON object in response');
        return clean(JSON.parse(text.slice(a, b + 1)));
    };

    COS.fetch = function (url) {
        function once() {
            return fetch(url, { credentials: 'same-origin', cache: 'no-store' }).then(function (r) {
                if (!r.ok) throw new Error('HTTP ' + r.status);
                return r.text();
            }).then(function (text) { return { text: text, data: COS.parse(text) }; });
        }
        /* A read during a commit may fail (SH-16): retry once before reporting. */
        return once().catch(function () {
            return new Promise(function (res) { setTimeout(res, 500); }).then(once);
        });
    };

    /* ---------------------------------------------------------------- formatting (SH-05) */

    var nf0 = new Intl.NumberFormat('en-GB', { maximumFractionDigits: 0 });
    var nf1 = new Intl.NumberFormat('en-GB', { maximumFractionDigits: 1 });
    var nf2 = new Intl.NumberFormat('en-GB', { maximumFractionDigits: 2 });

    COS.fmt = {
        int: function (v) { return v === null || v === undefined || isNaN(v) ? '—' : nf0.format(Math.round(v)); },
        num: function (v, d) {
            if (v === null || v === undefined || isNaN(v)) return '—';
            return (d === 0 ? nf0 : d === 1 ? nf1 : nf2).format(v);
        },
        usd: function (v) { return v === null || v === undefined || isNaN(v) ? '—' : 'USD ' + nf0.format(v); },
        pts: function (v) { return v === null || v === undefined || isNaN(v) ? '—' : nf0.format(v) + ' pts'; },
        prob: function (v) {
            if (v === null || v === undefined || isNaN(v)) return '—';
            if (v === 0) return '0';
            return Math.abs(v) < 1e-3 ? v.toExponential(2) : v.toFixed(3);
        },
        pct: function (v) { return v === null || v === undefined || isNaN(v) ? '—' : nf1.format(v * 100) + ' %'; },
        /* Simulated seconds as h:mm:ss (simulated time, never wall time). */
        time: function (s) {
            if (s === null || s === undefined || isNaN(s)) return '—';
            s = Math.round(s);
            var h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), x = s % 60;
            return (h ? h + ':' + String(m).padStart(2, '0') : m) + ':' + String(x).padStart(2, '0');
        },
        dur: function (s) {
            if (s === null || s === undefined || isNaN(s)) return '—';
            return s < 120 ? nf0.format(s) + ' s' : s < 7200 ? nf1.format(s / 60) + ' min' : nf1.format(s / 3600) + ' h';
        }
    };

    /* ---------------------------------------------------------------- encodings (SH-08, UX P6) */

    function token(name) {
        return getComputedStyle(document.documentElement).getPropertyValue(name).trim() || '#888';
    }
    COS.token = token;

    COS.enc = {
        zones: [
            { key: 'high_seas', label: 'High seas', short: 'High seas', tok: '--zone-1' },
            { key: 'territorial_waters', label: 'Territorial waters', short: 'Territorial', tok: '--zone-2' },
            { key: 'internal_waters', label: 'Internal waters', short: 'Internal', tok: '--zone-3' },
            { key: 'port', label: 'Port', short: 'Port', tok: '--zone-4' }
        ],
        concerns: [
            { key: 'safety', label: 'Safety', tok: '--series-1' },
            { key: 'traffic', label: 'Traffic', tok: '--series-2' },
            { key: 'environmental', label: 'Environmental', tok: '--series-3' },
            { key: 'operational', label: 'Operational', tok: '--series-4' }
        ],
        sources: [
            { key: 'colreg', label: 'COLREG', symbol: 'triangle', tok: '--src-colreg' },
            { key: 'local', label: 'Local rules', symbol: 'diamond', tok: '--src-local' },
            { key: 'examiner', label: 'Seamanship', symbol: 'circle', tok: '--src-practice' }
        ],
        hazards: [
            { key: 'p_collision', label: 'P_C collision', tok: '--series-5', dash: 'solid' },
            { key: 'p_grounding', label: 'P_G grounding', tok: '--series-6', dash: 'dashed' },
            { key: 'p_comms_loss', label: 'P_L loss of comms', tok: '--series-7', dash: 'dotted' }
        ],
        encounters: [
            { key: 'crossing', label: 'Crossing' }, { key: 'give_way', label: 'Give-way' },
            { key: 'head_on', label: 'Head-on' }, { key: 'overtaking', label: 'Overtaking' }
        ],
        color: function (item) { return token(item.tok); },
        find: function (list, key) {
            for (var i = 0; i < list.length; i++) if (list[i].key === key) return list[i];
            /* Unknown values are never dropped: shown in neutral ink under their own name. */
            return { key: key, label: key, tok: '--text-muted', symbol: 'rect' };
        },
        sourceFamily: function (source) {
            if (source === 'colreg') return 'colreg';
            if (source === 'examiner') return 'examiner';
            return 'local';
        }
    };

    /* ---------------------------------------------------------------- mock data (SH-17) */

    COS.mock = {
        rng: function (seedText) {
            var h = 1779033703 ^ String(seedText).length;
            for (var i = 0; i < String(seedText).length; i++) {
                h = Math.imul(h ^ String(seedText).charCodeAt(i), 3432918353);
                h = (h << 13) | (h >>> 19);
            }
            var a = h >>> 0;
            return function () {
                a = (a + 0x6D2B79F5) >>> 0;
                var t = a;
                t = Math.imul(t ^ (t >>> 15), t | 1);
                t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
                return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
            };
        },
        vessels: ['MOCK ARIADNE', 'MOCK BERGE ODEL', 'MOCK TRUE NORTH', 'MOCK FLEET100', 'MOCK X100', 'MOCK ORANGE'],
        imos: [9000001, 9000002, 9000003, 9000004, 9000005, 9000006]
    };

    /* ---------------------------------------------------------------- captions (DB-06) */

    var BANNED = /\b(because|should|safe|unsafe|violated|violates|violation|compliant|non-compliant|guilty|fault)\b/i;
    COS.caption = function (text) {
        if (!text) return '';
        if (BANNED.test(text)) {
            if (window.console) console.warn('COS caption contains judgement wording:', text);
            text = text.replace(BANNED, '[…]');
        }
        return text;
    };

    /* ---------------------------------------------------------------- UI helpers */

    COS.ui = {};

    COS.ui.notice = function (box, text, kind) {
        box.innerHTML = '<p class="cos-notice ' + (kind || '') + '">' + COS.esc(text) + '</p>';
    };

    COS.ui.missing = function (ticket) {
        return '<span class="cos-missing" title="Not in the data">not recorded' +
            (ticket ? ' — ' + COS.esc(ticket) : '') + '</span>';
    };

    COS.ui.kv = function (box, pairs) {
        var h = '<dl class="cos-kv">';
        pairs.forEach(function (p) {
            h += '<dt>' + COS.esc(p[0]) + '</dt><dd>' + (p[2] ? p[1] : COS.esc(p[1])) + '</dd>';
        });
        box.innerHTML = h + '</dl>';
    };

    COS.ui.tiles = function (box, tiles) {
        var h = '<div class="cos-tiles">';
        tiles.forEach(function (t) {
            var tag = t.href ? 'a href="' + COS.esc(t.href) + '"' : (t.onclick ? 'button type="button"' : 'div');
            var close = t.href ? 'a' : (t.onclick ? 'button' : 'div');
            h += '<' + tag + ' class="cos-tile" data-key="' + COS.esc(t.key || '') + '">' +
                '<span class="cos-tile-label">' + COS.esc(t.label) + '</span>' +
                '<span class="cos-tile-value">' + (t.html ? t.value : COS.esc(t.value)) + '</span>' +
                (t.sub ? '<span class="cos-tile-sub">' + (t.subHtml ? t.sub : COS.esc(t.sub)) + '</span>' : '') +
                '</' + close + '>';
        });
        box.innerHTML = h + '</div>';
        tiles.forEach(function (t) {
            if (t.onclick) {
                var b = box.querySelector('[data-key="' + t.key + '"]');
                if (b) b.addEventListener('click', t.onclick);
            }
        });
    };

    /* Sortable table. cols: [{key,label,fmt(v,row),html,num,cls,sort:false}]. Sort kept in ctx.state. */
    COS.ui.table = function (box, cols, rows, opts) {
        opts = opts || {};
        var ctx = opts.ctx || { state: {} };
        var sort = ctx.state.sort || opts.sort || null;
        var data = rows.slice();
        if (sort) {
            var c = cols.filter(function (x) { return x.key === sort.key; })[0];
            if (c) {
                data.sort(function (a, b) {
                    var x = c.sortVal ? c.sortVal(a) : a[c.key], y = c.sortVal ? c.sortVal(b) : b[c.key];
                    if (x === y) return 0;
                    if (x === null || x === undefined) return 1;
                    if (y === null || y === undefined) return -1;
                    return (x < y ? -1 : 1) * (sort.dir === 'desc' ? -1 : 1);
                });
            }
        }
        var wrap = box.querySelector('.cos-tablewrap');
        var scroll = wrap ? wrap.scrollTop : 0;
        var h = '<div class="cos-tablewrap"' + (opts.maxHeight ? ' style="max-height:' + opts.maxHeight + 'px"' : '') +
            '><table class="cos-table"><thead><tr>';
        cols.forEach(function (c) {
            var mark = sort && sort.key === c.key ? (sort.dir === 'desc' ? ' ▼' : ' ▲') : '';
            var sortable = opts.sortable !== false && c.sort !== false;
            h += '<th class="' + (c.num ? 'num ' : '') + (c.cls || '') + '"' +
                (sortable ? ' data-sort="' + COS.esc(c.key) + '" tabindex="0" aria-sort="' +
                    (mark ? (sort.dir === 'desc' ? 'descending' : 'ascending') : 'none') + '"' : '') +
                ' scope="col">' + COS.esc(c.label) + mark + '</th>';
        });
        h += '</tr></thead><tbody>';
        if (!data.length) {
            h += '<tr><td class="cos-empty" colspan="' + cols.length + '">' +
                COS.esc(opts.emptyText || 'No data for this run.') + '</td></tr>';
        }
        data.forEach(function (r, i) {
            h += '<tr data-i="' + i + '"' + (opts.rowClass ? ' class="' + opts.rowClass(r) + '"' : '') + '>';
            cols.forEach(function (c) {
                var v = c.fmt ? c.fmt(r[c.key], r) : r[c.key];
                h += '<td class="' + (c.num ? 'num ' : '') + (c.cls || '') + '">' +
                    (c.html ? v : COS.esc(v === null || v === undefined ? '—' : v)) + '</td>';
            });
            h += '</tr>';
        });
        h += '</tbody></table></div>';
        box.innerHTML = h;
        var nw = box.querySelector('.cos-tablewrap');
        if (nw) nw.scrollTop = scroll;
        box.querySelectorAll('th[data-sort]').forEach(function (th) {
            function go() {
                var k = th.getAttribute('data-sort');
                var cur = ctx.state.sort;
                ctx.state.sort = { key: k, dir: cur && cur.key === k && cur.dir === 'asc' ? 'desc' : 'asc' };
                if (opts.onSort) opts.onSort(ctx.state.sort);
                COS.ui.table(box, cols, rows, opts);
            }
            th.addEventListener('click', go);
            th.addEventListener('keydown', function (e) { if (e.key === 'Enter') go(); });
        });
        if (opts.onRow) {
            box.querySelectorAll('tbody tr[data-i]').forEach(function (tr) {
                tr.classList.add('clickable');
                tr.addEventListener('click', function () { opts.onRow(data[+tr.getAttribute('data-i')]); });
            });
        }
    };

    /* Sequential single-hue matrix (heat map as a table, values in cells). */
    COS.ui.matrix = function (box, m) {
        var max = 0;
        m.rows.forEach(function (r, i) { m.cols.forEach(function (c, j) {
            var v = m.val(i, j); if (v !== null && v !== undefined && v > max) max = v;
        }); });
        var h = '<div class="cos-tablewrap"><table class="cos-table cos-matrix"><thead><tr><th scope="col">' +
            COS.esc(m.corner || '') + '</th>';
        m.cols.forEach(function (c) { h += '<th scope="col" class="num">' + COS.esc(c) + '</th>'; });
        h += '</tr></thead><tbody>';
        m.rows.forEach(function (r, i) {
            h += '<tr' + (m.highlightRow === i ? ' class="cos-hl"' : '') + '><th scope="row">' + COS.esc(r) + '</th>';
            m.cols.forEach(function (c, j) {
                var v = m.val(i, j);
                var step = v === null || v === undefined || max === 0 ? 0 : Math.min(8, Math.round(8 * v / max));
                var sub = m.sub ? m.sub(i, j) : '';
                h += '<td class="num seq-' + step + '"' + (m.title ? ' title="' + COS.esc(m.title(i, j)) + '"' : '') +
                    ' data-r="' + i + '" data-c="' + j + '">' + COS.esc(m.fmt(v)) +
                    (sub ? '<span class="cos-sub">' + COS.esc(sub) + '</span>' : '') + '</td>';
            });
            h += '</tr>';
        });
        h += '</tbody></table></div>';
        if (m.legend !== false) {
            h += '<div class="cos-seqlegend"><span>0</span>';
            for (var s = 0; s <= 8; s++) h += '<i class="seq-' + s + '"></i>';
            h += '<span>' + COS.esc(m.fmt(max)) + '</span></div>';
        }
        box.innerHTML = h;
        if (m.onCell) {
            box.querySelectorAll('td[data-r]').forEach(function (td) {
                td.classList.add('clickable');
                td.addEventListener('click', function () { m.onCell(+td.getAttribute('data-r'), +td.getAttribute('data-c')); });
            });
        }
    };

    /* ---------------------------------------------------------------- charts (TK-04) */

    COS.chart = function (ctx, key, box, option, opts) {
        opts = opts || {};
        if (!window.echarts) {
            COS.ui.notice(box, 'Chart library not loaded (ECharts from cdnjs).', 'cos-error');
            return null;
        }
        var height = opts.height || 260;
        var inst = ctx.charts[key];
        if (!inst || inst.isDisposed() || inst.getDom() !== box) {
            box.style.height = height + 'px';
            inst = echarts.init(box, null, {
                renderer: 'svg',
                width: box.clientWidth || opts.width || 720,
                height: height
            });
            ctx.charts[key] = inst;
            if (opts.group) { inst.group = opts.group; echarts.connect(opts.group); }
            if (window.ResizeObserver) {
                new ResizeObserver(function () { if (!inst.isDisposed()) inst.resize({ width: box.clientWidth || 'auto' }); }).observe(box);
            }
            if (opts.onClick) inst.on('click', opts.onClick);
        }
        var base = {
            animation: false,
            textStyle: { color: token('--text-secondary'), fontFamily: 'inherit', fontSize: 12 },
            grid: { left: 64, right: 24, top: 28, bottom: 40, containLabel: false },
            tooltip: { trigger: opts.trigger || 'axis', confine: true,
                backgroundColor: token('--surface-2'), borderColor: token('--line'),
                textStyle: { color: token('--text-primary') } }
        };
        inst.setOption(Object.assign(base, option), { notMerge: true });
        return inst;
    };

    /* Map frame at equal ground scale: the box height follows its width, so a map is never stretched.
       pts are [lon, lat]; returns the box height, the grid and the axis ranges. */
    COS.mapFrame = function (box, pts, opts) {
        var o = Object.assign({ left: 88, right: 32, top: 36, bottom: 40, min: 240, max: 640, pad: 0.1 }, opts || {});
        var xs = pts.map(function (p) { return p[0]; }), ys = pts.map(function (p) { return p[1]; });
        var x0 = Math.min.apply(null, xs), x1 = Math.max.apply(null, xs), y0 = Math.min.apply(null, ys), y1 = Math.max.apply(null, ys);
        var k = Math.cos((y0 + y1) / 2 * Math.PI / 180);
        var gx = Math.max((x1 - x0) * k, 1e-5) * (1 + 2 * o.pad), gy = Math.max(y1 - y0, 1e-5) * (1 + 2 * o.pad);
        var w = Math.max(box.clientWidth, 200) - o.left - o.right, h = w * gy / gx;
        var lo = o.min - o.top - o.bottom, hi = o.max - o.top - o.bottom;
        if (h > hi) { h = hi; gx = gy * w / h; }		/* too tall: widen the longitude span */
        else if (h < lo) { h = lo; gy = gx * h / w; }	/* too flat: widen the latitude span */
        var cx = (x0 + x1) / 2, cy = (y0 + y1) / 2;
        return { height: Math.round(h + o.top + o.bottom), grid: { left: o.left, right: o.right, top: o.top, bottom: o.bottom },
                 x: [cx - gx / k / 2, cx + gx / k / 2], y: [cy - gy / 2, cy + gy / 2] };
    };

    /* Redraws a map with its latest redraw function when its box changes width (a tab shown, a window resized) */
    COS.mapWatch = function (box, redraw) {
        box.__mapRedraw = redraw;
        if (box.__mapWatch || !window.ResizeObserver) return;
        var last = box.clientWidth;
        box.__mapWatch = new ResizeObserver(function () {
            var w = box.clientWidth;
            if (w && Math.abs(w - last) > 2) { last = w; box.__mapRedraw(); }
        });
        box.__mapWatch.observe(box);
    };

    /* Sets a map chart's height after COS.chart, which sizes a box only when it creates the chart */
    COS.mapHeight = function (inst, box, height) {
        if (!inst || box.style.height === height + 'px') return;
        box.style.height = height + 'px';
        inst.resize({ width: box.clientWidth, height: height });
    };

    COS.axis = function (name, extra) {
        return Object.assign({
            name: name, nameLocation: 'middle', nameGap: 44,
            nameTextStyle: { color: token('--text-secondary') },
            axisLine: { lineStyle: { color: token('--line') } },
            axisLabel: { color: token('--text-secondary') },
            splitLine: { lineStyle: { color: token('--grid') } }
        }, extra || {});
    };

    /* ---------------------------------------------------------------- shared voyage timeline (VES-06) */

    /* Every timeline component uses the same x-axis, margins and group, so their axes align and
       their tooltips and zoom move together; a click publishes cos:time-cursor (CP-10). */
    COS.TL = { group: 'cos-tl', grid: { left: 96, right: 90, top: 10, bottom: 30 } };
    /* The x-range is the vessel's voyage span from meta (t0, t1), never each component's own data. */
    COS.tlAxis = function (show, ctx) {
        var m = (ctx && ctx.meta) || {};
        var lo = m.t1 > m.t0 ? m.t0 : 'dataMin', hi = m.t1 > m.t0 ? m.t1 : 'dataMax';
        return COS.axis('', { type: 'value', min: lo, max: hi, nameGap: 0,
            axisLabel: { show: show !== false, formatter: COS.fmt.time, color: token('--text-secondary') },
            splitLine: { show: false } });
    };
    COS.tlOpts = function (height) {
        return { height: height, group: COS.TL.group, onClick: function (p) {
            var t = Array.isArray(p.value) ? p.value[0] : p.value;
            if (t !== undefined) { COS.state.set({ t: Math.round(t) }); COS.emit('time-cursor', { t: Math.round(t) }); }
        } };
    };

    /* ---------------------------------------------------------------- component framework */

    COS.params = function () {
        return {
            case: COS.state.get('case', '0'),
            imo: COS.state.get('imo', '0'),
            t: COS.state.get('t', null)
        };
    };

    COS.link = function (page, extra) {
        var p = COS.params();
        var u = new URL(COS.root + '/' + page, window.location.origin);
        if (p.case && p.case !== '0') u.searchParams.set('case', p.case);
        Object.keys(extra || {}).forEach(function (k) { u.searchParams.set(k, extra[k]); });
        return u.pathname + u.search;
    };

    COS.cite = function (ctx) {
        var m = ctx.meta || {};
        var u = new URL(window.location.href);
        if (m.case && !u.searchParams.get('case')) u.searchParams.set('case', m.case);
        var line = u.toString() + '\n' + 'COS case ' + (m.case || '?') +
            (m.imo ? ' · vessel ' + m.imo : '') + (u.searchParams.get('t') ? ' · t=' + u.searchParams.get('t') : '') +
            ' · ' + ctx.spec.code + ' ' + ctx.spec.title + (ctx.mode === 'mock' ? ' · MOCK DATA' : '') +
            (m.written ? ' · data written ' + m.written : '');
        if (navigator.clipboard) navigator.clipboard.writeText(line).catch(function () {});
        return line;
    };

    COS.components = {};

    COS.component = function (name, spec) {
        var el = document.querySelector('section[data-component="' + name + '"]');
        if (!el) return null;
        if (!document.querySelector('.cos-app.cos-composed')) document.title = spec.code + ' ' + spec.title + ' — COS';
        el.classList.add('part');
        if (!el.id) el.id = 'part-' + name;
        el.innerHTML =
            '<header class="part-head">' +
            '<div class="part-titles"><h2><span class="part-code">' + COS.esc(spec.code) + '</span> ' + COS.esc(spec.title) + '</h2>' +
            (spec.hint ? '<p class="part-hint">' + COS.esc(spec.hint) + '</p>' : '') + '</div>' +
            '<span class="part-badges"></span>' +
            '<button type="button" class="part-cite" title="Copy a link to this view, with where the data came from">Cite</button>' +
            '</header>' +
            (spec.controls ? '<div class="part-controls">' + spec.controls + '</div>' : '') +
            '<div class="part-body" aria-live="polite"></div>' +
            '<p class="part-caption"></p>';
        var ctx = {
            name: name, el: el, spec: spec, state: {}, charts: {}, mode: 'live', meta: {}, last: null,
            body: el.querySelector('.part-body'),
            controls: el.querySelector('.part-controls'),
            badges: el.querySelector('.part-badges'),
            captionEl: el.querySelector('.part-caption'),
            params: COS.params(),
            rerender: function () { if (ctx.data) draw(ctx.data); }
        };
        COS.components[name] = ctx;
        el.querySelector('.part-cite').addEventListener('click', function (e) {
            var line = COS.cite(ctx);
            e.target.title = line;
            e.target.textContent = 'Copied';
            setTimeout(function () { e.target.textContent = 'Cite'; }, 1500);
        });

        var endpoint = el.getAttribute('data-endpoint');
        var timer = null;

        function setBadges(flags) {
            var h = '';
            if (ctx.mode === 'mock') {
                h += '<span class="badge badge-mock" title="' + COS.esc(ctx.mockReason || '') + '">MOCK DATA</span>';
            }
            (flags || []).forEach(function (f) {
                h += '<span class="badge badge-flag" title="' + COS.esc(f.text) + '">⚑ ' + COS.esc(f.ticket) + '</span>';
            });
            ctx.badges.innerHTML = h;
        }

        function draw(data) {
            ctx.data = data;
            try {
                spec.render(ctx, data);
                var flags = spec.flags ? spec.flags(ctx, data) : [];
                setBadges(flags);
                var cap = spec.caption ? spec.caption(ctx, data) : '';
                var pre = ctx.mode === 'mock' ? 'MOCK DATA — ' + (ctx.mockReason || '') + (cap ? ' · ' : '') : '';
                ctx.captionEl.textContent = pre + COS.caption(cap);
            } catch (e) {
                COS.ui.notice(ctx.body, 'This part could not be drawn: ' + e.message, 'cos-error');
                if (window.console) console.error(name, e);
            }
        }

        function url() {
            var p = COS.params();
            var u = new URL(endpoint, window.location.origin);
            u.searchParams.set('case', p.case || '0');
            if (spec.vessel) u.searchParams.set('imo', p.imo || '0');
            if (spec.query) {
                var q = spec.query(ctx);
                Object.keys(q).forEach(function (k) { u.searchParams.set(k, q[k]); });
            }
            return u.toString();
        }

        function schedule() {
            clearTimeout(timer);
            if (spec.static && ctx.data) return;
            timer = setTimeout(load, COS.pollMs);
        }

        function load() {
            if (document.hidden) { schedule(); return; }
            /* ?mock=1 forces the labelled mock (testing and demonstration, SH-17). */
            if (COS.state.get('mock') === '1' && !ctx.mockData) {
                ctx.mode = 'mock';
                ctx.mockReason = 'shown because the address has ?mock=1';
                ctx.mockData = spec.mock(ctx, {});
                draw(ctx.mockData);
                return;
            }
            if (COS.state.get('mock') === '1') return;
            if (!endpoint) {
                ctx.mode = 'mock';
                ctx.mockReason = spec.mockReason || 'no endpoint';
                if (!ctx.mockData) ctx.mockData = spec.mock(ctx);
                draw(ctx.mockData);
                return;
            }
            COS.fetch(url()).then(function (res) {
                var data = res.data;
                ctx.meta = data.meta || {};
                if (ctx.meta.nf_case) ctx.meta.notfound = 'Run ' + ctx.meta.asked_case + ' is not in the data.';
                else if (ctx.meta.nf_imo && spec.vessel) ctx.meta.notfound = 'Vessel ' + ctx.meta.asked_imo + ' has no data in run ' + ctx.meta.case + '.';
                if (ctx.meta.notfound && !spec.allowNotfound) {
                    ctx.mode = 'notfound';
                    COS.ui.notice(ctx.body, ctx.meta.notfound, 'cos-error');
                    setBadges([]);
                    ctx.captionEl.textContent = '';
                    return;
                }
                /* Live/ended (SH-14): the run is live while its newest tick advances between polls. */
                if (ctx.meta.maxtick !== undefined) {
                    var mt = +ctx.meta.maxtick;
                    if (ctx.state.maxtick !== undefined && mt > ctx.state.maxtick) { ctx.state.idle = 0; ctx.state.live = true; }
                    else if (ctx.state.maxtick !== undefined) {
                        ctx.state.idle = (ctx.state.idle || 0) + 1;
                        if (ctx.state.idle >= 3) ctx.state.live = false;
                    }
                    ctx.state.maxtick = mt;
                }
                /* An incremental poll with nothing new is not an empty store. */
                if (spec.merge && ctx.data && ctx.mode === 'live') {
                    if (!data.rows || !data.rows.length) { setBadges(spec.flags ? spec.flags(ctx, ctx.data) : []); return; }
                    draw(spec.merge(ctx.data, data, ctx));
                    return;
                }
                var empty = spec.empty ? spec.empty(data, ctx) : !(data.rows && data.rows.length);
                if (empty) {
                    if (ctx.mode !== 'mock' || !ctx.mockData) {
                        ctx.mode = 'mock';
                        ctx.mockReason = (spec.mockReason || 'no data for this run') +
                            (spec.ticket ? ' (' + spec.ticket + ')' : '');
                        ctx.mockData = spec.mock(ctx, data);
                        draw(ctx.mockData);
                    }
                    return;
                }
                ctx.mode = 'live';
                if (res.text === ctx.last) {
                    if (spec.everyPoll) { draw(ctx.data); return; }
                    setBadges(spec.flags ? spec.flags(ctx, ctx.data) : []);
                    return;   /* unchanged: keep the reader's view (SH-15) */
                }
                ctx.last = res.text;
                draw(data);
            }).catch(function (err) {
                ctx.badges.insertAdjacentHTML('beforeend',
                    '<span class="badge badge-error" title="' + COS.esc(err.message) + '">could not load — trying again</span>');
                if (!ctx.data) COS.ui.notice(ctx.body, 'Could not load the data (' + err.message + '). Trying again every ' +
                    (COS.pollMs / 1000) + ' s.', 'cos-error');
            }).then(schedule, schedule);
        }

        ctx.reload = function () { ctx.last = null; ctx.data = null; clearTimeout(timer); load(); };
        document.addEventListener('visibilitychange', function () { if (!document.hidden) { clearTimeout(timer); load(); } });
        load();
        return ctx;
    };

    /* ---------------------------------------------------------------- page tabs (UX §2.3, VES-19) */

    /* Buttons [data-tab] select panels [data-tabpanel] inside root. The open tab is kept in ?tab=
       (T1); charts in a panel are resized when it is shown (T4); a time-cursor selection made outside
       the cursor tab opens it (T3). Components keep polling while hidden (T5). */
    COS.tabs = function (root, opts) {
        opts = opts || {};
        var buttons = root.querySelectorAll('[data-tab]');
        var panels = root.querySelectorAll('[data-tabpanel]');
        var names = Array.prototype.map.call(buttons, function (b) { return b.getAttribute('data-tab'); });
        function show(name, push) {
            if (names.indexOf(name) < 0) name = names[0];
            buttons.forEach(function (b) {
                var on = b.getAttribute('data-tab') === name;
                b.setAttribute('aria-selected', on ? 'true' : 'false');
                b.tabIndex = on ? 0 : -1;
            });
            panels.forEach(function (p) { p.hidden = p.getAttribute('data-tabpanel') !== name; });
            if (push !== undefined) COS.state.set({ tab: name }, push);
            /* A chart initialised while hidden has no width: resize the shown panel's charts. */
            Object.keys(COS.components).forEach(function (k) {
                var c = COS.components[k];
                Object.keys(c.charts).forEach(function (n) {
                    var inst = c.charts[n];
                    if (!inst.isDisposed() && inst.getDom().clientWidth) inst.resize({ width: inst.getDom().clientWidth, height: inst.getHeight() });
                });
            });
            COS.tabs.current = name;
        }
        buttons.forEach(function (b) {
            b.addEventListener('click', function () { show(b.getAttribute('data-tab'), true); });
            b.addEventListener('keydown', function (e) {
                var i = names.indexOf(b.getAttribute('data-tab'));
                if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
                    var n = names[(i + (e.key === 'ArrowRight' ? 1 : names.length - 1)) % names.length];
                    show(n, true);
                    root.querySelector('[data-tab="' + n + '"]').focus();
                }
            });
        });
        if (opts.cursorTab) COS.on('time-cursor', function () { if (COS.tabs.current !== opts.cursorTab) show(opts.cursorTab, true); });
        /* T6: a link to a component (#part-<name>) opens the tab that holds it, then scrolls to it. */
        function reveal(hash) {
            if (!hash || hash.length < 2) return false;
            var el = document.getElementById(decodeURIComponent(hash.slice(1)));
            var panel = el && el.closest('[data-tabpanel]');
            if (!panel) return false;
            show(panel.getAttribute('data-tabpanel'), true);
            if (el.scrollIntoView) el.scrollIntoView({ block: 'start' });
            return true;
        }
        root.addEventListener('click', function (e) {
            var a = e.target.closest && e.target.closest('a[href^="#"]');
            if (a && reveal(a.getAttribute('href'))) e.preventDefault();
        });
        COS.tabs.reveal = reveal;
        window.addEventListener('popstate', function () { show(COS.state.get('tab', names[0])); });
        show(COS.state.get('tab', names[0]));
        if (window.location.hash) setTimeout(function () { reveal(window.location.hash); }, 0);
        return show;
    };

    /* Incremental time series merge: rows carry `tick`; meta.since echoes the request. */
    COS.mergeRows = function (old, fresh, keyFn) {
        var seen = {};
        var rows = old.rows.slice();
        rows.forEach(function (r) { seen[keyFn(r)] = true; });
        (fresh.rows || []).forEach(function (r) { if (!seen[keyFn(r)]) rows.push(r); });
        return Object.assign({}, fresh, { rows: rows });
    };
})();
