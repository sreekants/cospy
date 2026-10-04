<!--: V23 ves.findings.log (DASH.046) — the citeable record of findings for the voyage. -->
<cfinclude template="/test/cos/shared/open.cfm">
<cfoutput><section data-component="ves.findings.log" data-endpoint="#cos_root#/data/ves.findings.log.data.cfm"></section></cfoutput>
<script>
COS.component('ves.findings.log', {
    code: 'V23', title: 'Findings', hint: 'Every finding for this vessel. Click one to see that moment.', vessel: true,
    query: function (ctx) { return { since: ctx.state.lastTick === undefined ? -1 : ctx.state.lastTick }; },
    merge: function (old, fresh) { return Object.assign({}, old, { rows: old.rows.concat(fresh.rows) }); },
    mock: function () {
        return { rows: [{ t: 171, zone: 'high_seas', by: 'Rule15', event: 'COLREG.Rule15/CrossAstern', pts: 50, val: null },
                        { t: 1820, zone: 'territorial_waters', by: 'GroundingExaminer', event: 'grounding.contact', pts: 95, val: -20.1 }] };
    },
    render: function (ctx, data) {
        data.rows.forEach(function (r) { ctx.state.lastTick = r.t; });
        COS.ui.table(ctx.body, [
            { key: 't', label: 'Time', fmt: COS.fmt.time },
            { key: 'zone', label: 'Zone', fmt: function (v) { return COS.enc.find(COS.enc.zones, v).label; } },
            { key: 'by', label: 'Recorded by → finding', html: true, fmt: function (v, r) { return COS.esc(v) + ' → <code>' + COS.esc(r.event) + '</code>'; } },
            { key: 'pts', label: 'Points', num: true, fmt: COS.fmt.int },
            { key: 'val', label: 'Value', num: true, fmt: function (v) { return v === null ? '—' : COS.fmt.num(v, 1); } }
        ], data.rows, { ctx: ctx, maxHeight: 360, onRow: function (r) {
            COS.state.set({ t: r.t }); COS.emit('time-cursor', { t: r.t }); } });
    },
    flags: function () { return [{ ticket: 'COS.044', text: 'Seamanship findings are counted again at every check (§2)' }]; },
    caption: function (ctx, data) { return data.rows.length + ' findings.'; }
});
</script>
<cfinclude template="/test/cos/shared/close.cfm">
