<!--: V7 ves.tl.hazards (DASH.030): collision and grounding probability per assessment; ?since=<tick>. -->
<cfinclude template="/test/cos/shared/params.cfm">
<cfquery name="v7_q" datasource="cos.bi">
select tick, cast(p_collision as text) as pc, cast(p_grounding as text) as pg from fact_risk_assessment
where case_id = #cos_case# and own_ship = #Int(cos_imo)# and tick > #cos_since# order by tick
</cfquery>
{<cfinclude template="/test/cos/shared/meta.cfm">,"rows":[<cfloop query="v7_q"><cfoutput>[#v7_q.tick#,#v7_q.pc#,#v7_q.pg#],</cfoutput></cfloop>null]}
