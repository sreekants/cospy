<!--: S1 sim.runstrip (DASH.003): identity and state of the run. -->
<cfinclude template="shared/params.cfm">
<cfquery name="s1_q" datasource="cos.bi">
select (select count(*) from fact_risk_assessment where case_id = #cos_case#) as n,
       (select coalesce(max(tick) - min(tick), 0) from fact_risk_assessment where case_id = #cos_case#) as dur,
       (select coalesce(max(name), '') from fact_under_test where case_id = #cos_case#) as vut,
       (select coalesce(max(vessel_id), 0) from fact_under_test where case_id = #cos_case#) as vutimo
</cfquery>
{<cfinclude template="shared/meta.cfm">,"rows":[<cfloop query="s1_q"><cfif s1_q.n GT 0><cfoutput>{"duration":#s1_q.dur#,"vut":"#URLEncodedFormat(s1_q.vut)#","vutimo":#s1_q.vutimo#},</cfoutput></cfif></cfloop>null]}
