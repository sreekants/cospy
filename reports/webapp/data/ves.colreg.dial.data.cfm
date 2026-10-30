<!--: V38 ves.colreg.dial (DASH.077, REQ.066): the vessel's COLREG findings and its encounters; the component derives the paragraph states. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="v38_q" datasource="cos.bi">
select o.id, o.tick, o.clause, cast(l.value as text) as pts
from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id
where o.case_id = #cos_case# and o.vessel_id = #Int(cos_imo)# and o.source = 'colreg' order by o.tick
</cfquery>
<cfquery name="v38_e" datasource="cos.bi">
select 0 as k, id, cast(start_time as text) as s, cast(end_time as text) as e, target_ship as tg from fact_crossing where case_id = #cos_case# and own_ship = #Int(cos_imo)#
union all select 1, id, cast(start_time as text), cast(end_time as text), target_ship from fact_give_way where case_id = #cos_case# and own_ship = #Int(cos_imo)#
union all select 2, id, cast(start_time as text), cast(end_time as text), target_ship from fact_head_on where case_id = #cos_case# and own_ship = #Int(cos_imo)#
union all select 3, id, cast(start_time as text), cast(end_time as text), target_ship from fact_overtaking where case_id = #cos_case# and own_ship = #Int(cos_imo)#
union all select 4, id, cast(start_time as text), cast(end_time as text), target_ship from fact_stand_on where case_id = #cos_case# and own_ship = #Int(cos_imo)#
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="v38_q"><cfoutput>{"id":#v38_q.id#,"t":#v38_q.tick#,"clause":"#URLEncodedFormat(v38_q.clause)#","pts":#v38_q.pts#},</cfoutput></cfloop>null],"enc":[<cfloop query="v38_e"><cfoutput>[#v38_e.k#,#v38_e.id#,#v38_e.s#,#v38_e.e#,#v38_e.tg#],</cfoutput></cfloop>null]}
