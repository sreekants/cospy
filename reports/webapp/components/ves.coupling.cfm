<!--: V26 ves.coupling (DASH.049) — what the voyage cannot yet show, and which ticket enables it. No endpoint. -->
<cfinclude template="../shared/open.cfm">
<section data-component="ves.coupling"></section>
<script>
COS.component('ves.coupling', {
    code: 'V26', title: 'Not measured yet', hint: 'What this page cannot show yet.', static: true,
    mockReason: 'not instrumented',
    mock: function () { return { rows: [] }; },
    render: function (ctx) {
        ctx.mode = 'statement';
        COS.ui.kv(ctx.body, [
            ['Coupling', 'how rule breaches feed into risk (Rb) — REQ.006, REQ.009'],
            ['Duties over time', 'which rule applied at each step, and whether all could be met — REQ.013'],
            ['Entry decision', 'whether the vessel entered, waited or turned back at a gate, and the weather then — REQ.013']
        ]);
    },
    caption: function () { return 'Nothing here is made up.'; }
});
</script>
<cfinclude template="../shared/close.cfm">
