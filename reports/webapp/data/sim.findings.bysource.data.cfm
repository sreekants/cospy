<!--: S8 sim.findings.bysource (DASH.010): findings by zone and source family. -->
<cfinclude template="shared/params.cfm">
<cfquery name="s8_q" datasource="cos.bi">
select zone, case when source in ('colreg', 'examiner') then source else 'local' end as fam,
       count(*) as n, cast(sum(penalty) as text) as pts
from fact_concern where case_id = #cos_case# group by 1, 2
</cfquery>
{<cfinclude template="shared/meta.cfm">,"rows":[<cfloop query="s8_q"><cfoutput>{"zone":"#URLEncodedFormat(s8_q.zone)#","fam":"#s8_q.fam#","n":#s8_q.n#,"pts":#s8_q.pts#},</cfoutput></cfloop>null]}
