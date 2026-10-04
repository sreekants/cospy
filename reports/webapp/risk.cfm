<cfparam name="URL.imo" default="2302074">

<cfquery name="risk" datasource="cos.bi">
select report_time, cumulative as cost  from fact_risk_assessment
   where own_ship=#URL.imo#
   order by report_time desc;
</cfquery>

<cfchart 
	xAxisType="category" 
	xAxisTitle="Time (Simulation Tick)"
	yAxisTitle="Cumulative Risk"
	scaleToX="1000"
	scaleToY="50000"
	chartWidth="800"
	chartHeight="600" 
	showXGridlines="Yes"
	showYGridlines="Yes"
	showMarkers="Yes"
	backgroundcolor="white">
	<cfchartseries type="area" serieslabel="one" colorlist="red,blue,green,orange" >
	<cfoutput query="risk">
		<cfchartdata Item="#Int(risk.report_time)#" y="#risk.cost#">
	</cfoutput>
	</cfchartseries>
</cfchart>
