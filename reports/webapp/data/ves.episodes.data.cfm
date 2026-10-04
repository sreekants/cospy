<!--: V14 ves.episodes (DASH.037): encounters of the vessel with findings and peak P_C in each window. -->
<cfinclude template="shared/params.cfm">
<cfquery name="v14_q" datasource="cos.bi">
with en as (
  select 'Crossing' as k, start_time as s, end_time as e, target_ship as tg from fact_crossing where case_id = #cos_case# and own_ship = #Int(cos_imo)#
  union all select 'Give-way', start_time, end_time, target_ship from fact_give_way where case_id = #cos_case# and own_ship = #Int(cos_imo)#
  union all select 'Head-on', start_time, end_time, target_ship from fact_head_on where case_id = #cos_case# and own_ship = #Int(cos_imo)#
  union all select 'Overtaking', start_time, end_time, target_ship from fact_overtaking where case_id = #cos_case# and own_ship = #Int(cos_imo)#)
select k, cast(s as text) as s, cast(e as text) as e, tg,
  (select count(*) from fact_concern f where f.case_id = #cos_case# and f.vessel_id = #Int(cos_imo)# and f.tick between en.s and en.e) as nf,
  coalesce((select cast(max(p_collision) as text) from fact_risk_assessment r where r.case_id = #cos_case# and r.own_ship = #Int(cos_imo)# and r.tick between en.s and en.e), 'null') as pc
from en order by en.s, en.e
</cfquery>
<cfquery name="v14_v" datasource="cos.vessels">
select imo, name from vessels
</cfquery>
{<cfinclude template="shared/meta.cfm">,"names":[<cfloop query="v14_v"><cfoutput>["#URLEncodedFormat(v14_v.imo)#","#URLEncodedFormat(v14_v.name)#"],</cfoutput></cfloop>null],"rows":[<cfloop query="v14_q"><cfoutput>{"k":"#v14_q.k#","s":#v14_q.s#,"e":#v14_q.e#,"tg":#v14_q.tg#,"nf":#v14_q.nf#,"pc":#v14_q.pc#},</cfoutput></cfloop>null]}
