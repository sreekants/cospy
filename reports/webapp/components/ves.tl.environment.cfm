<!--: V11 ves.tl.environment (DASH.034) — depth beneath the vessel, with assumed readings visible. -->
<cfparam name="composed" default="0">
<cfif composed EQ 0><cfinclude template="../shared/open.cfm"></cfif>
<cfoutput><section data-component="ves.tl.environment" data-endpoint="#cos_root#/data/ves.tl.environment.data.cfm"></section></cfoutput>
<script>
COS.component('ves.tl.environment', {
    code: 'V11', title: 'Depth', hint: 'Water depth under the vessel. Hollow dots are assumed depths.', vessel: true,
    query: function (ctx) { return { since: ctx.state.lastTick === undefined ? -1 : ctx.state.lastTick }; },
    merge: function (old, fresh) { return Object.assign({}, old, { rows: old.rows.concat(fresh.rows) }); },
    mock: function () {
        var r = COS.mock.rng('V11'), rows = [];
        for (var t = 1; t <= 4000; t += 20) rows.push([t, t > 3000 ? 4 + r() * 6 : 30 + r() * 60, r() < 0.02 ? 1 : 0]);
        return { weather: { pk: 0.02, th: 0.25, ni: 2, nw: 1, w: 'calm', nv: 1, v: 'good' }, rows: rows };
    },
    render: function (ctx, data) {
        data.rows.forEach(function (r) { ctx.state.lastTick = r[0]; });
        if (!ctx.body.querySelector('.cos-chart')) ctx.body.innerHTML = '<div class="cos-chart"></div>';
        var ink = COS.token('--text-primary');
        COS.chart(ctx, 'dp', ctx.body.firstChild, {
            grid: COS.TL.grid,
            tooltip: { trigger: 'axis', formatter: function (ps) {
                var p = ps[0]; return 't = ' + COS.fmt.time(p.value[0]) + '<br>depth ' + COS.fmt.num(p.value[1], 1) + ' m'; } },
            xAxis: COS.tlAxis(true, ctx),
            yAxis: COS.axis('Depth (m)', { type: 'value', nameGap: 64 }),
            series: [
                { name: 'measured', type: 'line', showSymbol: false, data: data.rows.map(function (r) { return [r[0], r[1]]; }),
                  lineStyle: { width: 1.5, color: ink }, itemStyle: { color: ink } },
                { name: 'fallback (nominal)', type: 'scatter', symbol: 'emptyCircle', symbolSize: 8,
                  itemStyle: { color: ink, borderWidth: 2 },
                  data: data.rows.filter(function (r) { return r[2] === 1; }).map(function (r) { return [r[0], r[1]]; }) }]
        }, COS.tlOpts(150));
    },
    flags: function (ctx, data) {
        return data.rows.some(function (r) { return r[2] === 1; }) ? [{ ticket: 'REQ.022', text: 'Some depths are assumed, not measured' }] : [];
    },
    caption: function (ctx, data) {
        var w = data.weather || {}, nom = data.rows.filter(function (r) { return r[2] === 1; }).length;
        var wx = (w.nw === 1 && w.nv === 1) ? 'Waves ' + w.w + ' and visibility ' + w.v + ' all voyage.' :
                 w.nw > 1 || w.nv > 1 ? 'The weather changed during the voyage.' : 'No weather recorded for this vessel.';
        var cz = w.pk === null || w.pk === undefined ? ' No capsize check recorded.' :
            ' Capsize chance peaked at ' + COS.fmt.prob(w.pk) + ' (alarm at ' + COS.fmt.prob(w.th) + ').' +
            (w.nw <= 1 && w.nv <= 1 && w.ni <= 2 ? ' Its inputs never changed (COS.043).' : '');
        return nom + ' assumed depths. ' + wx + cz;
    }
});
</script>
<cfif composed EQ 0><cfinclude template="../shared/close.cfm"></cfif>
