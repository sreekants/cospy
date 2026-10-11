<!--: V6 ves.tl.rb (DASH.029): risk (Rr) at each assessment for the vessel; ?since=<tick>. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="v6_q" datasource="cos.bi">
select tick, cast(rr as text) as r from fact_risk_assessment
where case_id = #cos_case# and vessel_id = #Int(cos_imo)# and tick > #cos_since# order by tick
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="v6_q"><cfoutput>[#v6_q.tick#,#v6_q.r#],</cfoutput></cfloop>null]}
