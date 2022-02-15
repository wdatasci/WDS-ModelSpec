#!/usr/bin/env python

#
# Generated Thu Nov 01 16:22:29 2007 by generateDS.py.
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

class SMDriverInfo:
    subclass = None
    def __init__(self, Handle='', Name='', ParameterList=None, NumberOfSimulations='', SimAggType='', ForecastHorizon='', OperatingMonthID='', OperatingMaxDelq='', PrimaryVinVar='', PrimaryVinVarNumber='', PrimaryVinVarStartIndex='', PrimaryVinVarStopIndex='', PrimaryVinVarSingleIndex='', SecondaryVinVar='', SecondaryVinVarNumber='', SecondaryVinVarStartIndex='', SecondaryVinVarStopIndex='', SecondaryVinVarSingleIndex='', Segments=None):
        self.Handle = Handle
        self.Name = Name
        self.ParameterList = ParameterList
        self.NumberOfSimulations = NumberOfSimulations
        self.SimAggType = SimAggType
        self.ForecastHorizon = ForecastHorizon
        self.OperatingMonthID = OperatingMonthID
        self.OperatingMaxDelq = OperatingMaxDelq
        self.PrimaryVinVar = PrimaryVinVar
        self.PrimaryVinVarNumber = PrimaryVinVarNumber
        self.PrimaryVinVarStartIndex = PrimaryVinVarStartIndex
        self.PrimaryVinVarStopIndex = PrimaryVinVarStopIndex
        self.PrimaryVinVarSingleIndex = PrimaryVinVarSingleIndex
        self.SecondaryVinVar = SecondaryVinVar
        self.SecondaryVinVarNumber = SecondaryVinVarNumber
        self.SecondaryVinVarStartIndex = SecondaryVinVarStartIndex
        self.SecondaryVinVarStopIndex = SecondaryVinVarStopIndex
        self.SecondaryVinVarSingleIndex = SecondaryVinVarSingleIndex
        self.Segments = Segments
    def factory(*args_, **kwargs_):
        if SMDriverInfo.subclass:
            return SMDriverInfo.subclass(*args_, **kwargs_)
        else:
            return SMDriverInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getParameterlist(self): return self.ParameterList
    def setParameterlist(self, ParameterList): self.ParameterList = ParameterList
    def getNumberofsimulations(self): return self.NumberOfSimulations
    def setNumberofsimulations(self, NumberOfSimulations): self.NumberOfSimulations = NumberOfSimulations
    def getSimaggtype(self): return self.SimAggType
    def setSimaggtype(self, SimAggType): self.SimAggType = SimAggType
    def getForecasthorizon(self): return self.ForecastHorizon
    def setForecasthorizon(self, ForecastHorizon): self.ForecastHorizon = ForecastHorizon
    def getOperatingmonthid(self): return self.OperatingMonthID
    def setOperatingmonthid(self, OperatingMonthID): self.OperatingMonthID = OperatingMonthID
    def getOperatingmaxdelq(self): return self.OperatingMaxDelq
    def setOperatingmaxdelq(self, OperatingMaxDelq): self.OperatingMaxDelq = OperatingMaxDelq
    def getPrimaryvinvar(self): return self.PrimaryVinVar
    def setPrimaryvinvar(self, PrimaryVinVar): self.PrimaryVinVar = PrimaryVinVar
    def getPrimaryvinvarnumber(self): return self.PrimaryVinVarNumber
    def setPrimaryvinvarnumber(self, PrimaryVinVarNumber): self.PrimaryVinVarNumber = PrimaryVinVarNumber
    def getPrimaryvinvarstartindex(self): return self.PrimaryVinVarStartIndex
    def setPrimaryvinvarstartindex(self, PrimaryVinVarStartIndex): self.PrimaryVinVarStartIndex = PrimaryVinVarStartIndex
    def getPrimaryvinvarstopindex(self): return self.PrimaryVinVarStopIndex
    def setPrimaryvinvarstopindex(self, PrimaryVinVarStopIndex): self.PrimaryVinVarStopIndex = PrimaryVinVarStopIndex
    def getPrimaryvinvarsingleindex(self): return self.PrimaryVinVarSingleIndex
    def setPrimaryvinvarsingleindex(self, PrimaryVinVarSingleIndex): self.PrimaryVinVarSingleIndex = PrimaryVinVarSingleIndex
    def getSecondaryvinvar(self): return self.SecondaryVinVar
    def setSecondaryvinvar(self, SecondaryVinVar): self.SecondaryVinVar = SecondaryVinVar
    def getSecondaryvinvarnumber(self): return self.SecondaryVinVarNumber
    def setSecondaryvinvarnumber(self, SecondaryVinVarNumber): self.SecondaryVinVarNumber = SecondaryVinVarNumber
    def getSecondaryvinvarstartindex(self): return self.SecondaryVinVarStartIndex
    def setSecondaryvinvarstartindex(self, SecondaryVinVarStartIndex): self.SecondaryVinVarStartIndex = SecondaryVinVarStartIndex
    def getSecondaryvinvarstopindex(self): return self.SecondaryVinVarStopIndex
    def setSecondaryvinvarstopindex(self, SecondaryVinVarStopIndex): self.SecondaryVinVarStopIndex = SecondaryVinVarStopIndex
    def getSecondaryvinvarsingleindex(self): return self.SecondaryVinVarSingleIndex
    def setSecondaryvinvarsingleindex(self, SecondaryVinVarSingleIndex): self.SecondaryVinVarSingleIndex = SecondaryVinVarSingleIndex
    def getSegments(self): return self.Segments
    def setSegments(self, Segments): self.Segments = Segments
    def getHandle(self): return self.Handle
    def setHandle(self, Handle): self.Handle = Handle
    def getName(self): return self.Name
    def setName(self, Name): self.Name = Name
    def export(self, outfile, level, name_='SMDriverInfo'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='SMDriverInfo')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='SMDriverInfo'):
        outfile.write(' Handle="%s"' % (self.getHandle(), ))
        outfile.write(' Name="%s"' % (self.getName(), ))
    def exportChildren(self, outfile, level, name_='SMDriverInfo'):
        if self.ParameterList:
            self.ParameterList.export(outfile, level)
        showIndent(outfile, level)
        outfile.write('<NumberOfSimulations>%s</NumberOfSimulations>\n' % quote_xml(self.getNumberofsimulations()))
        showIndent(outfile, level)
        outfile.write('<SimAggType>%s</SimAggType>\n' % quote_xml(self.getSimaggtype()))
        showIndent(outfile, level)
        outfile.write('<ForecastHorizon>%s</ForecastHorizon>\n' % quote_xml(self.getForecasthorizon()))
        showIndent(outfile, level)
        outfile.write('<OperatingMonthID>%s</OperatingMonthID>\n' % quote_xml(self.getOperatingmonthid()))
        showIndent(outfile, level)
        outfile.write('<OperatingMaxDelq>%s</OperatingMaxDelq>\n' % quote_xml(self.getOperatingmaxdelq()))
        showIndent(outfile, level)
        outfile.write('<PrimaryVinVar>%s</PrimaryVinVar>\n' % quote_xml(self.getPrimaryvinvar()))
        showIndent(outfile, level)
        outfile.write('<PrimaryVinVarNumber>%s</PrimaryVinVarNumber>\n' % quote_xml(self.getPrimaryvinvarnumber()))
        showIndent(outfile, level)
        outfile.write('<PrimaryVinVarStartIndex>%s</PrimaryVinVarStartIndex>\n' % quote_xml(self.getPrimaryvinvarstartindex()))
        showIndent(outfile, level)
        outfile.write('<PrimaryVinVarStopIndex>%s</PrimaryVinVarStopIndex>\n' % quote_xml(self.getPrimaryvinvarstopindex()))
        showIndent(outfile, level)
        outfile.write('<PrimaryVinVarSingleIndex>%s</PrimaryVinVarSingleIndex>\n' % quote_xml(self.getPrimaryvinvarsingleindex()))
        showIndent(outfile, level)
        outfile.write('<SecondaryVinVar>%s</SecondaryVinVar>\n' % quote_xml(self.getSecondaryvinvar()))
        showIndent(outfile, level)
        outfile.write('<SecondaryVinVarNumber>%s</SecondaryVinVarNumber>\n' % quote_xml(self.getSecondaryvinvarnumber()))
        showIndent(outfile, level)
        outfile.write('<SecondaryVinVarStartIndex>%s</SecondaryVinVarStartIndex>\n' % quote_xml(self.getSecondaryvinvarstartindex()))
        showIndent(outfile, level)
        outfile.write('<SecondaryVinVarStopIndex>%s</SecondaryVinVarStopIndex>\n' % quote_xml(self.getSecondaryvinvarstopindex()))
        showIndent(outfile, level)
        outfile.write('<SecondaryVinVarSingleIndex>%s</SecondaryVinVarSingleIndex>\n' % quote_xml(self.getSecondaryvinvarsingleindex()))
        if self.Segments:
            self.Segments.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='SMDriverInfo'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Handle = "%s",\n' % (self.getHandle(),))
        showIndent(outfile, level)
        outfile.write('Name = "%s",\n' % (self.getName(),))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.ParameterList:
            showIndent(outfile, level)
            outfile.write('ParameterList=ParameterList(\n')
            self.ParameterList.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('NumberOfSimulations=%s,\n' % quote_python(self.getNumberofsimulations()))
        showIndent(outfile, level)
        outfile.write('SimAggType=%s,\n' % quote_python(self.getSimaggtype()))
        showIndent(outfile, level)
        outfile.write('ForecastHorizon=%s,\n' % quote_python(self.getForecasthorizon()))
        showIndent(outfile, level)
        outfile.write('OperatingMonthID=%s,\n' % quote_python(self.getOperatingmonthid()))
        showIndent(outfile, level)
        outfile.write('OperatingMaxDelq=%s,\n' % quote_python(self.getOperatingmaxdelq()))
        showIndent(outfile, level)
        outfile.write('PrimaryVinVar=%s,\n' % quote_python(self.getPrimaryvinvar()))
        showIndent(outfile, level)
        outfile.write('PrimaryVinVarNumber=%s,\n' % quote_python(self.getPrimaryvinvarnumber()))
        showIndent(outfile, level)
        outfile.write('PrimaryVinVarStartIndex=%s,\n' % quote_python(self.getPrimaryvinvarstartindex()))
        showIndent(outfile, level)
        outfile.write('PrimaryVinVarStopIndex=%s,\n' % quote_python(self.getPrimaryvinvarstopindex()))
        showIndent(outfile, level)
        outfile.write('PrimaryVinVarSingleIndex=%s,\n' % quote_python(self.getPrimaryvinvarsingleindex()))
        showIndent(outfile, level)
        outfile.write('SecondaryVinVar=%s,\n' % quote_python(self.getSecondaryvinvar()))
        showIndent(outfile, level)
        outfile.write('SecondaryVinVarNumber=%s,\n' % quote_python(self.getSecondaryvinvarnumber()))
        showIndent(outfile, level)
        outfile.write('SecondaryVinVarStartIndex=%s,\n' % quote_python(self.getSecondaryvinvarstartindex()))
        showIndent(outfile, level)
        outfile.write('SecondaryVinVarStopIndex=%s,\n' % quote_python(self.getSecondaryvinvarstopindex()))
        showIndent(outfile, level)
        outfile.write('SecondaryVinVarSingleIndex=%s,\n' % quote_python(self.getSecondaryvinvarsingleindex()))
        if self.Segments:
            showIndent(outfile, level)
            outfile.write('Segments=Segments(\n')
            self.Segments.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
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
            nodeName_ == 'ParameterList':
            obj_ = ParameterList.factory()
            obj_.build(child_)
            self.setParameterlist(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NumberOfSimulations':
            NumberOfSimulations_ = ''
            for text__content_ in child_.childNodes:
                NumberOfSimulations_ += text__content_.nodeValue
            self.NumberOfSimulations = NumberOfSimulations_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'SimAggType':
            SimAggType_ = ''
            for text__content_ in child_.childNodes:
                SimAggType_ += text__content_.nodeValue
            self.SimAggType = SimAggType_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ForecastHorizon':
            ForecastHorizon_ = ''
            for text__content_ in child_.childNodes:
                ForecastHorizon_ += text__content_.nodeValue
            self.ForecastHorizon = ForecastHorizon_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'OperatingMonthID':
            OperatingMonthID_ = ''
            for text__content_ in child_.childNodes:
                OperatingMonthID_ += text__content_.nodeValue
            self.OperatingMonthID = OperatingMonthID_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'OperatingMaxDelq':
            OperatingMaxDelq_ = ''
            for text__content_ in child_.childNodes:
                OperatingMaxDelq_ += text__content_.nodeValue
            self.OperatingMaxDelq = OperatingMaxDelq_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'PrimaryVinVar':
            PrimaryVinVar_ = ''
            for text__content_ in child_.childNodes:
                PrimaryVinVar_ += text__content_.nodeValue
            self.PrimaryVinVar = PrimaryVinVar_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'PrimaryVinVarNumber':
            PrimaryVinVarNumber_ = ''
            for text__content_ in child_.childNodes:
                PrimaryVinVarNumber_ += text__content_.nodeValue
            self.PrimaryVinVarNumber = PrimaryVinVarNumber_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'PrimaryVinVarStartIndex':
            PrimaryVinVarStartIndex_ = ''
            for text__content_ in child_.childNodes:
                PrimaryVinVarStartIndex_ += text__content_.nodeValue
            self.PrimaryVinVarStartIndex = PrimaryVinVarStartIndex_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'PrimaryVinVarStopIndex':
            PrimaryVinVarStopIndex_ = ''
            for text__content_ in child_.childNodes:
                PrimaryVinVarStopIndex_ += text__content_.nodeValue
            self.PrimaryVinVarStopIndex = PrimaryVinVarStopIndex_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'PrimaryVinVarSingleIndex':
            PrimaryVinVarSingleIndex_ = ''
            for text__content_ in child_.childNodes:
                PrimaryVinVarSingleIndex_ += text__content_.nodeValue
            self.PrimaryVinVarSingleIndex = PrimaryVinVarSingleIndex_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'SecondaryVinVar':
            SecondaryVinVar_ = ''
            for text__content_ in child_.childNodes:
                SecondaryVinVar_ += text__content_.nodeValue
            self.SecondaryVinVar = SecondaryVinVar_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'SecondaryVinVarNumber':
            SecondaryVinVarNumber_ = ''
            for text__content_ in child_.childNodes:
                SecondaryVinVarNumber_ += text__content_.nodeValue
            self.SecondaryVinVarNumber = SecondaryVinVarNumber_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'SecondaryVinVarStartIndex':
            SecondaryVinVarStartIndex_ = ''
            for text__content_ in child_.childNodes:
                SecondaryVinVarStartIndex_ += text__content_.nodeValue
            self.SecondaryVinVarStartIndex = SecondaryVinVarStartIndex_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'SecondaryVinVarStopIndex':
            SecondaryVinVarStopIndex_ = ''
            for text__content_ in child_.childNodes:
                SecondaryVinVarStopIndex_ += text__content_.nodeValue
            self.SecondaryVinVarStopIndex = SecondaryVinVarStopIndex_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'SecondaryVinVarSingleIndex':
            SecondaryVinVarSingleIndex_ = ''
            for text__content_ in child_.childNodes:
                SecondaryVinVarSingleIndex_ += text__content_.nodeValue
            self.SecondaryVinVarSingleIndex = SecondaryVinVarSingleIndex_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Segments':
            obj_ = Segments.factory()
            obj_.build(child_)
            self.setSegments(obj_)
# end class SMDriverInfo


class ParameterList:
    subclass = None
    def __init__(self, Parameter=None):
        if Parameter is None:
            self.Parameter = []
        else:
            self.Parameter = Parameter
    def factory(*args_, **kwargs_):
        if ParameterList.subclass:
            return ParameterList.subclass(*args_, **kwargs_)
        else:
            return ParameterList(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getParameter(self): return self.Parameter
    def setParameter(self, Parameter): self.Parameter = Parameter
    def addParameter(self, value): self.Parameter.append(value)
    def insertParameter(self, index, value): self.Parameter[index] = value
    def export(self, outfile, level, name_='ParameterList'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='ParameterList'):
        pass
    def exportChildren(self, outfile, level, name_='ParameterList'):
        for Parameter_ in self.getParameter():
            Parameter_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='ParameterList'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Parameter=[\n')
        level += 1
        for Parameter in self.Parameter:
            showIndent(outfile, level)
            outfile.write('Parameter(\n')
            Parameter.exportLiteral(outfile, level)
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
            nodeName_ == 'Parameter':
            obj_ = Parameter.factory()
            obj_.build(child_)
            self.Parameter.append(obj_)
# end class ParameterList


class Parameter:
    subclass = None
    def __init__(self, Type='', Name='', Value=''):
        self.Type = Type
        self.Name = Name
        self.Value = Value
    def factory(*args_, **kwargs_):
        if Parameter.subclass:
            return Parameter.subclass(*args_, **kwargs_)
        else:
            return Parameter(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getValue(self): return self.Value
    def setValue(self, Value): self.Value = Value
    def getType(self): return self.Type
    def setType(self, Type): self.Type = Type
    def getName(self): return self.Name
    def setName(self, Name): self.Name = Name
    def export(self, outfile, level, name_='Parameter'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='Parameter')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='Parameter'):
        outfile.write(' Type="%s"' % (self.getType(), ))
        outfile.write(' Name="%s"' % (self.getName(), ))
    def exportChildren(self, outfile, level, name_='Parameter'):
        showIndent(outfile, level)
        outfile.write('<Value>%s</Value>\n' % quote_xml(self.getValue()))
    def exportLiteral(self, outfile, level, name_='Parameter'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Type = "%s",\n' % (self.getType(),))
        showIndent(outfile, level)
        outfile.write('Name = "%s",\n' % (self.getName(),))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Value=%s,\n' % quote_python(self.getValue()))
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        if attrs.get('Type'):
            self.Type = attrs.get('Type').value
        if attrs.get('Name'):
            self.Name = attrs.get('Name').value
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Value':
            Value_ = ''
            for text__content_ in child_.childNodes:
                Value_ += text__content_.nodeValue
            self.Value = Value_
# end class Parameter


class Segments:
    subclass = None
    def __init__(self, ParameterList=None, Segment=None):
        self.ParameterList = ParameterList
        if Segment is None:
            self.Segment = []
        else:
            self.Segment = Segment
    def factory(*args_, **kwargs_):
        if Segments.subclass:
            return Segments.subclass(*args_, **kwargs_)
        else:
            return Segments(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getParameterlist(self): return self.ParameterList
    def setParameterlist(self, ParameterList): self.ParameterList = ParameterList
    def getSegment(self): return self.Segment
    def setSegment(self, Segment): self.Segment = Segment
    def addSegment(self, value): self.Segment.append(value)
    def insertSegment(self, index, value): self.Segment[index] = value
    def export(self, outfile, level, name_='Segments'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='Segments'):
        pass
    def exportChildren(self, outfile, level, name_='Segments'):
        if self.ParameterList:
            self.ParameterList.export(outfile, level)
        for Segment_ in self.getSegment():
            Segment_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='Segments'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.ParameterList:
            showIndent(outfile, level)
            outfile.write('ParameterList=ParameterList(\n')
            self.ParameterList.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Segment=[\n')
        level += 1
        for Segment in self.Segment:
            showIndent(outfile, level)
            outfile.write('Segment(\n')
            Segment.exportLiteral(outfile, level)
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
            nodeName_ == 'ParameterList':
            obj_ = ParameterList.factory()
            obj_.build(child_)
            self.setParameterlist(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Segment':
            obj_ = Segment.factory()
            obj_.build(child_)
            self.Segment.append(obj_)
# end class Segments


class Segment:
    subclass = None
    def __init__(self, Position=None, Mneumonic='', Shorthand='', PrimaryVinVarValue='', Concept='', ToForecastInd='', PlaceSamplerCopyBefore='', AgeAtForecastMonth0='', MonthIDAtForecastMonth0='', NewProductionInd='', NewProductionInitialState='', NewProductionUnits='', NewProductionBCL='', NewProductionBAR='', NewProductionBPB='', NewProductionFFees='', NewProductionFPurch='', NewProductionFPmt='', NewProductionDefault=''):
        self.Position = Position
        self.Mneumonic = Mneumonic
        self.Shorthand = Shorthand
        self.PrimaryVinVarValue = PrimaryVinVarValue
        self.Concept = Concept
        self.ToForecastInd = ToForecastInd
        self.PlaceSamplerCopyBefore = PlaceSamplerCopyBefore
        self.AgeAtForecastMonth0 = AgeAtForecastMonth0
        self.MonthIDAtForecastMonth0 = MonthIDAtForecastMonth0
        self.NewProductionInd = NewProductionInd
        self.NewProductionInitialState = NewProductionInitialState
        self.NewProductionUnits = NewProductionUnits
        self.NewProductionBCL = NewProductionBCL
        self.NewProductionBAR = NewProductionBAR
        self.NewProductionBPB = NewProductionBPB
        self.NewProductionFFees = NewProductionFFees
        self.NewProductionFPurch = NewProductionFPurch
        self.NewProductionFPmt = NewProductionFPmt
        self.NewProductionDefault = NewProductionDefault
    def factory(*args_, **kwargs_):
        if Segment.subclass:
            return Segment.subclass(*args_, **kwargs_)
        else:
            return Segment(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMneumonic(self): return self.Mneumonic
    def setMneumonic(self, Mneumonic): self.Mneumonic = Mneumonic
    def getShorthand(self): return self.Shorthand
    def setShorthand(self, Shorthand): self.Shorthand = Shorthand
    def getPrimaryvinvarvalue(self): return self.PrimaryVinVarValue
    def setPrimaryvinvarvalue(self, PrimaryVinVarValue): self.PrimaryVinVarValue = PrimaryVinVarValue
    def getConcept(self): return self.Concept
    def setConcept(self, Concept): self.Concept = Concept
    def getToforecastind(self): return self.ToForecastInd
    def setToforecastind(self, ToForecastInd): self.ToForecastInd = ToForecastInd
    def getPlacesamplercopybefore(self): return self.PlaceSamplerCopyBefore
    def setPlacesamplercopybefore(self, PlaceSamplerCopyBefore): self.PlaceSamplerCopyBefore = PlaceSamplerCopyBefore
    def getAgeatforecastmonth0(self): return self.AgeAtForecastMonth0
    def setAgeatforecastmonth0(self, AgeAtForecastMonth0): self.AgeAtForecastMonth0 = AgeAtForecastMonth0
    def getMonthidatforecastmonth0(self): return self.MonthIDAtForecastMonth0
    def setMonthidatforecastmonth0(self, MonthIDAtForecastMonth0): self.MonthIDAtForecastMonth0 = MonthIDAtForecastMonth0
    def getNewproductionind(self): return self.NewProductionInd
    def setNewproductionind(self, NewProductionInd): self.NewProductionInd = NewProductionInd
    def getNewproductioninitialstate(self): return self.NewProductionInitialState
    def setNewproductioninitialstate(self, NewProductionInitialState): self.NewProductionInitialState = NewProductionInitialState
    def getNewproductionunits(self): return self.NewProductionUnits
    def setNewproductionunits(self, NewProductionUnits): self.NewProductionUnits = NewProductionUnits
    def getNewproductionbcl(self): return self.NewProductionBCL
    def setNewproductionbcl(self, NewProductionBCL): self.NewProductionBCL = NewProductionBCL
    def getNewproductionbar(self): return self.NewProductionBAR
    def setNewproductionbar(self, NewProductionBAR): self.NewProductionBAR = NewProductionBAR
    def getNewproductionbpb(self): return self.NewProductionBPB
    def setNewproductionbpb(self, NewProductionBPB): self.NewProductionBPB = NewProductionBPB
    def getNewproductionffees(self): return self.NewProductionFFees
    def setNewproductionffees(self, NewProductionFFees): self.NewProductionFFees = NewProductionFFees
    def getNewproductionfpurch(self): return self.NewProductionFPurch
    def setNewproductionfpurch(self, NewProductionFPurch): self.NewProductionFPurch = NewProductionFPurch
    def getNewproductionfpmt(self): return self.NewProductionFPmt
    def setNewproductionfpmt(self, NewProductionFPmt): self.NewProductionFPmt = NewProductionFPmt
    def getNewproductiondefault(self): return self.NewProductionDefault
    def setNewproductiondefault(self, NewProductionDefault): self.NewProductionDefault = NewProductionDefault
    def getPosition(self): return self.Position
    def setPosition(self, Position): self.Position = Position
    def export(self, outfile, level, name_='Segment'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='Segment')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='Segment'):
        outfile.write(' Position="%s"' % (self.getPosition(), ))
    def exportChildren(self, outfile, level, name_='Segment'):
        showIndent(outfile, level)
        outfile.write('<Mneumonic>%s</Mneumonic>\n' % quote_xml(self.getMneumonic()))
        showIndent(outfile, level)
        outfile.write('<Shorthand>%s</Shorthand>\n' % quote_xml(self.getShorthand()))
        showIndent(outfile, level)
        outfile.write('<PrimaryVinVarValue>%s</PrimaryVinVarValue>\n' % quote_xml(self.getPrimaryvinvarvalue()))
        showIndent(outfile, level)
        outfile.write('<Concept>%s</Concept>\n' % quote_xml(self.getConcept()))
        showIndent(outfile, level)
        outfile.write('<ToForecastInd>%s</ToForecastInd>\n' % quote_xml(self.getToforecastind()))
        showIndent(outfile, level)
        outfile.write('<PlaceSamplerCopyBefore>%s</PlaceSamplerCopyBefore>\n' % quote_xml(self.getPlacesamplercopybefore()))
        showIndent(outfile, level)
        outfile.write('<AgeAtForecastMonth0>%s</AgeAtForecastMonth0>\n' % quote_xml(self.getAgeatforecastmonth0()))
        showIndent(outfile, level)
        outfile.write('<MonthIDAtForecastMonth0>%s</MonthIDAtForecastMonth0>\n' % quote_xml(self.getMonthidatforecastmonth0()))
        showIndent(outfile, level)
        outfile.write('<NewProductionInd>%s</NewProductionInd>\n' % quote_xml(self.getNewproductionind()))
        showIndent(outfile, level)
        outfile.write('<NewProductionInitialState>%s</NewProductionInitialState>\n' % quote_xml(self.getNewproductioninitialstate()))
        showIndent(outfile, level)
        outfile.write('<NewProductionUnits>%s</NewProductionUnits>\n' % quote_xml(self.getNewproductionunits()))
        showIndent(outfile, level)
        outfile.write('<NewProductionBCL>%s</NewProductionBCL>\n' % quote_xml(self.getNewproductionbcl()))
        showIndent(outfile, level)
        outfile.write('<NewProductionBAR>%s</NewProductionBAR>\n' % quote_xml(self.getNewproductionbar()))
        showIndent(outfile, level)
        outfile.write('<NewProductionBPB>%s</NewProductionBPB>\n' % quote_xml(self.getNewproductionbpb()))
        showIndent(outfile, level)
        outfile.write('<NewProductionFFees>%s</NewProductionFFees>\n' % quote_xml(self.getNewproductionffees()))
        showIndent(outfile, level)
        outfile.write('<NewProductionFPurch>%s</NewProductionFPurch>\n' % quote_xml(self.getNewproductionfpurch()))
        showIndent(outfile, level)
        outfile.write('<NewProductionFPmt>%s</NewProductionFPmt>\n' % quote_xml(self.getNewproductionfpmt()))
        showIndent(outfile, level)
        outfile.write('<NewProductionDefault>%s</NewProductionDefault>\n' % quote_xml(self.getNewproductiondefault()))
    def exportLiteral(self, outfile, level, name_='Segment'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Position = "%s",\n' % (self.getPosition(),))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Mneumonic=%s,\n' % quote_python(self.getMneumonic()))
        showIndent(outfile, level)
        outfile.write('Shorthand=%s,\n' % quote_python(self.getShorthand()))
        showIndent(outfile, level)
        outfile.write('PrimaryVinVarValue=%s,\n' % quote_python(self.getPrimaryvinvarvalue()))
        showIndent(outfile, level)
        outfile.write('Concept=%s,\n' % quote_python(self.getConcept()))
        showIndent(outfile, level)
        outfile.write('ToForecastInd=%s,\n' % quote_python(self.getToforecastind()))
        showIndent(outfile, level)
        outfile.write('PlaceSamplerCopyBefore=%s,\n' % quote_python(self.getPlacesamplercopybefore()))
        showIndent(outfile, level)
        outfile.write('AgeAtForecastMonth0=%s,\n' % quote_python(self.getAgeatforecastmonth0()))
        showIndent(outfile, level)
        outfile.write('MonthIDAtForecastMonth0=%s,\n' % quote_python(self.getMonthidatforecastmonth0()))
        showIndent(outfile, level)
        outfile.write('NewProductionInd=%s,\n' % quote_python(self.getNewproductionind()))
        showIndent(outfile, level)
        outfile.write('NewProductionInitialState=%s,\n' % quote_python(self.getNewproductioninitialstate()))
        showIndent(outfile, level)
        outfile.write('NewProductionUnits=%s,\n' % quote_python(self.getNewproductionunits()))
        showIndent(outfile, level)
        outfile.write('NewProductionBCL=%s,\n' % quote_python(self.getNewproductionbcl()))
        showIndent(outfile, level)
        outfile.write('NewProductionBAR=%s,\n' % quote_python(self.getNewproductionbar()))
        showIndent(outfile, level)
        outfile.write('NewProductionBPB=%s,\n' % quote_python(self.getNewproductionbpb()))
        showIndent(outfile, level)
        outfile.write('NewProductionFFees=%s,\n' % quote_python(self.getNewproductionffees()))
        showIndent(outfile, level)
        outfile.write('NewProductionFPurch=%s,\n' % quote_python(self.getNewproductionfpurch()))
        showIndent(outfile, level)
        outfile.write('NewProductionFPmt=%s,\n' % quote_python(self.getNewproductionfpmt()))
        showIndent(outfile, level)
        outfile.write('NewProductionDefault=%s,\n' % quote_python(self.getNewproductiondefault()))
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        if attrs.get('Position'):
            self.Position = attrs.get('Position').value
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Mneumonic':
            Mneumonic_ = ''
            for text__content_ in child_.childNodes:
                Mneumonic_ += text__content_.nodeValue
            self.Mneumonic = Mneumonic_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Shorthand':
            Shorthand_ = ''
            for text__content_ in child_.childNodes:
                Shorthand_ += text__content_.nodeValue
            self.Shorthand = Shorthand_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'PrimaryVinVarValue':
            PrimaryVinVarValue_ = ''
            for text__content_ in child_.childNodes:
                PrimaryVinVarValue_ += text__content_.nodeValue
            self.PrimaryVinVarValue = PrimaryVinVarValue_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Concept':
            Concept_ = ''
            for text__content_ in child_.childNodes:
                Concept_ += text__content_.nodeValue
            self.Concept = Concept_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ToForecastInd':
            ToForecastInd_ = ''
            for text__content_ in child_.childNodes:
                ToForecastInd_ += text__content_.nodeValue
            self.ToForecastInd = ToForecastInd_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'PlaceSamplerCopyBefore':
            PlaceSamplerCopyBefore_ = ''
            for text__content_ in child_.childNodes:
                PlaceSamplerCopyBefore_ += text__content_.nodeValue
            self.PlaceSamplerCopyBefore = PlaceSamplerCopyBefore_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'AgeAtForecastMonth0':
            AgeAtForecastMonth0_ = ''
            for text__content_ in child_.childNodes:
                AgeAtForecastMonth0_ += text__content_.nodeValue
            self.AgeAtForecastMonth0 = AgeAtForecastMonth0_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'MonthIDAtForecastMonth0':
            MonthIDAtForecastMonth0_ = ''
            for text__content_ in child_.childNodes:
                MonthIDAtForecastMonth0_ += text__content_.nodeValue
            self.MonthIDAtForecastMonth0 = MonthIDAtForecastMonth0_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NewProductionInd':
            NewProductionInd_ = ''
            for text__content_ in child_.childNodes:
                NewProductionInd_ += text__content_.nodeValue
            self.NewProductionInd = NewProductionInd_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NewProductionInitialState':
            NewProductionInitialState_ = ''
            for text__content_ in child_.childNodes:
                NewProductionInitialState_ += text__content_.nodeValue
            self.NewProductionInitialState = NewProductionInitialState_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NewProductionUnits':
            NewProductionUnits_ = ''
            for text__content_ in child_.childNodes:
                NewProductionUnits_ += text__content_.nodeValue
            self.NewProductionUnits = NewProductionUnits_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NewProductionBCL':
            NewProductionBCL_ = ''
            for text__content_ in child_.childNodes:
                NewProductionBCL_ += text__content_.nodeValue
            self.NewProductionBCL = NewProductionBCL_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NewProductionBAR':
            NewProductionBAR_ = ''
            for text__content_ in child_.childNodes:
                NewProductionBAR_ += text__content_.nodeValue
            self.NewProductionBAR = NewProductionBAR_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NewProductionBPB':
            NewProductionBPB_ = ''
            for text__content_ in child_.childNodes:
                NewProductionBPB_ += text__content_.nodeValue
            self.NewProductionBPB = NewProductionBPB_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NewProductionFFees':
            NewProductionFFees_ = ''
            for text__content_ in child_.childNodes:
                NewProductionFFees_ += text__content_.nodeValue
            self.NewProductionFFees = NewProductionFFees_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NewProductionFPurch':
            NewProductionFPurch_ = ''
            for text__content_ in child_.childNodes:
                NewProductionFPurch_ += text__content_.nodeValue
            self.NewProductionFPurch = NewProductionFPurch_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NewProductionFPmt':
            NewProductionFPmt_ = ''
            for text__content_ in child_.childNodes:
                NewProductionFPmt_ += text__content_.nodeValue
            self.NewProductionFPmt = NewProductionFPmt_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NewProductionDefault':
            NewProductionDefault_ = ''
            for text__content_ in child_.childNodes:
                NewProductionDefault_ += text__content_.nodeValue
            self.NewProductionDefault = NewProductionDefault_
# end class Segment


from xml.sax import handler, make_parser

class SaxStackElement:
    def __init__(self, name='', obj=None):
        self.name = name
        self.obj = obj
        self.content = ''

#
# SAX handler
#
class SaxSmdriverinfoHandler(handler.ContentHandler):
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
        if name == 'SMDriverInfo':
            obj = SMDriverInfo.factory()
            stackObj = SaxStackElement('SMDriverInfo', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ParameterList':
            obj = ParameterList.factory()
            stackObj = SaxStackElement('ParameterList', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Parameter':
            obj = Parameter.factory()
            val = attrs.get('Type', None)
            if val is not None:
                obj.setType(val)
            val = attrs.get('Name', None)
            if val is not None:
                obj.setName(val)
            stackObj = SaxStackElement('Parameter', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Value':
            stackObj = SaxStackElement('Value', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NumberOfSimulations':
            stackObj = SaxStackElement('NumberOfSimulations', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'SimAggType':
            stackObj = SaxStackElement('SimAggType', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ForecastHorizon':
            stackObj = SaxStackElement('ForecastHorizon', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'OperatingMonthID':
            stackObj = SaxStackElement('OperatingMonthID', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'OperatingMaxDelq':
            stackObj = SaxStackElement('OperatingMaxDelq', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'PrimaryVinVar':
            stackObj = SaxStackElement('PrimaryVinVar', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'PrimaryVinVarNumber':
            stackObj = SaxStackElement('PrimaryVinVarNumber', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'PrimaryVinVarStartIndex':
            stackObj = SaxStackElement('PrimaryVinVarStartIndex', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'PrimaryVinVarStopIndex':
            stackObj = SaxStackElement('PrimaryVinVarStopIndex', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'PrimaryVinVarSingleIndex':
            stackObj = SaxStackElement('PrimaryVinVarSingleIndex', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'SecondaryVinVar':
            stackObj = SaxStackElement('SecondaryVinVar', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'SecondaryVinVarNumber':
            stackObj = SaxStackElement('SecondaryVinVarNumber', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'SecondaryVinVarStartIndex':
            stackObj = SaxStackElement('SecondaryVinVarStartIndex', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'SecondaryVinVarStopIndex':
            stackObj = SaxStackElement('SecondaryVinVarStopIndex', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'SecondaryVinVarSingleIndex':
            stackObj = SaxStackElement('SecondaryVinVarSingleIndex', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Segments':
            obj = Segments.factory()
            stackObj = SaxStackElement('Segments', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Segment':
            obj = Segment.factory()
            val = attrs.get('Position', None)
            if val is not None:
                obj.setPosition(val)
            stackObj = SaxStackElement('Segment', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Mneumonic':
            stackObj = SaxStackElement('Mneumonic', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Shorthand':
            stackObj = SaxStackElement('Shorthand', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'PrimaryVinVarValue':
            stackObj = SaxStackElement('PrimaryVinVarValue', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Concept':
            stackObj = SaxStackElement('Concept', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ToForecastInd':
            stackObj = SaxStackElement('ToForecastInd', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'PlaceSamplerCopyBefore':
            stackObj = SaxStackElement('PlaceSamplerCopyBefore', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'AgeAtForecastMonth0':
            stackObj = SaxStackElement('AgeAtForecastMonth0', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'MonthIDAtForecastMonth0':
            stackObj = SaxStackElement('MonthIDAtForecastMonth0', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NewProductionInd':
            stackObj = SaxStackElement('NewProductionInd', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NewProductionInitialState':
            stackObj = SaxStackElement('NewProductionInitialState', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NewProductionUnits':
            stackObj = SaxStackElement('NewProductionUnits', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NewProductionBCL':
            stackObj = SaxStackElement('NewProductionBCL', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NewProductionBAR':
            stackObj = SaxStackElement('NewProductionBAR', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NewProductionBPB':
            stackObj = SaxStackElement('NewProductionBPB', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NewProductionFFees':
            stackObj = SaxStackElement('NewProductionFFees', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NewProductionFPurch':
            stackObj = SaxStackElement('NewProductionFPurch', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NewProductionFPmt':
            stackObj = SaxStackElement('NewProductionFPmt', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NewProductionDefault':
            stackObj = SaxStackElement('NewProductionDefault', None)
            self.stack.append(stackObj)
            done = 1
        if not done:
            self.reportError('"%s" element not allowed here.' % name)

    def endElement(self, name):
        done = 0
        if name == 'SMDriverInfo':
            if len(self.stack) == 1:
                self.root = self.stack[-1].obj
                self.stack.pop()
                done = 1
        elif name == 'ParameterList':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setParameterlist(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Parameter':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addParameter(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Value':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setValue(content)
                self.stack.pop()
                done = 1
        elif name == 'NumberOfSimulations':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNumberofsimulations(content)
                self.stack.pop()
                done = 1
        elif name == 'SimAggType':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setSimaggtype(content)
                self.stack.pop()
                done = 1
        elif name == 'ForecastHorizon':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setForecasthorizon(content)
                self.stack.pop()
                done = 1
        elif name == 'OperatingMonthID':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setOperatingmonthid(content)
                self.stack.pop()
                done = 1
        elif name == 'OperatingMaxDelq':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setOperatingmaxdelq(content)
                self.stack.pop()
                done = 1
        elif name == 'PrimaryVinVar':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setPrimaryvinvar(content)
                self.stack.pop()
                done = 1
        elif name == 'PrimaryVinVarNumber':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setPrimaryvinvarnumber(content)
                self.stack.pop()
                done = 1
        elif name == 'PrimaryVinVarStartIndex':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setPrimaryvinvarstartindex(content)
                self.stack.pop()
                done = 1
        elif name == 'PrimaryVinVarStopIndex':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setPrimaryvinvarstopindex(content)
                self.stack.pop()
                done = 1
        elif name == 'PrimaryVinVarSingleIndex':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setPrimaryvinvarsingleindex(content)
                self.stack.pop()
                done = 1
        elif name == 'SecondaryVinVar':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setSecondaryvinvar(content)
                self.stack.pop()
                done = 1
        elif name == 'SecondaryVinVarNumber':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setSecondaryvinvarnumber(content)
                self.stack.pop()
                done = 1
        elif name == 'SecondaryVinVarStartIndex':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setSecondaryvinvarstartindex(content)
                self.stack.pop()
                done = 1
        elif name == 'SecondaryVinVarStopIndex':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setSecondaryvinvarstopindex(content)
                self.stack.pop()
                done = 1
        elif name == 'SecondaryVinVarSingleIndex':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setSecondaryvinvarsingleindex(content)
                self.stack.pop()
                done = 1
        elif name == 'Segments':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setSegments(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Segment':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addSegment(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Mneumonic':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setMneumonic(content)
                self.stack.pop()
                done = 1
        elif name == 'Shorthand':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setShorthand(content)
                self.stack.pop()
                done = 1
        elif name == 'PrimaryVinVarValue':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setPrimaryvinvarvalue(content)
                self.stack.pop()
                done = 1
        elif name == 'Concept':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setConcept(content)
                self.stack.pop()
                done = 1
        elif name == 'ToForecastInd':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setToforecastind(content)
                self.stack.pop()
                done = 1
        elif name == 'PlaceSamplerCopyBefore':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setPlacesamplercopybefore(content)
                self.stack.pop()
                done = 1
        elif name == 'AgeAtForecastMonth0':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setAgeatforecastmonth0(content)
                self.stack.pop()
                done = 1
        elif name == 'MonthIDAtForecastMonth0':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setMonthidatforecastmonth0(content)
                self.stack.pop()
                done = 1
        elif name == 'NewProductionInd':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNewproductionind(content)
                self.stack.pop()
                done = 1
        elif name == 'NewProductionInitialState':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNewproductioninitialstate(content)
                self.stack.pop()
                done = 1
        elif name == 'NewProductionUnits':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNewproductionunits(content)
                self.stack.pop()
                done = 1
        elif name == 'NewProductionBCL':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNewproductionbcl(content)
                self.stack.pop()
                done = 1
        elif name == 'NewProductionBAR':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNewproductionbar(content)
                self.stack.pop()
                done = 1
        elif name == 'NewProductionBPB':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNewproductionbpb(content)
                self.stack.pop()
                done = 1
        elif name == 'NewProductionFFees':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNewproductionffees(content)
                self.stack.pop()
                done = 1
        elif name == 'NewProductionFPurch':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNewproductionfpurch(content)
                self.stack.pop()
                done = 1
        elif name == 'NewProductionFPmt':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNewproductionfpmt(content)
                self.stack.pop()
                done = 1
        elif name == 'NewProductionDefault':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNewproductiondefault(content)
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
    documentHandler = SaxSmdriverinfoHandler()
    parser.setDocumentHandler(documentHandler)
    parser.parse('file:%s' % inFileName)
    root = documentHandler.getRoot()
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    root.export(sys.stdout, 0)
    return root


def saxParseString(inString):
    parser = make_parser()
    documentHandler = SaxSmdriverinfoHandler()
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
    rootObj = SMDriverInfo.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0, name_="SMDriverInfo")
    return rootObj


def parseString(inString):
    doc = minidom.parseString(inString)
    rootNode = doc.documentElement
    rootObj = SMDriverInfo.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0, name_="SMDriverInfo")
    return rootObj


def parseLiteral(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = SMDriverInfo.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('from gSMDriverInfo.py import *\n\n')
    #sys.stdout.write('rootObj = SMDriverInfo(\n')
    #rootObj.exportLiteral(sys.stdout, 0, name_="SMDriverInfo")
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

