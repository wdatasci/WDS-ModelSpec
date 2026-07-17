<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:param name="VariableProcess" select="Object"/>
    <xsl:output method="text"/>
    <xsl:strip-space elements="Enum EnumFields EnumField EnumValue Column"/>
    <xsl:decimal-format 
        decimal-separator="."
        grouping-separator=","
        infinity=" NaN "
        NaN=" NaN "
        />

<xsl:template name="SASProcessFitting">

*%include "&amp;wds.%str(\)..%str(\)ModelSpec%str(\)ArtificialTreatments.sas";

%LoadMacros(wdm.ArtificialTreatments);

<xsl:for-each select="Project">
<xsl:variable name="ProjectName" select="@Name"/>
<xsl:for-each select=".//Model">
<xsl:variable name="ModelName" select="@Name"/>
<xsl:for-each select="ComponentModels/ComponentModel">

%macro <xsl:value-of select="$ModelName"/>_<xsl:value-of select="@Name"/>_ProcessFitting
%global <xsl:value-of select="$ModelName"/>_<xsl:value-of select="@Name"/>_ModelVariables;
%global <xsl:value-of select="$ModelName"/>_<xsl:value-of select="@Name"/>_KeepList;
%global <xsl:value-of select="$ModelName"/>_<xsl:value-of select="@Name"/>_RunningTotalList;
%global <xsl:value-of select="$ModelName"/>_<xsl:value-of select="@Name"/>_RunningKeepList;

<xsl:for-each select="Variables/Variable">%AritificialTreatment(SourceVariable=<xsl:value-of select="@Name"/>
                , AlternateBaseName=<xsl:value-of select="@Handle"/>
                , Treatment=<xsl:value-of select="./Treatment"/>
                , CriticalValues=<xsl:value-of select="./CriticalValueList"/>
                , CleanLimits=<xsl:value-of select="./CleanLimitsList"/>
                , DropList=<xsl:value-of select="./DropList"/>
                , MarginalSetName=<xsl:value-of select="@Handle"/>Marginals
                , RunningMarginalSetName=<xsl:value-of select="@Handle"/><xsl:value-of select="$ModelName"/>_<xsl:value-of select="@Name"/>_RunningTotalList
                , RunningMarginalTrimmedSetName=<xsl:value-of select="@Handle"/><xsl:value-of select="$ModelName"/>_<xsl:value-of select="@Name"/>_RunningKeepList
                );

</xsl:for-each>

%mend;



</xsl:for-each>
</xsl:for-each>
</xsl:for-each>

    </xsl:template>

    <xsl:template match="/">
        <xsl:call-template name="SASProcessFitting"/>
    </xsl:template>

</xsl:stylesheet>
