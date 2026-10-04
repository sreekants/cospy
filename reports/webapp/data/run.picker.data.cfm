<!--: C1 run.picker (DASH.001): one row per run in the store. -->
<cfinclude template="/test/cos/shared/params.cfm">
<cfquery name="c1_q" datasource="cos.bi">
select cast(case_id as text) as k, max(tick) - min(tick) as d, max(creation_time) as w
from fact_risk_assessment group by case_id order by w desc
</cfquery>
{<cfinclude template="/test/cos/shared/meta.cfm">,"rows":[<cfloop query="c1_q"><cfoutput>{"case":"#c1_q.k#","duration":#c1_q.d#,"written":"#URLEncodedFormat(c1_q.w)#"},</cfoutput></cfloop>null]}
