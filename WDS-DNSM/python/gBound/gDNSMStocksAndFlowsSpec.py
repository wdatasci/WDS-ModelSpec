#!/usr/bin/env python

#
# Generated Thu Nov 01 16:22:32 2007 by generateDS.py.
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

class SMStocksAndFlows:
    subclass = None
    def __init__(self, Handle='', Name='', ParameterList=None, Units=None, Stocks=None, Flows=None, Orders=None):
        self.Handle = Handle
        self.Name = Name
        self.ParameterList = ParameterList
        self.Units = Units
        self.Stocks = Stocks
        self.Flows = Flows
        self.Orders = Orders
    def factory(*args_, **kwargs_):
        if SMStocksAndFlows.subclass:
            return SMStocksAndFlows.subclass(*args_, **kwargs_)
        else:
            return SMStocksAndFlows(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getParameterlist(self): return self.ParameterList
    def setParameterlist(self, ParameterList): self.ParameterList = ParameterList
    def getUnits(self): return self.Units
    def setUnits(self, Units): self.Units = Units
    def getStocks(self): return self.Stocks
    def setStocks(self, Stocks): self.Stocks = Stocks
    def getFlows(self): return self.Flows
    def setFlows(self, Flows): self.Flows = Flows
    def getOrders(self): return self.Orders
    def setOrders(self, Orders): self.Orders = Orders
    def getHandle(self): return self.Handle
    def setHandle(self, Handle): self.Handle = Handle
    def getName(self): return self.Name
    def setName(self, Name): self.Name = Name
    def export(self, outfile, level, name_='SMStocksAndFlows'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='SMStocksAndFlows')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='SMStocksAndFlows'):
        outfile.write(' Handle="%s"' % (self.getHandle(), ))
        outfile.write(' Name="%s"' % (self.getName(), ))
    def exportChildren(self, outfile, level, name_='SMStocksAndFlows'):
        if self.ParameterList:
            self.ParameterList.export(outfile, level)
        if self.Units:
            self.Units.export(outfile, level)
        if self.Stocks:
            self.Stocks.export(outfile, level)
        if self.Flows:
            self.Flows.export(outfile, level)
        if self.Orders:
            self.Orders.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='SMStocksAndFlows'):
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
        if self.Units:
            showIndent(outfile, level)
            outfile.write('Units=Units(\n')
            self.Units.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Stocks:
            showIndent(outfile, level)
            outfile.write('Stocks=Stocks(\n')
            self.Stocks.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Flows:
            showIndent(outfile, level)
            outfile.write('Flows=Flows(\n')
            self.Flows.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Orders:
            showIndent(outfile, level)
            outfile.write('Orders=Orders(\n')
            self.Orders.exportLiteral(outfile, level)
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
            nodeName_ == 'Units':
            obj_ = Units.factory()
            obj_.build(child_)
            self.setUnits(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Stocks':
            obj_ = Stocks.factory()
            obj_.build(child_)
            self.setStocks(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Flows':
            obj_ = Flows.factory()
            obj_.build(child_)
            self.setFlows(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Orders':
            obj_ = Orders.factory()
            obj_.build(child_)
            self.setOrders(obj_)
# end class SMStocksAndFlows


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


class Units:
    subclass = None
    def __init__(self, Handle='', ParameterList=None, Unit=None):
        self.Handle = Handle
        self.ParameterList = ParameterList
        if Unit is None:
            self.Unit = []
        else:
            self.Unit = Unit
    def factory(*args_, **kwargs_):
        if Units.subclass:
            return Units.subclass(*args_, **kwargs_)
        else:
            return Units(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getParameterlist(self): return self.ParameterList
    def setParameterlist(self, ParameterList): self.ParameterList = ParameterList
    def getUnit(self): return self.Unit
    def setUnit(self, Unit): self.Unit = Unit
    def addUnit(self, value): self.Unit.append(value)
    def insertUnit(self, index, value): self.Unit[index] = value
    def getHandle(self): return self.Handle
    def setHandle(self, Handle): self.Handle = Handle
    def export(self, outfile, level, name_='Units'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='Units')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='Units'):
        outfile.write(' Handle="%s"' % (self.getHandle(), ))
    def exportChildren(self, outfile, level, name_='Units'):
        if self.ParameterList:
            self.ParameterList.export(outfile, level)
        for Unit_ in self.getUnit():
            Unit_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='Units'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Handle = "%s",\n' % (self.getHandle(),))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.ParameterList:
            showIndent(outfile, level)
            outfile.write('ParameterList=ParameterList(\n')
            self.ParameterList.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Unit=[\n')
        level += 1
        for Unit in self.Unit:
            showIndent(outfile, level)
            outfile.write('Unit(\n')
            Unit.exportLiteral(outfile, level)
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
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ParameterList':
            obj_ = ParameterList.factory()
            obj_.build(child_)
            self.setParameterlist(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Unit':
            obj_ = Unit.factory()
            obj_.build(child_)
            self.Unit.append(obj_)
# end class Units


class Unit:
    subclass = None
    def __init__(self, Position=None, Mneumonic='', Shorthand='', Concept='', ActualsVariable='', Type='', ToSimInd='', SimCVStructural=0.0, SimCVPerPeriod=0.0):
        self.Position = Position
        self.Mneumonic = Mneumonic
        self.Shorthand = Shorthand
        self.Concept = Concept
        self.ActualsVariable = ActualsVariable
        self.Type = Type
        self.ToSimInd = ToSimInd
        self.SimCVStructural = SimCVStructural
        self.SimCVPerPeriod = SimCVPerPeriod
    def factory(*args_, **kwargs_):
        if Unit.subclass:
            return Unit.subclass(*args_, **kwargs_)
        else:
            return Unit(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMneumonic(self): return self.Mneumonic
    def setMneumonic(self, Mneumonic): self.Mneumonic = Mneumonic
    def getShorthand(self): return self.Shorthand
    def setShorthand(self, Shorthand): self.Shorthand = Shorthand
    def getConcept(self): return self.Concept
    def setConcept(self, Concept): self.Concept = Concept
    def getActualsvariable(self): return self.ActualsVariable
    def setActualsvariable(self, ActualsVariable): self.ActualsVariable = ActualsVariable
    def getType(self): return self.Type
    def setType(self, Type): self.Type = Type
    def getTosimind(self): return self.ToSimInd
    def setTosimind(self, ToSimInd): self.ToSimInd = ToSimInd
    def getSimcvstructural(self): return self.SimCVStructural
    def setSimcvstructural(self, SimCVStructural): self.SimCVStructural = SimCVStructural
    def getSimcvperperiod(self): return self.SimCVPerPeriod
    def setSimcvperperiod(self, SimCVPerPeriod): self.SimCVPerPeriod = SimCVPerPeriod
    def getPosition(self): return self.Position
    def setPosition(self, Position): self.Position = Position
    def export(self, outfile, level, name_='Unit'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='Unit')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='Unit'):
        outfile.write(' Position="%s"' % (self.getPosition(), ))
    def exportChildren(self, outfile, level, name_='Unit'):
        showIndent(outfile, level)
        outfile.write('<Mneumonic>%s</Mneumonic>\n' % quote_xml(self.getMneumonic()))
        showIndent(outfile, level)
        outfile.write('<Shorthand>%s</Shorthand>\n' % quote_xml(self.getShorthand()))
        showIndent(outfile, level)
        outfile.write('<Concept>%s</Concept>\n' % quote_xml(self.getConcept()))
        showIndent(outfile, level)
        outfile.write('<ActualsVariable>%s</ActualsVariable>\n' % quote_xml(self.getActualsvariable()))
        showIndent(outfile, level)
        outfile.write('<Type>%s</Type>\n' % quote_xml(self.getType()))
        showIndent(outfile, level)
        outfile.write('<ToSimInd>%s</ToSimInd>\n' % quote_xml(self.getTosimind()))
        showIndent(outfile, level)
        outfile.write('<SimCVStructural>%e</SimCVStructural>\n' % self.getSimcvstructural())
        showIndent(outfile, level)
        outfile.write('<SimCVPerPeriod>%e</SimCVPerPeriod>\n' % self.getSimcvperperiod())
    def exportLiteral(self, outfile, level, name_='Unit'):
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
        outfile.write('Concept=%s,\n' % quote_python(self.getConcept()))
        showIndent(outfile, level)
        outfile.write('ActualsVariable=%s,\n' % quote_python(self.getActualsvariable()))
        showIndent(outfile, level)
        outfile.write('Type=%s,\n' % quote_python(self.getType()))
        showIndent(outfile, level)
        outfile.write('ToSimInd=%s,\n' % quote_python(self.getTosimind()))
        showIndent(outfile, level)
        outfile.write('SimCVStructural=%e,\n' % self.getSimcvstructural())
        showIndent(outfile, level)
        outfile.write('SimCVPerPeriod=%e,\n' % self.getSimcvperperiod())
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
            nodeName_ == 'Concept':
            Concept_ = ''
            for text__content_ in child_.childNodes:
                Concept_ += text__content_.nodeValue
            self.Concept = Concept_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ActualsVariable':
            ActualsVariable_ = ''
            for text__content_ in child_.childNodes:
                ActualsVariable_ += text__content_.nodeValue
            self.ActualsVariable = ActualsVariable_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Type':
            Type_ = ''
            for text__content_ in child_.childNodes:
                Type_ += text__content_.nodeValue
            self.Type = Type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ToSimInd':
            ToSimInd_ = ''
            for text__content_ in child_.childNodes:
                ToSimInd_ += text__content_.nodeValue
            self.ToSimInd = ToSimInd_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'SimCVStructural':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.SimCVStructural = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'SimCVPerPeriod':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.SimCVPerPeriod = fval_
# end class Unit


class Stocks:
    subclass = None
    def __init__(self, Handle='', Number='', MacroReturnNumber='', FunctionReturnNumber='', ParameterList=None, Stock=None):
        self.Handle = Handle
        self.Number = Number
        self.MacroReturnNumber = MacroReturnNumber
        self.FunctionReturnNumber = FunctionReturnNumber
        self.ParameterList = ParameterList
        if Stock is None:
            self.Stock = []
        else:
            self.Stock = Stock
    def factory(*args_, **kwargs_):
        if Stocks.subclass:
            return Stocks.subclass(*args_, **kwargs_)
        else:
            return Stocks(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumber(self): return self.Number
    def setNumber(self, Number): self.Number = Number
    def getMacroreturnnumber(self): return self.MacroReturnNumber
    def setMacroreturnnumber(self, MacroReturnNumber): self.MacroReturnNumber = MacroReturnNumber
    def getFunctionreturnnumber(self): return self.FunctionReturnNumber
    def setFunctionreturnnumber(self, FunctionReturnNumber): self.FunctionReturnNumber = FunctionReturnNumber
    def getParameterlist(self): return self.ParameterList
    def setParameterlist(self, ParameterList): self.ParameterList = ParameterList
    def getStock(self): return self.Stock
    def setStock(self, Stock): self.Stock = Stock
    def addStock(self, value): self.Stock.append(value)
    def insertStock(self, index, value): self.Stock[index] = value
    def getHandle(self): return self.Handle
    def setHandle(self, Handle): self.Handle = Handle
    def export(self, outfile, level, name_='Stocks'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='Stocks')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='Stocks'):
        outfile.write(' Handle="%s"' % (self.getHandle(), ))
    def exportChildren(self, outfile, level, name_='Stocks'):
        showIndent(outfile, level)
        outfile.write('<Number>%s</Number>\n' % quote_xml(self.getNumber()))
        showIndent(outfile, level)
        outfile.write('<MacroReturnNumber>%s</MacroReturnNumber>\n' % quote_xml(self.getMacroreturnnumber()))
        showIndent(outfile, level)
        outfile.write('<FunctionReturnNumber>%s</FunctionReturnNumber>\n' % quote_xml(self.getFunctionreturnnumber()))
        if self.ParameterList:
            self.ParameterList.export(outfile, level)
        for Stock_ in self.getStock():
            Stock_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='Stocks'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Handle = "%s",\n' % (self.getHandle(),))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Number=%s,\n' % quote_python(self.getNumber()))
        showIndent(outfile, level)
        outfile.write('MacroReturnNumber=%s,\n' % quote_python(self.getMacroreturnnumber()))
        showIndent(outfile, level)
        outfile.write('FunctionReturnNumber=%s,\n' % quote_python(self.getFunctionreturnnumber()))
        if self.ParameterList:
            showIndent(outfile, level)
            outfile.write('ParameterList=ParameterList(\n')
            self.ParameterList.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Stock=[\n')
        level += 1
        for Stock in self.Stock:
            showIndent(outfile, level)
            outfile.write('Stock(\n')
            Stock.exportLiteral(outfile, level)
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
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Number':
            Number_ = ''
            for text__content_ in child_.childNodes:
                Number_ += text__content_.nodeValue
            self.Number = Number_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'MacroReturnNumber':
            MacroReturnNumber_ = ''
            for text__content_ in child_.childNodes:
                MacroReturnNumber_ += text__content_.nodeValue
            self.MacroReturnNumber = MacroReturnNumber_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'FunctionReturnNumber':
            FunctionReturnNumber_ = ''
            for text__content_ in child_.childNodes:
                FunctionReturnNumber_ += text__content_.nodeValue
            self.FunctionReturnNumber = FunctionReturnNumber_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ParameterList':
            obj_ = ParameterList.factory()
            obj_.build(child_)
            self.setParameterlist(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Stock':
            obj_ = Stock.factory()
            obj_.build(child_)
            self.Stock.append(obj_)
# end class Stocks


class Stock:
    subclass = None
    def __init__(self, Position=None, Mneumonic='', Shorthand='', Concept='', ActualsVariable='', Type='', LaterUse='', Treatment='', FOutput='', MOutput='', ToSimInd='', SimCV=0.0, NumberOfBases='', Base1Type='', Base1Variable='', Base1IndexOrCode='', Base1Weighting=0.0, Base2Type='', Base2Variable='', Base2IndexOrCode='', Base2Weighting=0.0, Base3Type='', Base3Variable='', Base3IndexOrCode='', Base3Weighting=0.0, Base4Type='', Base4Variable='', Base4IndexOrCode='', Base4Weighting=0.0, Base5Type='', Base5Variable='', Base5IndexOrCode='', Base5Weighting=0.0, Base6Type='', Base6Variable='', Base6IndexOrCode='', Base6Weighting=0.0):
        self.Position = Position
        self.Mneumonic = Mneumonic
        self.Shorthand = Shorthand
        self.Concept = Concept
        self.ActualsVariable = ActualsVariable
        self.Type = Type
        self.LaterUse = LaterUse
        self.Treatment = Treatment
        self.FOutput = FOutput
        self.MOutput = MOutput
        self.ToSimInd = ToSimInd
        self.SimCV = SimCV
        self.NumberOfBases = NumberOfBases
        self.Base1Type = Base1Type
        self.Base1Variable = Base1Variable
        self.Base1IndexOrCode = Base1IndexOrCode
        self.Base1Weighting = Base1Weighting
        self.Base2Type = Base2Type
        self.Base2Variable = Base2Variable
        self.Base2IndexOrCode = Base2IndexOrCode
        self.Base2Weighting = Base2Weighting
        self.Base3Type = Base3Type
        self.Base3Variable = Base3Variable
        self.Base3IndexOrCode = Base3IndexOrCode
        self.Base3Weighting = Base3Weighting
        self.Base4Type = Base4Type
        self.Base4Variable = Base4Variable
        self.Base4IndexOrCode = Base4IndexOrCode
        self.Base4Weighting = Base4Weighting
        self.Base5Type = Base5Type
        self.Base5Variable = Base5Variable
        self.Base5IndexOrCode = Base5IndexOrCode
        self.Base5Weighting = Base5Weighting
        self.Base6Type = Base6Type
        self.Base6Variable = Base6Variable
        self.Base6IndexOrCode = Base6IndexOrCode
        self.Base6Weighting = Base6Weighting
    def factory(*args_, **kwargs_):
        if Stock.subclass:
            return Stock.subclass(*args_, **kwargs_)
        else:
            return Stock(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMneumonic(self): return self.Mneumonic
    def setMneumonic(self, Mneumonic): self.Mneumonic = Mneumonic
    def getShorthand(self): return self.Shorthand
    def setShorthand(self, Shorthand): self.Shorthand = Shorthand
    def getConcept(self): return self.Concept
    def setConcept(self, Concept): self.Concept = Concept
    def getActualsvariable(self): return self.ActualsVariable
    def setActualsvariable(self, ActualsVariable): self.ActualsVariable = ActualsVariable
    def getType(self): return self.Type
    def setType(self, Type): self.Type = Type
    def getLateruse(self): return self.LaterUse
    def setLateruse(self, LaterUse): self.LaterUse = LaterUse
    def getTreatment(self): return self.Treatment
    def setTreatment(self, Treatment): self.Treatment = Treatment
    def getFoutput(self): return self.FOutput
    def setFoutput(self, FOutput): self.FOutput = FOutput
    def getMoutput(self): return self.MOutput
    def setMoutput(self, MOutput): self.MOutput = MOutput
    def getTosimind(self): return self.ToSimInd
    def setTosimind(self, ToSimInd): self.ToSimInd = ToSimInd
    def getSimcv(self): return self.SimCV
    def setSimcv(self, SimCV): self.SimCV = SimCV
    def getNumberofbases(self): return self.NumberOfBases
    def setNumberofbases(self, NumberOfBases): self.NumberOfBases = NumberOfBases
    def getBase1type(self): return self.Base1Type
    def setBase1type(self, Base1Type): self.Base1Type = Base1Type
    def getBase1variable(self): return self.Base1Variable
    def setBase1variable(self, Base1Variable): self.Base1Variable = Base1Variable
    def getBase1indexorcode(self): return self.Base1IndexOrCode
    def setBase1indexorcode(self, Base1IndexOrCode): self.Base1IndexOrCode = Base1IndexOrCode
    def getBase1weighting(self): return self.Base1Weighting
    def setBase1weighting(self, Base1Weighting): self.Base1Weighting = Base1Weighting
    def getBase2type(self): return self.Base2Type
    def setBase2type(self, Base2Type): self.Base2Type = Base2Type
    def getBase2variable(self): return self.Base2Variable
    def setBase2variable(self, Base2Variable): self.Base2Variable = Base2Variable
    def getBase2indexorcode(self): return self.Base2IndexOrCode
    def setBase2indexorcode(self, Base2IndexOrCode): self.Base2IndexOrCode = Base2IndexOrCode
    def getBase2weighting(self): return self.Base2Weighting
    def setBase2weighting(self, Base2Weighting): self.Base2Weighting = Base2Weighting
    def getBase3type(self): return self.Base3Type
    def setBase3type(self, Base3Type): self.Base3Type = Base3Type
    def getBase3variable(self): return self.Base3Variable
    def setBase3variable(self, Base3Variable): self.Base3Variable = Base3Variable
    def getBase3indexorcode(self): return self.Base3IndexOrCode
    def setBase3indexorcode(self, Base3IndexOrCode): self.Base3IndexOrCode = Base3IndexOrCode
    def getBase3weighting(self): return self.Base3Weighting
    def setBase3weighting(self, Base3Weighting): self.Base3Weighting = Base3Weighting
    def getBase4type(self): return self.Base4Type
    def setBase4type(self, Base4Type): self.Base4Type = Base4Type
    def getBase4variable(self): return self.Base4Variable
    def setBase4variable(self, Base4Variable): self.Base4Variable = Base4Variable
    def getBase4indexorcode(self): return self.Base4IndexOrCode
    def setBase4indexorcode(self, Base4IndexOrCode): self.Base4IndexOrCode = Base4IndexOrCode
    def getBase4weighting(self): return self.Base4Weighting
    def setBase4weighting(self, Base4Weighting): self.Base4Weighting = Base4Weighting
    def getBase5type(self): return self.Base5Type
    def setBase5type(self, Base5Type): self.Base5Type = Base5Type
    def getBase5variable(self): return self.Base5Variable
    def setBase5variable(self, Base5Variable): self.Base5Variable = Base5Variable
    def getBase5indexorcode(self): return self.Base5IndexOrCode
    def setBase5indexorcode(self, Base5IndexOrCode): self.Base5IndexOrCode = Base5IndexOrCode
    def getBase5weighting(self): return self.Base5Weighting
    def setBase5weighting(self, Base5Weighting): self.Base5Weighting = Base5Weighting
    def getBase6type(self): return self.Base6Type
    def setBase6type(self, Base6Type): self.Base6Type = Base6Type
    def getBase6variable(self): return self.Base6Variable
    def setBase6variable(self, Base6Variable): self.Base6Variable = Base6Variable
    def getBase6indexorcode(self): return self.Base6IndexOrCode
    def setBase6indexorcode(self, Base6IndexOrCode): self.Base6IndexOrCode = Base6IndexOrCode
    def getBase6weighting(self): return self.Base6Weighting
    def setBase6weighting(self, Base6Weighting): self.Base6Weighting = Base6Weighting
    def getPosition(self): return self.Position
    def setPosition(self, Position): self.Position = Position
    def export(self, outfile, level, name_='Stock'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='Stock')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='Stock'):
        outfile.write(' Position="%s"' % (self.getPosition(), ))
    def exportChildren(self, outfile, level, name_='Stock'):
        showIndent(outfile, level)
        outfile.write('<Mneumonic>%s</Mneumonic>\n' % quote_xml(self.getMneumonic()))
        showIndent(outfile, level)
        outfile.write('<Shorthand>%s</Shorthand>\n' % quote_xml(self.getShorthand()))
        showIndent(outfile, level)
        outfile.write('<Concept>%s</Concept>\n' % quote_xml(self.getConcept()))
        showIndent(outfile, level)
        outfile.write('<ActualsVariable>%s</ActualsVariable>\n' % quote_xml(self.getActualsvariable()))
        showIndent(outfile, level)
        outfile.write('<Type>%s</Type>\n' % quote_xml(self.getType()))
        showIndent(outfile, level)
        outfile.write('<LaterUse>%s</LaterUse>\n' % quote_xml(self.getLateruse()))
        showIndent(outfile, level)
        outfile.write('<Treatment>%s</Treatment>\n' % quote_xml(self.getTreatment()))
        showIndent(outfile, level)
        outfile.write('<FOutput>%s</FOutput>\n' % quote_xml(self.getFoutput()))
        showIndent(outfile, level)
        outfile.write('<MOutput>%s</MOutput>\n' % quote_xml(self.getMoutput()))
        showIndent(outfile, level)
        outfile.write('<ToSimInd>%s</ToSimInd>\n' % quote_xml(self.getTosimind()))
        showIndent(outfile, level)
        outfile.write('<SimCV>%e</SimCV>\n' % self.getSimcv())
        showIndent(outfile, level)
        outfile.write('<NumberOfBases>%s</NumberOfBases>\n' % quote_xml(self.getNumberofbases()))
        showIndent(outfile, level)
        outfile.write('<Base1Type>%s</Base1Type>\n' % quote_xml(self.getBase1type()))
        showIndent(outfile, level)
        outfile.write('<Base1Variable>%s</Base1Variable>\n' % quote_xml(self.getBase1variable()))
        showIndent(outfile, level)
        outfile.write('<Base1IndexOrCode>%s</Base1IndexOrCode>\n' % quote_xml(self.getBase1indexorcode()))
        showIndent(outfile, level)
        outfile.write('<Base1Weighting>%e</Base1Weighting>\n' % self.getBase1weighting())
        showIndent(outfile, level)
        outfile.write('<Base2Type>%s</Base2Type>\n' % quote_xml(self.getBase2type()))
        showIndent(outfile, level)
        outfile.write('<Base2Variable>%s</Base2Variable>\n' % quote_xml(self.getBase2variable()))
        showIndent(outfile, level)
        outfile.write('<Base2IndexOrCode>%s</Base2IndexOrCode>\n' % quote_xml(self.getBase2indexorcode()))
        showIndent(outfile, level)
        outfile.write('<Base2Weighting>%e</Base2Weighting>\n' % self.getBase2weighting())
        showIndent(outfile, level)
        outfile.write('<Base3Type>%s</Base3Type>\n' % quote_xml(self.getBase3type()))
        showIndent(outfile, level)
        outfile.write('<Base3Variable>%s</Base3Variable>\n' % quote_xml(self.getBase3variable()))
        showIndent(outfile, level)
        outfile.write('<Base3IndexOrCode>%s</Base3IndexOrCode>\n' % quote_xml(self.getBase3indexorcode()))
        showIndent(outfile, level)
        outfile.write('<Base3Weighting>%e</Base3Weighting>\n' % self.getBase3weighting())
        showIndent(outfile, level)
        outfile.write('<Base4Type>%s</Base4Type>\n' % quote_xml(self.getBase4type()))
        showIndent(outfile, level)
        outfile.write('<Base4Variable>%s</Base4Variable>\n' % quote_xml(self.getBase4variable()))
        showIndent(outfile, level)
        outfile.write('<Base4IndexOrCode>%s</Base4IndexOrCode>\n' % quote_xml(self.getBase4indexorcode()))
        showIndent(outfile, level)
        outfile.write('<Base4Weighting>%e</Base4Weighting>\n' % self.getBase4weighting())
        showIndent(outfile, level)
        outfile.write('<Base5Type>%s</Base5Type>\n' % quote_xml(self.getBase5type()))
        showIndent(outfile, level)
        outfile.write('<Base5Variable>%s</Base5Variable>\n' % quote_xml(self.getBase5variable()))
        showIndent(outfile, level)
        outfile.write('<Base5IndexOrCode>%s</Base5IndexOrCode>\n' % quote_xml(self.getBase5indexorcode()))
        showIndent(outfile, level)
        outfile.write('<Base5Weighting>%e</Base5Weighting>\n' % self.getBase5weighting())
        showIndent(outfile, level)
        outfile.write('<Base6Type>%s</Base6Type>\n' % quote_xml(self.getBase6type()))
        showIndent(outfile, level)
        outfile.write('<Base6Variable>%s</Base6Variable>\n' % quote_xml(self.getBase6variable()))
        showIndent(outfile, level)
        outfile.write('<Base6IndexOrCode>%s</Base6IndexOrCode>\n' % quote_xml(self.getBase6indexorcode()))
        showIndent(outfile, level)
        outfile.write('<Base6Weighting>%e</Base6Weighting>\n' % self.getBase6weighting())
    def exportLiteral(self, outfile, level, name_='Stock'):
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
        outfile.write('Concept=%s,\n' % quote_python(self.getConcept()))
        showIndent(outfile, level)
        outfile.write('ActualsVariable=%s,\n' % quote_python(self.getActualsvariable()))
        showIndent(outfile, level)
        outfile.write('Type=%s,\n' % quote_python(self.getType()))
        showIndent(outfile, level)
        outfile.write('LaterUse=%s,\n' % quote_python(self.getLateruse()))
        showIndent(outfile, level)
        outfile.write('Treatment=%s,\n' % quote_python(self.getTreatment()))
        showIndent(outfile, level)
        outfile.write('FOutput=%s,\n' % quote_python(self.getFoutput()))
        showIndent(outfile, level)
        outfile.write('MOutput=%s,\n' % quote_python(self.getMoutput()))
        showIndent(outfile, level)
        outfile.write('ToSimInd=%s,\n' % quote_python(self.getTosimind()))
        showIndent(outfile, level)
        outfile.write('SimCV=%e,\n' % self.getSimcv())
        showIndent(outfile, level)
        outfile.write('NumberOfBases=%s,\n' % quote_python(self.getNumberofbases()))
        showIndent(outfile, level)
        outfile.write('Base1Type=%s,\n' % quote_python(self.getBase1type()))
        showIndent(outfile, level)
        outfile.write('Base1Variable=%s,\n' % quote_python(self.getBase1variable()))
        showIndent(outfile, level)
        outfile.write('Base1IndexOrCode=%s,\n' % quote_python(self.getBase1indexorcode()))
        showIndent(outfile, level)
        outfile.write('Base1Weighting=%e,\n' % self.getBase1weighting())
        showIndent(outfile, level)
        outfile.write('Base2Type=%s,\n' % quote_python(self.getBase2type()))
        showIndent(outfile, level)
        outfile.write('Base2Variable=%s,\n' % quote_python(self.getBase2variable()))
        showIndent(outfile, level)
        outfile.write('Base2IndexOrCode=%s,\n' % quote_python(self.getBase2indexorcode()))
        showIndent(outfile, level)
        outfile.write('Base2Weighting=%e,\n' % self.getBase2weighting())
        showIndent(outfile, level)
        outfile.write('Base3Type=%s,\n' % quote_python(self.getBase3type()))
        showIndent(outfile, level)
        outfile.write('Base3Variable=%s,\n' % quote_python(self.getBase3variable()))
        showIndent(outfile, level)
        outfile.write('Base3IndexOrCode=%s,\n' % quote_python(self.getBase3indexorcode()))
        showIndent(outfile, level)
        outfile.write('Base3Weighting=%e,\n' % self.getBase3weighting())
        showIndent(outfile, level)
        outfile.write('Base4Type=%s,\n' % quote_python(self.getBase4type()))
        showIndent(outfile, level)
        outfile.write('Base4Variable=%s,\n' % quote_python(self.getBase4variable()))
        showIndent(outfile, level)
        outfile.write('Base4IndexOrCode=%s,\n' % quote_python(self.getBase4indexorcode()))
        showIndent(outfile, level)
        outfile.write('Base4Weighting=%e,\n' % self.getBase4weighting())
        showIndent(outfile, level)
        outfile.write('Base5Type=%s,\n' % quote_python(self.getBase5type()))
        showIndent(outfile, level)
        outfile.write('Base5Variable=%s,\n' % quote_python(self.getBase5variable()))
        showIndent(outfile, level)
        outfile.write('Base5IndexOrCode=%s,\n' % quote_python(self.getBase5indexorcode()))
        showIndent(outfile, level)
        outfile.write('Base5Weighting=%e,\n' % self.getBase5weighting())
        showIndent(outfile, level)
        outfile.write('Base6Type=%s,\n' % quote_python(self.getBase6type()))
        showIndent(outfile, level)
        outfile.write('Base6Variable=%s,\n' % quote_python(self.getBase6variable()))
        showIndent(outfile, level)
        outfile.write('Base6IndexOrCode=%s,\n' % quote_python(self.getBase6indexorcode()))
        showIndent(outfile, level)
        outfile.write('Base6Weighting=%e,\n' % self.getBase6weighting())
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
            nodeName_ == 'Concept':
            Concept_ = ''
            for text__content_ in child_.childNodes:
                Concept_ += text__content_.nodeValue
            self.Concept = Concept_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ActualsVariable':
            ActualsVariable_ = ''
            for text__content_ in child_.childNodes:
                ActualsVariable_ += text__content_.nodeValue
            self.ActualsVariable = ActualsVariable_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Type':
            Type_ = ''
            for text__content_ in child_.childNodes:
                Type_ += text__content_.nodeValue
            self.Type = Type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'LaterUse':
            LaterUse_ = ''
            for text__content_ in child_.childNodes:
                LaterUse_ += text__content_.nodeValue
            self.LaterUse = LaterUse_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Treatment':
            Treatment_ = ''
            for text__content_ in child_.childNodes:
                Treatment_ += text__content_.nodeValue
            self.Treatment = Treatment_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'FOutput':
            FOutput_ = ''
            for text__content_ in child_.childNodes:
                FOutput_ += text__content_.nodeValue
            self.FOutput = FOutput_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'MOutput':
            MOutput_ = ''
            for text__content_ in child_.childNodes:
                MOutput_ += text__content_.nodeValue
            self.MOutput = MOutput_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ToSimInd':
            ToSimInd_ = ''
            for text__content_ in child_.childNodes:
                ToSimInd_ += text__content_.nodeValue
            self.ToSimInd = ToSimInd_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'SimCV':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.SimCV = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NumberOfBases':
            NumberOfBases_ = ''
            for text__content_ in child_.childNodes:
                NumberOfBases_ += text__content_.nodeValue
            self.NumberOfBases = NumberOfBases_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base1Type':
            Base1Type_ = ''
            for text__content_ in child_.childNodes:
                Base1Type_ += text__content_.nodeValue
            self.Base1Type = Base1Type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base1Variable':
            Base1Variable_ = ''
            for text__content_ in child_.childNodes:
                Base1Variable_ += text__content_.nodeValue
            self.Base1Variable = Base1Variable_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base1IndexOrCode':
            Base1IndexOrCode_ = ''
            for text__content_ in child_.childNodes:
                Base1IndexOrCode_ += text__content_.nodeValue
            self.Base1IndexOrCode = Base1IndexOrCode_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base1Weighting':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Base1Weighting = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base2Type':
            Base2Type_ = ''
            for text__content_ in child_.childNodes:
                Base2Type_ += text__content_.nodeValue
            self.Base2Type = Base2Type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base2Variable':
            Base2Variable_ = ''
            for text__content_ in child_.childNodes:
                Base2Variable_ += text__content_.nodeValue
            self.Base2Variable = Base2Variable_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base2IndexOrCode':
            Base2IndexOrCode_ = ''
            for text__content_ in child_.childNodes:
                Base2IndexOrCode_ += text__content_.nodeValue
            self.Base2IndexOrCode = Base2IndexOrCode_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base2Weighting':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Base2Weighting = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base3Type':
            Base3Type_ = ''
            for text__content_ in child_.childNodes:
                Base3Type_ += text__content_.nodeValue
            self.Base3Type = Base3Type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base3Variable':
            Base3Variable_ = ''
            for text__content_ in child_.childNodes:
                Base3Variable_ += text__content_.nodeValue
            self.Base3Variable = Base3Variable_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base3IndexOrCode':
            Base3IndexOrCode_ = ''
            for text__content_ in child_.childNodes:
                Base3IndexOrCode_ += text__content_.nodeValue
            self.Base3IndexOrCode = Base3IndexOrCode_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base3Weighting':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Base3Weighting = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base4Type':
            Base4Type_ = ''
            for text__content_ in child_.childNodes:
                Base4Type_ += text__content_.nodeValue
            self.Base4Type = Base4Type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base4Variable':
            Base4Variable_ = ''
            for text__content_ in child_.childNodes:
                Base4Variable_ += text__content_.nodeValue
            self.Base4Variable = Base4Variable_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base4IndexOrCode':
            Base4IndexOrCode_ = ''
            for text__content_ in child_.childNodes:
                Base4IndexOrCode_ += text__content_.nodeValue
            self.Base4IndexOrCode = Base4IndexOrCode_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base4Weighting':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Base4Weighting = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base5Type':
            Base5Type_ = ''
            for text__content_ in child_.childNodes:
                Base5Type_ += text__content_.nodeValue
            self.Base5Type = Base5Type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base5Variable':
            Base5Variable_ = ''
            for text__content_ in child_.childNodes:
                Base5Variable_ += text__content_.nodeValue
            self.Base5Variable = Base5Variable_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base5IndexOrCode':
            Base5IndexOrCode_ = ''
            for text__content_ in child_.childNodes:
                Base5IndexOrCode_ += text__content_.nodeValue
            self.Base5IndexOrCode = Base5IndexOrCode_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base5Weighting':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Base5Weighting = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base6Type':
            Base6Type_ = ''
            for text__content_ in child_.childNodes:
                Base6Type_ += text__content_.nodeValue
            self.Base6Type = Base6Type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base6Variable':
            Base6Variable_ = ''
            for text__content_ in child_.childNodes:
                Base6Variable_ += text__content_.nodeValue
            self.Base6Variable = Base6Variable_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base6IndexOrCode':
            Base6IndexOrCode_ = ''
            for text__content_ in child_.childNodes:
                Base6IndexOrCode_ += text__content_.nodeValue
            self.Base6IndexOrCode = Base6IndexOrCode_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base6Weighting':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Base6Weighting = fval_
# end class Stock


class Flows:
    subclass = None
    def __init__(self, Handle='', Number='', MacroReturnNumber='', FunctionReturnNumber='', ParameterList=None, Flow=None):
        self.Handle = Handle
        self.Number = Number
        self.MacroReturnNumber = MacroReturnNumber
        self.FunctionReturnNumber = FunctionReturnNumber
        self.ParameterList = ParameterList
        if Flow is None:
            self.Flow = []
        else:
            self.Flow = Flow
    def factory(*args_, **kwargs_):
        if Flows.subclass:
            return Flows.subclass(*args_, **kwargs_)
        else:
            return Flows(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumber(self): return self.Number
    def setNumber(self, Number): self.Number = Number
    def getMacroreturnnumber(self): return self.MacroReturnNumber
    def setMacroreturnnumber(self, MacroReturnNumber): self.MacroReturnNumber = MacroReturnNumber
    def getFunctionreturnnumber(self): return self.FunctionReturnNumber
    def setFunctionreturnnumber(self, FunctionReturnNumber): self.FunctionReturnNumber = FunctionReturnNumber
    def getParameterlist(self): return self.ParameterList
    def setParameterlist(self, ParameterList): self.ParameterList = ParameterList
    def getFlow(self): return self.Flow
    def setFlow(self, Flow): self.Flow = Flow
    def addFlow(self, value): self.Flow.append(value)
    def insertFlow(self, index, value): self.Flow[index] = value
    def getHandle(self): return self.Handle
    def setHandle(self, Handle): self.Handle = Handle
    def export(self, outfile, level, name_='Flows'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='Flows')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='Flows'):
        outfile.write(' Handle="%s"' % (self.getHandle(), ))
    def exportChildren(self, outfile, level, name_='Flows'):
        showIndent(outfile, level)
        outfile.write('<Number>%s</Number>\n' % quote_xml(self.getNumber()))
        showIndent(outfile, level)
        outfile.write('<MacroReturnNumber>%s</MacroReturnNumber>\n' % quote_xml(self.getMacroreturnnumber()))
        showIndent(outfile, level)
        outfile.write('<FunctionReturnNumber>%s</FunctionReturnNumber>\n' % quote_xml(self.getFunctionreturnnumber()))
        if self.ParameterList:
            self.ParameterList.export(outfile, level)
        for Flow_ in self.getFlow():
            Flow_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='Flows'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Handle = "%s",\n' % (self.getHandle(),))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Number=%s,\n' % quote_python(self.getNumber()))
        showIndent(outfile, level)
        outfile.write('MacroReturnNumber=%s,\n' % quote_python(self.getMacroreturnnumber()))
        showIndent(outfile, level)
        outfile.write('FunctionReturnNumber=%s,\n' % quote_python(self.getFunctionreturnnumber()))
        if self.ParameterList:
            showIndent(outfile, level)
            outfile.write('ParameterList=ParameterList(\n')
            self.ParameterList.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Flow=[\n')
        level += 1
        for Flow in self.Flow:
            showIndent(outfile, level)
            outfile.write('Flow(\n')
            Flow.exportLiteral(outfile, level)
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
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Number':
            Number_ = ''
            for text__content_ in child_.childNodes:
                Number_ += text__content_.nodeValue
            self.Number = Number_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'MacroReturnNumber':
            MacroReturnNumber_ = ''
            for text__content_ in child_.childNodes:
                MacroReturnNumber_ += text__content_.nodeValue
            self.MacroReturnNumber = MacroReturnNumber_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'FunctionReturnNumber':
            FunctionReturnNumber_ = ''
            for text__content_ in child_.childNodes:
                FunctionReturnNumber_ += text__content_.nodeValue
            self.FunctionReturnNumber = FunctionReturnNumber_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ParameterList':
            obj_ = ParameterList.factory()
            obj_.build(child_)
            self.setParameterlist(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Flow':
            obj_ = Flow.factory()
            obj_.build(child_)
            self.Flow.append(obj_)
# end class Flows


class Flow:
    subclass = None
    def __init__(self, Position=None, Mneumonic='', Shorthand='', Concept='', PrePost='', AorS='', RollWeighting='', ActualsVariable='', NumberOfFlowMatrices='', ToSimInd='', SimCV=0.0, NumberOfBases='', Base1Type='', Base1Variable='', Base1IndexOrCode='', Base1Weighting=0.0, Base2Type='', Base2Variable='', Base2IndexOrCode='', Base2Weighting=0.0, Base3Type='', Base3Variable='', Base3IndexOrCode='', Base3Weighting=0.0, Base4Type='', Base4Variable='', Base4IndexOrCode='', Base4Weighting=0.0, Base5Type='', Base5Variable='', Base5IndexOrCode='', Base5Weighting=0.0, Base6Type='', Base6Variable='', Base6IndexOrCode='', Base6Weighting=0.0):
        self.Position = Position
        self.Mneumonic = Mneumonic
        self.Shorthand = Shorthand
        self.Concept = Concept
        self.PrePost = PrePost
        self.AorS = AorS
        self.RollWeighting = RollWeighting
        self.ActualsVariable = ActualsVariable
        self.NumberOfFlowMatrices = NumberOfFlowMatrices
        self.ToSimInd = ToSimInd
        self.SimCV = SimCV
        self.NumberOfBases = NumberOfBases
        self.Base1Type = Base1Type
        self.Base1Variable = Base1Variable
        self.Base1IndexOrCode = Base1IndexOrCode
        self.Base1Weighting = Base1Weighting
        self.Base2Type = Base2Type
        self.Base2Variable = Base2Variable
        self.Base2IndexOrCode = Base2IndexOrCode
        self.Base2Weighting = Base2Weighting
        self.Base3Type = Base3Type
        self.Base3Variable = Base3Variable
        self.Base3IndexOrCode = Base3IndexOrCode
        self.Base3Weighting = Base3Weighting
        self.Base4Type = Base4Type
        self.Base4Variable = Base4Variable
        self.Base4IndexOrCode = Base4IndexOrCode
        self.Base4Weighting = Base4Weighting
        self.Base5Type = Base5Type
        self.Base5Variable = Base5Variable
        self.Base5IndexOrCode = Base5IndexOrCode
        self.Base5Weighting = Base5Weighting
        self.Base6Type = Base6Type
        self.Base6Variable = Base6Variable
        self.Base6IndexOrCode = Base6IndexOrCode
        self.Base6Weighting = Base6Weighting
    def factory(*args_, **kwargs_):
        if Flow.subclass:
            return Flow.subclass(*args_, **kwargs_)
        else:
            return Flow(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMneumonic(self): return self.Mneumonic
    def setMneumonic(self, Mneumonic): self.Mneumonic = Mneumonic
    def getShorthand(self): return self.Shorthand
    def setShorthand(self, Shorthand): self.Shorthand = Shorthand
    def getConcept(self): return self.Concept
    def setConcept(self, Concept): self.Concept = Concept
    def getPrepost(self): return self.PrePost
    def setPrepost(self, PrePost): self.PrePost = PrePost
    def getAors(self): return self.AorS
    def setAors(self, AorS): self.AorS = AorS
    def getRollweighting(self): return self.RollWeighting
    def setRollweighting(self, RollWeighting): self.RollWeighting = RollWeighting
    def getActualsvariable(self): return self.ActualsVariable
    def setActualsvariable(self, ActualsVariable): self.ActualsVariable = ActualsVariable
    def getNumberofflowmatrices(self): return self.NumberOfFlowMatrices
    def setNumberofflowmatrices(self, NumberOfFlowMatrices): self.NumberOfFlowMatrices = NumberOfFlowMatrices
    def getTosimind(self): return self.ToSimInd
    def setTosimind(self, ToSimInd): self.ToSimInd = ToSimInd
    def getSimcv(self): return self.SimCV
    def setSimcv(self, SimCV): self.SimCV = SimCV
    def getNumberofbases(self): return self.NumberOfBases
    def setNumberofbases(self, NumberOfBases): self.NumberOfBases = NumberOfBases
    def getBase1type(self): return self.Base1Type
    def setBase1type(self, Base1Type): self.Base1Type = Base1Type
    def getBase1variable(self): return self.Base1Variable
    def setBase1variable(self, Base1Variable): self.Base1Variable = Base1Variable
    def getBase1indexorcode(self): return self.Base1IndexOrCode
    def setBase1indexorcode(self, Base1IndexOrCode): self.Base1IndexOrCode = Base1IndexOrCode
    def getBase1weighting(self): return self.Base1Weighting
    def setBase1weighting(self, Base1Weighting): self.Base1Weighting = Base1Weighting
    def getBase2type(self): return self.Base2Type
    def setBase2type(self, Base2Type): self.Base2Type = Base2Type
    def getBase2variable(self): return self.Base2Variable
    def setBase2variable(self, Base2Variable): self.Base2Variable = Base2Variable
    def getBase2indexorcode(self): return self.Base2IndexOrCode
    def setBase2indexorcode(self, Base2IndexOrCode): self.Base2IndexOrCode = Base2IndexOrCode
    def getBase2weighting(self): return self.Base2Weighting
    def setBase2weighting(self, Base2Weighting): self.Base2Weighting = Base2Weighting
    def getBase3type(self): return self.Base3Type
    def setBase3type(self, Base3Type): self.Base3Type = Base3Type
    def getBase3variable(self): return self.Base3Variable
    def setBase3variable(self, Base3Variable): self.Base3Variable = Base3Variable
    def getBase3indexorcode(self): return self.Base3IndexOrCode
    def setBase3indexorcode(self, Base3IndexOrCode): self.Base3IndexOrCode = Base3IndexOrCode
    def getBase3weighting(self): return self.Base3Weighting
    def setBase3weighting(self, Base3Weighting): self.Base3Weighting = Base3Weighting
    def getBase4type(self): return self.Base4Type
    def setBase4type(self, Base4Type): self.Base4Type = Base4Type
    def getBase4variable(self): return self.Base4Variable
    def setBase4variable(self, Base4Variable): self.Base4Variable = Base4Variable
    def getBase4indexorcode(self): return self.Base4IndexOrCode
    def setBase4indexorcode(self, Base4IndexOrCode): self.Base4IndexOrCode = Base4IndexOrCode
    def getBase4weighting(self): return self.Base4Weighting
    def setBase4weighting(self, Base4Weighting): self.Base4Weighting = Base4Weighting
    def getBase5type(self): return self.Base5Type
    def setBase5type(self, Base5Type): self.Base5Type = Base5Type
    def getBase5variable(self): return self.Base5Variable
    def setBase5variable(self, Base5Variable): self.Base5Variable = Base5Variable
    def getBase5indexorcode(self): return self.Base5IndexOrCode
    def setBase5indexorcode(self, Base5IndexOrCode): self.Base5IndexOrCode = Base5IndexOrCode
    def getBase5weighting(self): return self.Base5Weighting
    def setBase5weighting(self, Base5Weighting): self.Base5Weighting = Base5Weighting
    def getBase6type(self): return self.Base6Type
    def setBase6type(self, Base6Type): self.Base6Type = Base6Type
    def getBase6variable(self): return self.Base6Variable
    def setBase6variable(self, Base6Variable): self.Base6Variable = Base6Variable
    def getBase6indexorcode(self): return self.Base6IndexOrCode
    def setBase6indexorcode(self, Base6IndexOrCode): self.Base6IndexOrCode = Base6IndexOrCode
    def getBase6weighting(self): return self.Base6Weighting
    def setBase6weighting(self, Base6Weighting): self.Base6Weighting = Base6Weighting
    def getPosition(self): return self.Position
    def setPosition(self, Position): self.Position = Position
    def export(self, outfile, level, name_='Flow'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='Flow')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='Flow'):
        outfile.write(' Position="%s"' % (self.getPosition(), ))
    def exportChildren(self, outfile, level, name_='Flow'):
        showIndent(outfile, level)
        outfile.write('<Mneumonic>%s</Mneumonic>\n' % quote_xml(self.getMneumonic()))
        showIndent(outfile, level)
        outfile.write('<Shorthand>%s</Shorthand>\n' % quote_xml(self.getShorthand()))
        showIndent(outfile, level)
        outfile.write('<Concept>%s</Concept>\n' % quote_xml(self.getConcept()))
        showIndent(outfile, level)
        outfile.write('<PrePost>%s</PrePost>\n' % quote_xml(self.getPrepost()))
        showIndent(outfile, level)
        outfile.write('<AorS>%s</AorS>\n' % quote_xml(self.getAors()))
        showIndent(outfile, level)
        outfile.write('<RollWeighting>%s</RollWeighting>\n' % quote_xml(self.getRollweighting()))
        showIndent(outfile, level)
        outfile.write('<ActualsVariable>%s</ActualsVariable>\n' % quote_xml(self.getActualsvariable()))
        showIndent(outfile, level)
        outfile.write('<NumberOfFlowMatrices>%s</NumberOfFlowMatrices>\n' % quote_xml(self.getNumberofflowmatrices()))
        showIndent(outfile, level)
        outfile.write('<ToSimInd>%s</ToSimInd>\n' % quote_xml(self.getTosimind()))
        showIndent(outfile, level)
        outfile.write('<SimCV>%e</SimCV>\n' % self.getSimcv())
        showIndent(outfile, level)
        outfile.write('<NumberOfBases>%s</NumberOfBases>\n' % quote_xml(self.getNumberofbases()))
        showIndent(outfile, level)
        outfile.write('<Base1Type>%s</Base1Type>\n' % quote_xml(self.getBase1type()))
        showIndent(outfile, level)
        outfile.write('<Base1Variable>%s</Base1Variable>\n' % quote_xml(self.getBase1variable()))
        showIndent(outfile, level)
        outfile.write('<Base1IndexOrCode>%s</Base1IndexOrCode>\n' % quote_xml(self.getBase1indexorcode()))
        showIndent(outfile, level)
        outfile.write('<Base1Weighting>%e</Base1Weighting>\n' % self.getBase1weighting())
        showIndent(outfile, level)
        outfile.write('<Base2Type>%s</Base2Type>\n' % quote_xml(self.getBase2type()))
        showIndent(outfile, level)
        outfile.write('<Base2Variable>%s</Base2Variable>\n' % quote_xml(self.getBase2variable()))
        showIndent(outfile, level)
        outfile.write('<Base2IndexOrCode>%s</Base2IndexOrCode>\n' % quote_xml(self.getBase2indexorcode()))
        showIndent(outfile, level)
        outfile.write('<Base2Weighting>%e</Base2Weighting>\n' % self.getBase2weighting())
        showIndent(outfile, level)
        outfile.write('<Base3Type>%s</Base3Type>\n' % quote_xml(self.getBase3type()))
        showIndent(outfile, level)
        outfile.write('<Base3Variable>%s</Base3Variable>\n' % quote_xml(self.getBase3variable()))
        showIndent(outfile, level)
        outfile.write('<Base3IndexOrCode>%s</Base3IndexOrCode>\n' % quote_xml(self.getBase3indexorcode()))
        showIndent(outfile, level)
        outfile.write('<Base3Weighting>%e</Base3Weighting>\n' % self.getBase3weighting())
        showIndent(outfile, level)
        outfile.write('<Base4Type>%s</Base4Type>\n' % quote_xml(self.getBase4type()))
        showIndent(outfile, level)
        outfile.write('<Base4Variable>%s</Base4Variable>\n' % quote_xml(self.getBase4variable()))
        showIndent(outfile, level)
        outfile.write('<Base4IndexOrCode>%s</Base4IndexOrCode>\n' % quote_xml(self.getBase4indexorcode()))
        showIndent(outfile, level)
        outfile.write('<Base4Weighting>%e</Base4Weighting>\n' % self.getBase4weighting())
        showIndent(outfile, level)
        outfile.write('<Base5Type>%s</Base5Type>\n' % quote_xml(self.getBase5type()))
        showIndent(outfile, level)
        outfile.write('<Base5Variable>%s</Base5Variable>\n' % quote_xml(self.getBase5variable()))
        showIndent(outfile, level)
        outfile.write('<Base5IndexOrCode>%s</Base5IndexOrCode>\n' % quote_xml(self.getBase5indexorcode()))
        showIndent(outfile, level)
        outfile.write('<Base5Weighting>%e</Base5Weighting>\n' % self.getBase5weighting())
        showIndent(outfile, level)
        outfile.write('<Base6Type>%s</Base6Type>\n' % quote_xml(self.getBase6type()))
        showIndent(outfile, level)
        outfile.write('<Base6Variable>%s</Base6Variable>\n' % quote_xml(self.getBase6variable()))
        showIndent(outfile, level)
        outfile.write('<Base6IndexOrCode>%s</Base6IndexOrCode>\n' % quote_xml(self.getBase6indexorcode()))
        showIndent(outfile, level)
        outfile.write('<Base6Weighting>%e</Base6Weighting>\n' % self.getBase6weighting())
    def exportLiteral(self, outfile, level, name_='Flow'):
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
        outfile.write('Concept=%s,\n' % quote_python(self.getConcept()))
        showIndent(outfile, level)
        outfile.write('PrePost=%s,\n' % quote_python(self.getPrepost()))
        showIndent(outfile, level)
        outfile.write('AorS=%s,\n' % quote_python(self.getAors()))
        showIndent(outfile, level)
        outfile.write('RollWeighting=%s,\n' % quote_python(self.getRollweighting()))
        showIndent(outfile, level)
        outfile.write('ActualsVariable=%s,\n' % quote_python(self.getActualsvariable()))
        showIndent(outfile, level)
        outfile.write('NumberOfFlowMatrices=%s,\n' % quote_python(self.getNumberofflowmatrices()))
        showIndent(outfile, level)
        outfile.write('ToSimInd=%s,\n' % quote_python(self.getTosimind()))
        showIndent(outfile, level)
        outfile.write('SimCV=%e,\n' % self.getSimcv())
        showIndent(outfile, level)
        outfile.write('NumberOfBases=%s,\n' % quote_python(self.getNumberofbases()))
        showIndent(outfile, level)
        outfile.write('Base1Type=%s,\n' % quote_python(self.getBase1type()))
        showIndent(outfile, level)
        outfile.write('Base1Variable=%s,\n' % quote_python(self.getBase1variable()))
        showIndent(outfile, level)
        outfile.write('Base1IndexOrCode=%s,\n' % quote_python(self.getBase1indexorcode()))
        showIndent(outfile, level)
        outfile.write('Base1Weighting=%e,\n' % self.getBase1weighting())
        showIndent(outfile, level)
        outfile.write('Base2Type=%s,\n' % quote_python(self.getBase2type()))
        showIndent(outfile, level)
        outfile.write('Base2Variable=%s,\n' % quote_python(self.getBase2variable()))
        showIndent(outfile, level)
        outfile.write('Base2IndexOrCode=%s,\n' % quote_python(self.getBase2indexorcode()))
        showIndent(outfile, level)
        outfile.write('Base2Weighting=%e,\n' % self.getBase2weighting())
        showIndent(outfile, level)
        outfile.write('Base3Type=%s,\n' % quote_python(self.getBase3type()))
        showIndent(outfile, level)
        outfile.write('Base3Variable=%s,\n' % quote_python(self.getBase3variable()))
        showIndent(outfile, level)
        outfile.write('Base3IndexOrCode=%s,\n' % quote_python(self.getBase3indexorcode()))
        showIndent(outfile, level)
        outfile.write('Base3Weighting=%e,\n' % self.getBase3weighting())
        showIndent(outfile, level)
        outfile.write('Base4Type=%s,\n' % quote_python(self.getBase4type()))
        showIndent(outfile, level)
        outfile.write('Base4Variable=%s,\n' % quote_python(self.getBase4variable()))
        showIndent(outfile, level)
        outfile.write('Base4IndexOrCode=%s,\n' % quote_python(self.getBase4indexorcode()))
        showIndent(outfile, level)
        outfile.write('Base4Weighting=%e,\n' % self.getBase4weighting())
        showIndent(outfile, level)
        outfile.write('Base5Type=%s,\n' % quote_python(self.getBase5type()))
        showIndent(outfile, level)
        outfile.write('Base5Variable=%s,\n' % quote_python(self.getBase5variable()))
        showIndent(outfile, level)
        outfile.write('Base5IndexOrCode=%s,\n' % quote_python(self.getBase5indexorcode()))
        showIndent(outfile, level)
        outfile.write('Base5Weighting=%e,\n' % self.getBase5weighting())
        showIndent(outfile, level)
        outfile.write('Base6Type=%s,\n' % quote_python(self.getBase6type()))
        showIndent(outfile, level)
        outfile.write('Base6Variable=%s,\n' % quote_python(self.getBase6variable()))
        showIndent(outfile, level)
        outfile.write('Base6IndexOrCode=%s,\n' % quote_python(self.getBase6indexorcode()))
        showIndent(outfile, level)
        outfile.write('Base6Weighting=%e,\n' % self.getBase6weighting())
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
            nodeName_ == 'Concept':
            Concept_ = ''
            for text__content_ in child_.childNodes:
                Concept_ += text__content_.nodeValue
            self.Concept = Concept_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'PrePost':
            PrePost_ = ''
            for text__content_ in child_.childNodes:
                PrePost_ += text__content_.nodeValue
            self.PrePost = PrePost_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'AorS':
            AorS_ = ''
            for text__content_ in child_.childNodes:
                AorS_ += text__content_.nodeValue
            self.AorS = AorS_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'RollWeighting':
            RollWeighting_ = ''
            for text__content_ in child_.childNodes:
                RollWeighting_ += text__content_.nodeValue
            self.RollWeighting = RollWeighting_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ActualsVariable':
            ActualsVariable_ = ''
            for text__content_ in child_.childNodes:
                ActualsVariable_ += text__content_.nodeValue
            self.ActualsVariable = ActualsVariable_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NumberOfFlowMatrices':
            NumberOfFlowMatrices_ = ''
            for text__content_ in child_.childNodes:
                NumberOfFlowMatrices_ += text__content_.nodeValue
            self.NumberOfFlowMatrices = NumberOfFlowMatrices_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ToSimInd':
            ToSimInd_ = ''
            for text__content_ in child_.childNodes:
                ToSimInd_ += text__content_.nodeValue
            self.ToSimInd = ToSimInd_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'SimCV':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.SimCV = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NumberOfBases':
            NumberOfBases_ = ''
            for text__content_ in child_.childNodes:
                NumberOfBases_ += text__content_.nodeValue
            self.NumberOfBases = NumberOfBases_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base1Type':
            Base1Type_ = ''
            for text__content_ in child_.childNodes:
                Base1Type_ += text__content_.nodeValue
            self.Base1Type = Base1Type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base1Variable':
            Base1Variable_ = ''
            for text__content_ in child_.childNodes:
                Base1Variable_ += text__content_.nodeValue
            self.Base1Variable = Base1Variable_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base1IndexOrCode':
            Base1IndexOrCode_ = ''
            for text__content_ in child_.childNodes:
                Base1IndexOrCode_ += text__content_.nodeValue
            self.Base1IndexOrCode = Base1IndexOrCode_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base1Weighting':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Base1Weighting = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base2Type':
            Base2Type_ = ''
            for text__content_ in child_.childNodes:
                Base2Type_ += text__content_.nodeValue
            self.Base2Type = Base2Type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base2Variable':
            Base2Variable_ = ''
            for text__content_ in child_.childNodes:
                Base2Variable_ += text__content_.nodeValue
            self.Base2Variable = Base2Variable_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base2IndexOrCode':
            Base2IndexOrCode_ = ''
            for text__content_ in child_.childNodes:
                Base2IndexOrCode_ += text__content_.nodeValue
            self.Base2IndexOrCode = Base2IndexOrCode_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base2Weighting':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Base2Weighting = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base3Type':
            Base3Type_ = ''
            for text__content_ in child_.childNodes:
                Base3Type_ += text__content_.nodeValue
            self.Base3Type = Base3Type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base3Variable':
            Base3Variable_ = ''
            for text__content_ in child_.childNodes:
                Base3Variable_ += text__content_.nodeValue
            self.Base3Variable = Base3Variable_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base3IndexOrCode':
            Base3IndexOrCode_ = ''
            for text__content_ in child_.childNodes:
                Base3IndexOrCode_ += text__content_.nodeValue
            self.Base3IndexOrCode = Base3IndexOrCode_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base3Weighting':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Base3Weighting = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base4Type':
            Base4Type_ = ''
            for text__content_ in child_.childNodes:
                Base4Type_ += text__content_.nodeValue
            self.Base4Type = Base4Type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base4Variable':
            Base4Variable_ = ''
            for text__content_ in child_.childNodes:
                Base4Variable_ += text__content_.nodeValue
            self.Base4Variable = Base4Variable_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base4IndexOrCode':
            Base4IndexOrCode_ = ''
            for text__content_ in child_.childNodes:
                Base4IndexOrCode_ += text__content_.nodeValue
            self.Base4IndexOrCode = Base4IndexOrCode_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base4Weighting':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Base4Weighting = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base5Type':
            Base5Type_ = ''
            for text__content_ in child_.childNodes:
                Base5Type_ += text__content_.nodeValue
            self.Base5Type = Base5Type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base5Variable':
            Base5Variable_ = ''
            for text__content_ in child_.childNodes:
                Base5Variable_ += text__content_.nodeValue
            self.Base5Variable = Base5Variable_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base5IndexOrCode':
            Base5IndexOrCode_ = ''
            for text__content_ in child_.childNodes:
                Base5IndexOrCode_ += text__content_.nodeValue
            self.Base5IndexOrCode = Base5IndexOrCode_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base5Weighting':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Base5Weighting = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base6Type':
            Base6Type_ = ''
            for text__content_ in child_.childNodes:
                Base6Type_ += text__content_.nodeValue
            self.Base6Type = Base6Type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base6Variable':
            Base6Variable_ = ''
            for text__content_ in child_.childNodes:
                Base6Variable_ += text__content_.nodeValue
            self.Base6Variable = Base6Variable_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base6IndexOrCode':
            Base6IndexOrCode_ = ''
            for text__content_ in child_.childNodes:
                Base6IndexOrCode_ += text__content_.nodeValue
            self.Base6IndexOrCode = Base6IndexOrCode_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Base6Weighting':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Base6Weighting = fval_
# end class Flow


class Orders:
    subclass = None
    def __init__(self, Handle='', Order=None):
        self.Handle = Handle
        if Order is None:
            self.Order = []
        else:
            self.Order = Order
    def factory(*args_, **kwargs_):
        if Orders.subclass:
            return Orders.subclass(*args_, **kwargs_)
        else:
            return Orders(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getOrder(self): return self.Order
    def setOrder(self, Order): self.Order = Order
    def addOrder(self, value): self.Order.append(value)
    def insertOrder(self, index, value): self.Order[index] = value
    def getHandle(self): return self.Handle
    def setHandle(self, Handle): self.Handle = Handle
    def export(self, outfile, level, name_='Orders'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='Orders')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='Orders'):
        outfile.write(' Handle="%s"' % (self.getHandle(), ))
    def exportChildren(self, outfile, level, name_='Orders'):
        for Order_ in self.getOrder():
            Order_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='Orders'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Handle = "%s",\n' % (self.getHandle(),))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Order=[\n')
        level += 1
        for Order in self.Order:
            showIndent(outfile, level)
            outfile.write('Order(\n')
            Order.exportLiteral(outfile, level)
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
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Order':
            obj_ = Order.factory()
            obj_.build(child_)
            self.Order.append(obj_)
# end class Orders


class Order:
    subclass = None
    def __init__(self, Position=None, Mneumonic='', USF='', IndexOrCode=''):
        self.Position = Position
        self.Mneumonic = Mneumonic
        self.USF = USF
        self.IndexOrCode = IndexOrCode
    def factory(*args_, **kwargs_):
        if Order.subclass:
            return Order.subclass(*args_, **kwargs_)
        else:
            return Order(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMneumonic(self): return self.Mneumonic
    def setMneumonic(self, Mneumonic): self.Mneumonic = Mneumonic
    def getUsf(self): return self.USF
    def setUsf(self, USF): self.USF = USF
    def getIndexorcode(self): return self.IndexOrCode
    def setIndexorcode(self, IndexOrCode): self.IndexOrCode = IndexOrCode
    def getPosition(self): return self.Position
    def setPosition(self, Position): self.Position = Position
    def export(self, outfile, level, name_='Order'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='Order')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='Order'):
        outfile.write(' Position="%s"' % (self.getPosition(), ))
    def exportChildren(self, outfile, level, name_='Order'):
        showIndent(outfile, level)
        outfile.write('<Mneumonic>%s</Mneumonic>\n' % quote_xml(self.getMneumonic()))
        showIndent(outfile, level)
        outfile.write('<USF>%s</USF>\n' % quote_xml(self.getUsf()))
        showIndent(outfile, level)
        outfile.write('<IndexOrCode>%s</IndexOrCode>\n' % quote_xml(self.getIndexorcode()))
    def exportLiteral(self, outfile, level, name_='Order'):
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
        outfile.write('USF=%s,\n' % quote_python(self.getUsf()))
        showIndent(outfile, level)
        outfile.write('IndexOrCode=%s,\n' % quote_python(self.getIndexorcode()))
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
            nodeName_ == 'USF':
            USF_ = ''
            for text__content_ in child_.childNodes:
                USF_ += text__content_.nodeValue
            self.USF = USF_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'IndexOrCode':
            IndexOrCode_ = ''
            for text__content_ in child_.childNodes:
                IndexOrCode_ += text__content_.nodeValue
            self.IndexOrCode = IndexOrCode_
# end class Order


from xml.sax import handler, make_parser

class SaxStackElement:
    def __init__(self, name='', obj=None):
        self.name = name
        self.obj = obj
        self.content = ''

#
# SAX handler
#
class SaxSmstocksandflowsHandler(handler.ContentHandler):
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
        if name == 'SMStocksAndFlows':
            obj = SMStocksAndFlows.factory()
            stackObj = SaxStackElement('SMStocksAndFlows', obj)
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
        elif name == 'Units':
            obj = Units.factory()
            val = attrs.get('Handle', None)
            if val is not None:
                obj.setHandle(val)
            stackObj = SaxStackElement('Units', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Unit':
            obj = Unit.factory()
            val = attrs.get('Position', None)
            if val is not None:
                obj.setPosition(val)
            stackObj = SaxStackElement('Unit', obj)
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
        elif name == 'Concept':
            stackObj = SaxStackElement('Concept', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ActualsVariable':
            stackObj = SaxStackElement('ActualsVariable', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Type':
            stackObj = SaxStackElement('Type', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ToSimInd':
            stackObj = SaxStackElement('ToSimInd', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'SimCVStructural':
            stackObj = SaxStackElement('SimCVStructural', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'SimCVPerPeriod':
            stackObj = SaxStackElement('SimCVPerPeriod', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Stocks':
            obj = Stocks.factory()
            val = attrs.get('Handle', None)
            if val is not None:
                obj.setHandle(val)
            stackObj = SaxStackElement('Stocks', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Number':
            stackObj = SaxStackElement('Number', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'MacroReturnNumber':
            stackObj = SaxStackElement('MacroReturnNumber', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'FunctionReturnNumber':
            stackObj = SaxStackElement('FunctionReturnNumber', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Stock':
            obj = Stock.factory()
            val = attrs.get('Position', None)
            if val is not None:
                obj.setPosition(val)
            stackObj = SaxStackElement('Stock', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'LaterUse':
            stackObj = SaxStackElement('LaterUse', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Treatment':
            stackObj = SaxStackElement('Treatment', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'FOutput':
            stackObj = SaxStackElement('FOutput', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'MOutput':
            stackObj = SaxStackElement('MOutput', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'SimCV':
            stackObj = SaxStackElement('SimCV', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NumberOfBases':
            stackObj = SaxStackElement('NumberOfBases', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base1Type':
            stackObj = SaxStackElement('Base1Type', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base1Variable':
            stackObj = SaxStackElement('Base1Variable', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base1IndexOrCode':
            stackObj = SaxStackElement('Base1IndexOrCode', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base1Weighting':
            stackObj = SaxStackElement('Base1Weighting', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base2Type':
            stackObj = SaxStackElement('Base2Type', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base2Variable':
            stackObj = SaxStackElement('Base2Variable', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base2IndexOrCode':
            stackObj = SaxStackElement('Base2IndexOrCode', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base2Weighting':
            stackObj = SaxStackElement('Base2Weighting', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base3Type':
            stackObj = SaxStackElement('Base3Type', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base3Variable':
            stackObj = SaxStackElement('Base3Variable', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base3IndexOrCode':
            stackObj = SaxStackElement('Base3IndexOrCode', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base3Weighting':
            stackObj = SaxStackElement('Base3Weighting', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base4Type':
            stackObj = SaxStackElement('Base4Type', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base4Variable':
            stackObj = SaxStackElement('Base4Variable', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base4IndexOrCode':
            stackObj = SaxStackElement('Base4IndexOrCode', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base4Weighting':
            stackObj = SaxStackElement('Base4Weighting', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base5Type':
            stackObj = SaxStackElement('Base5Type', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base5Variable':
            stackObj = SaxStackElement('Base5Variable', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base5IndexOrCode':
            stackObj = SaxStackElement('Base5IndexOrCode', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base5Weighting':
            stackObj = SaxStackElement('Base5Weighting', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base6Type':
            stackObj = SaxStackElement('Base6Type', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base6Variable':
            stackObj = SaxStackElement('Base6Variable', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base6IndexOrCode':
            stackObj = SaxStackElement('Base6IndexOrCode', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Base6Weighting':
            stackObj = SaxStackElement('Base6Weighting', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Flows':
            obj = Flows.factory()
            val = attrs.get('Handle', None)
            if val is not None:
                obj.setHandle(val)
            stackObj = SaxStackElement('Flows', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Flow':
            obj = Flow.factory()
            val = attrs.get('Position', None)
            if val is not None:
                obj.setPosition(val)
            stackObj = SaxStackElement('Flow', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'PrePost':
            stackObj = SaxStackElement('PrePost', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'AorS':
            stackObj = SaxStackElement('AorS', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'RollWeighting':
            stackObj = SaxStackElement('RollWeighting', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NumberOfFlowMatrices':
            stackObj = SaxStackElement('NumberOfFlowMatrices', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Orders':
            obj = Orders.factory()
            val = attrs.get('Handle', None)
            if val is not None:
                obj.setHandle(val)
            stackObj = SaxStackElement('Orders', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Order':
            obj = Order.factory()
            val = attrs.get('Position', None)
            if val is not None:
                obj.setPosition(val)
            stackObj = SaxStackElement('Order', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'USF':
            stackObj = SaxStackElement('USF', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'IndexOrCode':
            stackObj = SaxStackElement('IndexOrCode', None)
            self.stack.append(stackObj)
            done = 1
        if not done:
            self.reportError('"%s" element not allowed here.' % name)

    def endElement(self, name):
        done = 0
        if name == 'SMStocksAndFlows':
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
        elif name == 'Units':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setUnits(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Unit':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addUnit(self.stack[-1].obj)
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
        elif name == 'Concept':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setConcept(content)
                self.stack.pop()
                done = 1
        elif name == 'ActualsVariable':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setActualsvariable(content)
                self.stack.pop()
                done = 1
        elif name == 'Type':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setType(content)
                self.stack.pop()
                done = 1
        elif name == 'ToSimInd':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setTosimind(content)
                self.stack.pop()
                done = 1
        elif name == 'SimCVStructural':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"SimCVStructural" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setSimcvstructural(content)
                self.stack.pop()
                done = 1
        elif name == 'SimCVPerPeriod':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"SimCVPerPeriod" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setSimcvperperiod(content)
                self.stack.pop()
                done = 1
        elif name == 'Stocks':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStocks(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Number':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNumber(content)
                self.stack.pop()
                done = 1
        elif name == 'MacroReturnNumber':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setMacroreturnnumber(content)
                self.stack.pop()
                done = 1
        elif name == 'FunctionReturnNumber':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setFunctionreturnnumber(content)
                self.stack.pop()
                done = 1
        elif name == 'Stock':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addStock(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'LaterUse':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setLateruse(content)
                self.stack.pop()
                done = 1
        elif name == 'Treatment':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setTreatment(content)
                self.stack.pop()
                done = 1
        elif name == 'FOutput':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setFoutput(content)
                self.stack.pop()
                done = 1
        elif name == 'MOutput':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setMoutput(content)
                self.stack.pop()
                done = 1
        elif name == 'SimCV':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"SimCV" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setSimcv(content)
                self.stack.pop()
                done = 1
        elif name == 'NumberOfBases':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNumberofbases(content)
                self.stack.pop()
                done = 1
        elif name == 'Base1Type':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase1type(content)
                self.stack.pop()
                done = 1
        elif name == 'Base1Variable':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase1variable(content)
                self.stack.pop()
                done = 1
        elif name == 'Base1IndexOrCode':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase1indexorcode(content)
                self.stack.pop()
                done = 1
        elif name == 'Base1Weighting':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Base1Weighting" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setBase1weighting(content)
                self.stack.pop()
                done = 1
        elif name == 'Base2Type':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase2type(content)
                self.stack.pop()
                done = 1
        elif name == 'Base2Variable':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase2variable(content)
                self.stack.pop()
                done = 1
        elif name == 'Base2IndexOrCode':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase2indexorcode(content)
                self.stack.pop()
                done = 1
        elif name == 'Base2Weighting':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Base2Weighting" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setBase2weighting(content)
                self.stack.pop()
                done = 1
        elif name == 'Base3Type':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase3type(content)
                self.stack.pop()
                done = 1
        elif name == 'Base3Variable':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase3variable(content)
                self.stack.pop()
                done = 1
        elif name == 'Base3IndexOrCode':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase3indexorcode(content)
                self.stack.pop()
                done = 1
        elif name == 'Base3Weighting':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Base3Weighting" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setBase3weighting(content)
                self.stack.pop()
                done = 1
        elif name == 'Base4Type':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase4type(content)
                self.stack.pop()
                done = 1
        elif name == 'Base4Variable':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase4variable(content)
                self.stack.pop()
                done = 1
        elif name == 'Base4IndexOrCode':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase4indexorcode(content)
                self.stack.pop()
                done = 1
        elif name == 'Base4Weighting':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Base4Weighting" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setBase4weighting(content)
                self.stack.pop()
                done = 1
        elif name == 'Base5Type':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase5type(content)
                self.stack.pop()
                done = 1
        elif name == 'Base5Variable':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase5variable(content)
                self.stack.pop()
                done = 1
        elif name == 'Base5IndexOrCode':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase5indexorcode(content)
                self.stack.pop()
                done = 1
        elif name == 'Base5Weighting':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Base5Weighting" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setBase5weighting(content)
                self.stack.pop()
                done = 1
        elif name == 'Base6Type':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase6type(content)
                self.stack.pop()
                done = 1
        elif name == 'Base6Variable':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase6variable(content)
                self.stack.pop()
                done = 1
        elif name == 'Base6IndexOrCode':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBase6indexorcode(content)
                self.stack.pop()
                done = 1
        elif name == 'Base6Weighting':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Base6Weighting" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setBase6weighting(content)
                self.stack.pop()
                done = 1
        elif name == 'Flows':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFlows(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Flow':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addFlow(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'PrePost':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setPrepost(content)
                self.stack.pop()
                done = 1
        elif name == 'AorS':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setAors(content)
                self.stack.pop()
                done = 1
        elif name == 'RollWeighting':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setRollweighting(content)
                self.stack.pop()
                done = 1
        elif name == 'NumberOfFlowMatrices':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNumberofflowmatrices(content)
                self.stack.pop()
                done = 1
        elif name == 'Orders':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setOrders(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Order':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addOrder(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'USF':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setUsf(content)
                self.stack.pop()
                done = 1
        elif name == 'IndexOrCode':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setIndexorcode(content)
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
    documentHandler = SaxSmstocksandflowsHandler()
    parser.setDocumentHandler(documentHandler)
    parser.parse('file:%s' % inFileName)
    root = documentHandler.getRoot()
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    root.export(sys.stdout, 0)
    return root


def saxParseString(inString):
    parser = make_parser()
    documentHandler = SaxSmstocksandflowsHandler()
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
    rootObj = SMStocksAndFlows.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0, name_="SMStocksAndFlows")
    return rootObj


def parseString(inString):
    doc = minidom.parseString(inString)
    rootNode = doc.documentElement
    rootObj = SMStocksAndFlows.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0, name_="SMStocksAndFlows")
    return rootObj


def parseLiteral(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = SMStocksAndFlows.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('from gSMStocksAndFlowsSpec.py import *\n\n')
    #sys.stdout.write('rootObj = SMStocksAndFlows(\n')
    #rootObj.exportLiteral(sys.stdout, 0, name_="SMStocksAndFlows")
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

