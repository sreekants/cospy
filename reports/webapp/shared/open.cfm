<!--: Standalone harness, start (CP-02, CP-03): emits nothing when included by a master. -->
<cfparam name="composed" default="0">
<cfinclude template="../shared/config.cfm">
<cfif composed EQ 0>
<!DOCTYPE html>
<html lang="en">
<head>
<cfinclude template="../shared/head.cfm">
<title>COS component</title>
</head>
<body>
<main class="cos-app cos-single">
</cfif>
