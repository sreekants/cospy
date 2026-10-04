<!--: V15 ves.episode.clauses (DASH.038): the encounter at ?t= (or the nearest), with what is recorded in its window. -->
<cfinclude template="../shared/params.cfm">
<cfparam name="URL.t" default="-1">
<cfquery name="v15_q" datasource="cos.bi">
with en as (
  select 'Crossing' as k, start_time as s, end_time as e, target_ship as tg from fact_crossing where case_id = #cos_case# and own_ship = #Int(cos_imo)#
  union all select 'Give-way', start_time, end_time, target_ship from fact_give_way where case_id = #cos_case# and own_ship = #Int(cos_imo)#
  union all select 'Head-on', start_time, end_time, target_ship from fact_head_on where case_id = #cos_case# and own_ship = #Int(cos_imo)#
  union all select 'Overtaking', start_time, end_time, target_ship from fact_overtaking where case_id = #cos_case# and own_ship = #Int(cos_imo)#),
pick as (select * from en order by case when #Int(URL.t)# between s and e then 0 else 1 end,
                                   abs(s - (case when #Int(URL.t)# < 0 then 0 else #Int(URL.t)# end)) limit 1)
select k, cast(s as text) as s, cast(e as text) as e, cast(s as integer) as si, cast(e as integer) as ei, tg,
       case when #Int(URL.t)# between s and e then 1 else 0 end as at,
       coalesce((select cast(max(p_collision) as text) from fact_risk_assessment r where r.case_id = #cos_case# and r.own_ship = #Int(cos_imo)# and r.tick between pick.s and pick.e), 'null') as pc,
       coalesce((select r.tick from fact_risk_assessment r where r.case_id = #cos_case# and r.own_ship = #Int(cos_imo)# and r.tick between pick.s and pick.e order by r.p_collision desc limit 1), -1) as pct
from pick
</cfquery>
<cfquery name="v15_f" datasource="cos.bi">
select f.tick, f.examiner, f.event from fact_concern f
where f.case_id = #cos_case# and f.vessel_id = #Int(cos_imo)# and f.source = 'colreg' and f.tick between #Int(v15_q.si)# and #Int(v15_q.ei)#
</cfquery>
<cfquery name="v15_v" datasource="cos.vessels">
select coalesce((select name from vessels where imo = '#Int(v15_q.tg)#'), '') as name
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"fnd":[<cfloop query="v15_f"><cfoutput>[#v15_f.tick#,"#URLEncodedFormat(v15_f.examiner)#","#URLEncodedFormat(v15_f.event)#"],</cfoutput></cfloop>null],"rows":[<cfloop query="v15_q"><cfoutput>{"k":"#v15_q.k#","s":#v15_q.s#,"e":#v15_q.e#,"tg":#v15_q.tg#,"name":"#URLEncodedFormat(v15_v.name)#","at":#v15_q.at#,"pc":#v15_q.pc#,"pct":#v15_q.pct#},</cfoutput></cfloop>null]}
