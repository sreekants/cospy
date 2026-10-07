<!--: V9 ves.tl.findings (DASH.032): findings for the vessel; ?since=<tick>. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="v9_q" datasource="cos.bi">
select tick, case when source in ('colreg', 'examiner') then source else 'local' end as fam, examiner, event, zone, concern,
       cast(penalty as text) as pts, coalesce(cast(value as text), 'null') as val
from (select o.case_id, o.tick, o.report_time, o.vessel_id, o.source, o.source as examiner, o.clause as event, o.zone as area, o.zone, o.concern, l.value as penalty, w.value as weight, null as value from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id) where case_id = #cos_case# and vessel_id = #Int(cos_imo)# and tick > #cos_since# order by tick
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="v9_q"><cfoutput>[#v9_q.tick#,"#v9_q.fam#","#URLEncodedFormat(v9_q.examiner)#","#URLEncodedFormat(v9_q.event)#","#URLEncodedFormat(v9_q.zone)#","#URLEncodedFormat(v9_q.concern)#",#v9_q.pts#,#v9_q.val#],</cfoutput></cfloop>null]}
