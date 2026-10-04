<!--: V15 ves.episode.clauses (DASH.038) — one encounter: what is recorded, and what cannot yet be said. -->
<cfparam name="composed" default="0">
<cfif composed EQ 0><cfinclude template="../shared/open.cfm"></cfif>
<cfoutput><section data-component="ves.episode.clauses" data-endpoint="#cos_root#/data/ves.episode.clauses.data.cfm"></section></cfoutput>
<script>
(function () {
    var GAPS = [
        ['whether each rule was met', 'REQ.037-06'], ['which vessel was give-way or stand-on', 'REQ.037-07'],
        ['closest approach (DCPA, TCPA)', 'REQ.037-05'], ['what the other vessel did', 'REQ.037-02'],
        ['why P_C peaked', 'REQ.037-03/04']];
    var ctx = COS.component('ves.episode.clauses', {
        code: 'V15', title: 'Selected encounter', hint: 'What is known about one encounter, and what is not.', vessel: true,
        query: function () { return { t: COS.state.get('t', '-1') }; },
        mock: function () {
            return { fnd: [[171, 'Rule15', 'COLREG.Rule15/CrossAstern']],
                     rows: [{ k: 'Crossing', s: 171, e: 187, tg: 9000002, name: 'MOCK BERGE ODEL', at: 1, pc: 0.196, pct: 171 }] };
        },
        render: function (ctx, data) {
            var r = data.rows[0];
            var fnd = (data.fnd || []).map(function (f) { return COS.esc(f[1]) + ' → <code>' + COS.esc(f[2]) + '</code> (' + COS.fmt.time(f[0]) + ')'; }).join('<br>');
            var h = r.at ? '' : '<p class="cos-notice">No encounter at this moment: showing the nearest one.</p>';
            ctx.body.innerHTML = h + '<div class="v15-kv"></div><p class="cos-notice">Not recorded: ' + GAPS.map(function (g) {
                return COS.esc(g[0]) + ' — ' + COS.esc(g[1]); }).join(' · ') + '</p>';
            COS.ui.kv(ctx.body.querySelector('.v15-kv'), [
                ['Encounter', r.k + ' with ' + (r.name || 'vessel') + ' ' + r.tg],
                ['Time', COS.fmt.time(r.s) + ' – ' + COS.fmt.time(r.e) + (r.s === r.e ? ' (seen once)' : '')],
                ['Highest P_C', COS.fmt.prob(r.pc) + ' at ' + COS.fmt.time(r.pct)],
                ['COLREG findings', fnd || 'none', true]
            ]);
        },
        caption: function (ctx, data) {
            return GAPS.length + ' things cannot be shown yet (REQ.037).';
        }
    });
    if (ctx) COS.on('time-cursor', function () { ctx.reload(); });
})();
</script>
<cfif composed EQ 0><cfinclude template="../shared/close.cfm"></cfif>
