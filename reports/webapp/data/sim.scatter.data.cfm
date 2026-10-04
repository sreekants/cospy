<!--: S19 sim.scatter (DASH.021): penalty points and final Rb per vessel. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="s19_q" datasource="cos.bi">
select r.own_ship as imo, cast(max(r.cumulative) as text) as rb,
       coalesce((select cast(sum(penalty) as text) from fact_concern f where f.case_id = #cos_case# and f.vessel_id = r.own_ship), '0') as pts
from fact_risk_assessment r where r.case_id = #cos_case# group by r.own_ship
</cfquery>
<cfquery name="s19_v" datasource="cos.vessels">
select imo, name from vessels
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"names":[<cfloop query="s19_v"><cfoutput>["#URLEncodedFormat(s19_v.imo)#","#URLEncodedFormat(s19_v.name)#"],</cfoutput></cfloop>null],"rows":[<cfloop query="s19_q"><cfoutput>[#s19_q.imo#,#s19_q.pts#,#s19_q.rb#],</cfoutput></cfloop>null]}
