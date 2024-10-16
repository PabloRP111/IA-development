<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl= "http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
    <html lang="es">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Books price</title>
        </head>
        <body>
            <h2>books price more than 100</h2>
            <ol>
                <xsl:for-each select="bib/libro[precio &lt;= 100]">
                    <li>
                        <td><xsl:value-of select="nombre" /></td>
                        <td><xsl:value-of select="precio" />€</td>
                    </li>
                </xsl:for-each>
            </ol>
        </body>
    </html>
</xsl:template>

</xsl:stylesheet>