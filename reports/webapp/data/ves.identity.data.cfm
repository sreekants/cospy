<!--: V1 ves.identity (DASH.024): register entry for the vessel. -->
<cfinclude template="/test/cos/shared/params.cfm">
<cfquery name="v1_q" datasource="cos.vessels">
select name, imo, coalesce(settings, '') as settings from vessels where imo = '#Int(cos_imo)#'
</cfquery>
{<cfinclude template="/test/cos/shared/meta.cfm">,"rows":[<cfloop query="v1_q"><cfoutput>{"name":"#URLEncodedFormat(v1_q.name)#","imo":"#URLEncodedFormat(v1_q.imo)#","settings":"#URLEncodedFormat(v1_q.settings)#"},</cfoutput></cfloop>null]}
