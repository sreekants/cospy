<!--: V23 ves.findings.log (DASH.046): findings of the vessel; ?since=<tick>. -->
<cfinclude template="/test/cos/shared/params.cfm">
<cfquery name="v23_q" datasource="cos.bi">
select tick, zone, examiner, event, cast(penalty as text) as pts, coalesce(cast(value as text), 'null') as val
from fact_concern where case_id = #cos_case# and vessel_id = #Int(cos_imo)# and tick > #cos_since# order by tick
</cfquery>
{<cfinclude template="/test/cos/shared/meta.cfm">,"rows":[<cfloop query="v23_q"><cfoutput>{"t":#v23_q.tick#,"zone":"#v23_q.zone#","by":"#URLEncodedFormat(v23_q.examiner)#","event":"#URLEncodedFormat(v23_q.event)#","pts":#v23_q.pts#,"val":#v23_q.val#},</cfoutput></cfloop>null]}
