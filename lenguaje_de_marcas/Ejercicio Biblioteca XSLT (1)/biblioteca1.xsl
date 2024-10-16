<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="html" version="4.0" encoding="UTF-8" indent="yes" />
  
   <!-- Plantilla raíz -->
  <xsl:template match="/">
    <html>
      <body>
        <ol>
          <xsl:apply-templates select="bib/libro/autor">
            <xsl:sort select="apellido" order="ascending" />
          </xsl:apply-templates>
        </ol>
      </body>
    </html>
  </xsl:template>

  <!-- Plantilla autor -->
  <xsl:template match="/bib/libro/autor">
      <li><xsl:apply-templates select="apellido" />, <xsl:apply-templates select="nombre" /></li>
  </xsl:template>

  <!-- Plantilla apellido -->
  <xsl:template match="/bib/libro/autor/apellido">
    <xsl:value-of select="." />
  </xsl:template>

  <!-- Plantilla nombre -->
  <xsl:template match="/bib/libro/autor/nombre">
    <xsl:value-of select="." />
  </xsl:template>

</xsl:stylesheet>