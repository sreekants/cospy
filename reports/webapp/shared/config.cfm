<!--: Dashboard parameters (REQUIREMENTS SH-13, CP-12). Poll interval: default 3 000 ms, overridable
      with ?poll=<ms>, never below 3 000 ms. -->
<cfparam name="URL.poll" default="0">
<cfparam name="cos_poll_ms" default="3000">
<cfparam name="cos_root" default="/test/cos">
<cfparam name="cos_echarts" default="https://cdnjs.cloudflare.com/ajax/libs/echarts/5.5.0/echarts.min.js">
<cfparam name="cos_proj4" default="https://cdnjs.cloudflare.com/ajax/libs/proj4js/2.11.0/proj4.js">
<!--: Map databases are read only from under this folder (REQ-049-02). -->
<cfparam name="cos_maproot" default="/home/ssreedharan/projects/cos-data/config/map">
<cfif Int(URL.poll) GT 0><cfset cos_poll_ms = Int(URL.poll)></cfif>
<cfif cos_poll_ms LT 3000><cfset cos_poll_ms = 3000></cfif>
