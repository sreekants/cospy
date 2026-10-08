<!--: Shared base map (DASH.065 §2): georeference from configs, polygons of each recorded map database through CreateQuery. Paths are output unencoded (URLEncodedFormat fails on long strings). -->
<cfinclude template="../shared/config.cfm">
<cfinclude template="../shared/params.cfm">
<cfquery name="maplayers_cfg" datasource="cos.bi">
with m as (
  select name, value from configs
  where name in ('map.database.land', 'map.database.sea', 'map.database.sky')
    and value like '#cos_maproot#/%.s3db'
    and value not like '%..%' and value not like '%;%' and value not like '%}%'
)
select
  coalesce((select value from m where name = 'map.database.land'), '') as land,
  coalesce((select value from m where name = 'map.database.sea'),  '') as sea,
  coalesce((select value from m where name = 'map.database.sky'),  '') as sky,
  (select count(*) from m where name = 'map.database.land') as has_land,
  (select count(*) from m where name = 'map.database.sea')  as has_sea,
  (select count(*) from m where name = 'map.database.sky')  as has_sky,
  (select count(*) from configs where name like 'map.database.%') - (select count(*) from m) as refused,
  coalesce((select value from configs where name = 'map.crs'), '')            as crs,
  coalesce((select value from configs where name = 'map.origin.easting'), '0') as e0,
  coalesce((select value from configs where name = 'map.origin.northing'),'0') as n0,
  coalesce((select value from configs where name = 'map.axis.y'), 'south')     as axis,
  coalesce((select value from configs where name = 'map.unit.metres.x'), '1')  as mx,
  coalesce((select value from configs where name = 'map.unit.metres.y'), '1')  as my,
  coalesce((select value from configs where name = 'map.bounds'), '')          as bounds,
  coalesce((select value from configs where name = 'map.centre.lat'), 'null')  as clat,
  coalesce((select value from configs where name = 'map.centre.lon'), 'null')  as clon,
  coalesce((select value from configs where name = 'map.key'), '')            as mapkey
</cfquery>
<cfset maplayers_landpath = maplayers_cfg.land>
<cfset maplayers_seapath = maplayers_cfg.sea>
<cfset maplayers_skypath = maplayers_cfg.sky>
<cfif maplayers_cfg.has_land EQ 1>
<cfscript>
  maplayers_cs  = Format( "DRIVER={{SQLite}};DBQ={0}", "maplayers_landpath" );
  CreateQuery( "maplayers_land", maplayers_cs, "SELECT type, COALESCE(CAST(height AS TEXT), 'null') AS lvl, name, path FROM isohypses ORDER BY type, id" );
</cfscript>
</cfif>
<cfif maplayers_cfg.has_sea EQ 1>
<cfscript>
  maplayers_cs  = Format( "DRIVER={{SQLite}};DBQ={0}", "maplayers_seapath" );
  CreateQuery( "maplayers_sea", maplayers_cs, "SELECT type, COALESCE(CAST(depth AS TEXT), 'null') AS lvl, name, path FROM isohypses ORDER BY depth DESC, id" );
</cfscript>
</cfif>
<cfif maplayers_cfg.has_sky EQ 1>
<cfscript>
  maplayers_cs  = Format( "DRIVER={{SQLite}};DBQ={0}", "maplayers_skypath" );
  CreateQuery( "maplayers_sky", maplayers_cs, "SELECT type, COALESCE(CAST(height AS TEXT), 'null') AS lvl, name, path FROM isohypses ORDER BY type, id" );
</cfscript>
</cfif>
{<cfinclude template="../shared/meta.cfm">,<cfoutput>"key":"#URLEncodedFormat(maplayers_cfg.mapkey)#","georef":{"crs":"#URLEncodedFormat(maplayers_cfg.crs)#","e0":#maplayers_cfg.e0#,"n0":#maplayers_cfg.n0#,"axis":"#URLEncodedFormat(maplayers_cfg.axis)#","mx":#maplayers_cfg.mx#,"my":#maplayers_cfg.my#,"bounds":"#URLEncodedFormat(maplayers_cfg.bounds)#","clat":#maplayers_cfg.clat#,"clon":#maplayers_cfg.clon#},"refused":#Int(maplayers_cfg.refused)#,</cfoutput>"rows":[<cfif maplayers_cfg.has_sea EQ 1><cfoutput query="maplayers_sea">{"db":"sea","t":#Int(type)#,"l":#lvl#,"n":"#URLEncodedFormat(name)#","p":"#path#"},</cfoutput><cfset QueryClose("maplayers_sea")></cfif><cfif maplayers_cfg.has_land EQ 1><cfoutput query="maplayers_land">{"db":"land","t":#Int(type)#,"l":#lvl#,"n":"#URLEncodedFormat(name)#","p":"#path#"},</cfoutput><cfset QueryClose("maplayers_land")></cfif><cfif maplayers_cfg.has_sky EQ 1><cfoutput query="maplayers_sky">{"db":"sky","t":#Int(type)#,"l":#lvl#,"n":"#URLEncodedFormat(name)#","p":"#path#"},</cfoutput><cfset QueryClose("maplayers_sky")></cfif>null]}
