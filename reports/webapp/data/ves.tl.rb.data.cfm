<!--: V6 ves.tl.rb (DASH.029): cumulative Rb and increment per assessment for the vessel; ?since=<tick>. -->
<cfinclude template="shared/params.cfm">
<cfquery name="v6_q" datasource="cos.bi">
select tick, cast(cumulative as text) as c, cast(increment as text) as i from fact_risk_assessment
where case_id = #cos_case# and own_ship = #Int(cos_imo)# and tick > #cos_since# order by tick
</cfquery>
{<cfinclude template="shared/meta.cfm">,"rows":[<cfloop query="v6_q"><cfoutput>[#v6_q.tick#,#v6_q.c#,#v6_q.i#],</cfoutput></cfloop>null]}
