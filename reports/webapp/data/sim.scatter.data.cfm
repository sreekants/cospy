<!--: S19 sim.scatter (DASH.021): penalty points and final Rb per vessel. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="s19_q" datasource="cos.bi">
select r.vessel_id as imo, cast(max(r.cumulative) as text) as rb,
       coalesce((select cast(sum(penalty) as text) from (select o.case_id, o.tick, o.report_time, o.vessel_id, o.source, o.source as examiner, o.clause as event, o.zone as area, o.zone, o.concern, l.value as penalty, w.value as weight, null as value from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id) f where f.case_id = #cos_case# and f.vessel_id = r.vessel_id), '0') as pts
from fact_risk_assessment r where r.case_id = #cos_case# group by r.vessel_id
</cfquery>
<cfquery name="s19_v" datasource="cos.vessels">
select imo, name from vessels
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"names":[<cfloop query="s19_v"><cfoutput>["#URLEncodedFormat(s19_v.imo)#","#URLEncodedFormat(s19_v.name)#"],</cfoutput></cfloop>null],"rows":[<cfloop query="s19_q"><cfoutput>[#s19_q.imo#,#s19_q.pts#,#s19_q.rb#],</cfoutput></cfloop>null]}
