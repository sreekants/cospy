<!--: S11 sim.rb.byconcern (DASH.013): accumulated Rb by concern for the run. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="s11_q" datasource="cos.bi">
select b.concern as concern, cast(sum(case when r.rr > 0 then r.increment * b.value / r.rr else 0 end) as text) as usd
from fact_rr b join fact_risk_assessment r on r.case_id = b.case_id and r.finding_id = b.finding_id
where b.case_id = #cos_case# group by b.concern
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="s11_q"><cfoutput>{"concern":"#URLEncodedFormat(s11_q.concern)#","usd":#s11_q.usd#},</cfoutput></cfloop>null]}
