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

class SMFID:
    subclass = None
    def __init__(self, Name='', NumberOfStates='', StateLabels=None, Betas=None, FunctionalInputs=None, RedundantFunctionalInputs=None):
        self.Name = Name
        self.NumberOfStates = NumberOfStates
        self.StateLabels = StateLabels
        self.Betas = Betas
        self.FunctionalInputs = FunctionalInputs
        self.RedundantFunctionalInputs = RedundantFunctionalInputs
    def factory(*args_, **kwargs_):
        if SMFID.subclass:
            return SMFID.subclass(*args_, **kwargs_)
        else:
            return SMFID(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumberofstates(self): return self.NumberOfStates
    def setNumberofstates(self, NumberOfStates): self.NumberOfStates = NumberOfStates
    def getStatelabels(self): return self.StateLabels
    def setStatelabels(self, StateLabels): self.StateLabels = StateLabels
    def getBetas(self): return self.Betas
    def setBetas(self, Betas): self.Betas = Betas
    def getFunctionalinputs(self): return self.FunctionalInputs
    def setFunctionalinputs(self, FunctionalInputs): self.FunctionalInputs = FunctionalInputs
    def getRedundantfunctionalinputs(self): return self.RedundantFunctionalInputs
    def setRedundantfunctionalinputs(self, RedundantFunctionalInputs): self.RedundantFunctionalInputs = RedundantFunctionalInputs
    def getName(self): return self.Name
    def setName(self, Name): self.Name = Name
    def export(self, outfile, level, name_='SMFID'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='SMFID')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='SMFID'):
        outfile.write(' Name="%s"' % (self.getName(), ))
    def exportChildren(self, outfile, level, name_='SMFID'):
        showIndent(outfile, level)
        outfile.write('<NumberOfStates>%s</NumberOfStates>\n' % quote_xml(self.getNumberofstates()))
        if self.StateLabels:
            self.StateLabels.export(outfile, level)
        if self.Betas:
            self.Betas.export(outfile, level)
        if self.FunctionalInputs:
            self.FunctionalInputs.export(outfile, level)
        if self.RedundantFunctionalInputs:
            self.RedundantFunctionalInputs.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='SMFID'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Name = "%s",\n' % (self.getName(),))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('NumberOfStates=%s,\n' % quote_python(self.getNumberofstates()))
        if self.StateLabels:
            showIndent(outfile, level)
            outfile.write('StateLabels=StateLabels(\n')
            self.StateLabels.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Betas:
            showIndent(outfile, level)
            outfile.write('Betas=Betas(\n')
            self.Betas.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.FunctionalInputs:
            showIndent(outfile, level)
            outfile.write('FunctionalInputs=FunctionalInputs(\n')
            self.FunctionalInputs.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.RedundantFunctionalInputs:
            showIndent(outfile, level)
            outfile.write('RedundantFunctionalInputs=RedundantFunctionalInputs(\n')
            self.RedundantFunctionalInputs.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
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
            nodeName_ == 'StateLabels':
            obj_ = StateLabels.factory()
            obj_.build(child_)
            self.setStatelabels(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Betas':
            obj_ = Betas.factory()
            obj_.build(child_)
            self.setBetas(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'FunctionalInputs':
            obj_ = FunctionalInputs.factory()
            obj_.build(child_)
            self.setFunctionalinputs(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'RedundantFunctionalInputs':
            obj_ = RedundantFunctionalInputs.factory()
            obj_.build(child_)
            self.setRedundantfunctionalinputs(obj_)
# end class SMFID


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


class Betas:
    subclass = None
    def __init__(self, Number='', Beta=None):
        self.Number = Number
        if Beta is None:
            self.Beta = []
        else:
            self.Beta = Beta
    def factory(*args_, **kwargs_):
        if Betas.subclass:
            return Betas.subclass(*args_, **kwargs_)
        else:
            return Betas(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumber(self): return self.Number
    def setNumber(self, Number): self.Number = Number
    def getBeta(self): return self.Beta
    def setBeta(self, Beta): self.Beta = Beta
    def addBeta(self, value): self.Beta.append(value)
    def insertBeta(self, index, value): self.Beta[index] = value
    def export(self, outfile, level, name_='Betas'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='Betas'):
        pass
    def exportChildren(self, outfile, level, name_='Betas'):
        showIndent(outfile, level)
        outfile.write('<Number>%s</Number>\n' % quote_xml(self.getNumber()))
        for Beta_ in self.getBeta():
            Beta_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='Betas'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Number=%s,\n' % quote_python(self.getNumber()))
        showIndent(outfile, level)
        outfile.write('Beta=[\n')
        level += 1
        for Beta in self.Beta:
            showIndent(outfile, level)
            outfile.write('Beta(\n')
            Beta.exportLiteral(outfile, level)
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
            nodeName_ == 'Number':
            Number_ = ''
            for text__content_ in child_.childNodes:
                Number_ += text__content_.nodeValue
            self.Number = Number_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Beta':
            obj_ = Beta.factory()
            obj_.build(child_)
            self.Beta.append(obj_)
# end class Betas


class Beta:
    subclass = None
    def __init__(self, Position=None, Label='', I='', J='', Value=0.0, FlowRef='', OpZeroOrOne=''):
        self.Position = Position
        self.Label = Label
        self.I = I
        self.J = J
        self.Value = Value
        self.FlowRef = FlowRef
        self.OpZeroOrOne = OpZeroOrOne
    def factory(*args_, **kwargs_):
        if Beta.subclass:
            return Beta.subclass(*args_, **kwargs_)
        else:
            return Beta(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getLabel(self): return self.Label
    def setLabel(self, Label): self.Label = Label
    def getI(self): return self.I
    def setI(self, I): self.I = I
    def getJ(self): return self.J
    def setJ(self, J): self.J = J
    def getValue(self): return self.Value
    def setValue(self, Value): self.Value = Value
    def getFlowref(self): return self.FlowRef
    def setFlowref(self, FlowRef): self.FlowRef = FlowRef
    def getOpzeroorone(self): return self.OpZeroOrOne
    def setOpzeroorone(self, OpZeroOrOne): self.OpZeroOrOne = OpZeroOrOne
    def getPosition(self): return self.Position
    def setPosition(self, Position): self.Position = Position
    def export(self, outfile, level, name_='Beta'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='Beta')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='Beta'):
        outfile.write(' Position="%s"' % (self.getPosition(), ))
    def exportChildren(self, outfile, level, name_='Beta'):
        showIndent(outfile, level)
        outfile.write('<Label>%s</Label>\n' % quote_xml(self.getLabel()))
        showIndent(outfile, level)
        outfile.write('<I>%s</I>\n' % quote_xml(self.getI()))
        showIndent(outfile, level)
        outfile.write('<J>%s</J>\n' % quote_xml(self.getJ()))
        showIndent(outfile, level)
        outfile.write('<Value>%e</Value>\n' % self.getValue())
        showIndent(outfile, level)
        outfile.write('<FlowRef>%s</FlowRef>\n' % quote_xml(self.getFlowref()))
        showIndent(outfile, level)
        outfile.write('<OpZeroOrOne>%s</OpZeroOrOne>\n' % quote_xml(self.getOpzeroorone()))
    def exportLiteral(self, outfile, level, name_='Beta'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Position = "%s",\n' % (self.getPosition(),))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Label=%s,\n' % quote_python(self.getLabel()))
        showIndent(outfile, level)
        outfile.write('I=%s,\n' % quote_python(self.getI()))
        showIndent(outfile, level)
        outfile.write('J=%s,\n' % quote_python(self.getJ()))
        showIndent(outfile, level)
        outfile.write('Value=%e,\n' % self.getValue())
        showIndent(outfile, level)
        outfile.write('FlowRef=%s,\n' % quote_python(self.getFlowref()))
        showIndent(outfile, level)
        outfile.write('OpZeroOrOne=%s,\n' % quote_python(self.getOpzeroorone()))
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
            nodeName_ == 'Label':
            Label_ = ''
            for text__content_ in child_.childNodes:
                Label_ += text__content_.nodeValue
            self.Label = Label_
        elif child_.nodeType == Node.ELEMENT_NODE and \
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
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Value':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Value = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'FlowRef':
            FlowRef_ = ''
            for text__content_ in child_.childNodes:
                FlowRef_ += text__content_.nodeValue
            self.FlowRef = FlowRef_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'OpZeroOrOne':
            OpZeroOrOne_ = ''
            for text__content_ in child_.childNodes:
                OpZeroOrOne_ += text__content_.nodeValue
            self.OpZeroOrOne = OpZeroOrOne_
# end class Beta


class FunctionalInputs:
    subclass = None
    def __init__(self, Number='', FunctionInput=None):
        self.Number = Number
        if FunctionInput is None:
            self.FunctionInput = []
        else:
            self.FunctionInput = FunctionInput
    def factory(*args_, **kwargs_):
        if FunctionalInputs.subclass:
            return FunctionalInputs.subclass(*args_, **kwargs_)
        else:
            return FunctionalInputs(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumber(self): return self.Number
    def setNumber(self, Number): self.Number = Number
    def getFunctioninput(self): return self.FunctionInput
    def setFunctioninput(self, FunctionInput): self.FunctionInput = FunctionInput
    def addFunctioninput(self, value): self.FunctionInput.append(value)
    def insertFunctioninput(self, index, value): self.FunctionInput[index] = value
    def export(self, outfile, level, name_='FunctionalInputs'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='FunctionalInputs'):
        pass
    def exportChildren(self, outfile, level, name_='FunctionalInputs'):
        showIndent(outfile, level)
        outfile.write('<Number>%s</Number>\n' % quote_xml(self.getNumber()))
        for FunctionInput_ in self.getFunctioninput():
            FunctionInput_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='FunctionalInputs'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Number=%s,\n' % quote_python(self.getNumber()))
        showIndent(outfile, level)
        outfile.write('FunctionInput=[\n')
        level += 1
        for FunctionInput in self.FunctionInput:
            showIndent(outfile, level)
            outfile.write('FunctionInput(\n')
            FunctionInput.exportLiteral(outfile, level)
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
            nodeName_ == 'Number':
            Number_ = ''
            for text__content_ in child_.childNodes:
                Number_ += text__content_.nodeValue
            self.Number = Number_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'FunctionInput':
            obj_ = FunctionInput.factory()
            obj_.build(child_)
            self.FunctionInput.append(obj_)
# end class FunctionalInputs


class FunctionInput:
    subclass = None
    def __init__(self, Position=None, Label='', I='', J='', Value=0.0, FlowRef='', OpZeroOrOne='', BaseSetInd='', Script='', InputReference=''):
        self.Position = Position
        self.Label = Label
        self.I = I
        self.J = J
        self.Value = Value
        self.FlowRef = FlowRef
        self.OpZeroOrOne = OpZeroOrOne
        self.BaseSetInd = BaseSetInd
        self.Script = Script
        self.InputReference = InputReference
    def factory(*args_, **kwargs_):
        if FunctionInput.subclass:
            return FunctionInput.subclass(*args_, **kwargs_)
        else:
            return FunctionInput(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getLabel(self): return self.Label
    def setLabel(self, Label): self.Label = Label
    def getI(self): return self.I
    def setI(self, I): self.I = I
    def getJ(self): return self.J
    def setJ(self, J): self.J = J
    def getValue(self): return self.Value
    def setValue(self, Value): self.Value = Value
    def getFlowref(self): return self.FlowRef
    def setFlowref(self, FlowRef): self.FlowRef = FlowRef
    def getOpzeroorone(self): return self.OpZeroOrOne
    def setOpzeroorone(self, OpZeroOrOne): self.OpZeroOrOne = OpZeroOrOne
    def getBasesetind(self): return self.BaseSetInd
    def setBasesetind(self, BaseSetInd): self.BaseSetInd = BaseSetInd
    def getScript(self): return self.Script
    def setScript(self, Script): self.Script = Script
    def getInputreference(self): return self.InputReference
    def setInputreference(self, InputReference): self.InputReference = InputReference
    def getPosition(self): return self.Position
    def setPosition(self, Position): self.Position = Position
    def export(self, outfile, level, name_='FunctionInput'):
        showIndent(outfile, level)
        outfile.write('<%s' % (name_, ))
        self.exportAttributes(outfile, level, name_='FunctionInput')
        outfile.write('>\n')
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='FunctionInput'):
        outfile.write(' Position="%s"' % (self.getPosition(), ))
    def exportChildren(self, outfile, level, name_='FunctionInput'):
        showIndent(outfile, level)
        outfile.write('<Label>%s</Label>\n' % quote_xml(self.getLabel()))
        showIndent(outfile, level)
        outfile.write('<I>%s</I>\n' % quote_xml(self.getI()))
        showIndent(outfile, level)
        outfile.write('<J>%s</J>\n' % quote_xml(self.getJ()))
        showIndent(outfile, level)
        outfile.write('<Value>%e</Value>\n' % self.getValue())
        showIndent(outfile, level)
        outfile.write('<FlowRef>%s</FlowRef>\n' % quote_xml(self.getFlowref()))
        showIndent(outfile, level)
        outfile.write('<OpZeroOrOne>%s</OpZeroOrOne>\n' % quote_xml(self.getOpzeroorone()))
        showIndent(outfile, level)
        outfile.write('<BaseSetInd>%s</BaseSetInd>\n' % quote_xml(self.getBasesetind()))
        showIndent(outfile, level)
        outfile.write('<Script>%s</Script>\n' % quote_xml(self.getScript()))
        showIndent(outfile, level)
        outfile.write('<InputReference>%s</InputReference>\n' % quote_xml(self.getInputreference()))
    def exportLiteral(self, outfile, level, name_='FunctionInput'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Position = "%s",\n' % (self.getPosition(),))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Label=%s,\n' % quote_python(self.getLabel()))
        showIndent(outfile, level)
        outfile.write('I=%s,\n' % quote_python(self.getI()))
        showIndent(outfile, level)
        outfile.write('J=%s,\n' % quote_python(self.getJ()))
        showIndent(outfile, level)
        outfile.write('Value=%e,\n' % self.getValue())
        showIndent(outfile, level)
        outfile.write('FlowRef=%s,\n' % quote_python(self.getFlowref()))
        showIndent(outfile, level)
        outfile.write('OpZeroOrOne=%s,\n' % quote_python(self.getOpzeroorone()))
        showIndent(outfile, level)
        outfile.write('BaseSetInd=%s,\n' % quote_python(self.getBasesetind()))
        showIndent(outfile, level)
        outfile.write('Script=%s,\n' % quote_python(self.getScript()))
        showIndent(outfile, level)
        outfile.write('InputReference=%s,\n' % quote_python(self.getInputreference()))
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
            nodeName_ == 'Label':
            Label_ = ''
            for text__content_ in child_.childNodes:
                Label_ += text__content_.nodeValue
            self.Label = Label_
        elif child_.nodeType == Node.ELEMENT_NODE and \
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
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Value':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self.Value = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'FlowRef':
            FlowRef_ = ''
            for text__content_ in child_.childNodes:
                FlowRef_ += text__content_.nodeValue
            self.FlowRef = FlowRef_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'OpZeroOrOne':
            OpZeroOrOne_ = ''
            for text__content_ in child_.childNodes:
                OpZeroOrOne_ += text__content_.nodeValue
            self.OpZeroOrOne = OpZeroOrOne_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'BaseSetInd':
            BaseSetInd_ = ''
            for text__content_ in child_.childNodes:
                BaseSetInd_ += text__content_.nodeValue
            self.BaseSetInd = BaseSetInd_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Script':
            Script_ = ''
            for text__content_ in child_.childNodes:
                Script_ += text__content_.nodeValue
            self.Script = Script_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'InputReference':
            InputReference_ = ''
            for text__content_ in child_.childNodes:
                InputReference_ += text__content_.nodeValue
            self.InputReference = InputReference_
# end class FunctionInput


class RedundantFunctionalInputs:
    subclass = None
    def __init__(self, Number='', FunctionInput=None):
        self.Number = Number
        if FunctionInput is None:
            self.FunctionInput = []
        else:
            self.FunctionInput = FunctionInput
    def factory(*args_, **kwargs_):
        if RedundantFunctionalInputs.subclass:
            return RedundantFunctionalInputs.subclass(*args_, **kwargs_)
        else:
            return RedundantFunctionalInputs(*args_, **kwargs_)
    factory = staticmethod(factory)
    def getNumber(self): return self.Number
    def setNumber(self, Number): self.Number = Number
    def getFunctioninput(self): return self.FunctionInput
    def setFunctioninput(self, FunctionInput): self.FunctionInput = FunctionInput
    def addFunctioninput(self, value): self.FunctionInput.append(value)
    def insertFunctioninput(self, index, value): self.FunctionInput[index] = value
    def export(self, outfile, level, name_='RedundantFunctionalInputs'):
        showIndent(outfile, level)
        outfile.write('<%s>\n' % name_)
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write('</%s>\n' % name_)
    def exportAttributes(self, outfile, level, name_='RedundantFunctionalInputs'):
        pass
    def exportChildren(self, outfile, level, name_='RedundantFunctionalInputs'):
        showIndent(outfile, level)
        outfile.write('<Number>%s</Number>\n' % quote_xml(self.getNumber()))
        for FunctionInput_ in self.getFunctioninput():
            FunctionInput_.export(outfile, level)
    def exportLiteral(self, outfile, level, name_='RedundantFunctionalInputs'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Number=%s,\n' % quote_python(self.getNumber()))
        showIndent(outfile, level)
        outfile.write('FunctionInput=[\n')
        level += 1
        for FunctionInput in self.FunctionInput:
            showIndent(outfile, level)
            outfile.write('FunctionInput(\n')
            FunctionInput.exportLiteral(outfile, level)
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
            nodeName_ == 'Number':
            Number_ = ''
            for text__content_ in child_.childNodes:
                Number_ += text__content_.nodeValue
            self.Number = Number_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'FunctionInput':
            obj_ = FunctionInput.factory()
            obj_.build(child_)
            self.FunctionInput.append(obj_)
# end class RedundantFunctionalInputs


from xml.sax import handler, make_parser

class SaxStackElement:
    def __init__(self, name='', obj=None):
        self.name = name
        self.obj = obj
        self.content = ''

#
# SAX handler
#
class SaxSmfidHandler(handler.ContentHandler):
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
        if name == 'SMFID':
            obj = SMFID.factory()
            stackObj = SaxStackElement('SMFID', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'NumberOfStates':
            stackObj = SaxStackElement('NumberOfStates', None)
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
        elif name == 'Betas':
            obj = Betas.factory()
            stackObj = SaxStackElement('Betas', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Number':
            stackObj = SaxStackElement('Number', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Beta':
            obj = Beta.factory()
            val = attrs.get('Position', None)
            if val is not None:
                obj.setPosition(val)
            stackObj = SaxStackElement('Beta', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Label':
            stackObj = SaxStackElement('Label', None)
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
        elif name == 'Value':
            stackObj = SaxStackElement('Value', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'FlowRef':
            stackObj = SaxStackElement('FlowRef', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'OpZeroOrOne':
            stackObj = SaxStackElement('OpZeroOrOne', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'FunctionalInputs':
            obj = FunctionalInputs.factory()
            stackObj = SaxStackElement('FunctionalInputs', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'FunctionInput':
            obj = FunctionInput.factory()
            val = attrs.get('Position', None)
            if val is not None:
                obj.setPosition(val)
            stackObj = SaxStackElement('FunctionInput', obj)
            self.stack.append(stackObj)
            done = 1
        elif name == 'BaseSetInd':
            stackObj = SaxStackElement('BaseSetInd', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'Script':
            stackObj = SaxStackElement('Script', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'InputReference':
            stackObj = SaxStackElement('InputReference', None)
            self.stack.append(stackObj)
            done = 1
        elif name == 'RedundantFunctionalInputs':
            obj = RedundantFunctionalInputs.factory()
            stackObj = SaxStackElement('RedundantFunctionalInputs', obj)
            self.stack.append(stackObj)
            done = 1
        if not done:
            self.reportError('"%s" element not allowed here.' % name)

    def endElement(self, name):
        done = 0
        if name == 'SMFID':
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
        elif name == 'Betas':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setBetas(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Number':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setNumber(content)
                self.stack.pop()
                done = 1
        elif name == 'Beta':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addBeta(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'Label':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setLabel(content)
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
        elif name == 'Value':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                if content:
                    try:
                        content = float(content)
                    except:
                        self.reportError('"Value" must be float -- content: %s' % content)
                else:
                    content = -1
                self.stack[-2].obj.setValue(content)
                self.stack.pop()
                done = 1
        elif name == 'FlowRef':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setFlowref(content)
                self.stack.pop()
                done = 1
        elif name == 'OpZeroOrOne':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setOpzeroorone(content)
                self.stack.pop()
                done = 1
        elif name == 'FunctionalInputs':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setFunctionalinputs(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'FunctionInput':
            if len(self.stack) >= 2:
                self.stack[-2].obj.addFunctioninput(self.stack[-1].obj)
                self.stack.pop()
                done = 1
        elif name == 'BaseSetInd':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setBasesetind(content)
                self.stack.pop()
                done = 1
        elif name == 'Script':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setScript(content)
                self.stack.pop()
                done = 1
        elif name == 'InputReference':
            if len(self.stack) >= 2:
                content = self.stack[-1].content
                self.stack[-2].obj.setInputreference(content)
                self.stack.pop()
                done = 1
        elif name == 'RedundantFunctionalInputs':
            if len(self.stack) >= 2:
                self.stack[-2].obj.setRedundantfunctionalinputs(self.stack[-1].obj)
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
    documentHandler = SaxSmfidHandler()
    parser.setDocumentHandler(documentHandler)
    parser.parse('file:%s' % inFileName)
    root = documentHandler.getRoot()
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    root.export(sys.stdout, 0)
    return root


def saxParseString(inString):
    parser = make_parser()
    documentHandler = SaxSmfidHandler()
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
    rootObj = SMFID.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0, name_="SMFID")
    return rootObj


def parseString(inString):
    doc = minidom.parseString(inString)
    rootNode = doc.documentElement
    rootObj = SMFID.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0, name_="SMFID")
    return rootObj


def parseLiteral(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = SMFID.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('from gSMFID.py import *\n\n')
    #sys.stdout.write('rootObj = SMFID(\n')
    #rootObj.exportLiteral(sys.stdout, 0, name_="SMFID")
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

