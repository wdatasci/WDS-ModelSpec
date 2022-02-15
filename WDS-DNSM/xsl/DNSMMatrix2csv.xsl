<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="text" omit-xml-declaration="yes"/>
<xsl:template match="/"><xsl:apply-templates select="/DNSMMatrix/MData"/></xsl:template>
<xsl:template match="NumberOfStates"/>
<xsl:template match="NumberOfAdditionalAxes"/>
<xsl:template match="StateLabels"/>
<xsl:template match="AdditionalAxesLimits"/>
<xsl:template match="MData"><xsl:if test="./@Row='1'"><xsl:text>Row</xsl:text>
		<xsl:text>,Axis1</xsl:text>
		<xsl:text>,Axis2</xsl:text>
		<xsl:text>,Axis3</xsl:text>
		<xsl:text>,Axis4</xsl:text>
		<xsl:text>,Col1</xsl:text>
		<xsl:text>,Col2</xsl:text>
		<xsl:text>,Col3</xsl:text>
		<xsl:text>,Col4</xsl:text>
		<xsl:text>,Col5</xsl:text>
		<xsl:text>,Col6</xsl:text>
		<xsl:text>,Col7</xsl:text>
		<xsl:text>,Col8</xsl:text>
		<xsl:text>,Col9</xsl:text>
		<xsl:text>,Col10</xsl:text>
		<xsl:text>,Col11</xsl:text>
		<xsl:text>,Col12</xsl:text>
		<xsl:text>,Col13</xsl:text>
		<xsl:text>,Col14</xsl:text>
		<xsl:text>,Col15</xsl:text>
		<xsl:text>,Col16</xsl:text>
		<xsl:text>,Col17</xsl:text>
		<xsl:text>,Col18</xsl:text>
		<xsl:text>,Col19</xsl:text>
		<xsl:text>,Col20</xsl:text>
		<xsl:text>,Col21</xsl:text>
		<xsl:text>,Col22</xsl:text>
		<xsl:text>,Col23</xsl:text>
		<xsl:text>,Col24</xsl:text>
		<xsl:text>,Col25</xsl:text>
		<xsl:text>,Col26</xsl:text>
		<xsl:text>,Col27</xsl:text>
		<xsl:text>,Col28</xsl:text>
		<xsl:text>,Col29</xsl:text>
		<xsl:text>,Col30</xsl:text>
		<xsl:text>,Col31</xsl:text>
		<xsl:text>,Col32</xsl:text>
		<xsl:text>,Col33</xsl:text>
		<xsl:text>,Col34</xsl:text>
		<xsl:text>,Col35</xsl:text>
		<xsl:text>,Col36</xsl:text>
		<xsl:text>,Col37</xsl:text>
		<xsl:text>,Col38</xsl:text>
		<xsl:text>,Col39</xsl:text>
		<xsl:text>,Col40</xsl:text>
		<xsl:text>,Col41</xsl:text>
		<xsl:text>,Col42</xsl:text>
		<xsl:text>,Col43</xsl:text>
		<xsl:text>,Col44</xsl:text>
		<xsl:text>,Col45</xsl:text>
		<xsl:text>,Col46</xsl:text>
		<xsl:text>,Col47</xsl:text>
		<xsl:text>,Col48</xsl:text>
		<xsl:text>,Col49</xsl:text>
		<xsl:text>,Col50</xsl:text>
		<xsl:text>,Col51</xsl:text>
		<xsl:text>,Col52</xsl:text>
		<xsl:text>,Col53</xsl:text>
		<xsl:text>,Col54</xsl:text>
		<xsl:text>,Col55</xsl:text>
		<xsl:text>,Col56</xsl:text>
		<xsl:text>,Col57</xsl:text>
		<xsl:text>,Col58</xsl:text>
		<xsl:text>,Col59</xsl:text>
		<xsl:text>,Col60</xsl:text>
		<xsl:text>,Col61</xsl:text>
		<xsl:text>,Col62</xsl:text>
		<xsl:text>,Col63</xsl:text>
		<xsl:text>,Col64
</xsl:text></xsl:if>
		<xsl:value-of select="./@Row"/>
		<xsl:text>,</xsl:text><xsl:value-of select="./@Axis1"/>
		<xsl:text>,</xsl:text><xsl:value-of select="./@Axis2"/>
		<xsl:text>,</xsl:text><xsl:value-of select="./@Axis3"/>
		<xsl:text>,</xsl:text><xsl:value-of select="./@Axis4"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col1"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col2"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col3"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col4"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col5"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col6"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col7"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col8"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col9"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col10"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col11"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col12"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col13"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col14"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col15"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col16"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col17"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col18"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col19"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col20"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col21"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col22"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col23"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col24"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col25"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col26"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col27"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col28"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col29"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col30"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col31"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col32"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col33"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col34"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col35"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col36"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col37"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col38"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col39"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col40"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col41"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col42"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col43"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col44"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col45"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col46"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col47"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col48"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col49"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col50"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col51"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col52"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col53"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col54"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col55"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col56"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col57"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col58"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col59"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col60"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col61"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col62"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col63"/>
		<xsl:text>,</xsl:text><xsl:value-of select="Col64"/><xsl:text>
</xsl:text>

</xsl:template>


</xsl:stylesheet>


