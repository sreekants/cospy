<!--: V12 ves.snapshot (DASH.035): the vessel at the assessment nearest ?t=. -->
<cfinclude template="../shared/params.cfm">
<cfparam name="URL.t" default="-1">
<cfquery name="v12_q" datasource="cos.bi">
select tick, zone, coalesce(cast(depth as text), 'null') as d, coalesce(depth_source, '') as ds,
       cast(p_collision as text) as pc, cast(p_grounding as text) as pg, cast(cumulative as text) as c
from fact_risk_assessment where case_id = #cos_case# and own_ship = #Int(cos_imo)#
order by case when #Int(URL.t)# < 0 then -tick else abs(tick - #Int(URL.t)#) end limit 1
</cfquery>
<cfquery name="v12_e" datasource="cos.bi">
select 'Crossing' as k, target_ship as tg from fact_crossing where case_id = #cos_case# and own_ship = #Int(cos_imo)# and start_time <= #Int(v12_q.tick)# and end_time >= #Int(v12_q.tick)#
union all select 'Give-way', target_ship from fact_give_way where case_id = #cos_case# and own_ship = #Int(cos_imo)# and start_time <= #Int(v12_q.tick)# and end_time >= #Int(v12_q.tick)#
union all select 'Head-on', target_ship from fact_head_on where case_id = #cos_case# and own_ship = #Int(cos_imo)# and start_time <= #Int(v12_q.tick)# and end_time >= #Int(v12_q.tick)#
union all select 'Overtaking', target_ship from fact_overtaking where case_id = #cos_case# and own_ship = #Int(cos_imo)# and start_time <= #Int(v12_q.tick)# and end_time >= #Int(v12_q.tick)#
</cfquery>
<cfquery name="v12_v" datasource="cos.vessels">
select imo, name from vessels
</cfquery>
<cfquery name="v12_f" datasource="cos.bi">
select tick, examiner, event from fact_concern where case_id = #cos_case# and vessel_id = #Int(cos_imo)# and abs(tick - #Int(v12_q.tick)#) <= 20 order by tick
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"names":[<cfloop query="v12_v"><cfoutput>["#URLEncodedFormat(v12_v.imo)#","#URLEncodedFormat(v12_v.name)#"],</cfoutput></cfloop>null],"enc":[<cfloop query="v12_e"><cfoutput>["#v12_e.k#",#v12_e.tg#],</cfoutput></cfloop>null],"fnd":[<cfloop query="v12_f"><cfoutput>[#v12_f.tick#,"#URLEncodedFormat(v12_f.examiner)#","#URLEncodedFormat(v12_f.event)#"],</cfoutput></cfloop>null],"rows":[<cfloop query="v12_q"><cfoutput>{"t":#v12_q.tick#,"zone":"#v12_q.zone#","d":#v12_q.d#,"ds":"#v12_q.ds#","pc":#v12_q.pc#,"pg":#v12_q.pg#,"c":#v12_q.c#},</cfoutput></cfloop>null]}
