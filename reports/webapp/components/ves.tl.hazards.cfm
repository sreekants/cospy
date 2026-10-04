<!--: V7 ves.tl.hazards (DASH.030) — collision and grounding probability over the voyage. -->
<cfparam name="composed" default="0">
<cfif composed EQ 0><cfinclude template="../shared/open.cfm"></cfif>
<cfoutput><section data-component="ves.tl.hazards" data-endpoint="#cos_root#/data/ves.tl.hazards.data.cfm"></section></cfoutput>
<script>
COS.component('ves.tl.hazards', {
    code: 'V7', title: 'Collision and grounding', hint: 'Chance of collision (P_C) and of grounding (P_G) at each moment.', vessel: true,
    query: function (ctx) { return { since: ctx.state.lastTick === undefined ? -1 : ctx.state.lastTick }; },
    merge: function (old, fresh) { return Object.assign({}, old, { rows: old.rows.concat(fresh.rows) }); },
    mock: function () {
        var r = COS.mock.rng('V7'), rows = [];
        for (var t = 1; t <= 4000; t += 20) rows.push([t, r() < 0.05 ? r() * 0.2 : r() * 0.01, t > 3000 ? r() * 0.08 : r() * 0.005]);
        return { rows: rows };
    },
    render: function (ctx, data) {
        data.rows.forEach(function (r) { ctx.state.lastTick = r[0]; });
        var H = COS.enc.hazards.slice(0, 2);
        if (!ctx.body.querySelector('.cos-chart')) ctx.body.innerHTML = '<div class="cos-chart"></div>';
        COS.chart(ctx, 'hz', ctx.body.firstChild, {
            grid: COS.TL.grid,
            tooltip: { trigger: 'axis', formatter: function (ps) {
                return 't = ' + COS.fmt.time(ps[0].value[0]) + ps.map(function (p) {
                    return '<br>' + COS.esc(H[p.seriesIndex].label) + ': ' + COS.fmt.prob(p.value[1]); }).join(''); } },
            xAxis: COS.tlAxis(true, ctx),
            yAxis: COS.axis('Chance', { type: 'value', nameGap: 64 }),
            series: H.map(function (h, k) {
                return { name: h.label, type: 'line', showSymbol: false,
                    data: data.rows.map(function (r) { return [r[0], r[k + 1]]; }),
                    lineStyle: { width: 2, color: COS.enc.color(h), type: h.dash }, itemStyle: { color: COS.enc.color(h) },
                    endLabel: { show: true, formatter: h.label.split(' ')[0], color: COS.token('--text-primary') } };
            })
        }, COS.tlOpts(180));
    },
    caption: function (ctx, data) {
        var pc = [0, 0], pg = [0, 0];
        data.rows.forEach(function (r) { if (r[1] > pc[0]) pc = [r[1], r[0]]; if (r[2] > pg[0]) pg = [r[2], r[0]]; });
        return 'Highest P_C ' + COS.fmt.prob(pc[0]) + ' at ' + COS.fmt.time(pc[1]) + '. Highest P_G ' + COS.fmt.prob(pg[0]) + ' at ' + COS.fmt.time(pg[1]) + '.';
    }
});
</script>
<cfif composed EQ 0><cfinclude template="../shared/close.cfm"></cfif>
