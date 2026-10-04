<!--: V6 ves.tl.rb (DASH.029) — how consequential risk accumulated, and where it jumped. Replaces risk.cfm. -->
<cfparam name="composed" default="0">
<cfif composed EQ 0><cfinclude template="../shared/open.cfm"></cfif>
<cfoutput><section data-component="ves.tl.rb" data-endpoint="#cos_root#/data/ves.tl.rb.data.cfm"></section></cfoutput>
<script>
COS.component('ves.tl.rb', {
    code: 'V6', title: 'Risk over time', hint: 'How the risk (Rb) of this vessel built up. Dots mark the biggest jumps.', vessel: true,
    query: function (ctx) { return { since: ctx.state.lastTick === undefined ? -1 : ctx.state.lastTick }; },
    merge: function (old, fresh) { return Object.assign({}, old, { rows: old.rows.concat(fresh.rows) }); },
    mock: function () {
        var r = COS.mock.rng('V6'), rows = [], c = 0;
        for (var t = 1; t <= 4000; t += 20) { var i = r() < 0.03 ? 400 + r() * 900 : r() * 40; c += i; rows.push([t, c, i]); }
        return { rows: rows };
    },
    render: function (ctx, data) {
        data.rows.forEach(function (r) { ctx.state.lastTick = r[0]; });
        var peaks = data.rows.slice().sort(function (a, b) { return b[2] - a[2]; }).slice(0, 3);
        ctx.state.peaks = peaks;
        if (!ctx.body.querySelector('.cos-chart')) ctx.body.innerHTML = '<div class="cos-chart"></div>';
        COS.chart(ctx, 'rb', ctx.body.firstChild, {
            grid: COS.TL.grid,
            tooltip: { trigger: 'axis', formatter: function (ps) {
                var p = ps[0]; return 't = ' + COS.fmt.time(p.value[0]) + '<br>total ' + COS.fmt.usd(p.value[1]); } },
            xAxis: COS.tlAxis(true, ctx),
            yAxis: COS.axis('Risk (USD)', { type: 'value', nameGap: 64 }),
            series: [{ type: 'line', showSymbol: false, data: data.rows.map(function (r) { return [r[0], r[1]]; }),
                lineStyle: { width: 2, color: COS.token('--text-primary') }, itemStyle: { color: COS.token('--text-primary') },
                markPoint: { symbol: 'circle', symbolSize: 9, label: { show: false },
                    itemStyle: { color: COS.token('--surface-1'), borderColor: COS.token('--text-primary'), borderWidth: 2 },
                    tooltip: { formatter: function (p) { return 'Biggest jump<br>' + COS.fmt.usd(p.data.inc) + ' at ' + COS.fmt.time(p.data.coord[0]); } },
                    data: peaks.map(function (p) { return { coord: [p[0], p[1]], inc: p[2] }; }) } }]
        }, COS.tlOpts(200));
    },
    caption: function (ctx, data) {
        var last = data.rows[data.rows.length - 1], p = (ctx.state.peaks || [])[0];
        return 'Ended at ' + COS.fmt.usd(last ? last[1] : null) + '. Biggest jump: ' +
            COS.fmt.usd(p ? p[2] : null) + ' at ' + COS.fmt.time(p ? p[0] : null) + '.';
    }
});
</script>
<cfif composed EQ 0><cfinclude template="../shared/close.cfm"></cfif>
