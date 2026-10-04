<!--: S8 sim.findings.bysource (DASH.010) — how many findings came from law, local rules and practice, by zone. -->
<cfinclude template="/test/cos/shared/open.cfm">
<cfoutput><section data-component="sim.findings.bysource" data-endpoint="#cos_root#/data/sim.findings.bysource.data.cfm"></section></cfoutput>
<script>
COS.component('sim.findings.bysource', {
    code: 'S8', title: 'Findings by source', hint: 'Where findings came from: COLREG, local rules or seamanship.',
    mock: function () {
        var r = COS.mock.rng('S8'), rows = [];
        COS.enc.zones.forEach(function (z) {
            rows.push({ zone: z.key, fam: 'colreg', n: Math.round(r() * 12), pts: 0 });
            rows.push({ zone: z.key, fam: 'examiner', n: Math.round(200 + r() * 1500), pts: 0 });
        });
        rows.forEach(function (x) { x.pts = x.n * 50; });
        return { rows: rows };
    },
    render: function (ctx, data) {
        var zones = COS.enc.zones, fams = COS.enc.sources;
        var get = function (z, f, k) {
            var m = data.rows.filter(function (r) { return r.zone === z && r.fam === f; })[0];
            return m ? m[k] : 0;
        };
        ctx.body.innerHTML = '<div class="cos-chart"></div>';
        COS.chart(ctx, 'bars', ctx.body.firstChild, {
            grid: { left: 110, right: 48, top: 8, bottom: 56 },
            legend: { bottom: 0, data: fams.map(function (f) { return f.label; }), textStyle: { color: COS.token('--text-secondary') } },
            tooltip: { trigger: 'item', formatter: function (p) {
                var f = fams[p.seriesIndex], z = zones[p.dataIndex];
                return COS.esc(z.label) + '<br>' + COS.esc(f.label) + ': ' + COS.fmt.int(p.value) + ' findings · ' +
                    COS.fmt.pts(get(z.key, f.key, 'pts'));
            } },
            yAxis: COS.axis('', { type: 'category', inverse: true, data: zones.map(function (z) { return z.label; }), splitLine: { show: false } }),
            xAxis: COS.axis('Findings', { type: 'value', nameGap: 28 }),
            series: fams.map(function (f) {
                return { name: f.label, type: 'bar', stack: 'all', barWidth: 22,
                    itemStyle: { color: COS.enc.color(f), borderColor: COS.token('--surface-1'), borderWidth: 1 },
                    label: f.key === 'colreg' ? { show: true, position: 'right', color: COS.token('--text-primary'),
                        formatter: function (p) { return p.value ? 'COLREG ' + p.value : ''; } } : { show: false },
                    data: zones.map(function (z) { return get(z.key, f.key, 'n'); }) };
            })
        }, { height: 230 });
    },
    flags: function () { return [{ ticket: 'COS.044', text: 'Seamanship findings are counted again at every check (§2)' }]; },
    caption: function (ctx, data) {
        var tot = 0, c = 0;
        data.rows.forEach(function (r) { tot += r.n; if (r.fam === 'colreg') c += r.n; });
        return COS.fmt.int(c) + ' of ' + COS.fmt.int(tot) + ' findings (' + COS.fmt.pct(tot ? c / tot : null) + ') come from COLREG.';
    }
});
</script>
<cfinclude template="/test/cos/shared/close.cfm">
