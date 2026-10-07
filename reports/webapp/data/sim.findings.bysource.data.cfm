<!--: S8 sim.findings.bysource (DASH.010): findings by zone and source family. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="s8_q" datasource="cos.bi">
select zone, case when source in ('colreg', 'examiner') then source else 'local' end as fam,
       count(*) as n, cast(sum(penalty) as text) as pts
from (select o.case_id, o.tick, o.report_time, o.vessel_id, o.source, o.source as examiner, o.clause as event, o.zone as area, o.zone, o.concern, l.value as penalty, w.value as weight, null as value from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id) where case_id = #cos_case# group by 1, 2
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="s8_q"><cfoutput>{"zone":"#URLEncodedFormat(s8_q.zone)#","fam":"#s8_q.fam#","n":#s8_q.n#,"pts":#s8_q.pts#},</cfoutput></cfloop>null]}
