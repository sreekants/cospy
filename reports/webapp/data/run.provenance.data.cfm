<!--: C2 run.provenance (DASH.002): how the run was measured. -->
<cfinclude template="/test/cos/shared/params.cfm">
<cfquery name="c2_q" datasource="cos.bi">
with g as (select tick - lag(tick) over (partition by own_ship order by tick) as gap
           from fact_risk_assessment where case_id = #cos_case#),
     d as (select exposure_dt as dt from fact_risk_assessment where case_id = #cos_case#)
select (select count(*) from d) as n,
       (select coalesce(max(exposure_basis), '') from fact_risk_assessment where case_id = #cos_case#) as basis,
       (select coalesce(cast(max(exposure_period) as text), 'null') from fact_risk_assessment where case_id = #cos_case#) as period,
       coalesce((select cast(dt as text) from d order by dt limit 1 offset (select count(*) / 2 from d)), 'null') as dtmed,
       coalesce((select gap from g where gap is not null order by gap limit 1
                 offset (select count(*) / 2 from g where gap is not null)), -1) as cadence
</cfquery>
{<cfinclude template="/test/cos/shared/meta.cfm">,"rows":[<cfloop query="c2_q"><cfif c2_q.n GT 0><cfoutput>{"basis":"#URLEncodedFormat(c2_q.basis)#","period":#c2_q.period#,"dtmed":#c2_q.dtmed#,"cadence":#c2_q.cadence#},</cfoutput></cfif></cfloop>null]}
