<!--: V24 ves.baselines (DASH.047) — the metric-only baselines beside Rb: EL, P_HE (exact and bound), IR. -->
<cfinclude template="../shared/open.cfm">
<cfoutput><section data-component="ves.baselines" data-endpoint="#cos_root#/data/ves.baselines.data.cfm"></section></cfoutput>
<script>
COS.component('ves.baselines', {
    code: 'V24', title: 'Standard risk measures', hint: 'Classic measures to compare with Rb: expected loss, hazard chance, individual risk.', vessel: true,
    query: function (ctx) { return { since: ctx.state.lastTick === undefined ? -1 : ctx.state.lastTick }; },
    merge: function (old, fresh) { return Object.assign({}, old, { rows: old.rows.concat(fresh.rows) }); },
    mock: function () {
        var r = COS.mock.rng('V24'), rows = [];
        for (var t = 1; t <= 4000; t += 20) { var pa = 0.17 + r() * 0.1; rows.push([t, 4000 + r() * 3000, pa, pa + r() * 0.01, 1e-7 * (1 + r())]); }
        return { rows: rows };
    },
    render: function (ctx, data) {
        data.rows.forEach(function (r) { ctx.state.lastTick = r[0]; });
        if (!ctx.body.querySelector('.v24-a')) ctx.body.innerHTML = '<div class="cos-chart v24-a"></div><div class="cos-chart v24-b"></div>';
        var ink = COS.token('--text-primary'), mut = COS.token('--text-secondary');
        COS.chart(ctx, 'el', ctx.body.querySelector('.v24-a'), {
            grid: COS.TL.grid,
            tooltip: { trigger: 'axis', formatter: function (ps) { return 't = ' + COS.fmt.time(ps[0].value[0]) + '<br>expected loss ' + COS.fmt.usd(ps[0].value[1]); } },
            xAxis: COS.tlAxis(false, ctx), yAxis: COS.axis('Expected loss (USD)', { type: 'value', nameGap: 64 }),
            series: [{ type: 'line', showSymbol: false, data: data.rows.map(function (r) { return [r[0], r[1]]; }), lineStyle: { width: 1.5, color: ink }, itemStyle: { color: ink } }]
        }, COS.tlOpts(140));
        var S = [['Hazard chance', 2, 'solid', ink], ['Upper bound', 3, 'dashed', mut], ['Individual risk', 4, 'dotted', ink]];
        COS.chart(ctx, 'p', ctx.body.querySelector('.v24-b'), {
            grid: COS.TL.grid,
            tooltip: { trigger: 'axis', formatter: function (ps) {
                return 't = ' + COS.fmt.time(ps[0].value[0]) + ps.map(function (p) { return '<br>' + S[p.seriesIndex][0] + ': ' + COS.fmt.prob(p.value[1]); }).join(''); } },
            xAxis: COS.tlAxis(true, ctx), yAxis: COS.axis('Chance (log scale)', { type: 'log', nameGap: 64 }),
            series: S.map(function (s) {
                return { name: s[0], type: 'line', showSymbol: false, data: data.rows.filter(function (r) { return r[s[1]] > 0; }).map(function (r) { return [r[0], r[s[1]]]; }),
                    lineStyle: { width: 1.5, type: s[2], color: s[3] }, itemStyle: { color: s[3] },
                    endLabel: { show: true, formatter: s[0], color: COS.token('--text-primary'), fontSize: 11 } };
            })
        }, COS.tlOpts(180));
    },
    caption: function (ctx, data) {
        var gap = 0, ir = 0;
        data.rows.forEach(function (r) { gap = Math.max(gap, r[3] - r[2]); if (r[4] > ir) ir = r[4]; });
        return 'The upper bound is at most ' + COS.fmt.prob(gap) + ' above the hazard chance. Highest individual risk: ' + COS.fmt.prob(ir) + '.';
    }
});
</script>
<cfinclude template="../shared/close.cfm">
