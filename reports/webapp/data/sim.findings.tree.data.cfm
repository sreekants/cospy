<!--: S9 sim.findings.tree (DASH.011): findings by source family, recorder and event. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="s9_q" datasource="cos.bi">
select case when source in ('colreg', 'examiner') then source else 'local' end as fam, examiner, event,
       count(*) as n, cast(sum(penalty) as text) as pts
from fact_concern where case_id = #cos_case# group by 1, 2, 3 order by 1, 4 desc
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="s9_q"><cfoutput>{"fam":"#s9_q.fam#","by":"#URLEncodedFormat(s9_q.examiner)#","event":"#URLEncodedFormat(s9_q.event)#","n":#s9_q.n#,"pts":#s9_q.pts#},</cfoutput></cfloop>null]}
