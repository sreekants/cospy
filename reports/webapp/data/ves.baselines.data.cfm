<!--: V24 ves.baselines (DASH.047): EL, P_any, P_sum and IR per assessment; ?since=<tick>. -->
<cfinclude template="/test/cos/shared/params.cfm">
<cfquery name="v24_q" datasource="cos.bi">
select tick, cast(cost as text) as el, cast(p_any_hazard as text) as pa, cast(p_sum_hazard as text) as ps,
       coalesce(cast(individual_risk as text), 'null') as ir
from fact_risk_assessment where case_id = #cos_case# and own_ship = #Int(cos_imo)# and tick > #cos_since# order by tick
</cfquery>
{<cfinclude template="/test/cos/shared/meta.cfm">,"rows":[<cfloop query="v24_q"><cfoutput>[#v24_q.tick#,#v24_q.el#,#v24_q.pa#,#v24_q.ps#,#v24_q.ir#],</cfoutput></cfloop>null]}
