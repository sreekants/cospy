<!--: C2 run.provenance (DASH.002) — what a reader must know before trusting a figure (SH-07). -->
<cfparam name="composed" default="0">
<cfif composed EQ 0><cfinclude template="../shared/open.cfm"></cfif>
<cfoutput><section data-component="run.provenance" data-endpoint="#cos_root#/data/run.provenance.data.cfm"></section></cfoutput>
<script>
COS.component('run.provenance', {
    code: 'C2', title: 'How the run was measured', hint: 'Read this before you trust any number.', ticket: 'REQ.037-09',
    mock: function () { return { rows: [{ basis: 'rate', period: 3600, dtmed: 20, cadence: 20 }] }; },
    render: function (ctx, data) {
        var r = data.rows[0];
        COS.ui.kv(ctx.body, [
            ['Risk checked every', COS.fmt.dur(r.cadence) + ' (the method says 1 s)'],
            ['Risk counted as', r.basis ? 'a ' + r.basis + ' per ' + COS.fmt.dur(r.period) + (r.dtmed !== r.cadence ? ', usually ' + COS.fmt.dur(r.dtmed) + ' per check' : '') : '—'],
            ['Not recorded', '<span class="cos-missing">time step, coupling on or off, random seed — REQ.037-09</span>', true],
            ['Not yet settled', 'equal weights for all concerns · no criticality function (REQ.031) · no registered limits (REQ.014) · risk network tables, zone factors and penalty points are placeholders']
        ]);
    },
    flags: function (ctx, data) {
        return data.rows[0].cadence > 1 ? [{ ticket: 'COS.044', text: 'Assessed every ' + data.rows[0].cadence + ' s, not 1 s' }] : [];
    },
    caption: function (ctx, data) {
        return 'Risk was checked every ' + COS.fmt.dur(data.rows[0].cadence) + '. The method says 1 s.';
    }
});
</script>
<cfif composed EQ 0><cfinclude template="../shared/close.cfm"></cfif>
