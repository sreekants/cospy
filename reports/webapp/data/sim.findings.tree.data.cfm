<!--: S9 sim.findings.tree (DASH.011): findings by source family, recorder and event. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="s9_q" datasource="cos.bi">
select case when source in ('colreg', 'examiner') then source else 'local' end as fam, examiner, event,
       count(*) as n, cast(sum(penalty) as text) as pts
from (select o.case_id, o.tick, o.report_time, o.vessel_id, o.source, o.source as examiner, o.clause as event, o.zone as area, o.zone, o.concern, l.value as penalty, w.value as weight, null as value from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id) where case_id = #cos_case# group by 1, 2, 3 order by 1, 4 desc
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="s9_q"><cfoutput>{"fam":"#s9_q.fam#","by":"#URLEncodedFormat(s9_q.examiner)#","event":"#URLEncodedFormat(s9_q.event)#","n":#s9_q.n#,"pts":#s9_q.pts#},</cfoutput></cfloop>null]}
