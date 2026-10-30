<!--: V39 ves.summary (DASH.078): what the voyage summary is written from: findings (with the counterparty of COLREG ones), encounters, collisions, zones, names and the run's scenario. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="v39_q" datasource="cos.bi">
with s as (select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r01
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r02
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r03
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r04
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r05
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r06
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r07
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r08
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r09
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r10
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r11
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r12
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r13
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r14
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r15
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r16
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r17
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r18
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r19
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r20
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r21
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r22
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r23
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r24
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r25
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r26
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r27
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r28
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r29
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r30
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r31
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r32
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r33
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r34
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r35
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r36
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r37
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r38
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r39
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r40
                   union all select case_id, dim_vessel_id as v, tick, clause, situation from fact_colreg_r41)
select o.id, o.tick, o.source, o.clause, o.zone, o.concern, cast(l.value as text) as pts,
       case when o.source = 'colreg' then coalesce((select s.situation from s where s.case_id = o.case_id and s.v = o.vessel_id and s.tick = o.tick and s.clause = o.clause limit 1), '') else '' end as sit
from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id
where o.case_id = #cos_case# and o.vessel_id = #Int(cos_imo)# order by o.tick
</cfquery>
<cfquery name="v39_e" datasource="cos.bi">
select 0 as k, id, cast(start_time as text) as s, cast(end_time as text) as e, target_ship as tg from fact_crossing where case_id = #cos_case# and own_ship = #Int(cos_imo)#
union all select 1, id, cast(start_time as text), cast(end_time as text), target_ship from fact_give_way where case_id = #cos_case# and own_ship = #Int(cos_imo)#
union all select 2, id, cast(start_time as text), cast(end_time as text), target_ship from fact_head_on where case_id = #cos_case# and own_ship = #Int(cos_imo)#
union all select 3, id, cast(start_time as text), cast(end_time as text), target_ship from fact_overtaking where case_id = #cos_case# and own_ship = #Int(cos_imo)#
union all select 4, id, cast(start_time as text), cast(end_time as text), target_ship from fact_stand_on where case_id = #cos_case# and own_ship = #Int(cos_imo)#
</cfquery>
<cfquery name="v39_c" datasource="cos.bi">
select id, tick, target_ship as tg, coalesce(cast(distance as text), 'null') as d from fact_collision where case_id = #cos_case# and own_ship = #Int(cos_imo)# order by tick
</cfquery>
<cfquery name="v39_z" datasource="cos.bi">
select tick, coalesce(zone, '') as zone from fact_risk_assessment where case_id = #cos_case# and vessel_id = #Int(cos_imo)# order by tick
</cfquery>
<cfquery name="v39_g" datasource="cos.bi">
select name, coalesce(value, '') as value from configs where name in ('run.scenario', 'map.key')
</cfquery>
<cfquery name="v39_u" datasource="cos.bi">
select vessel_id, filtered from fact_under_test where case_id = #cos_case#
</cfquery>
<cfquery name="v39_v" datasource="cos.vessels">
select imo, name from vessels
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="v39_q"><cfoutput>{"id":#v39_q.id#,"t":#v39_q.tick#,"src":"#URLEncodedFormat(v39_q.source)#","clause":"#URLEncodedFormat(v39_q.clause)#","zone":"#URLEncodedFormat(v39_q.zone)#","pts":#v39_q.pts#,"sit":"#URLEncodedFormat(v39_q.sit)#"},</cfoutput></cfloop>null],"enc":[<cfloop query="v39_e"><cfoutput>[#v39_e.k#,#v39_e.id#,#v39_e.s#,#v39_e.e#,#v39_e.tg#],</cfoutput></cfloop>null],"coll":[<cfloop query="v39_c"><cfoutput>[#v39_c.id#,#v39_c.tick#,#v39_c.tg#,#v39_c.d#],</cfoutput></cfloop>null],"zones":[<cfloop query="v39_z"><cfoutput>[#v39_z.tick#,"#URLEncodedFormat(v39_z.zone)#"],</cfoutput></cfloop>null],"cfg":[<cfloop query="v39_g"><cfoutput>["#URLEncodedFormat(v39_g.name)#","#URLEncodedFormat(v39_g.value)#"],</cfoutput></cfloop>null],"ut":[<cfloop query="v39_u"><cfoutput>[#v39_u.vessel_id#,#v39_u.filtered#],</cfoutput></cfloop>null],"names":[<cfloop query="v39_v"><cfoutput>["#URLEncodedFormat(v39_v.imo)#","#URLEncodedFormat(v39_v.name)#"],</cfoutput></cfloop>null]}
