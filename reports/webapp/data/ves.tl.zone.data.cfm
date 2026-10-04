<!--: V5 ves.tl.zone (DASH.028): zone per assessment for the vessel; ?since=<tick>. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="v5_q" datasource="cos.bi">
select tick, zone from fact_risk_assessment where case_id = #cos_case# and own_ship = #Int(cos_imo)# and tick > #cos_since# order by tick
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="v5_q"><cfoutput>[#v5_q.tick#,"#v5_q.zone#"],</cfoutput></cfloop>null]}
