<!--: V19 ves.ro.matrix (DASH.042): points and counts by zone and concern for the vessel. -->
<cfinclude template="/test/cos/shared/params.cfm">
<cfquery name="v19_q" datasource="cos.bi">
select zone, concern, count(*) as n, cast(sum(penalty) as text) as pts from fact_concern
where case_id = #cos_case# and vessel_id = #Int(cos_imo)# group by zone, concern
</cfquery>
{<cfinclude template="/test/cos/shared/meta.cfm">,"rows":[<cfloop query="v19_q"><cfoutput>{"zone":"#URLEncodedFormat(v19_q.zone)#","concern":"#URLEncodedFormat(v19_q.concern)#","n":#v19_q.n#,"v":#v19_q.pts#},</cfoutput></cfloop>null]}
