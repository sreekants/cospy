<!--: S13 sim.fleet.table (DASH.015): one row per vessel. -->
<cfinclude template="shared/params.cfm">
<cfquery name="s13_q" datasource="cos.bi">
with ra as (select own_ship as v, cast(max(cumulative) as text) as rb, cast(min(survival) as text) as s,
                   cast(max(p_collision) as text) as pc, cast(max(p_grounding) as text) as pg,
                   cast(min(p_comms_loss) as text) as pl0, cast(max(p_comms_loss) as text) as pl1
            from fact_risk_assessment where case_id = #cos_case# group by own_ship),
     fc as (select vessel_id as v, sum(source = 'colreg') as nc, sum(source = 'examiner') as np
            from fact_concern where case_id = #cos_case# group by vessel_id),
     en as (select own_ship as v, count(*) as n from (
              select own_ship from fact_crossing where case_id = #cos_case# union all
              select own_ship from fact_give_way where case_id = #cos_case# union all
              select own_ship from fact_head_on where case_id = #cos_case# union all
              select own_ship from fact_overtaking where case_id = #cos_case#) group by own_ship)
select ra.v as imo, ra.rb, ra.s, ra.pc, ra.pg, ra.pl0, ra.pl1,
       coalesce(fc.nc, 0) as nc, coalesce(fc.np, 0) as np, coalesce(en.n, 0) as enc
from ra left join fc on fc.v = ra.v left join en on en.v = ra.v
</cfquery>
<cfquery name="s13_v" datasource="cos.vessels">
select imo, name from vessels
</cfquery>
{<cfinclude template="shared/meta.cfm">,"names":[<cfloop query="s13_v"><cfoutput>["#URLEncodedFormat(s13_v.imo)#","#URLEncodedFormat(s13_v.name)#"],</cfoutput></cfloop>null],"rows":[<cfloop query="s13_q"><cfoutput>{"imo":#s13_q.imo#,"rb":#s13_q.rb#,"surv":#s13_q.s#,"pc":#s13_q.pc#,"pg":#s13_q.pg#,"pl0":#s13_q.pl0#,"pl1":#s13_q.pl1#,"nc":#s13_q.nc#,"np":#s13_q.np#,"enc":#s13_q.enc#},</cfoutput></cfloop>null]}
