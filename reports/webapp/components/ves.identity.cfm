<!--: V1 ves.identity (DASH.024) — which vessel, and its role in the run. -->
<cfinclude template="/test/cos/shared/open.cfm">
<cfoutput><section data-component="ves.identity" data-endpoint="#cos_root#/data/ves.identity.data.cfm"></section></cfoutput>
<script>
COS.component('ves.identity', {
    code: 'V1', title: 'Vessel', hint: 'Which vessel this page is about.', vessel: true, static: true,
    mock: function () { return { rows: [{ name: 'MOCK TRUE NORTH', imo: '9000003', settings: 'ship.model=$(CONFIG)/vehicle/ship/ferry.yaml' }] }; },
    render: function (ctx, data) {
        var r = data.rows[0], m = /ship\.model=\S*\/([\w.-]+)\.yaml/.exec(r.settings || '');
        if (ctx.mode === 'live' && ctx.meta.imo_default && COS.state.get('imo', '0') === '0') COS.state.set({ imo: r.imo });
        var miss = function (t) { return '<span class="cos-missing">' + COS.esc(t) + '</span>'; };
        var cells = [
            ['Name', COS.esc(r.name)], ['IMO', COS.esc(r.imo)],
            ['Ship model', m ? COS.esc(m[1]) : miss('not in the register')],
            ['Role', miss('not recorded — REQ.037-08')],
            ['Length / draught', miss('not in the register')],
            ['', '<a href="' + COS.esc(COS.link('sim.cfm')) + '">← Back to the run</a>']
        ];
        ctx.body.innerHTML = (ctx.meta.imo_default && ctx.mode === 'live' ? '<p class="cos-notice">No vessel chosen: showing the one with the most data.</p>' : '') +
            '<div class="cos-strip">' + cells.map(function (c) { return '<div><span>' + c[0] + '</span><b>' + c[1] + '</b></div>'; }).join('') + '</div>';
    },
    caption: function () { return ''; }
});
</script>
<cfinclude template="/test/cos/shared/close.cfm">
