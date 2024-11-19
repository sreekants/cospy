<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
        <title>
          COS Reference : <xsl:value-of select="Class/Name"/>
        </title>
        <link rel="stylesheet" href="style.css" type="text/css" />
      </head>
      <body>
        <h1>
          Class : <xsl:value-of select="Class/Name"/>
        </h1>

        <h2>Description</h2>
        <xsl:value-of select="Class/Description"/>

        <h2>Source Code</h2>
        <ul>
          <li>
            <span>Source File :</span>
            <a>
              <xsl:attribute name="href">
                <xsl:value-of select="'https://github.com/NTNU-Autoship-Internal/modcolreg/blob/main/src/'"/>
                <xsl:value-of select="translate(Class/Module,'.','/')"/>
                <xsl:value-of select="'.py'"/>
                <xsl:value-of select="'#L'"/>
                <xsl:value-of select="Class/SourceLine"/>
              </xsl:attribute>
              <xsl:value-of select="Class/SourceFile"/>
            </a>
          </li>
          <li>
            <span>Layer :</span>
            <xsl:value-of select="Class/Layer"/>
          </li>
        </ul>

        <xsl:choose>
          <xsl:when test="not(Class/Constructors/node())" />
          <xsl:otherwise>
            <xsl:apply-templates select="Class/Constructors"/>
          </xsl:otherwise>
        </xsl:choose>

        <xsl:choose>
          <xsl:when test="not(Class/Functions/node())" />
          <xsl:otherwise>
            <xsl:apply-templates select="Class/Functions"/>
          </xsl:otherwise>
        </xsl:choose>
      </body>
    </html>
  </xsl:template>


  <xsl:template match="Constructors">
    <h2>Constructors &amp; Destructors</h2>
    <table width="900px">
      <thead>
        <td class="tableheading" >Method</td>
        <td class="tableheading" >Description</td>
      </thead>
      <xsl:for-each select="Function">
        <xsl:apply-templates select="."/>
      </xsl:for-each>
    </table>
  </xsl:template>

  <xsl:template match="Functions">
    <h2>Functions</h2>
    <table width="900px">
      <thead>
        <td class="tableheading" >Method</td>
        <td class="tableheading" >Description</td>
      </thead>
      <xsl:for-each select="Function">
        <xsl:apply-templates select="."/>
      </xsl:for-each>
    </table>
  </xsl:template>

  <xsl:template match="Function">
    <tr>
      <td width="300px">
        <a href="{concat(OutputFile,'.xml')}">
          <xsl:value-of select="Name"/>
        </a>
      </td>
      <td>
        <xsl:value-of select="Description"/>
      </td>
    </tr>
  </xsl:template>

</xsl:stylesheet>
