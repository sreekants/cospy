<!--: C1 run.picker (DASH.001) — choose the run under discussion (SH-01, SH-02). -->
<cfinclude template="../shared/open.cfm">
<cfoutput><section data-component="run.picker" data-endpoint="#cos_root#/data/run.picker.data.cfm"></section></cfoutput>
<script>
COS.component('run.picker', {
    code: 'C1', title: 'Runs', hint: 'Pick the simulation run to look at.', allowNotfound: true, mockReason: 'no runs in the data',
    mock: function () {
        return { rows: [{ case: '100000000000001', duration: 9909, written: '2026-10-04T03:46:34' },
                        { case: '100000000000002', duration: 4399, written: '2026-10-03T18:02:11' }] };
    },
    render: function (ctx, data) {
        var current = ctx.meta.notfound ? null : (ctx.meta.case || data.rows[0].case);
        /* Write the resolved run into the address so the view and citations cannot drift. */
        if (ctx.mode === 'live' && current && COS.state.get('case', '0') === '0') COS.state.set({ case: current });
        ctx.body.innerHTML = (ctx.meta.notfound ? '<p class="cos-notice cos-error">' + COS.esc(ctx.meta.notfound) + '</p>' : '') +
            '<div class="c1-t"></div>';
        COS.ui.table(ctx.body.querySelector('.c1-t'), [
            { key: 'case', label: 'Run', html: true, fmt: function (v) { return (v === current ? '▶ ' : '') + COS.esc(v); } },
            { key: 'duration', label: 'Duration', num: true, fmt: COS.fmt.dur },
            { key: 'written', label: 'Last data (UTC)', fmt: function (v) { return v ? v.replace('T', ' ').slice(0, 19) : '—'; } }
        ], data.rows, {
            ctx: ctx, maxHeight: 220,
            rowClass: function (r) { return r.case === current ? 'cos-selected' : ''; },
            onRow: ctx.mode === 'mock' ? null : function (r) { COS.state.set({ case: r.case }, true); window.location.reload(); }
        });
    },
    caption: function (ctx, data) {
        return data.rows.length + (data.rows.length === 1 ? ' run' : ' runs') + '. Scenario details are not recorded.';
    }
});
</script>
<cfinclude template="../shared/close.cfm">
