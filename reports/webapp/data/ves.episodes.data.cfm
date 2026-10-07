<!--: V14 ves.episodes (DASH.037): encounters of the vessel with findings and peak P_C in each window.
      The vessel's findings and assessments are materialised once (SQLite 3.35+), not rescanned per encounter:
      the store has no usable index on case/vessel, and a large run has ~4 000 encounters per vessel. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="v14_q" datasource="cos.bi">
with fc as materialized (select tick from (select o.case_id, o.tick, o.report_time, o.vessel_id, o.source, o.source as examiner, o.clause as event, o.zone as area, o.zone, o.concern, l.value as penalty, w.value as weight, null as value from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id) where case_id = #cos_case# and vessel_id = #Int(cos_imo)#),
     ra as materialized (select tick, p_collision from fact_risk_assessment where case_id = #cos_case# and vessel_id = #Int(cos_imo)#),
     en as materialized (
  select 'Crossing' as k, start_time as s, end_time as e, target_ship as tg from fact_crossing where case_id = #cos_case# and own_ship = #Int(cos_imo)#
  union all select 'Give-way', start_time, end_time, target_ship from fact_give_way where case_id = #cos_case# and own_ship = #Int(cos_imo)#
  union all select 'Head-on', start_time, end_time, target_ship from fact_head_on where case_id = #cos_case# and own_ship = #Int(cos_imo)#
  union all select 'Overtaking', start_time, end_time, target_ship from fact_overtaking where case_id = #cos_case# and own_ship = #Int(cos_imo)#)
select en.k as k, cast(en.s as text) as s, cast(en.e as text) as e, en.tg as tg,
  (select count(*) from fc where fc.tick between en.s and en.e) as nf,
  coalesce((select cast(max(ra.p_collision) as text) from ra where ra.tick between en.s and en.e), 'null') as pc
from en order by en.s, en.e
</cfquery>
<cfquery name="v14_v" datasource="cos.vessels">
select imo, name from vessels
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"names":[<cfloop query="v14_v"><cfoutput>["#URLEncodedFormat(v14_v.imo)#","#URLEncodedFormat(v14_v.name)#"],</cfoutput></cfloop>null],"rows":[<cfloop query="v14_q"><cfoutput>{"k":"#v14_q.k#","s":#v14_q.s#,"e":#v14_q.e#,"tg":#v14_q.tg#,"nf":#v14_q.nf#,"pc":#v14_q.pc#},</cfoutput></cfloop>null]}
