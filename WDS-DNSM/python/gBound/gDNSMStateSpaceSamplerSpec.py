#!/usr/bin/env python

#
# Generated Thu Nov 01 16:22:31 2007 by generateDS.py.
#

import sys
import getopt
from xml.dom import minidom
from xml.dom import Node

#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Support/utility functions.
#

def showIndent(outfile, level):
    for idx in range(level):
        outfile.write('    ')

def quote_xml(inStr):
    s1 = inStr
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('"', '&quot;')
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, name)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


#
# Data representation classes.
#

class SMStateSpaceSampler:
    subclass = None
    def __init__(self, Handle='', Name='', NumberOfAggregates='', StateLabels=None, MData=None):
        self.Handle = Handle
        self.Name = Name
        self.NumberOfAggregates = NumberOfAggregates
        self.StateLabels = StateLabels
        if MData is None:
            self.MData = []
        else:
            self.MData = MData
    def factory(*args_, **kwargs_):
        if SMStateSpaceSampler.subclass:
            return SMStateSpaceSampler.subclass(*args_, **kwargs_)
        else:
            return SMStateSpaceSampler(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumberofaggregates(self): return self.NumberOfAggregates
    def setNumberofaggregates(self, NumberOfAggregates): self.NumberOfAggregates = NumberOfAggregates
    def getStatelabels(self): return self.StateLabels
    def setStatelabels(self, StateLabels): self.StateLabels = StateLabels
    def getMdata(self): return self.MData
    def setMdata(self, MData): self.MData = MData
    def addMdata(self, value): self.MData.append(value)
    def insertMdata(self, index, value): self.MData[index] = value
    def getHandle(self): return self.Handle
    def setHandle(self, Handle): self.Handle = Handle
    def getName(self): return self.Name
    def setName(self, Name): self.Name = Name
    def export(self, outfile, level, name_='SMStateSpaceSampler'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='SMStateSpaceSampler')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='SMStateSpaceSampler'):
        outfile.write(' Handle="%s"' % (self.getHandle(), ))
        outfile.write(' Name="%s"' % (self.getName(), ))
    def exportChildren(self, outfile, level, name_='SMStateSpaceSampler'):
        showIndent(outfile, level)
        outfile.write('<NumberOfAggregates>%s</NumberOfAggregates>\n' % quote_xml(self.getNumberofaggregates()))
        if self.StateLabels:
            self.StateLabels.export(outfile, level)
        for MData_ in self.getMdata():
            MData_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='SMStateSpaceSampler'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Handle = "%s",\n' % (self.getHandle(),))
        showIndent(outfile, level)
        outfile.write('Name = "%s",\n' % (self.getName(),))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('NumberOfAggregates=%s,\n' % quote_python(self.getNumberofaggregates()))
        if self.StateLabels:
            showIndent(outfile, level)
            outfile.write('StateLabels=StateLabels(\n')
            self.StateLabels.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('MData=[\n')
        level += 1
        for MData in self.MData:
            showIndent(outfile, level)
            outfile.write('MData(\n')
            MData.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        if attrs.get('Handle'):
            self.Handle = attrs.get('Handle').value
        if attrs.get('Name'):
            self.Name = attrs.get('Name').value
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NumberOfAggregates':
            NumberOfAggregates_ = ''
            for text__content_ in child_.childNodes:
                NumberOfAggregates_ += text__content_.nodeValue
            self.NumberOfAggregates = NumberOfAggregates_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'StateLabels':
            obj_ = StateLabels.factory()
            obj_.build(child_)
            self.setStatelabels(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'MData':
            obj_ = MData.factory()
            obj_.build(child_)
            self.MData.append(obj_)
# end class SMStateSpaceSampler


class StateLabels:
    subclass = None
    def __init__(self, StateLabel=None):
        if StateLabel is None:
            self.StateLabel = []
        else:
            self.StateLabel = StateLabel
    def factory(*args_, **kwargs_):
        if StateLabels.subclass:
            return StateLabels.subclass(*args_, **kwargs_)
        else:
            return StateLabels(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getStatelabel(self): return self.StateLabel
    def setStatelabel(self, StateLabel): self.StateLabel = StateLabel
    def addStatelabel(self, value): self.StateLabel.append(value)
    def insertStatelabel(self, index, value): self.StateLabel[index] = value
    def export(self, outfile, level, name_='StateLabels'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='StateLabels'):
        pass
    def exportChildren(self, outfile, level, name_='StateLabels'):
        for StateLabel_ in self.getStatelabel():
            StateLabel_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='StateLabels'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('StateLabel=[\n')
        level += 1
        for StateLabel in self.StateLabel:
            showIndent(outfile, level)
            outfile.write('StateLabel(\n')
            StateLabel.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        pass
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'StateLabel':
            obj_ = StateLabel.factory()
            obj_.build(child_)
            self.StateLabel.append(obj_)
# end class StateLabels


class StateLabel:
    subclass = None
    def __init__(self, Position=None, valueOf_=''):
        self.Position = Position
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if StateLabel.subclass:
            return StateLabel.subclass(*args_, **kwargs_)
        else:
            return StateLabel(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getPosition(self): return self.Position
    def setPosition(self, Position): self.Position = Position
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, name_='StateLabel'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='StateLabel')
        outfile.write('>')
        self.exportChildren(outfile, level + 1, name_)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='StateLabel'):
        outfile.write(' Position="%s"' % (self.getPosition(), ))
    def exportChildren(self, outfile, level, name_='StateLabel'):
        outfile.write(self.valueOf_)
    def exportLiteral(self, outfile, level, name_='StateLabel'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Position = "%s",\n' % (self.getPosition(),))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        self.valueOf_ = ''
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        if attrs.get('Position'):
            self.Position = attrs.get('Position').value
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
# end class StateLabel


class MData:
    subclass = None
    def __init__(self, Mneumonic='', Label='', MaxStateIndex=None, Row=None, Col1='', Col2='', Col3='', Col4='', Col5='', Col6='', Col7='', Col8='', Col9='', Col10='', Col11='', Col12='', Col13='', Col14='', Col15='', Col16='', Col17='', Col18='', Col19='', Col20='', Col21='', Col22='', Col23='', Col24='', Col25='', Col26='', Col27='', Col28='', Col29='', Col30='', Col31='', Col32='', Col33='', Col34='', Col35='', Col36='', Col37='', Col38='', Col39='', Col40='', Col41='', Col42='', Col43='', Col44='', Col45='', Col46='', Col47='', Col48='', Col49='', Col50='', Col51='', Col52='', Col53='', Col54='', Col55='', Col56='', Col57='', Col58='', Col59='', Col60='', Col61='', Col62='', Col63='', Col64=''):
        self.Mneumonic = Mneumonic
        self.Label = Label
        self.MaxStateIndex = MaxStateIndex
        self.Row = Row
        self.Col1 = Col1
        self.Col2 = Col2
        self.Col3 = Col3
        self.Col4 = Col4
        self.Col5 = Col5
        self.Col6 = Col6
        self.Col7 = Col7
        self.Col8 = Col8
        self.Col9 = Col9
        self.Col10 = Col10
        self.Col11 = Col11
        self.Col12 = Col12
        self.Col13 = Col13
        self.Col14 = Col14
        self.Col15 = Col15
        self.Col16 = Col16
        self.Col17 = Col17
        self.Col18 = Col18
        self.Col19 = Col19
        self.Col20 = Col20
        self.Col21 = Col21
        self.Col22 = Col22
        self.Col23 = Col23
        self.Col24 = Col24
        self.Col25 = Col25
        self.Col26 = Col26
        self.Col27 = Col27
        self.Col28 = Col28
        self.Col29 = Col29
        self.Col30 = Col30
        self.Col31 = Col31
        self.Col32 = Col32
        self.Col33 = Col33
        self.Col34 = Col34
        self.Col35 = Col35
        self.Col36 = Col36
        self.Col37 = Col37
        self.Col38 = Col38
        self.Col39 = Col39
        self.Col40 = Col40
        self.Col41 = Col41
        self.Col42 = Col42
        self.Col43 = Col43
        self.Col44 = Col44
        self.Col45 = Col45
        self.Col46 = Col46
        self.Col47 = Col47
        self.Col48 = Col48
        self.Col49 = Col49
        self.Col50 = Col50
        self.Col51 = Col51
        self.Col52 = Col52
        self.Col53 = Col53
        self.Col54 = Col54
        self.Col55 = Col55
        self.Col56 = Col56
        self.Col57 = Col57
        self.Col58 = Col58
        self.Col59 = Col59
        self.Col60 = Col60
        self.Col61 = Col61
        self.Col62 = Col62
        self.Col63 = Col63
        self.Col64 = Col64
    def factory(*args_, **kwargs_):
        if MData.subclass:
            return MData.subclass(*args_, **kwargs_)
        else:
            return MData(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getCol1(self): return self.Col1
    def setCol1(self, Col1): self.Col1 = Col1
    def getCol2(self): return self.Col2
    def setCol2(self, Col2): self.Col2 = Col2
    def getCol3(self): return self.Col3
    def setCol3(self, Col3): self.Col3 = Col3
    def getCol4(self): return self.Col4
    def setCol4(self, Col4): self.Col4 = Col4
    def getCol5(self): return self.Col5
    def setCol5(self, Col5): self.Col5 = Col5
    def getCol6(self): return self.Col6
    def setCol6(self, Col6): self.Col6 = Col6
    def getCol7(self): return self.Col7
    def setCol7(self, Col7): self.Col7 = Col7
    def getCol8(self): return self.Col8
    def setCol8(self, Col8): self.Col8 = Col8
    def getCol9(self): return self.Col9
    def setCol9(self, Col9): self.Col9 = Col9
    def getCol10(self): return self.Col10
    def setCol10(self, Col10): self.Col10 = Col10
    def getCol11(self): return self.Col11
    def setCol11(self, Col11): self.Col11 = Col11
    def getCol12(self): return self.Col12
    def setCol12(self, Col12): self.Col12 = Col12
    def getCol13(self): return self.Col13
    def setCol13(self, Col13): self.Col13 = Col13
    def getCol14(self): return self.Col14
    def setCol14(self, Col14): self.Col14 = Col14
    def getCol15(self): return self.Col15
    def setCol15(self, Col15): self.Col15 = Col15
    def getCol16(self): return self.Col16
    def setCol16(self, Col16): self.Col16 = Col16
    def getCol17(self): return self.Col17
    def setCol17(self, Col17): self.Col17 = Col17
    def getCol18(self): return self.Col18
    def setCol18(self, Col18): self.Col18 = Col18
    def getCol19(self): return self.Col19
    def setCol19(self, Col19): self.Col19 = Col19
    def getCol20(self): return self.Col20
    def setCol20(self, Col20): self.Col20 = Col20
    def getCol21(self): return self.Col21
    def setCol21(self, Col21): self.Col21 = Col21
    def getCol22(self): return self.Col22
    def setCol22(self, Col22): self.Col22 = Col22
    def getCol23(self): return self.Col23
    def setCol23(self, Col23): self.Col23 = Col23
    def getCol24(self): return self.Col24
    def setCol24(self, Col24): self.Col24 = Col24
    def getCol25(self): return self.Col25
    def setCol25(self, Col25): self.Col25 = Col25
    def getCol26(self): return self.Col26
    def setCol26(self, Col26): self.Col26 = Col26
    def getCol27(self): return self.Col27
    def setCol27(self, Col27): self.Col27 = Col27
    def getCol28(self): return self.Col28
    def setCol28(self, Col28): self.Col28 = Col28
    def getCol29(self): return self.Col29
    def setCol29(self, Col29): self.Col29 = Col29
    def getCol30(self): return self.Col30
    def setCol30(self, Col30): self.Col30 = Col30
    def getCol31(self): return self.Col31
    def setCol31(self, Col31): self.Col31 = Col31
    def getCol32(self): return self.Col32
    def setCol32(self, Col32): self.Col32 = Col32
    def getCol33(self): return self.Col33
    def setCol33(self, Col33): self.Col33 = Col33
    def getCol34(self): return self.Col34
    def setCol34(self, Col34): self.Col34 = Col34
    def getCol35(self): return self.Col35
    def setCol35(self, Col35): self.Col35 = Col35
    def getCol36(self): return self.Col36
    def setCol36(self, Col36): self.Col36 = Col36
    def getCol37(self): return self.Col37
    def setCol37(self, Col37): self.Col37 = Col37
    def getCol38(self): return self.Col38
    def setCol38(self, Col38): self.Col38 = Col38
    def getCol39(self): return self.Col39
    def setCol39(self, Col39): self.Col39 = Col39
    def getCol40(self): return self.Col40
    def setCol40(self, Col40): self.Col40 = Col40
    def getCol41(self): return self.Col41
    def setCol41(self, Col41): self.Col41 = Col41
    def getCol42(self): return self.Col42
    def setCol42(self, Col42): self.Col42 = Col42
    def getCol43(self): return self.Col43
    def setCol43(self, Col43): self.Col43 = Col43
    def getCol44(self): return self.Col44
    def setCol44(self, Col44): self.Col44 = Col44
    def getCol45(self): return self.Col45
    def setCol45(self, Col45): self.Col45 = Col45
    def getCol46(self): return self.Col46
    def setCol46(self, Col46): self.Col46 = Col46
    def getCol47(self): return self.Col47
    def setCol47(self, Col47): self.Col47 = Col47
    def getCol48(self): return self.Col48
    def setCol48(self, Col48): self.Col48 = Col48
    def getCol49(self): return self.Col49
    def setCol49(self, Col49): self.Col49 = Col49
    def getCol50(self): return self.Col50
    def setCol50(self, Col50): self.Col50 = Col50
    def getCol51(self): return self.Col51
    def setCol51(self, Col51): self.Col51 = Col51
    def getCol52(self): return self.Col52
    def setCol52(self, Col52): self.Col52 = Col52
    def getCol53(self): return self.Col53
    def setCol53(self, Col53): self.Col53 = Col53
    def getCol54(self): return self.Col54
    def setCol54(self, Col54): self.Col54 = Col54
    def getCol55(self): return self.Col55
    def setCol55(self, Col55): self.Col55 = Col55
    def getCol56(self): return self.Col56
    def setCol56(self, Col56): self.Col56 = Col56
    def getCol57(self): return self.Col57
    def setCol57(self, Col57): self.Col57 = Col57
    def getCol58(self): return self.Col58
    def setCol58(self, Col58): self.Col58 = Col58
    def getCol59(self): return self.Col59
    def setCol59(self, Col59): self.Col59 = Col59
    def getCol60(self): return self.Col60
    def setCol60(self, Col60): self.Col60 = Col60
    def getCol61(self): return self.Col61
    def setCol61(self, Col61): self.Col61 = Col61
    def getCol62(self): return self.Col62
    def setCol62(self, Col62): self.Col62 = Col62
    def getCol63(self): return self.Col63
    def setCol63(self, Col63): self.Col63 = Col63
    def getCol64(self): return self.Col64
    def setCol64(self, Col64): self.Col64 = Col64
    def getMneumonic(self): return self.Mneumonic
    def setMneumonic(self, Mneumonic): self.Mneumonic = Mneumonic
    def getLabel(self): return self.Label
    def setLabel(self, Label): self.Label = Label
    def getMaxstateindex(self): return self.MaxStateIndex
    def setMaxstateindex(self, MaxStateIndex): self.MaxStateIndex = MaxStateIndex
    def getRow(self): return self.Row
    def setRow(self, Row): self.Row = Row
    def export(self, outfile, level, name_='MData'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='MData')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='MData'):
        outfile.write(' Mneumonic="%s"' % (self.getMneumonic(), ))
        outfile.write(' Label="%s"' % (self.getLabel(), ))
        outfile.write(' MaxStateIndex="%s"' % (self.getMaxstateindex(), ))
        outfile.write(' Row="%s"' % (self.getRow(), ))
    def exportChildren(self, outfile, level, name_='MData'):
        showIndent(outfile, level)
        outfile.write('<Col1>%s</Col1>\n' % quote_xml(self.getCol1()))
        showIndent(outfile, level)
        outfile.write('<Col2>%s</Col2>\n' % quote_xml(self.getCol2()))
        showIndent(outfile, level)
        outfile.write('<Col3>%s</Col3>\n' % quote_xml(self.getCol3()))
        showIndent(outfile, level)
        outfile.write('<Col4>%s</Col4>\n' % quote_xml(self.getCol4()))
        showIndent(outfile, level)
        outfile.write('<Col5>%s</Col5>\n' % quote_xml(self.getCol5()))
        showIndent(outfile, level)
        outfile.write('<Col6>%s</Col6>\n' % quote_xml(self.getCol6()))
        showIndent(outfile, level)
        outfile.write('<Col7>%s</Col7>\n' % quote_xml(self.getCol7()))
        showIndent(outfile, level)
        outfile.write('<Col8>%s</Col8>\n' % quote_xml(self.getCol8()))
        showIndent(outfile, level)
        outfile.write('<Col9>%s</Col9>\n' % quote_xml(self.getCol9()))
        showIndent(outfile, level)
        outfile.write('<Col10>%s</Col10>\n' % quote_xml(self.getCol10()))
        showIndent(outfile, level)
        outfile.write('<Col11>%s</Col11>\n' % quote_xml(self.getCol11()))
        showIndent(outfile, level)
        outfile.write('<Col12>%s</Col12>\n' % quote_xml(self.getCol12()))
        showIndent(outfile, level)
        outfile.write('<Col13>%s</Col13>\n' % quote_xml(self.getCol13()))
        showIndent(outfile, level)
        outfile.write('<Col14>%s</Col14>\n' % quote_xml(self.getCol14()))
        showIndent(outfile, level)
        outfile.write('<Col15>%s</Col15>\n' % quote_xml(self.getCol15()))
        showIndent(outfile, level)
        outfile.write('<Col16>%s</Col16>\n' % quote_xml(self.getCol16()))
        showIndent(outfile, level)
        outfile.write('<Col17>%s</Col17>\n' % quote_xml(self.getCol17()))
        showIndent(outfile, level)
        outfile.write('<Col18>%s</Col18>\n' % quote_xml(self.getCol18()))
        showIndent(outfile, level)
        outfile.write('<Col19>%s</Col19>\n' % quote_xml(self.getCol19()))
        showIndent(outfile, level)
        outfile.write('<Col20>%s</Col20>\n' % quote_xml(self.getCol20()))
        showIndent(outfile, level)
        outfile.write('<Col21>%s</Col21>\n' % quote_xml(self.getCol21()))
        showIndent(outfile, level)
        outfile.write('<Col22>%s</Col22>\n' % quote_xml(self.getCol22()))
        showIndent(outfile, level)
        outfile.write('<Col23>%s</Col23>\n' % quote_xml(self.getCol23()))
        showIndent(outfile, level)
        outfile.write('<Col24>%s</Col24>\n' % quote_xml(self.getCol24()))
        showIndent(outfile, level)
        outfile.write('<Col25>%s</Col25>\n' % quote_xml(self.getCol25()))
        showIndent(outfile, level)
        outfile.write('<Col26>%s</Col26>\n' % quote_xml(self.getCol26()))
        showIndent(outfile, level)
        outfile.write('<Col27>%s</Col27>\n' % quote_xml(self.getCol27()))
        showIndent(outfile, level)
        outfile.write('<Col28>%s</Col28>\n' % quote_xml(self.getCol28()))
        showIndent(outfile, level)
        outfile.write('<Col29>%s</Col29>\n' % quote_xml(self.getCol29()))
        showIndent(outfile, level)
        outfile.write('<Col30>%s</Col30>\n' % quote_xml(self.getCol30()))
        showIndent(outfile, level)
        outfile.write('<Col31>%s</Col31>\n' % quote_xml(self.getCol31()))
        showIndent(outfile, level)
        outfile.write('<Col32>%s</Col32>\n' % quote_xml(self.getCol32()))
        showIndent(outfile, level)
        outfile.write('<Col33>%s</Col33>\n' % quote_xml(self.getCol33()))
        showIndent(outfile, level)
        outfile.write('<Col34>%s</Col34>\n' % quote_xml(self.getCol34()))
        showIndent(outfile, level)
        outfile.write('<Col35>%s</Col35>\n' % quote_xml(self.getCol35()))
        showIndent(outfile, level)
        outfile.write('<Col36>%s</Col36>\n' % quote_xml(self.getCol36()))
        showIndent(outfile, level)
        outfile.write('<Col37>%s</Col37>\n' % quote_xml(self.getCol37()))
        showIndent(outfile, level)
        outfile.write('<Col38>%s</Col38>\n' % quote_xml(self.getCol38()))
        showIndent(outfile, level)
        outfile.write('<Col39>%s</Col39>\n' % quote_xml(self.getCol39()))
        showIndent(outfile, level)
        outfile.write('<Col40>%s</Col40>\n' % quote_xml(self.getCol40()))
        showIndent(outfile, level)
        outfile.write('<Col41>%s</Col41>\n' % quote_xml(self.getCol41()))
        showIndent(outfile, level)
        outfile.write('<Col42>%s</Col42>\n' % quote_xml(self.getCol42()))
        showIndent(outfile, level)
        outfile.write('<Col43>%s</Col43>\n' % quote_xml(self.getCol43()))
        showIndent(outfile, level)
        outfile.write('<Col44>%s</Col44>\n' % quote_xml(self.getCol44()))
        showIndent(outfile, level)
        outfile.write('<Col45>%s</Col45>\n' % quote_xml(self.getCol45()))
        showIndent(outfile, level)
        outfile.write('<Col46>%s</Col46>\n' % quote_xml(self.getCol46()))
        showIndent(outfile, level)
        outfile.write('<Col47>%s</Col47>\n' % quote_xml(self.getCol47()))
        showIndent(outfile, level)
        outfile.write('<Col48>%s</Col48>\n' % quote_xml(self.getCol48()))
        showIndent(outfile, level)
        outfile.write('<Col49>%s</Col49>\n' % quote_xml(self.getCol49()))
        showIndent(outfile, level)
        outfile.write('<Col50>%s</Col50>\n' % quote_xml(self.getCol50()))
        showIndent(outfile, level)
        outfile.write('<Col51>%s</Col51>\n' % quote_xml(self.getCol51()))
        showIndent(outfile, level)
        outfile.write('<Col52>%s</Col52>\n' % quote_xml(self.getCol52()))
        showIndent(outfile, level)
        outfile.write('<Col53>%s</Col53>\n' % quote_xml(self.getCol53()))
        showIndent(outfile, level)
        outfile.write('<Col54>%s</Col54>\n' % quote_xml(self.getCol54()))
        showIndent(outfile, level)
        outfile.write('<Col55>%s</Col55>\n' % quote_xml(self.getCol55()))
        showIndent(outfile, level)
        outfile.write('<Col56>%s</Col56>\n' % quote_xml(self.getCol56()))
        showIndent(outfile, level)
        outfile.write('<Col57>%s</Col57>\n' % quote_xml(self.getCol57()))
        showIndent(outfile, level)
        outfile.write('<Col58>%s</Col58>\n' % quote_xml(self.getCol58()))
        showIndent(outfile, level)
        outfile.write('<Col59>%s</Col59>\n' % quote_xml(self.getCol59()))
        showIndent(outfile, level)
        outfile.write('<Col60>%s</Col60>\n' % quote_xml(self.getCol60()))
        showIndent(outfile, level)
        outfile.write('<Col61>%s</Col61>\n' % quote_xml(self.getCol61()))
        showIndent(outfile, level)
        outfile.write('<Col62>%s</Col62>\n' % quote_xml(self.getCol62()))
        showIndent(outfile, level)
        outfile.write('<Col63>%s</Col63>\n' % quote_xml(self.getCol63()))
        showIndent(outfile, level)
        outfile.write('<Col64>%s</Col64>\n' % quote_xml(self.getCol64()))
    def exportLiteral(self, outfile, level, name_='MData'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Mneumonic = "%s",\n' % (self.getMneumonic(),))
        showIndent(outfile, level)
        outfile.write('Label = "%s",\n' % (self.getLabel(),))
        showIndent(outfile, level)
        outfile.write('MaxStateIndex = "%s",\n' % (self.getMaxstateindex(),))
        showIndent(outfile, level)
        outfile.write('Row = "%s",\n' % (self.getRow(),))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Col1=%s,\n' % quote_python(self.getCol1()))
        showIndent(outfile, level)
        outfile.write('Col2=%s,\n' % quote_python(self.getCol2()))
        showIndent(outfile, level)
        outfile.write('Col3=%s,\n' % quote_python(self.getCol3()))
        showIndent(outfile, level)
        outfile.write('Col4=%s,\n' % quote_python(self.getCol4()))
        showIndent(outfile, level)
        outfile.write('Col5=%s,\n' % quote_python(self.getCol5()))
        showIndent(outfile, level)
        outfile.write('Col6=%s,\n' % quote_python(self.getCol6()))
        showIndent(outfile, level)
        outfile.write('Col7=%s,\n' % quote_python(self.getCol7()))
        showIndent(outfile, level)
        outfile.write('Col8=%s,\n' % quote_python(self.getCol8()))
        showIndent(outfile, level)
        outfile.write('Col9=%s,\n' % quote_python(self.getCol9()))
        showIndent(outfile, level)
        outfile.write('Col10=%s,\n' % quote_python(self.getCol10()))
        showIndent(outfile, level)
        outfile.write('Col11=%s,\n' % quote_python(self.getCol11()))
        showIndent(outfile, level)
        outfile.write('Col12=%s,\n' % quote_python(self.getCol12()))
        showIndent(outfile, level)
        outfile.write('Col13=%s,\n' % quote_python(self.getCol13()))
        showIndent(outfile, level)
        outfile.write('Col14=%s,\n' % quote_python(self.getCol14()))
        showIndent(outfile, level)
        outfile.write('Col15=%s,\n' % quote_python(self.getCol15()))
        showIndent(outfile, level)
        outfile.write('Col16=%s,\n' % quote_python(self.getCol16()))
        showIndent(outfile, level)
        outfile.write('Col17=%s,\n' % quote_python(self.getCol17()))
        showIndent(outfile, level)
        outfile.write('Col18=%s,\n' % quote_python(self.getCol18()))
        showIndent(outfile, level)
        outfile.write('Col19=%s,\n' % quote_python(self.getCol19()))
        showIndent(outfile, level)
        outfile.write('Col20=%s,\n' % quote_python(self.getCol20()))
        showIndent(outfile, level)
        outfile.write('Col21=%s,\n' % quote_python(self.getCol21()))
        showIndent(outfile, level)
        outfile.write('Col22=%s,\n' % quote_python(self.getCol22()))
        showIndent(outfile, level)
        outfile.write('Col23=%s,\n' % quote_python(self.getCol23()))
        showIndent(outfile, level)
        outfile.write('Col24=%s,\n' % quote_python(self.getCol24()))
        showIndent(outfile, level)
        outfile.write('Col25=%s,\n' % quote_python(self.getCol25()))
        showIndent(outfile, level)
        outfile.write('Col26=%s,\n' % quote_python(self.getCol26()))
        showIndent(outfile, level)
        outfile.write('Col27=%s,\n' % quote_python(self.getCol27()))
        showIndent(outfile, level)
        outfile.write('Col28=%s,\n' % quote_python(self.getCol28()))
        showIndent(outfile, level)
        outfile.write('Col29=%s,\n' % quote_python(self.getCol29()))
        showIndent(outfile, level)
        outfile.write('Col30=%s,\n' % quote_python(self.getCol30()))
        showIndent(outfile, level)
        outfile.write('Col31=%s,\n' % quote_python(self.getCol31()))
        showIndent(outfile, level)
        outfile.write('Col32=%s,\n' % quote_python(self.getCol32()))
        showIndent(outfile, level)
        outfile.write('Col33=%s,\n' % quote_python(self.getCol33()))
        showIndent(outfile, level)
        outfile.write('Col34=%s,\n' % quote_python(self.getCol34()))
        showIndent(outfile, level)
        outfile.write('Col35=%s,\n' % quote_python(self.getCol35()))
        showIndent(outfile, level)
        outfile.write('Col36=%s,\n' % quote_python(self.getCol36()))
        showIndent(outfile, level)
        outfile.write('Col37=%s,\n' % quote_python(self.getCol37()))
        showIndent(outfile, level)
        outfile.write('Col38=%s,\n' % quote_python(self.getCol38()))
        showIndent(outfile, level)
        outfile.write('Col39=%s,\n' % quote_python(self.getCol39()))
        showIndent(outfile, level)
        outfile.write('Col40=%s,\n' % quote_python(self.getCol40()))
        showIndent(outfile, level)
        outfile.write('Col41=%s,\n' % quote_python(self.getCol41()))
        showIndent(outfile, level)
        outfile.write('Col42=%s,\n' % quote_python(self.getCol42()))
        showIndent(outfile, level)
        outfile.write('Col43=%s,\n' % quote_python(self.getCol43()))
        showIndent(outfile, level)
        outfile.write('Col44=%s,\n' % quote_python(self.getCol44()))
        showIndent(outfile, level)
        outfile.write('Col45=%s,\n' % quote_python(self.getCol45()))
        showIndent(outfile, level)
        outfile.write('Col46=%s,\n' % quote_python(self.getCol46()))
        showIndent(outfile, level)
        outfile.write('Col47=%s,\n' % quote_python(self.getCol47()))
        showIndent(outfile, level)
        outfile.write('Col48=%s,\n' % quote_python(self.getCol48()))
        showIndent(outfile, level)
        outfile.write('Col49=%s,\n' % quote_python(self.getCol49()))
        showIndent(outfile, level)
        outfile.write('Col50=%s,\n' % quote_python(self.getCol50()))
        showIndent(outfile, level)
        outfile.write('Col51=%s,\n' % quote_python(self.getCol51()))
        showIndent(outfile, level)
        outfile.write('Col52=%s,\n' % quote_python(self.getCol52()))
        showIndent(outfile, level)
        outfile.write('Col53=%s,\n' % quote_python(self.getCol53()))
        showIndent(outfile, level)
        outfile.write('Col54=%s,\n' % quote_python(self.getCol54()))
        showIndent(outfile, level)
        outfile.write('Col55=%s,\n' % quote_python(self.getCol55()))
        showIndent(outfile, level)
        outfile.write('Col56=%s,\n' % quote_python(self.getCol56()))
        showIndent(outfile, level)
        outfile.write('Col57=%s,\n' % quote_python(self.getCol57()))
        showIndent(outfile, level)
        outfile.write('Col58=%s,\n' % quote_python(self.getCol58()))
        showIndent(outfile, level)
        outfile.write('Col59=%s,\n' % quote_python(self.getCol59()))
        showIndent(outfile, level)
        outfile.write('Col60=%s,\n' % quote_python(self.getCol60()))
        showIndent(outfile, level)
        outfile.write('Col61=%s,\n' % quote_python(self.getCol61()))
        showIndent(outfile, level)
        outfile.write('Col62=%s,\n' % quote_python(self.getCol62()))
        showIndent(outfile, level)
        outfile.write('Col63=%s,\n' % quote_python(self.getCol63()))
        showIndent(outfile, level)
        outfile.write('Col64=%s,\n' % quote_python(self.getCol64()))
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        if attrs.get('Mneumonic'):
            self.Mneumonic = attrs.get('Mneumonic').value
        if attrs.get('Label'):
            self.Label = attrs.get('Label').value
        if attrs.get('MaxStateIndex'):
            self.MaxStateIndex = attrs.get('MaxStateIndex').value
        if attrs.get('Row'):
            self.Row = attrs.get('Row').value
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col1':
            Col1_ = ''
            for text__content_ in child_.childNodes:
                Col1_ += text__content_.nodeValue
            self.Col1 = Col1_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col2':
            Col2_ = ''
            for text__content_ in child_.childNodes:
                Col2_ += text__content_.nodeValue
            self.Col2 = Col2_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col3':
            Col3_ = ''
            for text__content_ in child_.childNodes:
                Col3_ += text__content_.nodeValue
            self.Col3 = Col3_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col4':
            Col4_ = ''
            for text__content_ in child_.childNodes:
                Col4_ += text__content_.nodeValue
            self.Col4 = Col4_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col5':
            Col5_ = ''
            for text__content_ in child_.childNodes:
                Col5_ += text__content_.nodeValue
            self.Col5 = Col5_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col6':
            Col6_ = ''
            for text__content_ in child_.childNodes:
                Col6_ += text__content_.nodeValue
            self.Col6 = Col6_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col7':
            Col7_ = ''
            for text__content_ in child_.childNodes:
                Col7_ += text__content_.nodeValue
            self.Col7 = Col7_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col8':
            Col8_ = ''
            for text__content_ in child_.childNodes:
                Col8_ += text__content_.nodeValue
            self.Col8 = Col8_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col9':
            Col9_ = ''
            for text__content_ in child_.childNodes:
                Col9_ += text__content_.nodeValue
            self.Col9 = Col9_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col10':
            Col10_ = ''
            for text__content_ in child_.childNodes:
                Col10_ += text__content_.nodeValue
            self.Col10 = Col10_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col11':
            Col11_ = ''
            for text__content_ in child_.childNodes:
                Col11_ += text__content_.nodeValue
            self.Col11 = Col11_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col12':
            Col12_ = ''
            for text__content_ in child_.childNodes:
                Col12_ += text__content_.nodeValue
            self.Col12 = Col12_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col13':
            Col13_ = ''
            for text__content_ in child_.childNodes:
                Col13_ += text__content_.nodeValue
            self.Col13 = Col13_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col14':
            Col14_ = ''
            for text__content_ in child_.childNodes:
                Col14_ += text__content_.nodeValue
            self.Col14 = Col14_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col15':
            Col15_ = ''
            for text__content_ in child_.childNodes:
                Col15_ += text__content_.nodeValue
            self.Col15 = Col15_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col16':
            Col16_ = ''
            for text__content_ in child_.childNodes:
                Col16_ += text__content_.nodeValue
            self.Col16 = Col16_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col17':
            Col17_ = ''
            for text__content_ in child_.childNodes:
                Col17_ += text__content_.nodeValue
            self.Col17 = Col17_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col18':
            Col18_ = ''
            for text__content_ in child_.childNodes:
                Col18_ += text__content_.nodeValue
            self.Col18 = Col18_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col19':
            Col19_ = ''
            for text__content_ in child_.childNodes:
                Col19_ += text__content_.nodeValue
            self.Col19 = Col19_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col20':
            Col20_ = ''
            for text__content_ in child_.childNodes:
                Col20_ += text__content_.nodeValue
            self.Col20 = Col20_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col21':
            Col21_ = ''
            for text__content_ in child_.childNodes:
                Col21_ += text__content_.nodeValue
            self.Col21 = Col21_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col22':
            Col22_ = ''
            for text__content_ in child_.childNodes:
                Col22_ += text__content_.nodeValue
            self.Col22 = Col22_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col23':
            Col23_ = ''
            for text__content_ in child_.childNodes:
                Col23_ += text__content_.nodeValue
            self.Col23 = Col23_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col24':
            Col24_ = ''
            for text__content_ in child_.childNodes:
                Col24_ += text__content_.nodeValue
            self.Col24 = Col24_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col25':
            Col25_ = ''
            for text__content_ in child_.childNodes:
                Col25_ += text__content_.nodeValue
            self.Col25 = Col25_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col26':
            Col26_ = ''
            for text__content_ in child_.childNodes:
                Col26_ += text__content_.nodeValue
            self.Col26 = Col26_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col27':
            Col27_ = ''
            for text__content_ in child_.childNodes:
                Col27_ += text__content_.nodeValue
            self.Col27 = Col27_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col28':
            Col28_ = ''
            for text__content_ in child_.childNodes:
                Col28_ += text__content_.nodeValue
            self.Col28 = Col28_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col29':
            Col29_ = ''
            for text__content_ in child_.childNodes:
                Col29_ += text__content_.nodeValue
            self.Col29 = Col29_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col30':
            Col30_ = ''
            for text__content_ in child_.childNodes:
                Col30_ += text__content_.nodeValue
            self.Col30 = Col30_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col31':
            Col31_ = ''
            for text__content_ in child_.childNodes:
                Col31_ += text__content_.nodeValue
            self.Col31 = Col31_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col32':
            Col32_ = ''
            for text__content_ in child_.childNodes:
                Col32_ += text__content_.nodeValue
            self.Col32 = Col32_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col33':
            Col33_ = ''
            for text__content_ in child_.childNodes:
                Col33_ += text__content_.nodeValue
            self.Col33 = Col33_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col34':
            Col34_ = ''
            for text__content_ in child_.childNodes:
                Col34_ += text__content_.nodeValue
            self.Col34 = Col34_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col35':
            Col35_ = ''
            for text__content_ in child_.childNodes:
                Col35_ += text__content_.nodeValue
            self.Col35 = Col35_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col36':
            Col36_ = ''
            for text__content_ in child_.childNodes:
                Col36_ += text__content_.nodeValue
            self.Col36 = Col36_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col37':
            Col37_ = ''
            for text__content_ in child_.childNodes:
                Col37_ += text__content_.nodeValue
            self.Col37 = Col37_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col38':
            Col38_ = ''
            for text__content_ in child_.childNodes:
                Col38_ += text__content_.nodeValue
            self.Col38 = Col38_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col39':
            Col39_ = ''
            for text__content_ in child_.childNodes:
                Col39_ += text__content_.nodeValue
            self.Col39 = Col39_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col40':
            Col40_ = ''
            for text__content_ in child_.childNodes:
                Col40_ += text__content_.nodeValue
            self.Col40 = Col40_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col41':
            Col41_ = ''
            for text__content_ in child_.childNodes:
                Col41_ += text__content_.nodeValue
            self.Col41 = Col41_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col42':
            Col42_ = ''
            for text__content_ in child_.childNodes:
                Col42_ += text__content_.nodeValue
            self.Col42 = Col42_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col43':
            Col43_ = ''
            for text__content_ in child_.childNodes:
                Col43_ += text__content_.nodeValue
            self.Col43 = Col43_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col44':
            Col44_ = ''
            for text__content_ in child_.childNodes:
                Col44_ += text__content_.nodeValue
            self.Col44 = Col44_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col45':
            Col45_ = ''
            for text__content_ in child_.childNodes:
                Col45_ += text__content_.nodeValue
            self.Col45 = Col45_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col46':
            Col46_ = ''
            for text__content_ in child_.childNodes:
                Col46_ += text__content_.nodeValue
            self.Col46 = Col46_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col47':
            Col47_ = ''
            for text__content_ in child_.childNodes:
                Col47_ += text__content_.nodeValue
            self.Col47 = Col47_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col48':
            Col48_ = ''
            for text__content_ in child_.childNodes:
                Col48_ += text__content_.nodeValue
            self.Col48 = Col48_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col49':
            Col49_ = ''
            for text__content_ in child_.childNodes:
                Col49_ += text__content_.nodeValue
            self.Col49 = Col49_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col50':
            Col50_ = ''
            for text__content_ in child_.childNodes:
                Col50_ += text__content_.nodeValue
            self.Col50 = Col50_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col51':
            Col51_ = ''
            for text__content_ in child_.childNodes:
                Col51_ += text__content_.nodeValue
            self.Col51 = Col51_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col52':
            Col52_ = ''
            for text__content_ in child_.childNodes:
                Col52_ += text__content_.nodeValue
            self.Col52 = Col52_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col53':
            Col53_ = ''
            for text__content_ in child_.childNodes:
                Col53_ += text__content_.nodeValue
            self.Col53 = Col53_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col54':
            Col54_ = ''
            for text__content_ in child_.childNodes:
                Col54_ += text__content_.nodeValue
            self.Col54 = Col54_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col55':
            Col55_ = ''
            for text__content_ in child_.childNodes:
                Col55_ += text__content_.nodeValue
            self.Col55 = Col55_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col56':
            Col56_ = ''
            for text__content_ in child_.childNodes:
                Col56_ += text__content_.nodeValue
            self.Col56 = Col56_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col57':
            Col57_ = ''
            for text__content_ in child_.childNodes:
                Col57_ += text__content_.nodeValue
            self.Col57 = Col57_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col58':
            Col58_ = ''
            for text__content_ in child_.childNodes:
                Col58_ += text__content_.nodeValue
            self.Col58 = Col58_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col59':
            Col59_ = ''
            for text__content_ in child_.childNodes:
                Col59_ += text__content_.nodeValue
            self.Col59 = Col59_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col60':
            Col60_ = ''
            for text__content_ in child_.childNodes:
                Col60_ += text__content_.nodeValue
            self.Col60 = Col60_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col61':
            Col61_ = ''
            for text__content_ in child_.childNodes:
                Col61_ += text__content_.nodeValue
            self.Col61 = Col61_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col62':
            Col62_ = ''
            for text__content_ in child_.childNodes:
                Col62_ += text__content_.nodeValue
            self.Col62 = Col62_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col63':
            Col63_ = ''
            for text__content_ in child_.childNodes:
                Col63_ += text__content_.nodeValue
            self.Col63 = Col63_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col64':
            Col64_ = ''
            for text__content_ in child_.childNodes:
                Col64_ += text__content_.nodeValue
            self.Col64 = Col64_
# end class MData


from xml.sax import handler, make_parser

class SaxStackElement:
    def __init__(self, name='', obj=None):
        self.name = name
        self.obj = obj
        self.content = ''

#
# SAX handler
#
class SaxSmstatespacesamplerHandler(handler.ContentHandler):
    def __init__(self):
        self.stack = []
        self.root = None

    def getRoot(self):
        return self.root

    def setDocumentLocator(self, locator):
        self.locator = locator
    
    def showError(self, msg):
        print '*** (showError):', msg
        sys.exit(-1)

    def startElement(self, name, attrs):
        done = 0
        if name == 'SMStateSpaceSampler':
            obj = SMStateSpaceSampler.factory()
            stackObj = SaxStackElement('SMStateSpaceSampler', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NumberOfAggregates':
            stackObj = SaxStackElement('NumberOfAggregates', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'StateLabels':
            obj = StateLabels.factory()
            stackObj = SaxStackElement('StateLabels', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'StateLabel':
            obj = StateLabel.factory()
            val = attrs.get('Position', None)
            if val is not None:
                obj.setPosition(val)
            stackObj = SaxStackElement('StateLabel', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'MData':
            obj = MData.factory()
            val = attrs.get('Mneumonic', None)
            if val is not None:
                obj.setMneumonic(val)
            val = attrs.get('Label', None)
            if val is not None:
                obj.setLabel(val)
            val = attrs.get('MaxStateIndex', None)
            if val is not None:
                obj.setMaxstateindex(val)
            val = attrs.get('Row', None)
            if val is not None:
                obj.setRow(val)
            stackObj = SaxStackElement('MData', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col1':
            stackObj = SaxStackElement('Col1', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col2':
            stackObj = SaxStackElement('Col2', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col3':
            stackObj = SaxStackElement('Col3', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col4':
            stackObj = SaxStackElement('Col4', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col5':
            stackObj = SaxStackElement('Col5', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col6':
            stackObj = SaxStackElement('Col6', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col7':
            stackObj = SaxStackElement('Col7', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col8':
            stackObj = SaxStackElement('Col8', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col9':
            stackObj = SaxStackElement('Col9', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col10':
            stackObj = SaxStackElement('Col10', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col11':
            stackObj = SaxStackElement('Col11', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col12':
            stackObj = SaxStackElement('Col12', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col13':
            stackObj = SaxStackElement('Col13', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col14':
            stackObj = SaxStackElement('Col14', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col15':
            stackObj = SaxStackElement('Col15', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col16':
            stackObj = SaxStackElement('Col16', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col17':
            stackObj = SaxStackElement('Col17', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col18':
            stackObj = SaxStackElement('Col18', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col19':
            stackObj = SaxStackElement('Col19', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col20':
            stackObj = SaxStackElement('Col20', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col21':
            stackObj = SaxStackElement('Col21', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col22':
            stackObj = SaxStackElement('Col22', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col23':
            stackObj = SaxStackElement('Col23', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col24':
            stackObj = SaxStackElement('Col24', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col25':
            stackObj = SaxStackElement('Col25', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col26':
            stackObj = SaxStackElement('Col26', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col27':
            stackObj = SaxStackElement('Col27', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col28':
            stackObj = SaxStackElement('Col28', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col29':
            stackObj = SaxStackElement('Col29', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col30':
            stackObj = SaxStackElement('Col30', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col31':
            stackObj = SaxStackElement('Col31', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col32':
            stackObj = SaxStackElement('Col32', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col33':
            stackObj = SaxStackElement('Col33', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col34':
            stackObj = SaxStackElement('Col34', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col35':
            stackObj = SaxStackElement('Col35', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col36':
            stackObj = SaxStackElement('Col36', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col37':
            stackObj = SaxStackElement('Col37', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col38':
            stackObj = SaxStackElement('Col38', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col39':
            stackObj = SaxStackElement('Col39', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col40':
            stackObj = SaxStackElement('Col40', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col41':
            stackObj = SaxStackElement('Col41', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col42':
            stackObj = SaxStackElement('Col42', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col43':
            stackObj = SaxStackElement('Col43', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col44':
            stackObj = SaxStackElement('Col44', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col45':
            stackObj = SaxStackElement('Col45', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col46':
            stackObj = SaxStackElement('Col46', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col47':
            stackObj = SaxStackElement('Col47', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col48':
            stackObj = SaxStackElement('Col48', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col49':
            stackObj = SaxStackElement('Col49', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col50':
            stackObj = SaxStackElement('Col50', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col51':
            stackObj = SaxStackElement('Col51', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col52':
            stackObj = SaxStackElement('Col52', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col53':
            stackObj = SaxStackElement('Col53', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col54':
            stackObj = SaxStackElement('Col54', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col55':
            stackObj = SaxStackElement('Col55', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col56':
            stackObj = SaxStackElement('Col56', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col57':
            stackObj = SaxStackElement('Col57', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col58':
            stackObj = SaxStackElement('Col58', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col59':
            stackObj = SaxStackElement('Col59', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col60':
            stackObj = SaxStackElement('Col60', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col61':
            stackObj = SaxStackElement('Col61', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col62':
            stackObj = SaxStackElement('Col62', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col63':
            stackObj = SaxStackElement('Col63', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Col64':
            stackObj = SaxStackElement('Col64', None)
            self.stack.append(stackObj)
            done = 1
        if not done:
            self.reportError('"%s" element not allowed here.' % name)

    def endElement(self, name):
        done = 0
        if name == 'SMStateSpaceSampler':
            if len(self.stack) == 1:
                self.root = self.stack[-1].obj
                self.stack.pop()
                done = 1
        elif name == 'NumberOfAggregates':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNumberofaggregates(content)
                self.stack.pop()
                done = 1
        elif name == 'StateLabels':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStatelabels(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'StateLabel':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addStatelabel(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'MData':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addMdata(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Col1':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol1(content)
                self.stack.pop()
                done = 1
        elif name == 'Col2':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol2(content)
                self.stack.pop()
                done = 1
        elif name == 'Col3':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol3(content)
                self.stack.pop()
                done = 1
        elif name == 'Col4':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol4(content)
                self.stack.pop()
                done = 1
        elif name == 'Col5':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol5(content)
                self.stack.pop()
                done = 1
        elif name == 'Col6':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol6(content)
                self.stack.pop()
                done = 1
        elif name == 'Col7':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol7(content)
                self.stack.pop()
                done = 1
        elif name == 'Col8':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol8(content)
                self.stack.pop()
                done = 1
        elif name == 'Col9':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol9(content)
                self.stack.pop()
                done = 1
        elif name == 'Col10':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol10(content)
                self.stack.pop()
                done = 1
        elif name == 'Col11':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol11(content)
                self.stack.pop()
                done = 1
        elif name == 'Col12':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol12(content)
                self.stack.pop()
                done = 1
        elif name == 'Col13':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol13(content)
                self.stack.pop()
                done = 1
        elif name == 'Col14':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol14(content)
                self.stack.pop()
                done = 1
        elif name == 'Col15':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol15(content)
                self.stack.pop()
                done = 1
        elif name == 'Col16':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol16(content)
                self.stack.pop()
                done = 1
        elif name == 'Col17':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol17(content)
                self.stack.pop()
                done = 1
        elif name == 'Col18':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol18(content)
                self.stack.pop()
                done = 1
        elif name == 'Col19':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol19(content)
                self.stack.pop()
                done = 1
        elif name == 'Col20':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol20(content)
                self.stack.pop()
                done = 1
        elif name == 'Col21':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol21(content)
                self.stack.pop()
                done = 1
        elif name == 'Col22':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol22(content)
                self.stack.pop()
                done = 1
        elif name == 'Col23':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol23(content)
                self.stack.pop()
                done = 1
        elif name == 'Col24':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol24(content)
                self.stack.pop()
                done = 1
        elif name == 'Col25':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol25(content)
                self.stack.pop()
                done = 1
        elif name == 'Col26':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol26(content)
                self.stack.pop()
                done = 1
        elif name == 'Col27':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol27(content)
                self.stack.pop()
                done = 1
        elif name == 'Col28':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol28(content)
                self.stack.pop()
                done = 1
        elif name == 'Col29':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol29(content)
                self.stack.pop()
                done = 1
        elif name == 'Col30':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol30(content)
                self.stack.pop()
                done = 1
        elif name == 'Col31':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol31(content)
                self.stack.pop()
                done = 1
        elif name == 'Col32':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol32(content)
                self.stack.pop()
                done = 1
        elif name == 'Col33':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol33(content)
                self.stack.pop()
                done = 1
        elif name == 'Col34':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol34(content)
                self.stack.pop()
                done = 1
        elif name == 'Col35':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol35(content)
                self.stack.pop()
                done = 1
        elif name == 'Col36':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol36(content)
                self.stack.pop()
                done = 1
        elif name == 'Col37':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol37(content)
                self.stack.pop()
                done = 1
        elif name == 'Col38':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol38(content)
                self.stack.pop()
                done = 1
        elif name == 'Col39':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol39(content)
                self.stack.pop()
                done = 1
        elif name == 'Col40':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol40(content)
                self.stack.pop()
                done = 1
        elif name == 'Col41':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol41(content)
                self.stack.pop()
                done = 1
        elif name == 'Col42':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol42(content)
                self.stack.pop()
                done = 1
        elif name == 'Col43':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol43(content)
                self.stack.pop()
                done = 1
        elif name == 'Col44':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol44(content)
                self.stack.pop()
                done = 1
        elif name == 'Col45':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol45(content)
                self.stack.pop()
                done = 1
        elif name == 'Col46':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol46(content)
                self.stack.pop()
                done = 1
        elif name == 'Col47':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol47(content)
                self.stack.pop()
                done = 1
        elif name == 'Col48':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol48(content)
                self.stack.pop()
                done = 1
        elif name == 'Col49':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol49(content)
                self.stack.pop()
                done = 1
        elif name == 'Col50':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol50(content)
                self.stack.pop()
                done = 1
        elif name == 'Col51':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol51(content)
                self.stack.pop()
                done = 1
        elif name == 'Col52':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol52(content)
                self.stack.pop()
                done = 1
        elif name == 'Col53':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol53(content)
                self.stack.pop()
                done = 1
        elif name == 'Col54':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol54(content)
                self.stack.pop()
                done = 1
        elif name == 'Col55':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol55(content)
                self.stack.pop()
                done = 1
        elif name == 'Col56':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol56(content)
                self.stack.pop()
                done = 1
        elif name == 'Col57':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol57(content)
                self.stack.pop()
                done = 1
        elif name == 'Col58':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol58(content)
                self.stack.pop()
                done = 1
        elif name == 'Col59':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol59(content)
                self.stack.pop()
                done = 1
        elif name == 'Col60':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol60(content)
                self.stack.pop()
                done = 1
        elif name == 'Col61':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol61(content)
                self.stack.pop()
                done = 1
        elif name == 'Col62':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol62(content)
                self.stack.pop()
                done = 1
        elif name == 'Col63':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol63(content)
                self.stack.pop()
                done = 1
        elif name == 'Col64':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setCol64(content)
                self.stack.pop()
                done = 1
        if not done:
            self.reportError('"%s" element not allowed here.' % name)

    def characters(self, chrs, start, end):
        if len(self.stack) > 0:
            self.stack[-1].content += chrs[start:end]

    def reportError(self, mesg):
        locator = self.locator
        sys.stderr.write('Doc: %s  Line: %d  Column: %d\n' % \
            (locator.getSystemId(), locator.getLineNumber(), 
            locator.getColumnNumber() + 1))
        sys.stderr.write(mesg)
        sys.stderr.write('\n')
        sys.exit(-1)
        #raise RuntimeError

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
Options:
    -s        Use the SAX parser, not the minidom parser.
"""

def usage():
    print USAGE_TEXT
    sys.exit(-1)


#
# SAX handler used to determine the top level element.
#
class SaxSelectorHandler(handler.ContentHandler):
    def __init__(self):
        self.topElementName = None
    def getTopElementName(self):
        return self.topElementName
    def startElement(self, name, attrs):
        self.topElementName = name
        raise StopIteration


def parseSelect(inFileName):
    infile = file(inFileName, 'r')
    topElementName = None
    parser = make_parser()
    documentHandler = SaxSelectorHandler()
    parser.setContentHandler(documentHandler)
    try:
        try:
            parser.parse(infile)
        except StopIteration:
            topElementName = documentHandler.getTopElementName()
        if topElementName is None:
            raise RuntimeError, 'no top level element'
        topElementName = topElementName.replace('-', '_').replace(':', '_')
        if topElementName not in globals():
            raise RuntimeError, 'no class for top element: %s' % topElementName
        topElement = globals()[topElementName]
        infile.seek(0)
        doc = minidom.parse(infile)
    finally:
        infile.close()
    rootNode = doc.childNodes[0]
    rootObj = topElement.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0)
    return rootObj


def saxParse(inFileName):
    parser = make_parser()
    documentHandler = SaxSmstatespacesamplerHandler()
    parser.setDocumentHandler(documentHandler)
    parser.parse('file:%s' % inFileName)
    root = documentHandler.getRoot()
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    root.export(sys.stdout, 0)
    return root


def saxParseString(inString):
    parser = make_parser()
    documentHandler = SaxSmstatespacesamplerHandler()
    parser.setDocumentHandler(documentHandler)
    parser.feed(inString)
    parser.close()
    rootObj = documentHandler.getRoot()
    ##sys.stdout.write('<?xml version="1.0" ?>\n')
    ##rootObj.export(sys.stdout, 0)
    return rootObj


def parse(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = SMStateSpaceSampler.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0, name_="SMStateSpaceSampler")
    return rootObj


def parseString(inString):
    doc = minidom.parseString(inString)
    rootNode = doc.documentElement
    rootObj = SMStateSpaceSampler.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0, name_="SMStateSpaceSampler")
    return rootObj


def parseLiteral(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = SMStateSpaceSampler.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('from gSMStateSpaceSamplerSpec.py import *\n\n')
    #sys.stdout.write('rootObj = SMStateSpaceSampler(\n')
    #rootObj.exportLiteral(sys.stdout, 0, name_="SMStateSpaceSampler")
    #sys.stdout.write(')\n')
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '-s':
        saxParse(args[1])
    elif len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    main()
    #import pdb
    #pdb.run('main()')

