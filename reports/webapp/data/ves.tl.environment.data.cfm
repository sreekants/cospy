<!--: V11 ves.tl.environment (DASH.034): depth beneath the vessel; ?since=<tick>. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="v11_q" datasource="cos.bi">
select tick, coalesce(cast(depth as text), 'null') as d, case when depth_source = 'nominal' then 1 else 0 end as nom
from fact_risk_assessment where case_id = #cos_case# and vessel_id = #Int(cos_imo)# and tick > #cos_since# order by tick
</cfquery>
<cfquery name="v11_w" datasource="cos.bi">
select coalesce(cast(max(p_capsize) as text), 'null') as pk, coalesce(cast(max(threshold) as text), 'null') as th, count(distinct payload_state) + count(distinct size_state) as ni, count(distinct wave_state) as nw, coalesce(max(wave_state), '') as w, count(distinct visibility_state) as nv, coalesce(max(visibility_state), '') as v
from fact_capsize where case_id = #cos_case# and vessel_id = #Int(cos_imo)#
</cfquery>
{<cfinclude template="../shared/meta.cfm">,<cfoutput>"weather":{"pk":#v11_w.pk#,"th":#v11_w.th#,"ni":#v11_w.ni#,"nw":#v11_w.nw#,"w":"#URLEncodedFormat(v11_w.w)#","nv":#v11_w.nv#,"v":"#URLEncodedFormat(v11_w.v)#"}</cfoutput>,"rows":[<cfloop query="v11_q"><cfoutput>[#v11_q.tick#,#v11_q.d#,#v11_q.nom#],</cfoutput></cfloop>null]}
