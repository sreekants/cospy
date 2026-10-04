<!--: V5 ves.tl.zone (DASH.028) — which regime governed the vessel at every moment. -->
<cfinclude template="../shared/open.cfm">
<cfoutput><section data-component="ves.tl.zone" data-endpoint="#cos_root#/data/ves.tl.zone.data.cfm"></section></cfoutput>
<script>
COS.component('ves.tl.zone', {
    code: 'V5', title: 'Zone', hint: 'Which waters the vessel was in, and when.', vessel: true,
    query: function (ctx) { return { since: ctx.state.lastTick === undefined ? -1 : ctx.state.lastTick }; },
    merge: function (old, fresh) { return Object.assign({}, old, { rows: old.rows.concat(fresh.rows) }); },
    mock: function () {
        var rows = [], z = ['high_seas', 'territorial_waters', 'internal_waters', 'territorial_waters', 'port'];
        for (var t = 1; t <= 4000; t += 20) rows.push([t, z[Math.min(4, Math.floor(t / 850))]]);
        return { rows: rows };
    },
    render: function (ctx, data) {
        var Z = COS.enc.zones, idx = {}, segs = [], cur = null;
        Z.forEach(function (z, i) { idx[z.key] = i; });
        data.rows.forEach(function (r) {
            ctx.state.lastTick = r[0];
            if (cur && cur[2] === r[1]) cur[1] = r[0];
            else { if (cur) cur[1] = r[0]; cur = [r[0], r[0], r[1]]; segs.push(cur); }
        });
        ctx.state.segs = segs;
        if (!ctx.body.querySelector('.cos-chart')) {
            ctx.body.innerHTML = '<div class="cos-chart"></div><div class="cos-legend">' + Z.map(function (z, i) {
                return '<span class="chip chip-z' + (i + 1) + '">' + COS.esc(z.label) + '</span>'; }).join('') + '</div>';
        }
        COS.chart(ctx, 'band', ctx.body.firstChild, {
            grid: COS.TL.grid,
            tooltip: { trigger: 'item', formatter: function (p) {
                return COS.esc((Z[idx[p.value[2]]] || { label: p.value[2] }).label) + '<br>' + COS.fmt.time(p.value[0]) + ' – ' + COS.fmt.time(p.value[1]); } },
            xAxis: COS.tlAxis(true, ctx),
            yAxis: { type: 'category', data: ['Zone'], axisLabel: { color: COS.token('--text-secondary') }, axisTick: { show: false }, axisLine: { show: false } },
            series: [{ type: 'custom', encode: { x: [0, 1], y: 3 },
                renderItem: function (params, api) {
                    var a = api.coord([api.value(0), 0]), b = api.coord([api.value(1), 0]);
                    var h = api.size([0, 1])[1] * 0.7, zi = idx[api.value(2)];
                    var z = Z[zi] || { tok: '--text-muted', short: api.value(2) };
                    var w = Math.max(1, b[0] - a[0]);
                    return { type: 'group', children: [
                        { type: 'rect', shape: { x: a[0], y: a[1] - h / 2, width: w, height: h },
                          style: { fill: COS.token(z.tok), stroke: COS.token('--surface-1'), lineWidth: 1 } },
                        { type: 'text', style: { text: w > 70 ? z.short : '', x: a[0] + 4, y: a[1] - 6,
                          fill: COS.token('--zone-text-' + ((zi || 0) + 1)), fontSize: 11 } }] };
                },
                data: segs.map(function (s) { return [s[0], s[1], s[2], 0]; }) }]
        }, COS.tlOpts(64));
    },
    caption: function (ctx) {
        var n = (ctx.state.segs || []).length;
        return n <= 1 ? 'The vessel stayed in one zone.' : 'The vessel changed zone ' + (n - 1) + ' times.';
    }
});
</script>
<cfinclude template="../shared/close.cfm">
