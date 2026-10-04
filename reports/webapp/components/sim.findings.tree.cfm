<!--: S9 sim.findings.tree (DASH.011) — which recorder produced which findings. -->
<cfinclude template="/test/cos/shared/open.cfm">
<cfoutput><section data-component="sim.findings.tree" data-endpoint="#cos_root#/data/sim.findings.tree.data.cfm"></section></cfoutput>
<script>
COS.component('sim.findings.tree', {
    code: 'S9', title: 'Findings in detail', hint: 'Each kind of finding, who recorded it, and how often.',
    mock: function () {
        return { rows: [
            { fam: 'colreg', by: 'Rule15', event: 'COLREG.Rule15/CrossAstern', n: 25, pts: 1250 },
            { fam: 'colreg', by: 'Rule14', event: 'COLREG.Rule14.a', n: 13, pts: 650 },
            { fam: 'examiner', by: 'GroundingExaminer', event: 'grounding.contact', n: 400, pts: 38000 },
            { fam: 'examiner', by: 'CollisionExaminer', event: 'collision.cost', n: 60, pts: 4200 }] };
    },
    render: function (ctx, data) {
        var h = '<div class="cos-tablewrap"><table class="cos-table"><thead><tr><th scope="col">Recorded by → finding</th>' +
                '<th scope="col" class="num">Findings</th><th scope="col" class="num">Points</th></tr></thead><tbody>';
        COS.enc.sources.forEach(function (f) {
            var rows = data.rows.filter(function (r) { return r.fam === f.key; });
            if (!rows.length) return;
            var n = 0, p = 0;
            rows.forEach(function (r) { n += r.n; p += r.pts; });
            h += '<tr class="cos-group-row"><td>' + COS.esc(f.label) + '</td><td class="num">' + COS.fmt.int(n) +
                 '</td><td class="num">' + COS.fmt.int(p) + '</td></tr>';
            rows.forEach(function (r) {
                h += '<tr><td>&nbsp;&nbsp;' + COS.esc(r.by) + ' → <code>' + COS.esc(r.event) + '</code></td><td class="num">' +
                     COS.fmt.int(r.n) + '</td><td class="num">' + COS.fmt.int(r.pts) + '</td></tr>';
            });
        });
        h += '</tbody></table></div><p class="cos-notice">Checks that never fired: <span class="cos-missing">not known (the list of checks is not recorded)</span></p>';
        ctx.body.innerHTML = h;
    },
    flags: function () { return [{ ticket: 'COS.044', text: 'Seamanship findings are counted again at every check (§2)' }]; },
    caption: function (ctx, data) {
        var by = {};
        data.rows.forEach(function (r) { by[r.by] = 1; });
        return Object.keys(by).length + ' checks produced findings.';
    }
});
</script>
<cfinclude template="/test/cos/shared/close.cfm">
