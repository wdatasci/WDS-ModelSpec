<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

<xsl:template match="/"><xsl:apply-templates select="/."/></xsl:template>

<xsl:template match="DNSMMatrix">
	<xsl:element name="DNSMMatrix">
		<xsl:attribute name="Name"><xsl:value-of select="@Name"/></xsl:attribute>
		<xsl:apply-templates select="./."/>
	</xsl:element>
</xsl:template>


<xsl:template match="NumberOfStates">
<xsl:element name="NumberOfStates"><xsl:value-of select="."/></xsl:element>
</xsl:template>



<xsl:template match="NumberOfAdditionalAxes">
<xsl:element name="NumberOfAdditionalAxes"><xsl:value-of select="."/></xsl:element>
</xsl:template>

<xsl:template match="AdditionalAxesLimits">
<xsl:element name="AdditionalAxesLimits">
<xsl:apply-templates select="./."/>
</xsl:element>
</xsl:template>

<xsl:template match="AdditionalAxesUpperLimits">
<xsl:element name="AdditionalAxesUpperLimits">
<xsl:apply-templates select="./."/>
</xsl:element>
</xsl:template>

<xsl:template match="AdditionalAxesLowerLimits">
<xsl:element name="AdditionalAxesLowerLimits">
<xsl:apply-templates select="./."/>
</xsl:element>
</xsl:template>

<xsl:template match="Axis1">
<xsl:element name="Axis1"><xsl:value-of select="."/></xsl:element>
</xsl:template>

<xsl:template match="Axis2">
<xsl:element name="Axis2"><xsl:value-of select="."/></xsl:element>
</xsl:template>

<xsl:template match="Axis3">
<xsl:element name="Axis3"><xsl:value-of select="."/></xsl:element>
</xsl:template>

<xsl:template match="Axis4">
<xsl:element name="Axis4"><xsl:value-of select="."/></xsl:element>
</xsl:template>




<xsl:template match="StateLabels">
<xsl:element name="StateLabels"><xsl:apply-templates select="./."/></xsl:element>
</xsl:template>


<xsl:template match="StateLabel">
<xsl:element name="StateLabel"><xsl:attribute name="Position"><xsl:value-of select="@Position"/></xsl:attribute>
<xsl:value-of select="."/>
</xsl:element>
</xsl:template>


<xsl:template match="MData"/>
<xsl:template match="Row"/>
<xsl:template match="Col1"/>
<xsl:template match="Col2"/>
<xsl:template match="Col3"/>
<xsl:template match="Col4"/>
<xsl:template match="Col5"/>
<xsl:template match="Col6"/>
<xsl:template match="Col7"/>
<xsl:template match="Col8"/>
<xsl:template match="Col9"/>
<xsl:template match="Col10"/>
<xsl:template match="Col11"/>
<xsl:template match="Col12"/>
<xsl:template match="Col13"/>
<xsl:template match="Col14"/>
<xsl:template match="Col15"/>
<xsl:template match="Col16"/>
<xsl:template match="Col17"/>
<xsl:template match="Col18"/>
<xsl:template match="Col19"/>
<xsl:template match="Col20"/>
<xsl:template match="Col21"/>
<xsl:template match="Col22"/>
<xsl:template match="Col23"/>
<xsl:template match="Col24"/>
<xsl:template match="Col25"/>
<xsl:template match="Col26"/>
<xsl:template match="Col27"/>
<xsl:template match="Col28"/>
<xsl:template match="Col29"/>
<xsl:template match="Col30"/>
<xsl:template match="Col31"/>
<xsl:template match="Col32"/>
<xsl:template match="Col33"/>
<xsl:template match="Col34"/>
<xsl:template match="Col35"/>
<xsl:template match="Col36"/>
<xsl:template match="Col37"/>
<xsl:template match="Col38"/>
<xsl:template match="Col39"/>
<xsl:template match="Col40"/>
<xsl:template match="Col41"/>
<xsl:template match="Col42"/>
<xsl:template match="Col43"/>
<xsl:template match="Col44"/>
<xsl:template match="Col45"/>
<xsl:template match="Col46"/>
<xsl:template match="Col47"/>
<xsl:template match="Col48"/>
<xsl:template match="Col49"/>
<xsl:template match="Col50"/>
<xsl:template match="Col51"/>
<xsl:template match="Col52"/>
<xsl:template match="Col53"/>
<xsl:template match="Col54"/>
<xsl:template match="Col55"/>
<xsl:template match="Col56"/>
<xsl:template match="Col57"/>
<xsl:template match="Col58"/>
<xsl:template match="Col59"/>
<xsl:template match="Col60"/>
<xsl:template match="Col61"/>
<xsl:template match="Col62"/>
<xsl:template match="Col63"/>
<xsl:template match="Col64"/>
</xsl:stylesheet>

