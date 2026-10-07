<!--: S14 sim.heat.zoneconcern (DASH.016): points and counts by zone and concern. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="s14_q" datasource="cos.bi">
select zone, concern, count(*) as n, cast(sum(penalty) as text) as pts from (select o.case_id, o.tick, o.report_time, o.vessel_id, o.source, o.source as examiner, o.clause as event, o.zone as area, o.zone, o.concern, l.value as penalty, w.value as weight, null as value from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id) where case_id = #cos_case# group by zone, concern
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="s14_q"><cfoutput>{"zone":"#URLEncodedFormat(s14_q.zone)#","concern":"#URLEncodedFormat(s14_q.concern)#","n":#s14_q.n#,"pts":#s14_q.pts#},</cfoutput></cfloop>null]}
