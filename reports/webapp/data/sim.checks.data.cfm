<!--: S2 sim.checks (DASH.004): data checks for the run; n = offending rows (0 = pass). -->
<cfinclude template="../shared/params.cfm">
<cfquery name="s2_q" datasource="cos.bi">
with ra as (select * from fact_risk_assessment where case_id = #cos_case#),
     fc as (select * from (select o.case_id, o.tick, o.report_time, o.vessel_id, o.source, o.source as examiner, o.clause as event, o.zone as area, o.zone, o.concern, l.value as penalty, w.value as weight, null as value from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id) where case_id = #cos_case#),
     cad as (select tick - lag(tick) over (partition by vessel_id order by tick) as gap from ra),
     med as (select coalesce((select gap from cad where gap is not null order by gap limit 1
             offset (select count(*) / 2 from cad where gap is not null)), 20) as m),
     fg as (select tick - lag(tick) over (partition by vessel_id, examiner, event order by tick) as gap from fc),
     rb as (select finding_id, sum(value) as s from fact_rr where case_id = #cos_case# group by finding_id)
select 'bound' as id, 'Hazard probability above its upper bound' as label, '' as ticket,
       (select count(*) from ra where p_any_hazard > p_sum_hazard + 1e-12) as n
union all select 'cum', 'Total risk goes down during a voyage', '',
       (select count(*) from (select cumulative - lag(cumulative) over (partition by vessel_id order by tick) as d from ra) where d < -1e-9)
union all select 'surv', 'Survival goes up during a voyage', '',
       (select count(*) from (select survival - lag(survival) over (partition by vessel_id order by tick) as d from ra) where d > 1e-12)
union all select 'rbsum', 'Risk by concern does not add up to the total', '',
       (select count(*) from rb join ra on ra.finding_id = rb.finding_id where abs(rb.s - ra.rr) > 1e-6 * max(1, ra.rr))
union all select 'zero', 'Findings with no penalty', 'PLAN-E1', (select count(*) from fc where penalty = 0)
union all select 'c1000', 'Rows with the dummy run number 1000', 'PLAN-E1', (select count(*) from (select o.case_id, o.tick, o.report_time, o.vessel_id, o.source, o.source as examiner, o.clause as event, o.zone as area, o.zone, o.concern, l.value as penalty, w.value as weight, null as value from fact_ro o join fact_rl l on l.case_id = o.case_id and l.finding_id = o.finding_id join fact_rw w on w.case_id = o.case_id and w.finding_id = o.finding_id) where case_id = 1000)
union all select 'vocab', 'Findings without a zone or concern', 'REQ.018', (select count(*) from fc where coalesce(zone, '') = '' or coalesce(concern, '') = '')
union all select 'rescore', 'Same finding scored again within two checks', 'COS.044',
       (select count(*) from fg where gap is not null and gap <= 2 * (select m from med))
union all select 'dup', 'Duplicate findings', 'COS.044',
       (select coalesce(sum(c - 1), 0) from (select count(*) as c from fc group by vessel_id, tick, event having count(*) > 1))
union all select 'depth', 'Grounding findings in water 20 m deep or more', 'COS.044',
       (select count(*) from fc join ra on ra.vessel_id = fc.vessel_id and ra.tick = fc.tick where fc.event like 'grounding.%' and ra.depth >= 20)
union all select 'depth0', 'Depth assumed, not measured', 'REQ.022',
       (select count(*) from ra where depth_source = 'nominal')
union all select 'enc0', 'Encounters seen only once', 'COS.044',
       (select (select count(*) from fact_crossing where case_id = #cos_case# and end_time = start_time)
             + (select count(*) from fact_give_way where case_id = #cos_case# and end_time = start_time)
             + (select count(*) from fact_head_on where case_id = #cos_case# and end_time = start_time)
             + (select count(*) from fact_overtaking where case_id = #cos_case# and end_time = start_time))
</cfquery>
<cfquery name="s2_n" datasource="cos.bi">
select count(*) as n from fact_risk_assessment where case_id = #cos_case#
</cfquery>
{<cfinclude template="../shared/meta.cfm">,"rows":[<cfif s2_n.n GT 0><cfloop query="s2_q"><cfoutput>{"id":"#s2_q.id#","label":"#URLEncodedFormat(s2_q.label)#","ticket":"#URLEncodedFormat(s2_q.ticket)#","n":#s2_q.n#},</cfoutput></cfloop></cfif>null]}
