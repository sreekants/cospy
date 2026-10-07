<!--: V23 ves.findings.log (DASH.046): findings of the vessel; ?since=<tick>. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="v23_q" datasource="cos.bi">
select tick, zone, examiner, event, cast(penalty as text) as pts, coalesce(cast(value as text), 'null') as val
from (select o.case_id, o.tick, o.report_time, o.vessel_id, o.source, o.source as examiner, o.clause as event, o.zone as area, o.zone, o.concern, l.value as penalty, w.value as weight, null as value from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id) where case_id = #cos_case# and vessel_id = #Int(cos_imo)# and tick > #cos_since# order by tick
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="v23_q"><cfoutput>{"t":#v23_q.tick#,"zone":"#v23_q.zone#","by":"#URLEncodedFormat(v23_q.examiner)#","event":"#URLEncodedFormat(v23_q.event)#","pts":#v23_q.pts#,"val":#v23_q.val#},</cfoutput></cfloop>null]}
