<!--: V4 ves.map (DASH.027): the vessel's position at each risk assessment, as a Morton code cast to text (TK-05). -->
<cfinclude template="../shared/params.cfm">
<cfquery name="v4_q" datasource="cos.bi">
select cast(dim_gps_id as text) as gps, tick, coalesce(zone, '') as zone
from fact_risk_assessment
where case_id = #cos_case# and vessel_id = #Int(cos_imo)# and dim_gps_id is not null
order by tick
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="v4_q"><cfoutput>["#v4_q.gps#",#Int(v4_q.tick)#,"#URLEncodedFormat(v4_q.zone)#"],</cfoutput></cfloop>null]}
