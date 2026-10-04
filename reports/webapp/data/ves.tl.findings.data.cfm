<!--: V9 ves.tl.findings (DASH.032): findings for the vessel; ?since=<tick>. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="v9_q" datasource="cos.bi">
select tick, case when source in ('colreg', 'examiner') then source else 'local' end as fam, examiner, event, zone, concern,
       cast(penalty as text) as pts, coalesce(cast(value as text), 'null') as val
from fact_concern where case_id = #cos_case# and vessel_id = #Int(cos_imo)# and tick > #cos_since# order by tick
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="v9_q"><cfoutput>[#v9_q.tick#,"#v9_q.fam#","#URLEncodedFormat(v9_q.examiner)#","#URLEncodedFormat(v9_q.event)#","#URLEncodedFormat(v9_q.zone)#","#URLEncodedFormat(v9_q.concern)#",#v9_q.pts#,#v9_q.val#],</cfoutput></cfloop>null]}
