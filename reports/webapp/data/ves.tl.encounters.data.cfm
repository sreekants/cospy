<!--: V10 ves.tl.encounters (DASH.033): encounters of the vessel. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="v10_q" datasource="cos.bi">
select 0 as k, cast(start_time as text) as s, cast(end_time as text) as e, target_ship as tg from fact_crossing where case_id = #cos_case# and own_ship = #Int(cos_imo)#
union all select 1, cast(start_time as text), cast(end_time as text), target_ship from fact_give_way where case_id = #cos_case# and own_ship = #Int(cos_imo)#
union all select 2, cast(start_time as text), cast(end_time as text), target_ship from fact_head_on where case_id = #cos_case# and own_ship = #Int(cos_imo)#
union all select 3, cast(start_time as text), cast(end_time as text), target_ship from fact_overtaking where case_id = #cos_case# and own_ship = #Int(cos_imo)#
</cfquery>
<cfquery name="v10_v" datasource="cos.vessels">
select imo, name from vessels
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"names":[<cfloop query="v10_v"><cfoutput>["#URLEncodedFormat(v10_v.imo)#","#URLEncodedFormat(v10_v.name)#"],</cfoutput></cfloop>null],"rows":[<cfloop query="v10_q"><cfoutput>[#v10_q.k#,#v10_q.s#,#v10_q.e#,#v10_q.tg#],</cfoutput></cfloop>null]}
