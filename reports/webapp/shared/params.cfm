<!--: Endpoint guards (SH-01, SH-12, TK-05). Resolves the run and vessel once and sets:
      cos_case (text), cos_imo (int), cos_since (int), cos_maxtick, cos_written, cos_nf_case, cos_nf_imo,
      cos_imo_default, cos_t0/cos_t1 (the vessel's voyage span, shared by every timeline). All decisions are made in SQL: on this engine cfset cannot build strings
      (& yields "false", #..# is not interpolated) and cfif AND misjudges query columns, so the
      not-found message is composed by the client from the numeric flags. -->
<cfparam name="URL.case" default="0">
<cfparam name="URL.imo" default="0">
<cfparam name="URL.since" default="-1">
<cfquery name="cos_run" datasource="cos.bi">
select coalesce((select cast(case_id as text) from fact_risk_assessment where case_id = #Int(URL.case)# limit 1),
                (select cast(case_id as text) from fact_risk_assessment order by creation_time desc limit 1),
                '0') as k,
       case when #Int(URL.case)# > 0 and not exists (select 1 from fact_risk_assessment where case_id = #Int(URL.case)#)
            then 1 else 0 end as nf
</cfquery>
<cfset cos_case = cos_run.k>
<cfset cos_nf_case = cos_run.nf>
<cfset cos_since = Int(URL.since)>
<cfquery name="cos_tick" datasource="cos.bi">
select coalesce(max(tick), 0) as mt, coalesce(max(creation_time), '') as w from fact_risk_assessment where case_id = #cos_case#
</cfquery>
<cfset cos_maxtick = cos_tick.mt>
<cfset cos_written = cos_tick.w>
<cfquery name="cos_ves" datasource="cos.bi">
select coalesce((select own_ship from fact_risk_assessment where case_id = #cos_case# and own_ship = #Int(URL.imo)# limit 1),
                (select own_ship from fact_risk_assessment where case_id = #cos_case# group by own_ship order by count(*) desc, own_ship limit 1),
                0) as imo,
       case when #Int(URL.imo)# > 0 and not exists (select 1 from fact_risk_assessment where case_id = #cos_case# and own_ship = #Int(URL.imo)#)
            then 1 else 0 end as nf,
       case when #Int(URL.imo)# = 0 then 1 else 0 end as dflt
</cfquery>
<cfquery name="cos_span" datasource="cos.bi">
select coalesce(min(tick), 0) as t0, coalesce(max(tick), 0) as t1 from fact_risk_assessment where case_id = #cos_case# and own_ship = #cos_ves.imo#
</cfquery>
<cfset cos_imo = cos_ves.imo>
<cfset cos_nf_imo = cos_ves.nf>
<cfset cos_imo_default = cos_ves.dflt>
<cfset cos_t0 = cos_span.t0>
<cfset cos_t1 = cos_span.t1>
