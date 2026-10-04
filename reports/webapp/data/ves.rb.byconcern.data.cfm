<!--: V29 ves.rb.byconcern (DASH.052): accumulated Rb by concern for the vessel. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="v29_q" datasource="cos.bi">
select b.concern as concern, cast(sum(case when r.cost > 0 then r.increment * b.exposure / r.cost else 0 end) as text) as usd
from fact_rb b join fact_risk_assessment r on r.case_id = b.case_id and r.own_ship = b.vessel_id and r.tick = b.tick
where b.case_id = #cos_case# and b.vessel_id = #Int(cos_imo)# group by b.concern
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="v29_q"><cfoutput>{"concern":"#URLEncodedFormat(v29_q.concern)#","usd":#v29_q.usd#},</cfoutput></cfloop>null]}
