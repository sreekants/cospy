<!--: V3 ves.kpis (DASH.026): four voyage figures. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="v3_q" datasource="cos.bi">
with ra as (select * from fact_risk_assessment where case_id = #cos_case# and vessel_id = #Int(cos_imo)#)
select (select count(*) from ra) as n,
       coalesce((select cast(max(cumulative) as text) from ra), 'null') as rb,
       coalesce((select cast(min(survival) as text) from ra), 'null') as surv,
       (select count(*) from (select o.case_id, o.tick, o.report_time, o.vessel_id, o.source, o.source as examiner, o.clause as event, o.zone as area, o.zone, o.concern, l.value as penalty, w.value as weight, null as value from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id) where case_id = #cos_case# and vessel_id = #Int(cos_imo)# and source = 'colreg') as nc,
       (select count(*) from (select o.case_id, o.tick, o.report_time, o.vessel_id, o.source, o.source as examiner, o.clause as event, o.zone as area, o.zone, o.concern, l.value as penalty, w.value as weight, null as value from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id) where case_id = #cos_case# and vessel_id = #Int(cos_imo)# and source <> 'colreg') as np,
       (select count(*) from fact_crossing where case_id = #cos_case# and own_ship = #Int(cos_imo)#) + (select count(*) from fact_give_way where case_id = #cos_case# and own_ship = #Int(cos_imo)#)
         + (select count(*) from fact_head_on where case_id = #cos_case# and own_ship = #Int(cos_imo)#) + (select count(*) from fact_overtaking where case_id = #cos_case# and own_ship = #Int(cos_imo)#) as enc,
       (select count(*) from fact_crossing where case_id = #cos_case# and own_ship = #Int(cos_imo)# and end_time = start_time) + (select count(*) from fact_give_way where case_id = #cos_case# and own_ship = #Int(cos_imo)# and end_time = start_time)
         + (select count(*) from fact_head_on where case_id = #cos_case# and own_ship = #Int(cos_imo)# and end_time = start_time) + (select count(*) from fact_overtaking where case_id = #cos_case# and own_ship = #Int(cos_imo)# and end_time = start_time) as enc0,
       coalesce((select cast(sum(exposure_dt) as text) from ra where zone = 'high_seas'), '0') as z1,
       coalesce((select cast(sum(exposure_dt) as text) from ra where zone = 'territorial_waters'), '0') as z2,
       coalesce((select cast(sum(exposure_dt) as text) from ra where zone = 'internal_waters'), '0') as z3,
       coalesce((select cast(sum(exposure_dt) as text) from ra where zone = 'port'), '0') as z4
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="v3_q"><cfif v3_q.n GT 0><cfoutput>{"rb":#v3_q.rb#,"surv":#v3_q.surv#,"nc":#v3_q.nc#,"np":#v3_q.np#,"enc":#v3_q.enc#,"enc0":#v3_q.enc0#,"z":[#v3_q.z1#,#v3_q.z2#,#v3_q.z3#,#v3_q.z4#]},</cfoutput></cfif></cfloop>null]}
