<!--: S20 sim.rev (DASH.022) — the normative side that cannot yet be computed, and why. No endpoint. -->
<cfparam name="composed" default="0">
<cfif composed EQ 0><cfinclude template="../shared/open.cfm"></cfif>
<section data-component="sim.rev"></section>
<script>
COS.component('sim.rev', {
    code: 'S20', title: 'Rule-based risk (R_ev): not yet', hint: 'This number cannot be computed yet. The table only shows its future shape.',
    mockReason: 'R_ev cannot be computed yet (REQ.031, COS.044 §1)',
    mock: function () {
        var r = COS.mock.rng('S20');
        return { rows: COS.mock.vessels.slice(0, 4).map(function (v) {
            var ro = 1 + r() * 3, rl = 1000 + r() * 9000;
            return { vessel: v, ro: ro, rwrl: 0.25 * rl, rev: ro * 0.25 * rl * 4 };
        }) };
    },
    render: function (ctx, data) {
        ctx.body.innerHTML = '<p class="cos-notice cos-placeholder">R_ev cannot be computed yet. Two things are missing: the criticality ' +
            'function f (REQ.031) and a settled meaning of Rl (COS.044 §1). The regime chart comes after limits are registered (REQ.014). It is never shown with made-up values.</p><div class="s20-t"></div>';
        COS.ui.table(ctx.body.querySelector('.s20-t'), [
            { key: 'vessel', label: 'Vessel' },
            { key: 'rev', label: '‖R_ev‖₁ (USD)', num: true, fmt: COS.fmt.int },
            { key: 'ro', label: 'Ro (mean)', num: true, fmt: function (v) { return COS.fmt.num(v, 2); } },
            { key: 'rwrl', label: 'Rw × Rl (mean, USD)', num: true, fmt: COS.fmt.int }
        ], data.rows, { ctx: ctx, sortable: false });
    },
    caption: function () { return 'Every value in this table is made up.'; }
});
</script>
<cfif composed EQ 0><cfinclude template="../shared/close.cfm"></cfif>
