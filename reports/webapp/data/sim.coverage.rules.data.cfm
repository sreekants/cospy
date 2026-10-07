<!--: S7 sim.coverage.rules (DASH.009): encounters where each rule could apply, and breaches recorded. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="s7_q" datasource="cos.bi">
with cr as (select count(*) as n, sum(end_time = start_time) as z from fact_crossing where case_id = #cos_case#),
     gw as (select count(*) as n, sum(end_time = start_time) as z from fact_give_way where case_id = #cos_case#),
     ho as (select count(*) as n, sum(end_time = start_time) as z from fact_head_on where case_id = #cos_case#),
     ov as (select count(*) as n, sum(end_time = start_time) as z from fact_overtaking where case_id = #cos_case#),
     br as (select 'Rule' || substr(event, 12, 2) as examiner, count(*) as n from (select o.case_id, o.tick, o.report_time, o.vessel_id, o.source, o.source as examiner, o.clause as event, o.zone as area, o.zone, o.concern, l.value as penalty, w.value as weight, null as value from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id) where case_id = #cos_case# and source = 'colreg' group by 1)
select 13 as rule, 'overtaking' as enc, (select n from ov) as n, coalesce((select n from br where examiner = 'Rule13'), 0) as b
union all select 14, 'head-on', (select n from ho), coalesce((select n from br where examiner = 'Rule14'), 0)
union all select 15, 'crossing', (select n from cr), coalesce((select n from br where examiner = 'Rule15'), 0)
union all select 16, 'give-way', (select n from gw), coalesce((select n from br where examiner = 'Rule16'), 0)
union all select 17, 'crossing (stand-on)', (select n from cr), coalesce((select n from br where examiner = 'Rule17'), 0)
union all select 0, 'all', (select n from cr) + (select n from gw) + (select n from ho) + (select n from ov),
       coalesce((select z from cr), 0) + coalesce((select z from gw), 0) + coalesce((select z from ho), 0) + coalesce((select z from ov), 0)
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="s7_q"><cfif s7_q.n GT 0><cfoutput>{"rule":#s7_q.rule#,"enc":"#URLEncodedFormat(s7_q.enc)#","n":#s7_q.n#,"b":#s7_q.b#},</cfoutput></cfif></cfloop>null]}
