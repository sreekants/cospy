<!--: V20 ves.rb.matrix (DASH.043): accumulated Rb by zone and concern for the vessel, and the final cumulative. -->
<cfinclude template="shared/params.cfm">
<cfquery name="v20_q" datasource="cos.bi">
select b.zone as zone, b.concern as concern,
       cast(sum(case when r.cost > 0 then r.increment * b.exposure / r.cost else 0 end) as text) as usd
from fact_rb b join fact_risk_assessment r on r.case_id = b.case_id and r.own_ship = b.vessel_id and r.tick = b.tick
where b.case_id = #cos_case# and b.vessel_id = #Int(cos_imo)# group by b.zone, b.concern
</cfquery>
<cfquery name="v20_c" datasource="cos.bi">
select coalesce(cast(max(cumulative) as text), 'null') as c from fact_risk_assessment where case_id = #cos_case# and own_ship = #Int(cos_imo)#
</cfquery>
{<cfinclude template="shared/meta.cfm">,<cfoutput>"final":#v20_c.c#</cfoutput>,"rows":[<cfloop query="v20_q"><cfoutput>{"zone":"#URLEncodedFormat(v20_q.zone)#","concern":"#URLEncodedFormat(v20_q.concern)#","v":#v20_q.usd#},</cfoutput></cfloop>null]}
