<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html>
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
        <title>COS Reference</title>
        <link rel="stylesheet" href="style.css" type="text/css" />
      </head>
      <body>
        <h1>COS Reference</h1>
        <h3>Statistics</h3>
        <ul>
          <li>
            <span>Classes: </span>
            <xsl:value-of select="Index/ClassCount"/>
          </li>
          <li>
            <span>Functions: </span>
            <xsl:value-of select="Index/FunctionCount"/>
          </li>
        </ul>

        <h2>Classes</h2>
        <table width="900">
          <thead>
            <td class="tableheading" >Class</td>
            <td class="tableheading" >Description</td>
          </thead>
          <xsl:for-each select="Index/Classes/Class">
            <tr>
              <td>
                <a>
                  <xsl:attribute name="href">
                    <xsl:value-of select="OutputFile"/>
                    <xsl:value-of select="'.xml'"/>
                  </xsl:attribute>
                  <xsl:value-of select="Name"/>
                </a>
              </td>
              <td>
                <xsl:value-of select="Description"/>
              </td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
