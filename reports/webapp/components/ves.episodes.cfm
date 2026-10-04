<!--: V14 ves.episodes (DASH.037) — the encounters of the voyage, in order, as citeable episodes. -->
<cfinclude template="/test/cos/shared/open.cfm">
<cfoutput><section data-component="ves.episodes" data-endpoint="#cos_root#/data/ves.episodes.data.cfm"></section></cfoutput>
<script>
COS.component('ves.episodes', {
    code: 'V14', title: 'Encounter list', hint: 'Every encounter in order. Click one to see that moment.', vessel: true,
    mock: function () {
        return { names: [['9000002', 'MOCK BERGE ODEL']], rows: [
            { k: 'Crossing', s: 171, e: 171, tg: 9000002, nf: 0, pc: 0.196 },
            { k: 'Overtaking', s: 820, e: 1040, tg: 9000002, nf: 2, pc: 0.012 }] };
    },
    render: function (ctx, data) {
        var names = {};
        (data.names || []).forEach(function (n) { names[n[0]] = n[1]; });
        COS.ui.table(ctx.body, [
            { key: 's', label: 'Start', fmt: COS.fmt.time }, { key: 'e', label: 'End', fmt: COS.fmt.time },
            { key: 'k', label: 'Type' },
            { key: 'tg', label: 'Counterparty', fmt: function (v) { return (names[String(v)] || '') + ' ' + v; } },
            { key: 'nf', label: 'Findings', num: true, fmt: COS.fmt.int },
            { key: 'pc', label: 'Highest P_C', num: true, fmt: COS.fmt.prob }
        ], data.rows, { ctx: ctx, maxHeight: 320, onRow: function (r) {
            COS.state.set({ t: Math.round(r.s) }); COS.emit('time-cursor', { t: Math.round(r.s) }); } });
    },
    flags: function () { return [{ ticket: 'COS.044', text: 'One encounter can be counted many times (§2)' }]; },
    caption: function (ctx, data) { return data.rows.length + ' encounters.'; }
});
</script>
<cfinclude template="/test/cos/shared/close.cfm">
