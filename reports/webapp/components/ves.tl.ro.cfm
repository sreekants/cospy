<!--: V37 ves.tl.ro (DASH.076, RQ3) — penalty points given over time, by source, on V6's time scale. -->
<cfparam name="composed" default="0">
<cfif composed EQ 0><cfinclude template="../shared/open.cfm"></cfif>
<cfoutput><section data-component="ves.tl.ro" data-endpoint="#cos_root#/data/ves.tl.ro.data.cfm"></section></cfoutput>
<script>
COS.component('ves.tl.ro', {
    code: 'V37', title: 'Penalty points over time', hint: 'Each bar is the penalty points given at that moment, by source. Read it against the risk above.', vessel: true,
    query: function (ctx) { return { since: ctx.state.lastTick === undefined ? -1 : ctx.state.lastTick }; },
    merge: function (old, fresh) { return Object.assign({}, old, { rows: old.rows.concat(fresh.rows) }); },
    mock: function () {
        var r = COS.mock.rng('V37'), rows = [];
        for (var t = 1; t <= 4000; t += 20) {
            if (r() < 0.2) rows.push([t, 'examiner', 95, 1]);
            if (r() < 0.03) rows.push([t, 'colreg', 50, 1]);
            if (r() < 0.02) rows.push([t, 'local', 30, 1]);
        }
        return { rows: rows };
    },
    render: function (ctx, data) {
        var S = COS.enc.sources, BIN_PX = 4;
        data.rows.forEach(function (r) { ctx.state.lastTick = r[0]; });
        if (!ctx.body.querySelector('.cos-chart')) ctx.body.innerHTML = '<div class="cos-chart"></div>';
        var el = ctx.body.querySelector('.cos-chart');

        /* Ticks closer than a bar's width share a bin, so their bars stack instead of overlapping */
        function bins() {
            var m = ctx.meta || {}, ticks = data.rows.map(function (r) { return r[0]; });
            var lo = m.t1 > m.t0 ? m.t0 : Math.min.apply(null, ticks), hi = m.t1 > m.t0 ? m.t1 : Math.max.apply(null, ticks);
            var w = Math.max(el.clientWidth - COS.TL.grid.left - COS.TL.grid.right, 100), dt = Math.max((hi - lo) * BIN_PX / w, 1);
            var at = {}, keys = [];
            data.rows.forEach(function (r) {
                var k = Math.floor((r[0] - lo) / dt);
                if (!at[k]) { at[k] = { t: [lo + k * dt, lo + (k + 1) * dt] }; keys.push(k); }
                var f = COS.enc.sourceFamily(r[1]), b = at[k][f] = at[k][f] || { pts: 0, n: 0 };
                b.pts += r[2]; b.n += r[3];
            });
            return keys.map(function (k) { return at[k]; });
        }

        function draw() {
            if (!el.clientWidth) return;		/* hidden tab: drawn when shown (COS.mapWatch) */
            var B = bins();
            COS.chart(ctx, 'ro', el, {
                grid: Object.assign({}, COS.TL.grid, { top: 30 }),		/* room for the legend; left and right stay V6's */
                legend: { top: 0, right: COS.TL.grid.right, data: S.map(function (s) { return s.label; }), textStyle: { color: COS.token('--text-secondary') } },
                tooltip: { trigger: 'axis', formatter: function (ps) {
                    var b = ps[0] && ps[0].data.b;
                    if (!b) return '';
                    var head = Math.round(b.t[1]) - Math.round(b.t[0]) > 1 ? COS.fmt.time(b.t[0]) + ' – ' + COS.fmt.time(b.t[1]) : 't = ' + COS.fmt.time(b.t[0]);
                    return head + S.filter(function (s) { return b[s.key]; }).map(function (s) {
                        return '<br>' + COS.esc(s.label) + ': ' + COS.fmt.pts(b[s.key].pts) + ' (' + COS.fmt.int(b[s.key].n) + ' finding' + (b[s.key].n === 1 ? '' : 's') + ')';
                    }).join(''); } },
                xAxis: COS.tlAxis(true, ctx),
                yAxis: COS.axis('Penalty points', { type: 'value', min: 0, nameGap: 64 }),
                /* every series carries every bin (0 where a source has none), so the stack lines up;
                   points come first in each item because ECharts stacks the first value dimension, which on a value x-axis would be time */
                series: S.map(function (s) {
                    return { name: s.label, type: 'bar', stack: 'pts', barWidth: BIN_PX - 1, itemStyle: { color: COS.enc.color(s) },
                        dimensions: ['pts', 't'], encode: { x: 't', y: 'pts' },
                        data: B.map(function (b) { return { value: [b[s.key] ? b[s.key].pts : 0, (b.t[0] + b.t[1]) / 2], b: b }; }) };
                })
            }, COS.tlOpts(220));
        }
        COS.mapWatch(el, draw);
        draw();
    },
    flags: function () {
        return [{ ticket: 'RQ3-01', text: 'Bars are placed when the violation was posted, which is later than when it began.' },
                { ticket: 'COS.044', text: 'Points are too high: findings score again at every check (§2) and collisions are written more than once (§4).' }];
    },
    caption: function (ctx, data) {
        var tot = { colreg: 0, local: 0, examiner: 0 }, big = null;
        data.rows.forEach(function (r) {
            tot[COS.enc.sourceFamily(r[1])] += r[2];
            if (!big || r[2] > big[2]) big = r;
        });
        var n = tot.colreg + tot.local + tot.examiner;
        if (!big) return 'No penalty points recorded for this vessel.';
        return COS.fmt.int(n) + ' points in total: ' + COS.fmt.int(tot.colreg) + ' COLREG, ' + COS.fmt.int(tot.local) + ' local rules, ' +
            COS.fmt.int(tot.examiner) + ' seamanship. Largest at one moment: ' + COS.fmt.pts(big[2]) + ' (' + COS.enc.find(COS.enc.sources, COS.enc.sourceFamily(big[1])).label + ') at ' + COS.fmt.time(big[0]) + '.';
    }
});
</script>
<cfif composed EQ 0><cfinclude template="../shared/close.cfm"></cfif>
