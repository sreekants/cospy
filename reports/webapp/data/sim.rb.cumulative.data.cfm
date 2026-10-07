<!--: S10 sim.rb.cumulative (DASH.012): cumulative Rb per vessel per tick; ?since=<tick> for increments. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="s10_q" datasource="cos.bi">
select tick, vessel_id, cast(cumulative as text) as c from fact_risk_assessment
where case_id = #cos_case# and tick > #cos_since# order by tick
</cfquery>
<cfquery name="s10_v" datasource="cos.vessels">
select imo, name from vessels
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"names":[<cfloop query="s10_v"><cfoutput>["#URLEncodedFormat(s10_v.imo)#","#URLEncodedFormat(s10_v.name)#"],</cfoutput></cfloop>null],"rows":[<cfloop query="s10_q"><cfoutput>[#s10_q.tick#,#s10_q.vessel_id#,#s10_q.c#],</cfoutput></cfloop>null]}
