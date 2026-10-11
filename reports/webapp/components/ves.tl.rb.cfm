<!--: V6 ves.tl.rb (DASH.029) — the vessel's risk (Rr) at each assessment, and where it peaked. Replaces risk.cfm. -->
<cfparam name="composed" default="0">
<cfif composed EQ 0><cfinclude template="../shared/open.cfm"></cfif>
<cfoutput><section data-component="ves.tl.rb" data-endpoint="#cos_root#/data/ves.tl.rb.data.cfm"></section></cfoutput>
<script>
COS.component('ves.tl.rb', {
    code: 'V6', title: 'Risk over time', hint: 'The risk (Rr) of this vessel at each assessment. Dots mark where the three highest spikes began.', vessel: true,
    query: function (ctx) { return { since: ctx.state.lastTick === undefined ? -1 : ctx.state.lastTick }; },
    merge: function (old, fresh) { return Object.assign({}, old, { rows: old.rows.concat(fresh.rows) }); },
    mock: function () {
        var r = COS.mock.rng('V6'), rows = [];
        for (var t = 1; t <= 4000; t += 20) { rows.push([t, r() < 0.03 ? 40000 + r() * 30000 : 15000 + r() * 5000]); }
        return { rows: rows };
    },
    render: function (ctx, data) {
        data.rows.forEach(function (r) { ctx.state.lastTick = r[0]; });
        var runs = [];		// consecutive equal readings form one spike: [start, end, risk]
        data.rows.forEach(function (r) {
            var last = runs[runs.length - 1];
            if (last && last[2] === r[1]) last[1] = r[0]; else runs.push([r[0], r[0], r[1]]);
        });
        var peaks = runs.sort(function (a, b) { return b[2] - a[2]; }).slice(0, 3);
        ctx.state.peaks = peaks;
        if (!ctx.body.querySelector('.cos-chart')) ctx.body.innerHTML = '<div class="cos-chart"></div>';
        COS.chart(ctx, 'rb', ctx.body.firstChild, {
            grid: COS.TL.grid,
            tooltip: { trigger: 'axis', formatter: function (ps) {
                var p = ps[0]; return 't = ' + COS.fmt.time(p.value[0]) + '<br>risk ' + COS.fmt.usd(p.value[1]); } },
            xAxis: COS.tlAxis(true, ctx),
            yAxis: COS.axis('Risk (USD)', { type: 'value', nameGap: 64 }),
            series: [{ type: 'line', showSymbol: false, data: data.rows.map(function (r) { return [r[0], r[1]]; }),
                lineStyle: { width: 2, color: COS.token('--text-primary') }, itemStyle: { color: COS.token('--text-primary') },
                markPoint: { symbol: 'circle', symbolSize: 9, label: { show: false },
                    itemStyle: { color: COS.token('--surface-1'), borderColor: COS.token('--text-primary'), borderWidth: 2 },
                    tooltip: { formatter: function (p) { return 'Spike ' + COS.fmt.usd(p.data.coord[1]) + '<br>from ' + COS.fmt.time(p.data.coord[0]) + ' to ' + COS.fmt.time(p.data.end); } },
                    data: peaks.map(function (p) { return { coord: [p[0], p[2]], end: p[1] }; }) } }]
        }, COS.tlOpts(200));
    },
    caption: function (ctx, data) {
        var last = data.rows[data.rows.length - 1], p = (ctx.state.peaks || [])[0];
        return 'Latest ' + COS.fmt.usd(last ? last[1] : null) + '. Highest spike: ' +
            COS.fmt.usd(p ? p[2] : null) + ' from ' + COS.fmt.time(p ? p[0] : null) + ' to ' + COS.fmt.time(p ? p[1] : null) + '.';
    }
});
</script>
<cfif composed EQ 0><cfinclude template="../shared/close.cfm"></cfif>
