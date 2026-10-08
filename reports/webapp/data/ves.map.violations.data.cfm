<!--: V36 ves.map.violations (DASH.075, REQ.052): the vessel's violations with their recorded positions (Morton codes as text, TK-05). -->
<cfinclude template="../shared/params.cfm">
<cfquery name="v36_q" datasource="cos.bi">
select cast(ro.dim_gps_id as text) as gps, ro.tick, coalesce(ro.source, '') as source, coalesce(ro.clause, '') as clause,
       coalesce(ro.zone, '') as zone, coalesce(ro.concern, '') as concern, coalesce(cast(rl.value as text), 'null') as penalty
from fact_ro ro
left join fact_rl rl on rl.case_id = ro.case_id and rl.finding_id = ro.finding_id
where ro.case_id = #cos_case# and ro.vessel_id = #Int(cos_imo)#
  and ro.tick between #cos_t0# and #cos_t1# and ro.dim_gps_id is not null
order by ro.tick
</cfquery>
<cfquery name="v36_n" datasource="cos.bi">
select count(*) as n from fact_ro
where case_id = #cos_case# and vessel_id = #Int(cos_imo)# and tick between #cos_t0# and #cos_t1# and dim_gps_id is null
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"unpositioned":<cfoutput>#Int(v36_n.n)#</cfoutput>,"rows":[<cfloop query="v36_q"><cfoutput>["#v36_q.gps#",#Int(v36_q.tick)#,"#URLEncodedFormat(v36_q.source)#","#URLEncodedFormat(v36_q.clause)#","#URLEncodedFormat(v36_q.zone)#","#URLEncodedFormat(v36_q.concern)#",#v36_q.penalty#],</cfoutput></cfloop>null]}
