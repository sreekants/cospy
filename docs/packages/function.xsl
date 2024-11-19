<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html>
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
        <title>
          COS Reference : <xsl:value-of select="Function/Name"/>
        </title>
        <link rel="stylesheet" href="../style.css" type="text/css" />
      </head>
      <body>
        <h1>
          <xsl:value-of select="Function/Class"/>.<xsl:value-of select="Function/Name"/>
        </h1>
        <h2>Description</h2>
        <xsl:value-of select="Function/Description"/>
        <xsl:apply-templates select="Function/Signatures"/>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="Signatures">
    <xsl:for-each select="Signature">
      <hr></hr>
      <xsl:choose>
        <xsl:when test="not(Arguments/node())" />
        <xsl:otherwise>
          <h2>Arguments</h2>
          <table width="900px">
            <thead>
              <td class="tableheading" width="100px">Argument</td>
              <td class="tableheading" width="100px">Type</td>
              <td class="tableheading">Description</td>
            </thead>
            <xsl:for-each select="Arguments/Argument">
              <tr>
                <td width="100px">
                  <strong>
                    <xsl:value-of select="Name"/>
                  </strong>
                </td>
                <td width="200px">
                  <xsl:value-of select="Type"/>
                </td>
                <td>
                  <xsl:value-of select="Description"/>
                </td>
              </tr>
            </xsl:for-each>
          </table>
        </xsl:otherwise>
      </xsl:choose>
      
      <xsl:choose>
        <xsl:when test="string-length(Result/Argument/Description)>0">
          <h3>Result</h3>
          <xsl:value-of select="Result/Argument/Description"/>
        </xsl:when>
      </xsl:choose>

      <h2>Source Code</h2>
      <span>Source File :</span>
      <a>
        <xsl:attribute name="href">
          <xsl:value-of select="'https://github.com/NTNU-Autoship-Internal/modcolreg/blob/main/src/'"/>
          <xsl:value-of select="translate(../../Module,'.','/')"/>
          <xsl:value-of select="'.py'"/>
          <xsl:value-of select="'#L'"/>
          <xsl:value-of select="SourceLine"/>
        </xsl:attribute>
        <xsl:value-of select="SourceFile"/>
      </a>
      
    </xsl:for-each>
  </xsl:template>

</xsl:stylesheet>
