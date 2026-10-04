<!--: S10 sim.rb.cumulative (DASH.012) — how consequential risk accumulated for every vessel. -->
<cfinclude template="/test/cos/shared/open.cfm">
<cfoutput><section data-component="sim.rb.cumulative" data-endpoint="#cos_root#/data/sim.rb.cumulative.data.cfm"></section></cfoutput>
<script>
COS.component('sim.rb.cumulative', {
    code: 'S10', title: 'Risk over time', hint: 'How risk (Rb) built up for each vessel.',
    query: function (ctx) { return { since: ctx.state.lastTick === undefined ? -1 : ctx.state.lastTick }; },
    merge: function (old, fresh) {
        return Object.assign({}, old, { rows: old.rows.concat(fresh.rows) });
    },
    mock: function () {
        var r = COS.mock.rng('S10'), rows = [];
        COS.mock.imos.forEach(function (imo, i) {
            var c = 0, slope = 2 + r() * 12;
            for (var t = 1; t <= 4000; t += 40) { c += slope * (0.5 + r()); rows.push([t, imo, c]); }
        });
        return { names: COS.mock.imos.map(function (m, i) { return [String(m), COS.mock.vessels[i]]; }), rows: rows };
    },
    render: function (ctx, data) {
        var names = {}, byV = {}, last = {};
        (data.names || []).forEach(function (n) { names[n[0]] = n[1]; });
        data.rows.forEach(function (r) {
            (byV[r[1]] = byV[r[1]] || []).push([r[0], r[2]]);
            last[r[1]] = r[2];
            if (ctx.state.lastTick === undefined || r[0] > ctx.state.lastTick) ctx.state.lastTick = r[0];
        });
        var ids = Object.keys(byV).sort(function (a, b) { return last[b] - last[a]; });
        ctx.state.top = ids[0];
        ctx.state.names = names;
        if (!ctx.body.querySelector('.cos-chart')) ctx.body.innerHTML = '<div class="cos-chart"></div>';
        COS.chart(ctx, 'lines', ctx.body.firstChild, {
            grid: { left: 72, right: 150, top: 16, bottom: 44 },
            tooltip: { trigger: 'item', formatter: function (p) {
                return COS.esc(names[p.seriesName] || p.seriesName) + '<br>t = ' + COS.fmt.time(p.value[0]) + '<br>' + COS.fmt.usd(p.value[1]);
            } },
            xAxis: COS.axis('Simulated time', { type: 'value', axisLabel: { formatter: COS.fmt.time, color: COS.token('--text-secondary') }, splitLine: { show: false } }),
            yAxis: COS.axis('Total risk (USD)', { type: 'value', nameGap: 56 }),
            series: ids.map(function (id, i) {
                var hot = i === 0;
                return { name: id, type: 'line', showSymbol: false, data: byV[id], z: hot ? 3 : 2,
                    lineStyle: { width: hot ? 2.5 : 1, color: COS.token(hot ? '--text-primary' : '--text-muted'), opacity: hot ? 1 : 0.55 },
                    itemStyle: { color: COS.token(hot ? '--text-primary' : '--text-muted') },
                    emphasis: { focus: 'series', lineStyle: { width: 2.5, opacity: 1 } },
                    endLabel: { show: i < 3, formatter: function () { return names[id] || id; }, color: COS.token('--text-primary'), fontSize: 11 } };
            })
        }, { height: 300, onClick: function (p) {
            window.location.href = COS.link('vessel.cfm', { imo: p.seriesName });
        } });
    },
    caption: function (ctx, data) {
        var n = ctx.state.names || {}, top = ctx.state.top;
        var v = 0;
        data.rows.forEach(function (r) { if (String(r[1]) === String(top)) v = r[2]; });
        return (n[top] || top) + ' built up the most risk: ' + COS.fmt.usd(v) + '.';
    }
});
</script>
<cfinclude template="/test/cos/shared/close.cfm">
