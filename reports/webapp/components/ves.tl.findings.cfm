<!--: V9 ves.tl.findings (DASH.032) — every recorded finding on the voyage timeline, by source family. -->
<cfinclude template="/test/cos/shared/open.cfm">
<cfoutput><section data-component="ves.tl.findings" data-endpoint="#cos_root#/data/ves.tl.findings.data.cfm"></section></cfoutput>
<script>
COS.component('ves.tl.findings', {
    code: 'V9', title: 'Findings over time', hint: 'Each dot is a finding, placed by where it came from.', vessel: true,
    query: function (ctx) { return { since: ctx.state.lastTick === undefined ? -1 : ctx.state.lastTick }; },
    merge: function (old, fresh) { return Object.assign({}, old, { rows: old.rows.concat(fresh.rows) }); },
    mock: function () {
        var r = COS.mock.rng('V9'), rows = [];
        for (var t = 1; t <= 4000; t += 20) {
            if (r() < 0.25) rows.push([t, 'examiner', 'GroundingExaminer', 'grounding.contact', 'territorial_waters', 'safety', 95, -20.1]);
            if (r() < 0.02) rows.push([t, 'colreg', 'Rule15', 'COLREG.Rule15/CrossAstern', 'high_seas', 'traffic', 50, null]);
        }
        return { rows: rows };
    },
    render: function (ctx, data) {
        var F = COS.enc.sources, lane = { colreg: 0, local: 1, examiner: 2 };
        data.rows.forEach(function (r) { ctx.state.lastTick = r[0]; });
        if (!ctx.body.querySelector('.cos-chart')) ctx.body.innerHTML = '<div class="cos-chart"></div>';
        COS.chart(ctx, 'fd', ctx.body.firstChild, {
            grid: COS.TL.grid,
            tooltip: { trigger: 'item', formatter: function (p) {
                var r = p.data.r;
                return COS.esc(r[2]) + ' recorded <code>' + COS.esc(r[3]) + '</code><br>' + COS.fmt.time(r[0]) + ' · ' +
                    COS.esc(r[4].replace('_', ' ')) + ' · ' + COS.esc(r[5]) + '<br>' + COS.fmt.pts(r[6]) +
                    (r[7] !== null ? ' · value ' + COS.fmt.num(r[7], 1) : ''); } },
            xAxis: COS.tlAxis(true, ctx),
            yAxis: { type: 'category', inverse: true, data: F.map(function (f) { return f.label; }),
                axisLabel: { color: COS.token('--text-secondary'), fontSize: 11 }, axisTick: { show: false },
                splitLine: { show: true, lineStyle: { color: COS.token('--grid') } } },
            series: [{ type: 'scatter', symbolSize: 7,
                itemStyle: { color: COS.token('--text-primary'), opacity: 0.7 },
                data: data.rows.map(function (r) { return { value: [r[0], lane[r[1]]], r: r }; }) }]
        }, COS.tlOpts(130));
    },
    flags: function () { return [{ ticket: 'COS.044', text: 'Seamanship findings are counted again at every check (§2)' }]; },
    caption: function (ctx, data) {
        var n = { colreg: 0, local: 0, examiner: 0 };
        data.rows.forEach(function (r) { n[r[1]]++; });
        return n.colreg + ' COLREG, ' + n.local + ' local and ' + n.examiner + ' seamanship findings.';
    }
});
</script>
<cfinclude template="/test/cos/shared/close.cfm">
