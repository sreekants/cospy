<!--: V37 ves.tl.ro (DASH.076): penalty points and finding count per tick and source family for the vessel; ?since=<tick>. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="v37_q" datasource="cos.bi">
select tick, fam, cast(sum(penalty) as text) as pts, count(*) as n
from (select o.case_id, o.tick, o.vessel_id, case when o.source in ('colreg', 'examiner') then o.source else 'local' end as fam, l.value as penalty from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id)
where case_id = #cos_case# and vessel_id = #Int(cos_imo)# and tick > #cos_since#
group by tick, fam order by tick
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="v37_q"><cfoutput>[#v37_q.tick#,"#v37_q.fam#",#v37_q.pts#,#v37_q.n#],</cfoutput></cfloop>null]}
