<!--: V1 ves.identity (DASH.024): register entry for the vessel, and its role from fact_under_test. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="v1_q" datasource="cos.vessels">
select name, imo, coalesce(settings, '') as settings from vessels where imo = '#Int(cos_imo)#'
</cfquery>
<cfquery name="v1_r" datasource="cos.bi">
select case when exists (select 1 from fact_under_test where case_id = #cos_case# and filtered = 1 and vessel_id = #Int(cos_imo)#) then 'under test'
            when exists (select 1 from fact_under_test where case_id = #cos_case# and filtered = 1) then 'background'
            when exists (select 1 from fact_under_test where case_id = #cos_case#) then 'under test (every vessel, no list)'
            else '' end as role
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="v1_q"><cfoutput>{"name":"#URLEncodedFormat(v1_q.name)#","imo":"#URLEncodedFormat(v1_q.imo)#","settings":"#URLEncodedFormat(v1_q.settings)#","role":"#URLEncodedFormat(v1_r.role)#"},</cfoutput></cfloop>null]}
