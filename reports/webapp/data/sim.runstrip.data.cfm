<!--: S1 sim.runstrip (DASH.003): identity and state of the run. -->
<cfinclude template="../shared/params.cfm">
<cfquery name="s1_q" datasource="cos.bi">
select (select count(*) from fact_risk_assessment where case_id = #cos_case#) as n,
       (select coalesce(max(tick) - min(tick), 0) from fact_risk_assessment where case_id = #cos_case#) as dur,
       (select coalesce(group_concat(case when name = '' then cast(vessel_id as text) else name || ' (' || vessel_id || ')' end, ', '), '')
          from fact_under_test where case_id = #cos_case# and filtered = 1) as vut,
       (select count(*) from fact_under_test where case_id = #cos_case# and filtered = 1) as nvut,
       (select count(*) from fact_under_test where case_id = #cos_case#) as recorded
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfloop query="s1_q"><cfif s1_q.n GT 0><cfoutput>{"duration":#s1_q.dur#,"vut":"#URLEncodedFormat(s1_q.vut)#","nvut":#Int(s1_q.nvut)#,"recorded":#Int(s1_q.recorded)#},</cfoutput></cfif></cfloop>null]}
