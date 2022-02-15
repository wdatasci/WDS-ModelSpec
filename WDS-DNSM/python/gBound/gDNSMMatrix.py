#!/usr/bin/env python

#
# Generated Thu Nov 01 16:22:30 2007 by generateDS.py.
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

class SMMatrix:
    subclass = None
    def __init__(self, Name='', NumberOfStates='', NumberOfAdditionalAxes='', ProvidesNonZeroCoords='', AdditionalAxesUpperLimits=None, AdditionalAxesLowerLimits=None, StateLabels=None, NonZeroElements=None, MData=None):
        self.Name = Name
        self.NumberOfStates = NumberOfStates
        self.NumberOfAdditionalAxes = NumberOfAdditionalAxes
        self.ProvidesNonZeroCoords = ProvidesNonZeroCoords
        self.AdditionalAxesUpperLimits = AdditionalAxesUpperLimits
        self.AdditionalAxesLowerLimits = AdditionalAxesLowerLimits
        self.StateLabels = StateLabels
        self.NonZeroElements = NonZeroElements
        if MData is None:
            self.MData = []
        else:
            self.MData = MData
    def factory(*args_, **kwargs_):
        if SMMatrix.subclass:
            return SMMatrix.subclass(*args_, **kwargs_)
        else:
            return SMMatrix(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumberofstates(self): return self.NumberOfStates
    def setNumberofstates(self, NumberOfStates): self.NumberOfStates = NumberOfStates
    def getNumberofadditionalaxes(self): return self.NumberOfAdditionalAxes
    def setNumberofadditionalaxes(self, NumberOfAdditionalAxes): self.NumberOfAdditionalAxes = NumberOfAdditionalAxes
    def getProvidesnonzerocoords(self): return self.ProvidesNonZeroCoords
    def setProvidesnonzerocoords(self, ProvidesNonZeroCoords): self.ProvidesNonZeroCoords = ProvidesNonZeroCoords
    def getAdditionalaxesupperlimits(self): return self.AdditionalAxesUpperLimits
    def setAdditionalaxesupperlimits(self, AdditionalAxesUpperLimits): self.AdditionalAxesUpperLimits = AdditionalAxesUpperLimits
    def getAdditionalaxeslowerlimits(self): return self.AdditionalAxesLowerLimits
    def setAdditionalaxeslowerlimits(self, AdditionalAxesLowerLimits): self.AdditionalAxesLowerLimits = AdditionalAxesLowerLimits
    def getStatelabels(self): return self.StateLabels
    def setStatelabels(self, StateLabels): self.StateLabels = StateLabels
    def getNonzeroelements(self): return self.NonZeroElements
    def setNonzeroelements(self, NonZeroElements): self.NonZeroElements = NonZeroElements
    def getMdata(self): return self.MData
    def setMdata(self, MData): self.MData = MData
    def addMdata(self, value): self.MData.append(value)
    def insertMdata(self, index, value): self.MData[index] = value
    def getName(self): return self.Name
    def setName(self, Name): self.Name = Name
    def export(self, outfile, level, name_='SMMatrix'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='SMMatrix')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='SMMatrix'):
        outfile.write(' Name="%s"' % (self.getName(), ))
    def exportChildren(self, outfile, level, name_='SMMatrix'):
        showIndent(outfile, level)
        outfile.write('<NumberOfStates>%s</NumberOfStates>\n' % quote_xml(self.getNumberofstates()))
        showIndent(outfile, level)
        outfile.write('<NumberOfAdditionalAxes>%s</NumberOfAdditionalAxes>\n' % quote_xml(self.getNumberofadditionalaxes()))
        showIndent(outfile, level)
        outfile.write('<ProvidesNonZeroCoords>%s</ProvidesNonZeroCoords>\n' % quote_xml(self.getProvidesnonzerocoords()))
        if self.AdditionalAxesUpperLimits:
            self.AdditionalAxesUpperLimits.export(outfile, level)
        if self.AdditionalAxesLowerLimits:
            self.AdditionalAxesLowerLimits.export(outfile, level)
        if self.StateLabels:
            self.StateLabels.export(outfile, level)
        if self.NonZeroElements:
            self.NonZeroElements.export(outfile, level)
        for MData_ in self.getMdata():
            MData_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='SMMatrix'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Name = "%s",\n' % (self.getName(),))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('NumberOfStates=%s,\n' % quote_python(self.getNumberofstates()))
        showIndent(outfile, level)
        outfile.write('NumberOfAdditionalAxes=%s,\n' % quote_python(self.getNumberofadditionalaxes()))
        showIndent(outfile, level)
        outfile.write('ProvidesNonZeroCoords=%s,\n' % quote_python(self.getProvidesnonzerocoords()))
        if self.AdditionalAxesUpperLimits:
            showIndent(outfile, level)
            outfile.write('AdditionalAxesUpperLimits=AdditionalAxesUpperLimits(\n')
            self.AdditionalAxesUpperLimits.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.AdditionalAxesLowerLimits:
            showIndent(outfile, level)
            outfile.write('AdditionalAxesLowerLimits=AdditionalAxesLowerLimits(\n')
            self.AdditionalAxesLowerLimits.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.StateLabels:
            showIndent(outfile, level)
            outfile.write('StateLabels=StateLabels(\n')
            self.StateLabels.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.NonZeroElements:
            showIndent(outfile, level)
            outfile.write('NonZeroElements=NonZeroElements(\n')
            self.NonZeroElements.exportLiteral(outfile, level)
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
        if attrs.get('Name'):
            self.Name = attrs.get('Name').value
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NumberOfStates':
            NumberOfStates_ = ''
            for text__content_ in child_.childNodes:
                NumberOfStates_ += text__content_.nodeValue
            self.NumberOfStates = NumberOfStates_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NumberOfAdditionalAxes':
            NumberOfAdditionalAxes_ = ''
            for text__content_ in child_.childNodes:
                NumberOfAdditionalAxes_ += text__content_.nodeValue
            self.NumberOfAdditionalAxes = NumberOfAdditionalAxes_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ProvidesNonZeroCoords':
            ProvidesNonZeroCoords_ = ''
            for text__content_ in child_.childNodes:
                ProvidesNonZeroCoords_ += text__content_.nodeValue
            self.ProvidesNonZeroCoords = ProvidesNonZeroCoords_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'AdditionalAxesUpperLimits':
            obj_ = AdditionalAxesUpperLimits.factory()
            obj_.build(child_)
            self.setAdditionalaxesupperlimits(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'AdditionalAxesLowerLimits':
            obj_ = AdditionalAxesLowerLimits.factory()
            obj_.build(child_)
            self.setAdditionalaxeslowerlimits(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'StateLabels':
            obj_ = StateLabels.factory()
            obj_.build(child_)
            self.setStatelabels(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NonZeroElements':
            obj_ = NonZeroElements.factory()
            obj_.build(child_)
            self.setNonzeroelements(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'MData':
            obj_ = MData.factory()
            obj_.build(child_)
            self.MData.append(obj_)
# end class SMMatrix


class AdditionalAxesUpperLimits:
    subclass = None
    def __init__(self, Axis1='', Axis2='', Axis3='', Axis4=''):
        self.Axis1 = Axis1
        self.Axis2 = Axis2
        self.Axis3 = Axis3
        self.Axis4 = Axis4
    def factory(*args_, **kwargs_):
        if AdditionalAxesUpperLimits.subclass:
            return AdditionalAxesUpperLimits.subclass(*args_, **kwargs_)
        else:
            return AdditionalAxesUpperLimits(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getAxis1(self): return self.Axis1
    def setAxis1(self, Axis1): self.Axis1 = Axis1
    def getAxis2(self): return self.Axis2
    def setAxis2(self, Axis2): self.Axis2 = Axis2
    def getAxis3(self): return self.Axis3
    def setAxis3(self, Axis3): self.Axis3 = Axis3
    def getAxis4(self): return self.Axis4
    def setAxis4(self, Axis4): self.Axis4 = Axis4
    def export(self, outfile, level, name_='AdditionalAxesUpperLimits'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='AdditionalAxesUpperLimits'):
        pass
    def exportChildren(self, outfile, level, name_='AdditionalAxesUpperLimits'):
        showIndent(outfile, level)
        outfile.write('<Axis1>%s</Axis1>\n' % quote_xml(self.getAxis1()))
        showIndent(outfile, level)
        outfile.write('<Axis2>%s</Axis2>\n' % quote_xml(self.getAxis2()))
        showIndent(outfile, level)
        outfile.write('<Axis3>%s</Axis3>\n' % quote_xml(self.getAxis3()))
        showIndent(outfile, level)
        outfile.write('<Axis4>%s</Axis4>\n' % quote_xml(self.getAxis4()))
    def exportLiteral(self, outfile, level, name_='AdditionalAxesUpperLimits'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Axis1=%s,\n' % quote_python(self.getAxis1()))
        showIndent(outfile, level)
        outfile.write('Axis2=%s,\n' % quote_python(self.getAxis2()))
        showIndent(outfile, level)
        outfile.write('Axis3=%s,\n' % quote_python(self.getAxis3()))
        showIndent(outfile, level)
        outfile.write('Axis4=%s,\n' % quote_python(self.getAxis4()))
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
            nodeName_ == 'Axis1':
            Axis1_ = ''
            for text__content_ in child_.childNodes:
                Axis1_ += text__content_.nodeValue
            self.Axis1 = Axis1_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Axis2':
            Axis2_ = ''
            for text__content_ in child_.childNodes:
                Axis2_ += text__content_.nodeValue
            self.Axis2 = Axis2_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Axis3':
            Axis3_ = ''
            for text__content_ in child_.childNodes:
                Axis3_ += text__content_.nodeValue
            self.Axis3 = Axis3_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Axis4':
            Axis4_ = ''
            for text__content_ in child_.childNodes:
                Axis4_ += text__content_.nodeValue
            self.Axis4 = Axis4_
# end class AdditionalAxesUpperLimits


class AdditionalAxesLowerLimits:
    subclass = None
    def __init__(self, Axis1='', Axis2='', Axis3='', Axis4=''):
        self.Axis1 = Axis1
        self.Axis2 = Axis2
        self.Axis3 = Axis3
        self.Axis4 = Axis4
    def factory(*args_, **kwargs_):
        if AdditionalAxesLowerLimits.subclass:
            return AdditionalAxesLowerLimits.subclass(*args_, **kwargs_)
        else:
            return AdditionalAxesLowerLimits(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getAxis1(self): return self.Axis1
    def setAxis1(self, Axis1): self.Axis1 = Axis1
    def getAxis2(self): return self.Axis2
    def setAxis2(self, Axis2): self.Axis2 = Axis2
    def getAxis3(self): return self.Axis3
    def setAxis3(self, Axis3): self.Axis3 = Axis3
    def getAxis4(self): return self.Axis4
    def setAxis4(self, Axis4): self.Axis4 = Axis4
    def export(self, outfile, level, name_='AdditionalAxesLowerLimits'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='AdditionalAxesLowerLimits'):
        pass
    def exportChildren(self, outfile, level, name_='AdditionalAxesLowerLimits'):
        showIndent(outfile, level)
        outfile.write('<Axis1>%s</Axis1>\n' % quote_xml(self.getAxis1()))
        showIndent(outfile, level)
        outfile.write('<Axis2>%s</Axis2>\n' % quote_xml(self.getAxis2()))
        showIndent(outfile, level)
        outfile.write('<Axis3>%s</Axis3>\n' % quote_xml(self.getAxis3()))
        showIndent(outfile, level)
        outfile.write('<Axis4>%s</Axis4>\n' % quote_xml(self.getAxis4()))
    def exportLiteral(self, outfile, level, name_='AdditionalAxesLowerLimits'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Axis1=%s,\n' % quote_python(self.getAxis1()))
        showIndent(outfile, level)
        outfile.write('Axis2=%s,\n' % quote_python(self.getAxis2()))
        showIndent(outfile, level)
        outfile.write('Axis3=%s,\n' % quote_python(self.getAxis3()))
        showIndent(outfile, level)
        outfile.write('Axis4=%s,\n' % quote_python(self.getAxis4()))
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
            nodeName_ == 'Axis1':
            Axis1_ = ''
            for text__content_ in child_.childNodes:
                Axis1_ += text__content_.nodeValue
            self.Axis1 = Axis1_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Axis2':
            Axis2_ = ''
            for text__content_ in child_.childNodes:
                Axis2_ += text__content_.nodeValue
            self.Axis2 = Axis2_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Axis3':
            Axis3_ = ''
            for text__content_ in child_.childNodes:
                Axis3_ += text__content_.nodeValue
            self.Axis3 = Axis3_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Axis4':
            Axis4_ = ''
            for text__content_ in child_.childNodes:
                Axis4_ += text__content_.nodeValue
            self.Axis4 = Axis4_
# end class AdditionalAxesLowerLimits


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


class NonZeroElements:
    subclass = None
    def __init__(self, Number='', NonZeroCoordinates=None):
        self.Number = Number
        self.NonZeroCoordinates = NonZeroCoordinates
    def factory(*args_, **kwargs_):
        if NonZeroElements.subclass:
            return NonZeroElements.subclass(*args_, **kwargs_)
        else:
            return NonZeroElements(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumber(self): return self.Number
    def setNumber(self, Number): self.Number = Number
    def getNonzerocoordinates(self): return self.NonZeroCoordinates
    def setNonzerocoordinates(self, NonZeroCoordinates): self.NonZeroCoordinates = NonZeroCoordinates
    def export(self, outfile, level, name_='NonZeroElements'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='NonZeroElements'):
        pass
    def exportChildren(self, outfile, level, name_='NonZeroElements'):
        showIndent(outfile, level)
        outfile.write('<Number>%s</Number>\n' % quote_xml(self.getNumber()))
        if self.NonZeroCoordinates:
            self.NonZeroCoordinates.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='NonZeroElements'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Number=%s,\n' % quote_python(self.getNumber()))
        if self.NonZeroCoordinates:
            showIndent(outfile, level)
            outfile.write('NonZeroCoordinates=NonZeroCoordinates(\n')
            self.NonZeroCoordinates.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
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
            nodeName_ == 'Number':
            Number_ = ''
            for text__content_ in child_.childNodes:
                Number_ += text__content_.nodeValue
            self.Number = Number_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NonZeroCoordinates':
            obj_ = NonZeroCoordinates.factory()
            obj_.build(child_)
            self.setNonzerocoordinates(obj_)
# end class NonZeroElements


class NonZeroCoordinates:
    subclass = None
    def __init__(self, NonZeroCoordinate=None):
        if NonZeroCoordinate is None:
            self.NonZeroCoordinate = []
        else:
            self.NonZeroCoordinate = NonZeroCoordinate
    def factory(*args_, **kwargs_):
        if NonZeroCoordinates.subclass:
            return NonZeroCoordinates.subclass(*args_, **kwargs_)
        else:
            return NonZeroCoordinates(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNonzerocoordinate(self): return self.NonZeroCoordinate
    def setNonzerocoordinate(self, NonZeroCoordinate): self.NonZeroCoordinate = NonZeroCoordinate
    def addNonzerocoordinate(self, value): self.NonZeroCoordinate.append(value)
    def insertNonzerocoordinate(self, index, value): self.NonZeroCoordinate[index] = value
    def export(self, outfile, level, name_='NonZeroCoordinates'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='NonZeroCoordinates'):
        pass
    def exportChildren(self, outfile, level, name_='NonZeroCoordinates'):
        for NonZeroCoordinate_ in self.getNonzerocoordinate():
            NonZeroCoordinate_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='NonZeroCoordinates'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('NonZeroCoordinate=[\n')
        level += 1
        for NonZeroCoordinate in self.NonZeroCoordinate:
            showIndent(outfile, level)
            outfile.write('NonZeroCoordinate(\n')
            NonZeroCoordinate.exportLiteral(outfile, level)
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
            nodeName_ == 'NonZeroCoordinate':
            obj_ = NonZeroCoordinate.factory()
            obj_.build(child_)
            self.NonZeroCoordinate.append(obj_)
# end class NonZeroCoordinates


class NonZeroCoordinate:
    subclass = None
    def __init__(self, Position=None, I='', J=''):
        self.Position = Position
        self.I = I
        self.J = J
    def factory(*args_, **kwargs_):
        if NonZeroCoordinate.subclass:
            return NonZeroCoordinate.subclass(*args_, **kwargs_)
        else:
            return NonZeroCoordinate(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getI(self): return self.I
    def setI(self, I): self.I = I
    def getJ(self): return self.J
    def setJ(self, J): self.J = J
    def getPosition(self): return self.Position
    def setPosition(self, Position): self.Position = Position
    def export(self, outfile, level, name_='NonZeroCoordinate'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='NonZeroCoordinate')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='NonZeroCoordinate'):
        outfile.write(' Position="%s"' % (self.getPosition(), ))
    def exportChildren(self, outfile, level, name_='NonZeroCoordinate'):
        showIndent(outfile, level)
        outfile.write('<I>%s</I>\n' % quote_xml(self.getI()))
        showIndent(outfile, level)
        outfile.write('<J>%s</J>\n' % quote_xml(self.getJ()))
    def exportLiteral(self, outfile, level, name_='NonZeroCoordinate'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Position = "%s",\n' % (self.getPosition(),))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('I=%s,\n' % quote_python(self.getI()))
        showIndent(outfile, level)
        outfile.write('J=%s,\n' % quote_python(self.getJ()))
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
            nodeName_ == 'I':
            I_ = ''
            for text__content_ in child_.childNodes:
                I_ += text__content_.nodeValue
            self.I = I_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'J':
            J_ = ''
            for text__content_ in child_.childNodes:
                J_ += text__content_.nodeValue
            self.J = J_
# end class NonZeroCoordinate


class MData:
    subclass = None
    def __init__(self, Axis4=None, Axis3=None, Axis1=None, Axis2=None, Row=None, Col1=0.0, Col2=0.0, Col3=0.0, Col4=0.0, Col5=0.0, Col6=0.0, Col7=0.0, Col8=0.0, Col9=0.0, Col10=0.0, Col11=0.0, Col12=0.0, Col13=0.0, Col14=0.0, Col15=0.0, Col16=0.0, Col17=0.0, Col18=0.0, Col19=0.0, Col20=0.0, Col21=0.0, Col22=0.0, Col23=0.0, Col24=0.0, Col25=0.0, Col26=0.0, Col27=0.0, Col28=0.0, Col29=0.0, Col30=0.0, Col31=0.0, Col32=0.0, Col33=0.0, Col34=0.0, Col35=0.0, Col36=0.0, Col37=0.0, Col38=0.0, Col39=0.0, Col40=0.0, Col41=0.0, Col42=0.0, Col43=0.0, Col44=0.0, Col45=0.0, Col46=0.0, Col47=0.0, Col48=0.0, Col49=0.0, Col50=0.0, Col51=0.0, Col52=0.0, Col53=0.0, Col54=0.0, Col55=0.0, Col56=0.0, Col57=0.0, Col58=0.0, Col59=0.0, Col60=0.0, Col61=0.0, Col62=0.0, Col63=0.0, Col64=0.0):
        self.Axis4 = Axis4
        self.Axis3 = Axis3
        self.Axis1 = Axis1
        self.Axis2 = Axis2
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
    def getAxis4(self): return self.Axis4
    def setAxis4(self, Axis4): self.Axis4 = Axis4
    def getAxis3(self): return self.Axis3
    def setAxis3(self, Axis3): self.Axis3 = Axis3
    def getAxis1(self): return self.Axis1
    def setAxis1(self, Axis1): self.Axis1 = Axis1
    def getAxis2(self): return self.Axis2
    def setAxis2(self, Axis2): self.Axis2 = Axis2
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
        outfile.write(' Axis4="%s"' % (self.getAxis4(), ))
        outfile.write(' Axis3="%s"' % (self.getAxis3(), ))
        outfile.write(' Axis1="%s"' % (self.getAxis1(), ))
        outfile.write(' Axis2="%s"' % (self.getAxis2(), ))
        outfile.write(' Row="%s"' % (self.getRow(), ))
    def exportChildren(self, outfile, level, name_='MData'):
        showIndent(outfile, level)
        outfile.write('<Col1>%e</Col1>\n' % self.getCol1())
        showIndent(outfile, level)
        outfile.write('<Col2>%e</Col2>\n' % self.getCol2())
        showIndent(outfile, level)
        outfile.write('<Col3>%e</Col3>\n' % self.getCol3())
        showIndent(outfile, level)
        outfile.write('<Col4>%e</Col4>\n' % self.getCol4())
        showIndent(outfile, level)
        outfile.write('<Col5>%e</Col5>\n' % self.getCol5())
        showIndent(outfile, level)
        outfile.write('<Col6>%e</Col6>\n' % self.getCol6())
        showIndent(outfile, level)
        outfile.write('<Col7>%e</Col7>\n' % self.getCol7())
        showIndent(outfile, level)
        outfile.write('<Col8>%e</Col8>\n' % self.getCol8())
        showIndent(outfile, level)
        outfile.write('<Col9>%e</Col9>\n' % self.getCol9())
        showIndent(outfile, level)
        outfile.write('<Col10>%e</Col10>\n' % self.getCol10())
        showIndent(outfile, level)
        outfile.write('<Col11>%e</Col11>\n' % self.getCol11())
        showIndent(outfile, level)
        outfile.write('<Col12>%e</Col12>\n' % self.getCol12())
        showIndent(outfile, level)
        outfile.write('<Col13>%e</Col13>\n' % self.getCol13())
        showIndent(outfile, level)
        outfile.write('<Col14>%e</Col14>\n' % self.getCol14())
        showIndent(outfile, level)
        outfile.write('<Col15>%e</Col15>\n' % self.getCol15())
        showIndent(outfile, level)
        outfile.write('<Col16>%e</Col16>\n' % self.getCol16())
        showIndent(outfile, level)
        outfile.write('<Col17>%e</Col17>\n' % self.getCol17())
        showIndent(outfile, level)
        outfile.write('<Col18>%e</Col18>\n' % self.getCol18())
        showIndent(outfile, level)
        outfile.write('<Col19>%e</Col19>\n' % self.getCol19())
        showIndent(outfile, level)
        outfile.write('<Col20>%e</Col20>\n' % self.getCol20())
        showIndent(outfile, level)
        outfile.write('<Col21>%e</Col21>\n' % self.getCol21())
        showIndent(outfile, level)
        outfile.write('<Col22>%e</Col22>\n' % self.getCol22())
        showIndent(outfile, level)
        outfile.write('<Col23>%e</Col23>\n' % self.getCol23())
        showIndent(outfile, level)
        outfile.write('<Col24>%e</Col24>\n' % self.getCol24())
        showIndent(outfile, level)
        outfile.write('<Col25>%e</Col25>\n' % self.getCol25())
        showIndent(outfile, level)
        outfile.write('<Col26>%e</Col26>\n' % self.getCol26())
        showIndent(outfile, level)
        outfile.write('<Col27>%e</Col27>\n' % self.getCol27())
        showIndent(outfile, level)
        outfile.write('<Col28>%e</Col28>\n' % self.getCol28())
        showIndent(outfile, level)
        outfile.write('<Col29>%e</Col29>\n' % self.getCol29())
        showIndent(outfile, level)
        outfile.write('<Col30>%e</Col30>\n' % self.getCol30())
        showIndent(outfile, level)
        outfile.write('<Col31>%e</Col31>\n' % self.getCol31())
        showIndent(outfile, level)
        outfile.write('<Col32>%e</Col32>\n' % self.getCol32())
        showIndent(outfile, level)
        outfile.write('<Col33>%e</Col33>\n' % self.getCol33())
        showIndent(outfile, level)
        outfile.write('<Col34>%e</Col34>\n' % self.getCol34())
        showIndent(outfile, level)
        outfile.write('<Col35>%e</Col35>\n' % self.getCol35())
        showIndent(outfile, level)
        outfile.write('<Col36>%e</Col36>\n' % self.getCol36())
        showIndent(outfile, level)
        outfile.write('<Col37>%e</Col37>\n' % self.getCol37())
        showIndent(outfile, level)
        outfile.write('<Col38>%e</Col38>\n' % self.getCol38())
        showIndent(outfile, level)
        outfile.write('<Col39>%e</Col39>\n' % self.getCol39())
        showIndent(outfile, level)
        outfile.write('<Col40>%e</Col40>\n' % self.getCol40())
        showIndent(outfile, level)
        outfile.write('<Col41>%e</Col41>\n' % self.getCol41())
        showIndent(outfile, level)
        outfile.write('<Col42>%e</Col42>\n' % self.getCol42())
        showIndent(outfile, level)
        outfile.write('<Col43>%e</Col43>\n' % self.getCol43())
        showIndent(outfile, level)
        outfile.write('<Col44>%e</Col44>\n' % self.getCol44())
        showIndent(outfile, level)
        outfile.write('<Col45>%e</Col45>\n' % self.getCol45())
        showIndent(outfile, level)
        outfile.write('<Col46>%e</Col46>\n' % self.getCol46())
        showIndent(outfile, level)
        outfile.write('<Col47>%e</Col47>\n' % self.getCol47())
        showIndent(outfile, level)
        outfile.write('<Col48>%e</Col48>\n' % self.getCol48())
        showIndent(outfile, level)
        outfile.write('<Col49>%e</Col49>\n' % self.getCol49())
        showIndent(outfile, level)
        outfile.write('<Col50>%e</Col50>\n' % self.getCol50())
        showIndent(outfile, level)
        outfile.write('<Col51>%e</Col51>\n' % self.getCol51())
        showIndent(outfile, level)
        outfile.write('<Col52>%e</Col52>\n' % self.getCol52())
        showIndent(outfile, level)
        outfile.write('<Col53>%e</Col53>\n' % self.getCol53())
        showIndent(outfile, level)
        outfile.write('<Col54>%e</Col54>\n' % self.getCol54())
        showIndent(outfile, level)
        outfile.write('<Col55>%e</Col55>\n' % self.getCol55())
        showIndent(outfile, level)
        outfile.write('<Col56>%e</Col56>\n' % self.getCol56())
        showIndent(outfile, level)
        outfile.write('<Col57>%e</Col57>\n' % self.getCol57())
        showIndent(outfile, level)
        outfile.write('<Col58>%e</Col58>\n' % self.getCol58())
        showIndent(outfile, level)
        outfile.write('<Col59>%e</Col59>\n' % self.getCol59())
        showIndent(outfile, level)
        outfile.write('<Col60>%e</Col60>\n' % self.getCol60())
        showIndent(outfile, level)
        outfile.write('<Col61>%e</Col61>\n' % self.getCol61())
        showIndent(outfile, level)
        outfile.write('<Col62>%e</Col62>\n' % self.getCol62())
        showIndent(outfile, level)
        outfile.write('<Col63>%e</Col63>\n' % self.getCol63())
        showIndent(outfile, level)
        outfile.write('<Col64>%e</Col64>\n' % self.getCol64())
    def exportLiteral(self, outfile, level, name_='MData'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Axis4 = "%s",\n' % (self.getAxis4(),))
        showIndent(outfile, level)
        outfile.write('Axis3 = "%s",\n' % (self.getAxis3(),))
        showIndent(outfile, level)
        outfile.write('Axis1 = "%s",\n' % (self.getAxis1(),))
        showIndent(outfile, level)
        outfile.write('Axis2 = "%s",\n' % (self.getAxis2(),))
        showIndent(outfile, level)
        outfile.write('Row = "%s",\n' % (self.getRow(),))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Col1=%e,\n' % self.getCol1())
        showIndent(outfile, level)
        outfile.write('Col2=%e,\n' % self.getCol2())
        showIndent(outfile, level)
        outfile.write('Col3=%e,\n' % self.getCol3())
        showIndent(outfile, level)
        outfile.write('Col4=%e,\n' % self.getCol4())
        showIndent(outfile, level)
        outfile.write('Col5=%e,\n' % self.getCol5())
        showIndent(outfile, level)
        outfile.write('Col6=%e,\n' % self.getCol6())
        showIndent(outfile, level)
        outfile.write('Col7=%e,\n' % self.getCol7())
        showIndent(outfile, level)
        outfile.write('Col8=%e,\n' % self.getCol8())
        showIndent(outfile, level)
        outfile.write('Col9=%e,\n' % self.getCol9())
        showIndent(outfile, level)
        outfile.write('Col10=%e,\n' % self.getCol10())
        showIndent(outfile, level)
        outfile.write('Col11=%e,\n' % self.getCol11())
        showIndent(outfile, level)
        outfile.write('Col12=%e,\n' % self.getCol12())
        showIndent(outfile, level)
        outfile.write('Col13=%e,\n' % self.getCol13())
        showIndent(outfile, level)
        outfile.write('Col14=%e,\n' % self.getCol14())
        showIndent(outfile, level)
        outfile.write('Col15=%e,\n' % self.getCol15())
        showIndent(outfile, level)
        outfile.write('Col16=%e,\n' % self.getCol16())
        showIndent(outfile, level)
        outfile.write('Col17=%e,\n' % self.getCol17())
        showIndent(outfile, level)
        outfile.write('Col18=%e,\n' % self.getCol18())
        showIndent(outfile, level)
        outfile.write('Col19=%e,\n' % self.getCol19())
        showIndent(outfile, level)
        outfile.write('Col20=%e,\n' % self.getCol20())
        showIndent(outfile, level)
        outfile.write('Col21=%e,\n' % self.getCol21())
        showIndent(outfile, level)
        outfile.write('Col22=%e,\n' % self.getCol22())
        showIndent(outfile, level)
        outfile.write('Col23=%e,\n' % self.getCol23())
        showIndent(outfile, level)
        outfile.write('Col24=%e,\n' % self.getCol24())
        showIndent(outfile, level)
        outfile.write('Col25=%e,\n' % self.getCol25())
        showIndent(outfile, level)
        outfile.write('Col26=%e,\n' % self.getCol26())
        showIndent(outfile, level)
        outfile.write('Col27=%e,\n' % self.getCol27())
        showIndent(outfile, level)
        outfile.write('Col28=%e,\n' % self.getCol28())
        showIndent(outfile, level)
        outfile.write('Col29=%e,\n' % self.getCol29())
        showIndent(outfile, level)
        outfile.write('Col30=%e,\n' % self.getCol30())
        showIndent(outfile, level)
        outfile.write('Col31=%e,\n' % self.getCol31())
        showIndent(outfile, level)
        outfile.write('Col32=%e,\n' % self.getCol32())
        showIndent(outfile, level)
        outfile.write('Col33=%e,\n' % self.getCol33())
        showIndent(outfile, level)
        outfile.write('Col34=%e,\n' % self.getCol34())
        showIndent(outfile, level)
        outfile.write('Col35=%e,\n' % self.getCol35())
        showIndent(outfile, level)
        outfile.write('Col36=%e,\n' % self.getCol36())
        showIndent(outfile, level)
        outfile.write('Col37=%e,\n' % self.getCol37())
        showIndent(outfile, level)
        outfile.write('Col38=%e,\n' % self.getCol38())
        showIndent(outfile, level)
        outfile.write('Col39=%e,\n' % self.getCol39())
        showIndent(outfile, level)
        outfile.write('Col40=%e,\n' % self.getCol40())
        showIndent(outfile, level)
        outfile.write('Col41=%e,\n' % self.getCol41())
        showIndent(outfile, level)
        outfile.write('Col42=%e,\n' % self.getCol42())
        showIndent(outfile, level)
        outfile.write('Col43=%e,\n' % self.getCol43())
        showIndent(outfile, level)
        outfile.write('Col44=%e,\n' % self.getCol44())
        showIndent(outfile, level)
        outfile.write('Col45=%e,\n' % self.getCol45())
        showIndent(outfile, level)
        outfile.write('Col46=%e,\n' % self.getCol46())
        showIndent(outfile, level)
        outfile.write('Col47=%e,\n' % self.getCol47())
        showIndent(outfile, level)
        outfile.write('Col48=%e,\n' % self.getCol48())
        showIndent(outfile, level)
        outfile.write('Col49=%e,\n' % self.getCol49())
        showIndent(outfile, level)
        outfile.write('Col50=%e,\n' % self.getCol50())
        showIndent(outfile, level)
        outfile.write('Col51=%e,\n' % self.getCol51())
        showIndent(outfile, level)
        outfile.write('Col52=%e,\n' % self.getCol52())
        showIndent(outfile, level)
        outfile.write('Col53=%e,\n' % self.getCol53())
        showIndent(outfile, level)
        outfile.write('Col54=%e,\n' % self.getCol54())
        showIndent(outfile, level)
        outfile.write('Col55=%e,\n' % self.getCol55())
        showIndent(outfile, level)
        outfile.write('Col56=%e,\n' % self.getCol56())
        showIndent(outfile, level)
        outfile.write('Col57=%e,\n' % self.getCol57())
        showIndent(outfile, level)
        outfile.write('Col58=%e,\n' % self.getCol58())
        showIndent(outfile, level)
        outfile.write('Col59=%e,\n' % self.getCol59())
        showIndent(outfile, level)
        outfile.write('Col60=%e,\n' % self.getCol60())
        showIndent(outfile, level)
        outfile.write('Col61=%e,\n' % self.getCol61())
        showIndent(outfile, level)
        outfile.write('Col62=%e,\n' % self.getCol62())
        showIndent(outfile, level)
        outfile.write('Col63=%e,\n' % self.getCol63())
        showIndent(outfile, level)
        outfile.write('Col64=%e,\n' % self.getCol64())
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        if attrs.get('Axis4'):
            self.Axis4 = attrs.get('Axis4').value
        if attrs.get('Axis3'):
            self.Axis3 = attrs.get('Axis3').value
        if attrs.get('Axis1'):
            self.Axis1 = attrs.get('Axis1').value
        if attrs.get('Axis2'):
            self.Axis2 = attrs.get('Axis2').value
        if attrs.get('Row'):
            self.Row = attrs.get('Row').value
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col1':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col1 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col2':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col2 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col3':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col3 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col4':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col4 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col5':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col5 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col6':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col6 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col7':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col7 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col8':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col8 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col9':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col9 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col10':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col10 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col11':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col11 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col12':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col12 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col13':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col13 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col14':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col14 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col15':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col15 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col16':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col16 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col17':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col17 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col18':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col18 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col19':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col19 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col20':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col20 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col21':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col21 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col22':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col22 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col23':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col23 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col24':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col24 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col25':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col25 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col26':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col26 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col27':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col27 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col28':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col28 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col29':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col29 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col30':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col30 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col31':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col31 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col32':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col32 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col33':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col33 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col34':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col34 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col35':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col35 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col36':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col36 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col37':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col37 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col38':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col38 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col39':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col39 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col40':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col40 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col41':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col41 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col42':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col42 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col43':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col43 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col44':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col44 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col45':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col45 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col46':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col46 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col47':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col47 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col48':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col48 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col49':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col49 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col50':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col50 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col51':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col51 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col52':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col52 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col53':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col53 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col54':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col54 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col55':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col55 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col56':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col56 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col57':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col57 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col58':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col58 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col59':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col59 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col60':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col60 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col61':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col61 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col62':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col62 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col63':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col63 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Col64':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Col64 = fval_
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
class SaxSmmatrixHandler(handler.ContentHandler):
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
        if name == 'SMMatrix':
            obj = SMMatrix.factory()
            stackObj = SaxStackElement('SMMatrix', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NumberOfStates':
            stackObj = SaxStackElement('NumberOfStates', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NumberOfAdditionalAxes':
            stackObj = SaxStackElement('NumberOfAdditionalAxes', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'ProvidesNonZeroCoords':
            stackObj = SaxStackElement('ProvidesNonZeroCoords', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'AdditionalAxesUpperLimits':
            obj = AdditionalAxesUpperLimits.factory()
            stackObj = SaxStackElement('AdditionalAxesUpperLimits', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Axis1':
            stackObj = SaxStackElement('Axis1', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Axis2':
            stackObj = SaxStackElement('Axis2', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Axis3':
            stackObj = SaxStackElement('Axis3', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Axis4':
            stackObj = SaxStackElement('Axis4', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'AdditionalAxesLowerLimits':
            obj = AdditionalAxesLowerLimits.factory()
            stackObj = SaxStackElement('AdditionalAxesLowerLimits', obj)
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
        elif name == 'NonZeroElements':
            obj = NonZeroElements.factory()
            stackObj = SaxStackElement('NonZeroElements', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Number':
            stackObj = SaxStackElement('Number', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NonZeroCoordinates':
            obj = NonZeroCoordinates.factory()
            stackObj = SaxStackElement('NonZeroCoordinates', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NonZeroCoordinate':
            obj = NonZeroCoordinate.factory()
            val = attrs.get('Position', None)
            if val is not None:
                obj.setPosition(val)
            stackObj = SaxStackElement('NonZeroCoordinate', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'I':
            stackObj = SaxStackElement('I', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'J':
            stackObj = SaxStackElement('J', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'MData':
            obj = MData.factory()
            val = attrs.get('Axis4', None)
            if val is not None:
                obj.setAxis4(val)
            val = attrs.get('Axis3', None)
            if val is not None:
                obj.setAxis3(val)
            val = attrs.get('Axis1', None)
            if val is not None:
                obj.setAxis1(val)
            val = attrs.get('Axis2', None)
            if val is not None:
                obj.setAxis2(val)
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
        if name == 'SMMatrix':
            if len(self.stack) == 1:
                self.root = self.stack[-1].obj
                self.stack.pop()
                done = 1
        elif name == 'NumberOfStates':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNumberofstates(content)
                self.stack.pop()
                done = 1
        elif name == 'NumberOfAdditionalAxes':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNumberofadditionalaxes(content)
                self.stack.pop()
                done = 1
        elif name == 'ProvidesNonZeroCoords':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setProvidesnonzerocoords(content)
                self.stack.pop()
                done = 1
        elif name == 'AdditionalAxesUpperLimits':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAdditionalaxesupperlimits(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Axis1':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setAxis1(content)
                self.stack.pop()
                done = 1
        elif name == 'Axis2':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setAxis2(content)
                self.stack.pop()
                done = 1
        elif name == 'Axis3':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setAxis3(content)
                self.stack.pop()
                done = 1
        elif name == 'Axis4':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setAxis4(content)
                self.stack.pop()
                done = 1
        elif name == 'AdditionalAxesLowerLimits':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setAdditionalaxeslowerlimits(self.stack[-1].obj)
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
        elif name == 'NonZeroElements':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNonzeroelements(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Number':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNumber(content)
                self.stack.pop()
                done = 1
        elif name == 'NonZeroCoordinates':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setNonzerocoordinates(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'NonZeroCoordinate':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addNonzerocoordinate(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'I':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setI(content)
                self.stack.pop()
                done = 1
        elif name == 'J':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setJ(content)
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
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col1" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol1(content)
                self.stack.pop()
                done = 1
        elif name == 'Col2':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col2" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol2(content)
                self.stack.pop()
                done = 1
        elif name == 'Col3':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col3" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol3(content)
                self.stack.pop()
                done = 1
        elif name == 'Col4':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col4" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol4(content)
                self.stack.pop()
                done = 1
        elif name == 'Col5':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col5" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol5(content)
                self.stack.pop()
                done = 1
        elif name == 'Col6':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col6" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol6(content)
                self.stack.pop()
                done = 1
        elif name == 'Col7':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col7" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol7(content)
                self.stack.pop()
                done = 1
        elif name == 'Col8':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col8" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol8(content)
                self.stack.pop()
                done = 1
        elif name == 'Col9':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col9" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol9(content)
                self.stack.pop()
                done = 1
        elif name == 'Col10':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col10" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol10(content)
                self.stack.pop()
                done = 1
        elif name == 'Col11':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col11" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol11(content)
                self.stack.pop()
                done = 1
        elif name == 'Col12':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col12" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol12(content)
                self.stack.pop()
                done = 1
        elif name == 'Col13':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col13" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol13(content)
                self.stack.pop()
                done = 1
        elif name == 'Col14':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col14" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol14(content)
                self.stack.pop()
                done = 1
        elif name == 'Col15':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col15" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol15(content)
                self.stack.pop()
                done = 1
        elif name == 'Col16':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col16" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol16(content)
                self.stack.pop()
                done = 1
        elif name == 'Col17':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col17" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol17(content)
                self.stack.pop()
                done = 1
        elif name == 'Col18':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col18" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol18(content)
                self.stack.pop()
                done = 1
        elif name == 'Col19':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col19" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol19(content)
                self.stack.pop()
                done = 1
        elif name == 'Col20':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col20" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol20(content)
                self.stack.pop()
                done = 1
        elif name == 'Col21':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col21" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol21(content)
                self.stack.pop()
                done = 1
        elif name == 'Col22':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col22" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol22(content)
                self.stack.pop()
                done = 1
        elif name == 'Col23':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col23" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol23(content)
                self.stack.pop()
                done = 1
        elif name == 'Col24':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col24" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol24(content)
                self.stack.pop()
                done = 1
        elif name == 'Col25':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col25" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol25(content)
                self.stack.pop()
                done = 1
        elif name == 'Col26':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col26" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol26(content)
                self.stack.pop()
                done = 1
        elif name == 'Col27':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col27" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol27(content)
                self.stack.pop()
                done = 1
        elif name == 'Col28':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col28" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol28(content)
                self.stack.pop()
                done = 1
        elif name == 'Col29':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col29" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol29(content)
                self.stack.pop()
                done = 1
        elif name == 'Col30':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col30" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol30(content)
                self.stack.pop()
                done = 1
        elif name == 'Col31':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col31" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol31(content)
                self.stack.pop()
                done = 1
        elif name == 'Col32':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col32" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol32(content)
                self.stack.pop()
                done = 1
        elif name == 'Col33':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col33" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol33(content)
                self.stack.pop()
                done = 1
        elif name == 'Col34':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col34" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol34(content)
                self.stack.pop()
                done = 1
        elif name == 'Col35':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col35" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol35(content)
                self.stack.pop()
                done = 1
        elif name == 'Col36':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col36" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol36(content)
                self.stack.pop()
                done = 1
        elif name == 'Col37':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col37" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol37(content)
                self.stack.pop()
                done = 1
        elif name == 'Col38':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col38" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol38(content)
                self.stack.pop()
                done = 1
        elif name == 'Col39':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col39" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol39(content)
                self.stack.pop()
                done = 1
        elif name == 'Col40':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col40" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol40(content)
                self.stack.pop()
                done = 1
        elif name == 'Col41':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col41" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol41(content)
                self.stack.pop()
                done = 1
        elif name == 'Col42':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col42" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol42(content)
                self.stack.pop()
                done = 1
        elif name == 'Col43':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col43" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol43(content)
                self.stack.pop()
                done = 1
        elif name == 'Col44':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col44" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol44(content)
                self.stack.pop()
                done = 1
        elif name == 'Col45':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col45" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol45(content)
                self.stack.pop()
                done = 1
        elif name == 'Col46':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col46" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol46(content)
                self.stack.pop()
                done = 1
        elif name == 'Col47':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col47" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol47(content)
                self.stack.pop()
                done = 1
        elif name == 'Col48':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col48" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol48(content)
                self.stack.pop()
                done = 1
        elif name == 'Col49':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col49" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol49(content)
                self.stack.pop()
                done = 1
        elif name == 'Col50':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col50" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol50(content)
                self.stack.pop()
                done = 1
        elif name == 'Col51':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col51" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol51(content)
                self.stack.pop()
                done = 1
        elif name == 'Col52':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col52" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol52(content)
                self.stack.pop()
                done = 1
        elif name == 'Col53':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col53" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol53(content)
                self.stack.pop()
                done = 1
        elif name == 'Col54':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col54" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol54(content)
                self.stack.pop()
                done = 1
        elif name == 'Col55':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col55" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol55(content)
                self.stack.pop()
                done = 1
        elif name == 'Col56':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col56" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol56(content)
                self.stack.pop()
                done = 1
        elif name == 'Col57':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col57" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol57(content)
                self.stack.pop()
                done = 1
        elif name == 'Col58':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col58" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol58(content)
                self.stack.pop()
                done = 1
        elif name == 'Col59':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col59" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol59(content)
                self.stack.pop()
                done = 1
        elif name == 'Col60':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col60" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol60(content)
                self.stack.pop()
                done = 1
        elif name == 'Col61':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col61" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol61(content)
                self.stack.pop()
                done = 1
        elif name == 'Col62':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col62" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol62(content)
                self.stack.pop()
                done = 1
        elif name == 'Col63':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col63" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setCol63(content)
                self.stack.pop()
                done = 1
        elif name == 'Col64':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Col64" must be float -- content: %s' % content)
                else:
                    content = -1
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
    documentHandler = SaxSmmatrixHandler()
    parser.setDocumentHandler(documentHandler)
    parser.parse('file:%s' % inFileName)
    root = documentHandler.getRoot()
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    root.export(sys.stdout, 0)
    return root


def saxParseString(inString):
    parser = make_parser()
    documentHandler = SaxSmmatrixHandler()
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
    rootObj = SMMatrix.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0, name_="SMMatrix")
    return rootObj


def parseString(inString):
    doc = minidom.parseString(inString)
    rootNode = doc.documentElement
    rootObj = SMMatrix.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0, name_="SMMatrix")
    return rootObj


def parseLiteral(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = SMMatrix.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('from gSMMatrix.py import *\n\n')
    #sys.stdout.write('rootObj = SMMatrix(\n')
    #rootObj.exportLiteral(sys.stdout, 0, name_="SMMatrix")
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

