<!--: S5 sim.kpis (DASH.007): three run figures. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="s5_q" datasource="cos.bi">
with fv as (select vessel_id, max(cumulative) as rb, min(survival) as s from fact_risk_assessment where case_id = #cos_case# group by vessel_id),
     top as (select vessel_id, rb, s from fv order by rb desc limit 1)
select (select count(*) from fact_risk_assessment where case_id = #cos_case#) as n,
       (select coalesce(cast(sum(penalty) as text), '0') from (select o.case_id, o.tick, o.report_time, o.vessel_id, o.source, o.source as examiner, o.clause as event, o.zone as area, o.zone, o.concern, l.value as penalty, w.value as weight, null as value from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id) where case_id = #cos_case# and source = 'colreg') as pc,
       (select count(*) from (select o.case_id, o.tick, o.report_time, o.vessel_id, o.source, o.source as examiner, o.clause as event, o.zone as area, o.zone, o.concern, l.value as penalty, w.value as weight, null as value from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id) where case_id = #cos_case# and source = 'colreg') as nc,
       (select coalesce(cast(sum(penalty) as text), '0') from (select o.case_id, o.tick, o.report_time, o.vessel_id, o.source, o.source as examiner, o.clause as event, o.zone as area, o.zone, o.concern, l.value as penalty, w.value as weight, null as value from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id) where case_id = #cos_case# and source = 'examiner') as pp,
       (select count(*) from (select o.case_id, o.tick, o.report_time, o.vessel_id, o.source, o.source as examiner, o.clause as event, o.zone as area, o.zone, o.concern, l.value as penalty, w.value as weight, null as value from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id) where case_id = #cos_case# and source = 'examiner') as np,
       (select coalesce(cast(sum(penalty) as text), '0') from (select o.case_id, o.tick, o.report_time, o.vessel_id, o.source, o.source as examiner, o.clause as event, o.zone as area, o.zone, o.concern, l.value as penalty, w.value as weight, null as value from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id) where case_id = #cos_case# and source not in ('colreg', 'examiner')) as pl,
       coalesce((select vessel_id from top), 0) as imo,
       coalesce((select cast(rb as text) from top), 'null') as rb,
       coalesce((select cast(s as text) from top), 'null') as surv,
       (select count(*) from fact_crossing where case_id = #cos_case#) + (select count(*) from fact_give_way where case_id = #cos_case#)
         + (select count(*) from fact_head_on where case_id = #cos_case#) + (select count(*) from fact_overtaking where case_id = #cos_case#) as enc,
       (select count(*) from fact_crossing where case_id = #cos_case# and end_time = start_time) + (select count(*) from fact_give_way where case_id = #cos_case# and end_time = start_time)
         + (select count(*) from fact_head_on where case_id = #cos_case# and end_time = start_time) + (select count(*) from fact_overtaking where case_id = #cos_case# and end_time = start_time) as enc0
</cfquery>
<cfquery name="s5_v" datasource="cos.vessels">
select coalesce((select name from vessels where imo = '#s5_q.imo#'), '') as name
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="s5_q"><cfif s5_q.n GT 0><cfoutput>{"pc":#s5_q.pc#,"nc":#s5_q.nc#,"pp":#s5_q.pp#,"np":#s5_q.np#,"pl":#s5_q.pl#,"imo":#s5_q.imo#,"name":"#URLEncodedFormat(s5_v.name)#","rb":#s5_q.rb#,"surv":#s5_q.surv#,"enc":#s5_q.enc#,"enc0":#s5_q.enc0#},</cfoutput></cfif></cfloop>null]}
