<!--: V10 ves.tl.encounters (DASH.033) — when the vessel was in which kind of encounter, and with whom. -->
<cfinclude template="shared/open.cfm">
<cfoutput><section data-component="ves.tl.encounters" data-endpoint="#cos_root#/data/ves.tl.encounters.data.cfm"></section></cfoutput>
<script>
COS.component('ves.tl.encounters', {
    code: 'V10', title: 'Encounters', hint: 'When the vessel met other vessels, and how.', vessel: true,
    mock: function () {
        var r = COS.mock.rng('V10'), rows = [];
        for (var i = 0; i < 40; i++) { var s = Math.round(r() * 3900), d = r() < 0.6 ? 0 : Math.round(20 + r() * 200);
            rows.push([Math.floor(r() * 4), s, s + d, COS.mock.imos[i % 6]]); }
        return { names: COS.mock.imos.map(function (m, i) { return [String(m), COS.mock.vessels[i]]; }), rows: rows };
    },
    render: function (ctx, data) {
        var E = COS.enc.encounters, names = {};
        (data.names || []).forEach(function (n) { names[n[0]] = n[1]; });
        if (!ctx.body.querySelector('.cos-chart')) ctx.body.innerHTML = '<div class="cos-chart"></div>';
        COS.chart(ctx, 'en', ctx.body.firstChild, {
            grid: COS.TL.grid,
            tooltip: { trigger: 'item', formatter: function (p) {
                var v = p.value;
                return COS.esc(E[v[2]].label) + ' with ' + COS.esc(names[String(v[3])] || v[3]) + '<br>' +
                    COS.fmt.time(v[0]) + ' – ' + COS.fmt.time(v[1]) + (v[1] === v[0] ? ' (seen once)' : ''); } },
            xAxis: COS.tlAxis(true, ctx),
            yAxis: { type: 'category', inverse: true, data: E.map(function (e) { return e.label; }),
                axisLabel: { color: COS.token('--text-secondary'), fontSize: 11 }, axisTick: { show: false },
                splitLine: { show: true, lineStyle: { color: COS.token('--grid') } } },
            series: [{ type: 'custom', encode: { x: [0, 1], y: 2 },
                renderItem: function (params, api) {
                    var a = api.coord([api.value(0), api.value(2)]), b = api.coord([api.value(1), api.value(2)]);
                    var h = api.size([0, 1])[1] * 0.55;
                    return { type: 'rect', shape: { x: a[0], y: a[1] - h / 2, width: Math.max(2, b[0] - a[0]), height: h },
                        style: { fill: COS.token('--text-secondary'), opacity: 0.8 } };
                },
                data: data.rows.map(function (r) { return [r[1], r[2], r[0], r[3]]; }) }]
        }, COS.tlOpts(140));
    },
    flags: function () { return [{ ticket: 'COS.044', text: 'One encounter can be counted many times (§2)' }]; },
    caption: function (ctx, data) {
        var z = data.rows.filter(function (r) { return r[1] === r[2]; }).length;
        return data.rows.length + ' encounters. ' + z + ' were seen only once.';
    }
});
</script>
<cfinclude template="shared/close.cfm">
