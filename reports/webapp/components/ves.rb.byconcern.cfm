<!--: V29 ves.rb.byconcern (DASH.052) — what this vessel's consequential risk is made of. -->
<cfinclude template="../shared/open.cfm">
<cfoutput><section data-component="ves.rb.byconcern" data-endpoint="#cos_root#/data/ves.rb.byconcern.data.cfm"></section></cfoutput>
<script>
COS.component('ves.rb.byconcern', {
    code: 'V29', title: 'Risk by concern', hint: 'What kind of harm the risk of this vessel comes from.', vessel: true,
    mock: function () {
        return { rows: [{ concern: 'safety', usd: 9000 }, { concern: 'traffic', usd: 15000 },
                        { concern: 'environmental', usd: 0 }, { concern: 'operational', usd: 19000 }] };
    },
    render: function (ctx, data) {
        var cs = COS.enc.concerns, tot = 0, by = {};
        data.rows.forEach(function (r) { by[r.concern] = r.usd; tot += r.usd; });
        var shares = cs.map(function (c) { return tot ? 100 * (by[c.key] || 0) / tot : 0; });
        var ink = COS.token('--text-primary');
        if (!ctx.body.querySelector('.cos-chart')) ctx.body.innerHTML = '<div class="cos-chart"></div><p class="v29-note cos-notice"></p>';
        COS.chart(ctx, 'radar', ctx.body.firstChild, {
            tooltip: { trigger: 'item', formatter: function () {
                return cs.map(function (c, i) { return COS.esc(c.label) + ': ' + COS.fmt.usd(by[c.key] || 0) + ' (' + Math.round(shares[i]) + ' %)'; }).join('<br>'); } },
            radar: { radius: '66%', center: ['50%', '54%'], splitNumber: 4,
                indicator: cs.map(function (c) { return { name: c.label, max: 100 }; }),
                axisName: { color: COS.token('--text-secondary'), fontSize: 12 },
                splitLine: { lineStyle: { color: COS.token('--grid') } }, splitArea: { show: false },
                axisLine: { lineStyle: { color: COS.token('--line') } } },
            series: [{ type: 'radar', symbol: 'circle', symbolSize: 6,
                lineStyle: { width: 2, color: ink }, itemStyle: { color: ink },
                areaStyle: { color: COS.token('--accent'), opacity: 0.18 },
                label: { show: true, color: ink, fontSize: 11, formatter: function (p) { return Math.round(p.value) + ' %'; } },
                data: [{ value: shares, name: 'Share of this vessel\'s accumulated Rb' }] }]
        }, { height: 260, trigger: 'item' });
        var big = cs.slice().sort(function (a, b) { return (by[b.key] || 0) - (by[a.key] || 0); })[0];
        ctx.body.querySelector('.v29-note').textContent = big.key === 'operational'
            ? 'The operational share comes from AUV damage. It rests on a placeholder value (0.17 loss of communications).'
            : 'The largest share is ' + big.label.toLowerCase() + '.';
    },
    flags: function () { return [{ ticket: 'REQ.001', text: 'Risk network tables are placeholders' }]; },
    caption: function (ctx, data) {
        var tot = 0; data.rows.forEach(function (r) { tot += r.usd; });
        return 'This vessel built up ' + COS.fmt.usd(tot) + ' of risk.';
    }
});
</script>
<cfinclude template="../shared/close.cfm">
