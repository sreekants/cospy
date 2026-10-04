<!--: V12 ves.snapshot (DASH.035) — the vessel at one moment: the unit a debater cites. -->
<cfinclude template="../shared/open.cfm">
<cfoutput><section data-component="ves.snapshot" data-endpoint="#cos_root#/data/ves.snapshot.data.cfm"></section></cfoutput>
<script>
(function () {
    var ctx = COS.component('ves.snapshot', {
        code: 'V12', title: 'Selected moment', hint: 'The vessel at the moment you picked. Use Cite to share it.', vessel: true,
        query: function () { return { t: COS.state.get('t', '-1') }; },
        mock: function () {
            return { names: [['9000002', 'MOCK BERGE ODEL']], enc: [['Crossing', 9000002]], fnd: [[1820, 'GroundingExaminer', 'grounding.contact']],
                     rows: [{ t: 1820, zone: 'territorial_waters', d: 12.5, ds: 'measured', pc: 0.041, pg: 0.012, c: 8200 }] };
        },
        render: function (ctx, data) {
            var r = data.rows[0], z = COS.enc.find(COS.enc.zones, r.zone);
            var names = {};
            (data.names || []).forEach(function (n) { names[n[0]] = n[1]; });
            var enc = (data.enc || []).map(function (e) { return e[0] + ' with ' + (names[String(e[1])] || 'vessel') + ' (' + e[1] + ')'; }).join('; ') || 'none';
            var fnd = (data.fnd || []).map(function (f) { return f[1] + ' → ' + f[2] + ' (' + COS.fmt.time(f[0]) + ')'; }).join('; ') || 'none';
            COS.ui.kv(ctx.body, [
                ['Time', COS.fmt.time(r.t) + (COS.state.get('t', null) === null ? ' (last check; click a chart to pick a time)' : '')],
                ['Zone', z.label], ['Depth', COS.fmt.num(r.d, 1) + ' m (' + (r.ds || 'source not recorded') + ')'],
                ['P_C · P_G', COS.fmt.prob(r.pc) + ' · ' + COS.fmt.prob(r.pg)], ['Cumulative Rb', COS.fmt.usd(r.c)],
                ['Encounters now', enc], ['Findings near this time', fnd]
            ]);
        },
        caption: function () { return ''; }
    });
    if (ctx) COS.on('time-cursor', function () { ctx.reload(); });
})();
</script>
<cfinclude template="../shared/close.cfm">
