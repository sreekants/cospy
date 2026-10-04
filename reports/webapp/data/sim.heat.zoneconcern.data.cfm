<!--: S14 sim.heat.zoneconcern (DASH.016): points and counts by zone and concern. -->
<cfinclude template="/test/cos/shared/params.cfm">
<cfquery name="s14_q" datasource="cos.bi">
select zone, concern, count(*) as n, cast(sum(penalty) as text) as pts from fact_concern where case_id = #cos_case# group by zone, concern
</cfquery>
{<cfinclude template="/test/cos/shared/meta.cfm">,"rows":[<cfloop query="s14_q"><cfoutput>{"zone":"#URLEncodedFormat(s14_q.zone)#","concern":"#URLEncodedFormat(s14_q.concern)#","n":#s14_q.n#,"pts":#s14_q.pts#},</cfoutput></cfloop>null]}
