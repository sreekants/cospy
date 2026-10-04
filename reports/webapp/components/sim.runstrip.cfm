<!--: S1 sim.runstrip (DASH.003) — which run, which vessel, still running? (SIM-01, SH-14). -->
<cfinclude template="../shared/open.cfm">
<cfoutput><section data-component="sim.runstrip" data-endpoint="#cos_root#/data/sim.runstrip.data.cfm"></section></cfoutput>
<script>
COS.component('sim.runstrip', {
    code: 'S1', title: 'Run', hint: 'Which run, which vessel, and whether it is still running.', everyPoll: true,
    mock: function () { return { rows: [{ duration: 9909, vut: 'MOCK TRUE NORTH', vutimo: 9000003 }] }; },
    render: function (ctx, data) {
        var r = data.rows[0], miss = function (t) { return '<span class="cos-missing">' + COS.esc(t) + '</span>'; };
        var st = ctx.mode === 'mock' ? 'mock' : ctx.state.live === true ? 'live — tick ' + COS.fmt.int(ctx.meta.maxtick)
               : ctx.state.live === false ? 'ended' : 'checking';
        var cells = [
            ['Run', COS.esc(ctx.meta.case || (ctx.mode === 'mock' ? '100000000000001' : '—'))],
            ['Scenario', miss('not in manifest')],
            ['Vessel under test', r.vut ? COS.esc(r.vut) + ' (' + r.vutimo + ')' : miss('not recorded — REQ.037-08')],
            ['Length', COS.fmt.dur(r.duration) + ' (simulated)'],
            ['State', COS.esc(st)]
        ];
        ctx.body.innerHTML = '<div class="cos-strip">' + cells.map(function (c) {
            return '<div><span>' + c[0] + '</span><b>' + c[1] + '</b></div>'; }).join('') + '</div>';
    },
    caption: function () { return ''; }
});
</script>
<cfinclude template="../shared/close.cfm">
