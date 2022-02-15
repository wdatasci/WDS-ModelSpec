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

class SMStateSpace:
    subclass = None
    def __init__(self, Handle='', Name='', ParameterList=None, States=None, Stages=None, Bridges=None):
        self.Handle = Handle
        self.Name = Name
        self.ParameterList = ParameterList
        self.States = States
        self.Stages = Stages
        self.Bridges = Bridges
    def factory(*args_, **kwargs_):
        if SMStateSpace.subclass:
            return SMStateSpace.subclass(*args_, **kwargs_)
        else:
            return SMStateSpace(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getParameterlist(self): return self.ParameterList
    def setParameterlist(self, ParameterList): self.ParameterList = ParameterList
    def getStates(self): return self.States
    def setStates(self, States): self.States = States
    def getStages(self): return self.Stages
    def setStages(self, Stages): self.Stages = Stages
    def getBridges(self): return self.Bridges
    def setBridges(self, Bridges): self.Bridges = Bridges
    def getHandle(self): return self.Handle
    def setHandle(self, Handle): self.Handle = Handle
    def getName(self): return self.Name
    def setName(self, Name): self.Name = Name
    def export(self, outfile, level, name_='SMStateSpace'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='SMStateSpace')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='SMStateSpace'):
        outfile.write(' Handle="%s"' % (self.getHandle(), ))
        outfile.write(' Name="%s"' % (self.getName(), ))
    def exportChildren(self, outfile, level, name_='SMStateSpace'):
        if self.ParameterList:
            self.ParameterList.export(outfile, level)
        if self.States:
            self.States.export(outfile, level)
        if self.Stages:
            self.Stages.export(outfile, level)
        if self.Bridges:
            self.Bridges.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='SMStateSpace'):
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
        if self.States:
            showIndent(outfile, level)
            outfile.write('States=States(\n')
            self.States.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Stages:
            showIndent(outfile, level)
            outfile.write('Stages=Stages(\n')
            self.Stages.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Bridges:
            showIndent(outfile, level)
            outfile.write('Bridges=Bridges(\n')
            self.Bridges.exportLiteral(outfile, level)
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
            nodeName_ == 'States':
            obj_ = States.factory()
            obj_.build(child_)
            self.setStates(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Stages':
            obj_ = Stages.factory()
            obj_.build(child_)
            self.setStages(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Bridges':
            obj_ = Bridges.factory()
            obj_.build(child_)
            self.setBridges(obj_)
# end class SMStateSpace


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


class States:
    subclass = None
    def __init__(self, Handle='', Number='', NumberOfBaseDimensions='', NumberOfAgePages='', Axis1LimitDefault='', Axis2LimitDefault='', Axis3LimitDefault='', Axis4LimitDefault='', ParameterList=None, State=None):
        self.Handle = Handle
        self.Number = Number
        self.NumberOfBaseDimensions = NumberOfBaseDimensions
        self.NumberOfAgePages = NumberOfAgePages
        self.Axis1LimitDefault = Axis1LimitDefault
        self.Axis2LimitDefault = Axis2LimitDefault
        self.Axis3LimitDefault = Axis3LimitDefault
        self.Axis4LimitDefault = Axis4LimitDefault
        self.ParameterList = ParameterList
        if State is None:
            self.State = []
        else:
            self.State = State
    def factory(*args_, **kwargs_):
        if States.subclass:
            return States.subclass(*args_, **kwargs_)
        else:
            return States(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumber(self): return self.Number
    def setNumber(self, Number): self.Number = Number
    def getNumberofbasedimensions(self): return self.NumberOfBaseDimensions
    def setNumberofbasedimensions(self, NumberOfBaseDimensions): self.NumberOfBaseDimensions = NumberOfBaseDimensions
    def getNumberofagepages(self): return self.NumberOfAgePages
    def setNumberofagepages(self, NumberOfAgePages): self.NumberOfAgePages = NumberOfAgePages
    def getAxis1limitdefault(self): return self.Axis1LimitDefault
    def setAxis1limitdefault(self, Axis1LimitDefault): self.Axis1LimitDefault = Axis1LimitDefault
    def getAxis2limitdefault(self): return self.Axis2LimitDefault
    def setAxis2limitdefault(self, Axis2LimitDefault): self.Axis2LimitDefault = Axis2LimitDefault
    def getAxis3limitdefault(self): return self.Axis3LimitDefault
    def setAxis3limitdefault(self, Axis3LimitDefault): self.Axis3LimitDefault = Axis3LimitDefault
    def getAxis4limitdefault(self): return self.Axis4LimitDefault
    def setAxis4limitdefault(self, Axis4LimitDefault): self.Axis4LimitDefault = Axis4LimitDefault
    def getParameterlist(self): return self.ParameterList
    def setParameterlist(self, ParameterList): self.ParameterList = ParameterList
    def getState(self): return self.State
    def setState(self, State): self.State = State
    def addState(self, value): self.State.append(value)
    def insertState(self, index, value): self.State[index] = value
    def getHandle(self): return self.Handle
    def setHandle(self, Handle): self.Handle = Handle
    def export(self, outfile, level, name_='States'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='States')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='States'):
        outfile.write(' Handle="%s"' % (self.getHandle(), ))
    def exportChildren(self, outfile, level, name_='States'):
        showIndent(outfile, level)
        outfile.write('<Number>%s</Number>\n' % quote_xml(self.getNumber()))
        showIndent(outfile, level)
        outfile.write('<NumberOfBaseDimensions>%s</NumberOfBaseDimensions>\n' % quote_xml(self.getNumberofbasedimensions()))
        showIndent(outfile, level)
        outfile.write('<NumberOfAgePages>%s</NumberOfAgePages>\n' % quote_xml(self.getNumberofagepages()))
        showIndent(outfile, level)
        outfile.write('<Axis1LimitDefault>%s</Axis1LimitDefault>\n' % quote_xml(self.getAxis1limitdefault()))
        showIndent(outfile, level)
        outfile.write('<Axis2LimitDefault>%s</Axis2LimitDefault>\n' % quote_xml(self.getAxis2limitdefault()))
        showIndent(outfile, level)
        outfile.write('<Axis3LimitDefault>%s</Axis3LimitDefault>\n' % quote_xml(self.getAxis3limitdefault()))
        showIndent(outfile, level)
        outfile.write('<Axis4LimitDefault>%s</Axis4LimitDefault>\n' % quote_xml(self.getAxis4limitdefault()))
        if self.ParameterList:
            self.ParameterList.export(outfile, level)
        for State_ in self.getState():
            State_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='States'):
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
        outfile.write('NumberOfBaseDimensions=%s,\n' % quote_python(self.getNumberofbasedimensions()))
        showIndent(outfile, level)
        outfile.write('NumberOfAgePages=%s,\n' % quote_python(self.getNumberofagepages()))
        showIndent(outfile, level)
        outfile.write('Axis1LimitDefault=%s,\n' % quote_python(self.getAxis1limitdefault()))
        showIndent(outfile, level)
        outfile.write('Axis2LimitDefault=%s,\n' % quote_python(self.getAxis2limitdefault()))
        showIndent(outfile, level)
        outfile.write('Axis3LimitDefault=%s,\n' % quote_python(self.getAxis3limitdefault()))
        showIndent(outfile, level)
        outfile.write('Axis4LimitDefault=%s,\n' % quote_python(self.getAxis4limitdefault()))
        if self.ParameterList:
            showIndent(outfile, level)
            outfile.write('ParameterList=ParameterList(\n')
            self.ParameterList.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('State=[\n')
        level += 1
        for State in self.State:
            showIndent(outfile, level)
            outfile.write('State(\n')
            State.exportLiteral(outfile, level)
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
            nodeName_ == 'NumberOfBaseDimensions':
            NumberOfBaseDimensions_ = ''
            for text__content_ in child_.childNodes:
                NumberOfBaseDimensions_ += text__content_.nodeValue
            self.NumberOfBaseDimensions = NumberOfBaseDimensions_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NumberOfAgePages':
            NumberOfAgePages_ = ''
            for text__content_ in child_.childNodes:
                NumberOfAgePages_ += text__content_.nodeValue
            self.NumberOfAgePages = NumberOfAgePages_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Axis1LimitDefault':
            Axis1LimitDefault_ = ''
            for text__content_ in child_.childNodes:
                Axis1LimitDefault_ += text__content_.nodeValue
            self.Axis1LimitDefault = Axis1LimitDefault_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Axis2LimitDefault':
            Axis2LimitDefault_ = ''
            for text__content_ in child_.childNodes:
                Axis2LimitDefault_ += text__content_.nodeValue
            self.Axis2LimitDefault = Axis2LimitDefault_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Axis3LimitDefault':
            Axis3LimitDefault_ = ''
            for text__content_ in child_.childNodes:
                Axis3LimitDefault_ += text__content_.nodeValue
            self.Axis3LimitDefault = Axis3LimitDefault_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Axis4LimitDefault':
            Axis4LimitDefault_ = ''
            for text__content_ in child_.childNodes:
                Axis4LimitDefault_ += text__content_.nodeValue
            self.Axis4LimitDefault = Axis4LimitDefault_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ParameterList':
            obj_ = ParameterList.factory()
            obj_.build(child_)
            self.setParameterlist(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'State':
            obj_ = State.factory()
            obj_.build(child_)
            self.State.append(obj_)
# end class States


class State:
    subclass = None
    def __init__(self, Position=None, Mneumonic='', Shorthand='', Concept='', NullInd='', Type='', NotionalDelq=''):
        self.Position = Position
        self.Mneumonic = Mneumonic
        self.Shorthand = Shorthand
        self.Concept = Concept
        self.NullInd = NullInd
        self.Type = Type
        self.NotionalDelq = NotionalDelq
    def factory(*args_, **kwargs_):
        if State.subclass:
            return State.subclass(*args_, **kwargs_)
        else:
            return State(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMneumonic(self): return self.Mneumonic
    def setMneumonic(self, Mneumonic): self.Mneumonic = Mneumonic
    def getShorthand(self): return self.Shorthand
    def setShorthand(self, Shorthand): self.Shorthand = Shorthand
    def getConcept(self): return self.Concept
    def setConcept(self, Concept): self.Concept = Concept
    def getNullind(self): return self.NullInd
    def setNullind(self, NullInd): self.NullInd = NullInd
    def getType(self): return self.Type
    def setType(self, Type): self.Type = Type
    def getNotionaldelq(self): return self.NotionalDelq
    def setNotionaldelq(self, NotionalDelq): self.NotionalDelq = NotionalDelq
    def getPosition(self): return self.Position
    def setPosition(self, Position): self.Position = Position
    def export(self, outfile, level, name_='State'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='State')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='State'):
        outfile.write(' Position="%s"' % (self.getPosition(), ))
    def exportChildren(self, outfile, level, name_='State'):
        showIndent(outfile, level)
        outfile.write('<Mneumonic>%s</Mneumonic>\n' % quote_xml(self.getMneumonic()))
        showIndent(outfile, level)
        outfile.write('<Shorthand>%s</Shorthand>\n' % quote_xml(self.getShorthand()))
        showIndent(outfile, level)
        outfile.write('<Concept>%s</Concept>\n' % quote_xml(self.getConcept()))
        showIndent(outfile, level)
        outfile.write('<NullInd>%s</NullInd>\n' % quote_xml(self.getNullind()))
        showIndent(outfile, level)
        outfile.write('<Type>%s</Type>\n' % quote_xml(self.getType()))
        showIndent(outfile, level)
        outfile.write('<NotionalDelq>%s</NotionalDelq>\n' % quote_xml(self.getNotionaldelq()))
    def exportLiteral(self, outfile, level, name_='State'):
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
        outfile.write('NullInd=%s,\n' % quote_python(self.getNullind()))
        showIndent(outfile, level)
        outfile.write('Type=%s,\n' % quote_python(self.getType()))
        showIndent(outfile, level)
        outfile.write('NotionalDelq=%s,\n' % quote_python(self.getNotionaldelq()))
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
            nodeName_ == 'NullInd':
            NullInd_ = ''
            for text__content_ in child_.childNodes:
                NullInd_ += text__content_.nodeValue
            self.NullInd = NullInd_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Type':
            Type_ = ''
            for text__content_ in child_.childNodes:
                Type_ += text__content_.nodeValue
            self.Type = Type_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NotionalDelq':
            NotionalDelq_ = ''
            for text__content_ in child_.childNodes:
                NotionalDelq_ += text__content_.nodeValue
            self.NotionalDelq = NotionalDelq_
# end class State


class Stages:
    subclass = None
    def __init__(self, Handle='', Number='', ParameterList=None, Stage=None):
        self.Handle = Handle
        self.Number = Number
        self.ParameterList = ParameterList
        if Stage is None:
            self.Stage = []
        else:
            self.Stage = Stage
    def factory(*args_, **kwargs_):
        if Stages.subclass:
            return Stages.subclass(*args_, **kwargs_)
        else:
            return Stages(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumber(self): return self.Number
    def setNumber(self, Number): self.Number = Number
    def getParameterlist(self): return self.ParameterList
    def setParameterlist(self, ParameterList): self.ParameterList = ParameterList
    def getStage(self): return self.Stage
    def setStage(self, Stage): self.Stage = Stage
    def addStage(self, value): self.Stage.append(value)
    def insertStage(self, index, value): self.Stage[index] = value
    def getHandle(self): return self.Handle
    def setHandle(self, Handle): self.Handle = Handle
    def export(self, outfile, level, name_='Stages'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='Stages')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='Stages'):
        outfile.write(' Handle="%s"' % (self.getHandle(), ))
    def exportChildren(self, outfile, level, name_='Stages'):
        showIndent(outfile, level)
        outfile.write('<Number>%s</Number>\n' % quote_xml(self.getNumber()))
        if self.ParameterList:
            self.ParameterList.export(outfile, level)
        for Stage_ in self.getStage():
            Stage_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='Stages'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Handle = "%s",\n' % (self.getHandle(),))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Number=%s,\n' % quote_python(self.getNumber()))
        if self.ParameterList:
            showIndent(outfile, level)
            outfile.write('ParameterList=ParameterList(\n')
            self.ParameterList.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Stage=[\n')
        level += 1
        for Stage in self.Stage:
            showIndent(outfile, level)
            outfile.write('Stage(\n')
            Stage.exportLiteral(outfile, level)
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
            nodeName_ == 'ParameterList':
            obj_ = ParameterList.factory()
            obj_.build(child_)
            self.setParameterlist(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Stage':
            obj_ = Stage.factory()
            obj_.build(child_)
            self.Stage.append(obj_)
# end class Stages


class Stage:
    subclass = None
    def __init__(self, Position=None, Mneumonic='', Shorthand='', Concept=''):
        self.Position = Position
        self.Mneumonic = Mneumonic
        self.Shorthand = Shorthand
        self.Concept = Concept
    def factory(*args_, **kwargs_):
        if Stage.subclass:
            return Stage.subclass(*args_, **kwargs_)
        else:
            return Stage(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getMneumonic(self): return self.Mneumonic
    def setMneumonic(self, Mneumonic): self.Mneumonic = Mneumonic
    def getShorthand(self): return self.Shorthand
    def setShorthand(self, Shorthand): self.Shorthand = Shorthand
    def getConcept(self): return self.Concept
    def setConcept(self, Concept): self.Concept = Concept
    def getPosition(self): return self.Position
    def setPosition(self, Position): self.Position = Position
    def export(self, outfile, level, name_='Stage'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='Stage')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='Stage'):
        outfile.write(' Position="%s"' % (self.getPosition(), ))
    def exportChildren(self, outfile, level, name_='Stage'):
        showIndent(outfile, level)
        outfile.write('<Mneumonic>%s</Mneumonic>\n' % quote_xml(self.getMneumonic()))
        showIndent(outfile, level)
        outfile.write('<Shorthand>%s</Shorthand>\n' % quote_xml(self.getShorthand()))
        showIndent(outfile, level)
        outfile.write('<Concept>%s</Concept>\n' % quote_xml(self.getConcept()))
    def exportLiteral(self, outfile, level, name_='Stage'):
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
# end class Stage


class Bridges:
    subclass = None
    def __init__(self, Handle='', Number='', ParameterList=None, Bridge=None):
        self.Handle = Handle
        self.Number = Number
        self.ParameterList = ParameterList
        if Bridge is None:
            self.Bridge = []
        else:
            self.Bridge = Bridge
    def factory(*args_, **kwargs_):
        if Bridges.subclass:
            return Bridges.subclass(*args_, **kwargs_)
        else:
            return Bridges(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumber(self): return self.Number
    def setNumber(self, Number): self.Number = Number
    def getParameterlist(self): return self.ParameterList
    def setParameterlist(self, ParameterList): self.ParameterList = ParameterList
    def getBridge(self): return self.Bridge
    def setBridge(self, Bridge): self.Bridge = Bridge
    def addBridge(self, value): self.Bridge.append(value)
    def insertBridge(self, index, value): self.Bridge[index] = value
    def getHandle(self): return self.Handle
    def setHandle(self, Handle): self.Handle = Handle
    def export(self, outfile, level, name_='Bridges'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='Bridges')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='Bridges'):
        outfile.write(' Handle="%s"' % (self.getHandle(), ))
    def exportChildren(self, outfile, level, name_='Bridges'):
        showIndent(outfile, level)
        outfile.write('<Number>%s</Number>\n' % quote_xml(self.getNumber()))
        if self.ParameterList:
            self.ParameterList.export(outfile, level)
        for Bridge_ in self.getBridge():
            Bridge_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='Bridges'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Handle = "%s",\n' % (self.getHandle(),))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Number=%s,\n' % quote_python(self.getNumber()))
        if self.ParameterList:
            showIndent(outfile, level)
            outfile.write('ParameterList=ParameterList(\n')
            self.ParameterList.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Bridge=[\n')
        level += 1
        for Bridge in self.Bridge:
            showIndent(outfile, level)
            outfile.write('Bridge(\n')
            Bridge.exportLiteral(outfile, level)
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
            nodeName_ == 'ParameterList':
            obj_ = ParameterList.factory()
            obj_.build(child_)
            self.setParameterlist(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Bridge':
            obj_ = Bridge.factory()
            obj_.build(child_)
            self.Bridge.append(obj_)
# end class Bridges


class Bridge:
    subclass = None
    def __init__(self, Position=None, StatePosition='', From='', To='', Type=''):
        self.Position = Position
        self.StatePosition = StatePosition
        self.From = From
        self.To = To
        self.Type = Type
    def factory(*args_, **kwargs_):
        if Bridge.subclass:
            return Bridge.subclass(*args_, **kwargs_)
        else:
            return Bridge(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getStateposition(self): return self.StatePosition
    def setStateposition(self, StatePosition): self.StatePosition = StatePosition
    def getFrom(self): return self.From
    def setFrom(self, From): self.From = From
    def getTo(self): return self.To
    def setTo(self, To): self.To = To
    def getType(self): return self.Type
    def setType(self, Type): self.Type = Type
    def getPosition(self): return self.Position
    def setPosition(self, Position): self.Position = Position
    def export(self, outfile, level, name_='Bridge'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='Bridge')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='Bridge'):
        outfile.write(' Position="%s"' % (self.getPosition(), ))
    def exportChildren(self, outfile, level, name_='Bridge'):
        showIndent(outfile, level)
        outfile.write('<StatePosition>%s</StatePosition>\n' % quote_xml(self.getStateposition()))
        showIndent(outfile, level)
        outfile.write('<From>%s</From>\n' % quote_xml(self.getFrom()))
        showIndent(outfile, level)
        outfile.write('<To>%s</To>\n' % quote_xml(self.getTo()))
        showIndent(outfile, level)
        outfile.write('<Type>%s</Type>\n' % quote_xml(self.getType()))
    def exportLiteral(self, outfile, level, name_='Bridge'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Position = "%s",\n' % (self.getPosition(),))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('StatePosition=%s,\n' % quote_python(self.getStateposition()))
        showIndent(outfile, level)
        outfile.write('From=%s,\n' % quote_python(self.getFrom()))
        showIndent(outfile, level)
        outfile.write('To=%s,\n' % quote_python(self.getTo()))
        showIndent(outfile, level)
        outfile.write('Type=%s,\n' % quote_python(self.getType()))
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
            nodeName_ == 'StatePosition':
            StatePosition_ = ''
            for text__content_ in child_.childNodes:
                StatePosition_ += text__content_.nodeValue
            self.StatePosition = StatePosition_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'From':
            From_ = ''
            for text__content_ in child_.childNodes:
                From_ += text__content_.nodeValue
            self.From = From_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'To':
            To_ = ''
            for text__content_ in child_.childNodes:
                To_ += text__content_.nodeValue
            self.To = To_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Type':
            Type_ = ''
            for text__content_ in child_.childNodes:
                Type_ += text__content_.nodeValue
            self.Type = Type_
# end class Bridge


from xml.sax import handler, make_parser

class SaxStackElement:
    def __init__(self, name='', obj=None):
        self.name = name
        self.obj = obj
        self.content = ''

#
# SAX handler
#
class SaxSmstatespaceHandler(handler.ContentHandler):
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
        if name == 'SMStateSpace':
            obj = SMStateSpace.factory()
            stackObj = SaxStackElement('SMStateSpace', obj)
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
        elif name == 'States':
            obj = States.factory()
            val = attrs.get('Handle', None)
            if val is not None:
                obj.setHandle(val)
            stackObj = SaxStackElement('States', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Number':
            stackObj = SaxStackElement('Number', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NumberOfBaseDimensions':
            stackObj = SaxStackElement('NumberOfBaseDimensions', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NumberOfAgePages':
            stackObj = SaxStackElement('NumberOfAgePages', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Axis1LimitDefault':
            stackObj = SaxStackElement('Axis1LimitDefault', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Axis2LimitDefault':
            stackObj = SaxStackElement('Axis2LimitDefault', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Axis3LimitDefault':
            stackObj = SaxStackElement('Axis3LimitDefault', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Axis4LimitDefault':
            stackObj = SaxStackElement('Axis4LimitDefault', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'State':
            obj = State.factory()
            val = attrs.get('Position', None)
            if val is not None:
                obj.setPosition(val)
            stackObj = SaxStackElement('State', obj)
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
        elif name == 'NullInd':
            stackObj = SaxStackElement('NullInd', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Type':
            stackObj = SaxStackElement('Type', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NotionalDelq':
            stackObj = SaxStackElement('NotionalDelq', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Stages':
            obj = Stages.factory()
            val = attrs.get('Handle', None)
            if val is not None:
                obj.setHandle(val)
            stackObj = SaxStackElement('Stages', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Stage':
            obj = Stage.factory()
            val = attrs.get('Position', None)
            if val is not None:
                obj.setPosition(val)
            stackObj = SaxStackElement('Stage', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Bridges':
            obj = Bridges.factory()
            val = attrs.get('Handle', None)
            if val is not None:
                obj.setHandle(val)
            stackObj = SaxStackElement('Bridges', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Bridge':
            obj = Bridge.factory()
            val = attrs.get('Position', None)
            if val is not None:
                obj.setPosition(val)
            stackObj = SaxStackElement('Bridge', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'StatePosition':
            stackObj = SaxStackElement('StatePosition', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'From':
            stackObj = SaxStackElement('From', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'To':
            stackObj = SaxStackElement('To', None)
            self.stack.append(stackObj)
            done = 1
        if not done:
            self.reportError('"%s" element not allowed here.' % name)

    def endElement(self, name):
        done = 0
        if name == 'SMStateSpace':
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
        elif name == 'States':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStates(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Number':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNumber(content)
                self.stack.pop()
                done = 1
        elif name == 'NumberOfBaseDimensions':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNumberofbasedimensions(content)
                self.stack.pop()
                done = 1
        elif name == 'NumberOfAgePages':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNumberofagepages(content)
                self.stack.pop()
                done = 1
        elif name == 'Axis1LimitDefault':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setAxis1limitdefault(content)
                self.stack.pop()
                done = 1
        elif name == 'Axis2LimitDefault':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setAxis2limitdefault(content)
                self.stack.pop()
                done = 1
        elif name == 'Axis3LimitDefault':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setAxis3limitdefault(content)
                self.stack.pop()
                done = 1
        elif name == 'Axis4LimitDefault':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setAxis4limitdefault(content)
                self.stack.pop()
                done = 1
        elif name == 'State':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addState(self.stack[-1].obj)
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
        elif name == 'NullInd':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNullind(content)
                self.stack.pop()
                done = 1
        elif name == 'Type':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setType(content)
                self.stack.pop()
                done = 1
        elif name == 'NotionalDelq':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNotionaldelq(content)
                self.stack.pop()
                done = 1
        elif name == 'Stages':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setStages(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Stage':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addStage(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Bridges':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBridges(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Bridge':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addBridge(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'StatePosition':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setStateposition(content)
                self.stack.pop()
                done = 1
        elif name == 'From':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setFrom(content)
                self.stack.pop()
                done = 1
        elif name == 'To':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setTo(content)
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
    documentHandler = SaxSmstatespaceHandler()
    parser.setDocumentHandler(documentHandler)
    parser.parse('file:%s' % inFileName)
    root = documentHandler.getRoot()
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    root.export(sys.stdout, 0)
    return root


def saxParseString(inString):
    parser = make_parser()
    documentHandler = SaxSmstatespaceHandler()
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
    rootObj = SMStateSpace.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0, name_="SMStateSpace")
    return rootObj


def parseString(inString):
    doc = minidom.parseString(inString)
    rootNode = doc.documentElement
    rootObj = SMStateSpace.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0, name_="SMStateSpace")
    return rootObj


def parseLiteral(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = SMStateSpace.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('from gSMStateSpaceSpec.py import *\n\n')
    #sys.stdout.write('rootObj = SMStateSpace(\n')
    #rootObj.exportLiteral(sys.stdout, 0, name_="SMStateSpace")
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

