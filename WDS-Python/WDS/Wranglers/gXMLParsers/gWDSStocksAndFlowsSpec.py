#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Jun 30 06:32:34 2022 by generateDS.py version 2.40.13.
# Python 3.9.5 (default, Nov 23 2021, 15:27:38)  [GCC 9.3.0]
#
# Command line options:
#   ('--mixed-case-enums', '')
#   ('-f', '')
#   ('--export', 'write etree')
#   ('-o', './WDS-Python/WDS/Wranglers/gXMLParsers/gWDSStocksAndFlowsSpec.py')
#
# Command line arguments:
#   ./WDS-XML/XSD/WDSStocksAndFlowsSpec.xsd
#
# Command line:
#   ./WDS-Python/scripts/generateDS_unsnaked --mixed-case-enums -f --export="write etree" -o "./WDS-Python/WDS/Wranglers/gXMLParsers/gWDSStocksAndFlowsSpec.py" ./WDS-XML/XSD/WDSStocksAndFlowsSpec.xsd
#
# Current working directory (os.getcwd()):
#   master
#

import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
from lxml import etree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
TagNamePrefix = ""
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the _exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    try:
        from generatedssupersuper import GeneratedsSuperSuper
    except ModulenotfoundExp_ as exp:
        class GeneratedsSuperSuper(object):
            pass
    
    class GeneratedsSuper(GeneratedsSuperSuper):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def __str__(self):
            settings = {
                'str_pretty_print': True,
                'str_indent_level': 0,
                'str_namespaceprefix': '',
                'str_name': self.__class__.__name__,
                'str_namespacedefs': '',
            }
            for n in settings:
                if hasattr(self, n):
                    settings[n] = getattr(self, n)
            if sys.version_info.major == 2:
                from StringIO import StringIO
            else:
                from io import StringIO
            output = StringIO()
            self.export(
                output,
                settings['str_indent_level'],
                pretty_print=settings['str_pretty_print'],
                namespaceprefix_=settings['str_namespaceprefix'],
                name_=settings['str_name'],
                namespacedef_=settings['str_namespacedefs']
            )
            strval = output.getvalue()
            output.close()
            return strval
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data).decode('ascii')
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % int(input_data)
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % float(input_data)).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            input_data = input_data.strip()
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            target = str(target)
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


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
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    s1 = s1.replace('\n', '&#10;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
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


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


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
    TypeBase64 = 8
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
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class WDSStocksAndFlows(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, Handle=None, ParameterList=None, Units=None, Stocks=None, Flows=None, Orders=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "wds"
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        self.ParameterList = ParameterList
        self.ParameterList_nsprefix_ = "wds"
        self.Units = Units
        self.Units_nsprefix_ = "wds"
        self.Stocks = Stocks
        self.Stocks_nsprefix_ = "wds"
        self.Flows = Flows
        self.Flows_nsprefix_ = "wds"
        self.Orders = Orders
        self.Orders_nsprefix_ = "wds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, WDSStocksAndFlows)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if WDSStocksAndFlows.subclass:
            return WDSStocksAndFlows.subclass(*args_, **kwargs_)
        else:
            return WDSStocksAndFlows(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ParameterList(self):
        return self.ParameterList
    def set_ParameterList(self, ParameterList):
        self.ParameterList = ParameterList
    def get_Units(self):
        return self.Units
    def set_Units(self, Units):
        self.Units = Units
    def get_Stocks(self):
        return self.Stocks
    def set_Stocks(self, Stocks):
        self.Stocks = Stocks
    def get_Flows(self):
        return self.Flows
    def set_Flows(self, Flows):
        self.Flows = Flows
    def get_Orders(self):
        return self.Orders
    def set_Orders(self, Orders):
        self.Orders = Orders
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def get_Handle(self):
        return self.Handle
    def set_Handle(self, Handle):
        self.Handle = Handle
    def _hasContent(self):
        if (
            self.ParameterList is not None or
            self.Units is not None or
            self.Stocks is not None or
            self.Flows is not None or
            self.Orders is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='WDSStocksAndFlows', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('WDSStocksAndFlows')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'WDSStocksAndFlows':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='WDSStocksAndFlows')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='WDSStocksAndFlows', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='WDSStocksAndFlows'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='WDSStocksAndFlows', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ParameterList is not None:
            namespaceprefix_ = self.ParameterList_nsprefix_ + ':' if (UseCapturedNS_ and self.ParameterList_nsprefix_) else ''
            self.ParameterList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParameterList', pretty_print=pretty_print)
        if self.Units is not None:
            namespaceprefix_ = self.Units_nsprefix_ + ':' if (UseCapturedNS_ and self.Units_nsprefix_) else ''
            self.Units.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Units', pretty_print=pretty_print)
        if self.Stocks is not None:
            namespaceprefix_ = self.Stocks_nsprefix_ + ':' if (UseCapturedNS_ and self.Stocks_nsprefix_) else ''
            self.Stocks.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Stocks', pretty_print=pretty_print)
        if self.Flows is not None:
            namespaceprefix_ = self.Flows_nsprefix_ + ':' if (UseCapturedNS_ and self.Flows_nsprefix_) else ''
            self.Flows.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Flows', pretty_print=pretty_print)
        if self.Orders is not None:
            namespaceprefix_ = self.Orders_nsprefix_ + ':' if (UseCapturedNS_ and self.Orders_nsprefix_) else ''
            self.Orders.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Orders', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='WDSStocksAndFlows', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        if self.Name is not None:
            element.set('Name', self.gds_format_string(self.Name))
        if self.Handle is not None:
            element.set('Handle', self.gds_format_string(self.Handle))
        if self.ParameterList is not None:
            ParameterList_ = self.ParameterList
            ParameterList_.to_etree(element, name_='ParameterList', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        if self.Units is not None:
            Units_ = self.Units
            Units_.to_etree(element, name_='Units', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        if self.Stocks is not None:
            Stocks_ = self.Stocks
            Stocks_.to_etree(element, name_='Stocks', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        if self.Flows is not None:
            Flows_ = self.Flows
            Flows_.to_etree(element, name_='Flows', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        if self.Orders is not None:
            Orders_ = self.Orders
            Orders_.to_etree(element, name_='Orders', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        if reverse_mapping_ is not None:
            reverse_mapping_[element] = self
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Name', node)
        if value is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            self.Name = value
        value = find_attr_value_('Handle', node)
        if value is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            self.Handle = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ParameterList':
            obj_ = ParameterListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParameterList = obj_
            obj_.original_tagname_ = 'ParameterList'
        elif nodeName_ == 'Units':
            obj_ = UnitsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Units = obj_
            obj_.original_tagname_ = 'Units'
        elif nodeName_ == 'Stocks':
            obj_ = StocksType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Stocks = obj_
            obj_.original_tagname_ = 'Stocks'
        elif nodeName_ == 'Flows':
            obj_ = FlowsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Flows = obj_
            obj_.original_tagname_ = 'Flows'
        elif nodeName_ == 'Orders':
            obj_ = OrdersType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Orders = obj_
            obj_.original_tagname_ = 'Orders'
# end class WDSStocksAndFlows


class ParameterListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Parameter=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Parameter is None:
            self.Parameter = []
        else:
            self.Parameter = Parameter
        self.Parameter_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParameterListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParameterListType.subclass:
            return ParameterListType.subclass(*args_, **kwargs_)
        else:
            return ParameterListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Parameter(self):
        return self.Parameter
    def set_Parameter(self, Parameter):
        self.Parameter = Parameter
    def add_Parameter(self, value):
        self.Parameter.append(value)
    def insert_Parameter_at(self, index, value):
        self.Parameter.insert(index, value)
    def replace_Parameter_at(self, index, value):
        self.Parameter[index] = value
    def _hasContent(self):
        if (
            self.Parameter
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ParameterListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParameterListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParameterListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParameterListType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParameterListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParameterListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ParameterListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Parameter_ in self.Parameter:
            namespaceprefix_ = self.Parameter_nsprefix_ + ':' if (UseCapturedNS_ and self.Parameter_nsprefix_) else ''
            Parameter_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Parameter', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ParameterListType', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        for Parameter_ in self.Parameter:
            Parameter_.to_etree(element, name_='Parameter', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        if reverse_mapping_ is not None:
            reverse_mapping_[element] = self
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Parameter':
            obj_ = ParameterType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Parameter.append(obj_)
            obj_.original_tagname_ = 'Parameter'
# end class ParameterListType


class ParameterType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, Type=None, Value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Type = _cast(None, Type)
        self.Type_nsprefix_ = None
        self.Value = Value
        self.Value_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParameterType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParameterType.subclass:
            return ParameterType.subclass(*args_, **kwargs_)
        else:
            return ParameterType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Value(self):
        return self.Value
    def set_Value(self, Value):
        self.Value = Value
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def get_Type(self):
        return self.Type
    def set_Type(self, Type):
        self.Type = Type
    def _hasContent(self):
        if (
            self.Value is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ParameterType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParameterType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParameterType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParameterType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParameterType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParameterType'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Type is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            outfile.write(' Type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Type), input_name='Type')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ParameterType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Value is not None:
            namespaceprefix_ = self.Value_nsprefix_ + ':' if (UseCapturedNS_ and self.Value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValue>%s</%sValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Value), input_name='Value')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='ParameterType', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        if self.Name is not None:
            element.set('Name', self.gds_format_string(self.Name))
        if self.Type is not None:
            element.set('Type', self.gds_format_string(self.Type))
        if self.Value is not None:
            Value_ = self.Value
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Value').text = self.gds_format_string(Value_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        if reverse_mapping_ is not None:
            reverse_mapping_[element] = self
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Name', node)
        if value is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            self.Name = value
        value = find_attr_value_('Type', node)
        if value is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            self.Type = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Value':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Value')
            value_ = self.gds_validate_string(value_, node, 'Value')
            self.Value = value_
            self.Value_nsprefix_ = child_.prefix
# end class ParameterType


class UnitsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Handle=None, ParameterList=None, Unit=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        self.ParameterList = ParameterList
        self.ParameterList_nsprefix_ = None
        if Unit is None:
            self.Unit = []
        else:
            self.Unit = Unit
        self.Unit_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, UnitsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if UnitsType.subclass:
            return UnitsType.subclass(*args_, **kwargs_)
        else:
            return UnitsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ParameterList(self):
        return self.ParameterList
    def set_ParameterList(self, ParameterList):
        self.ParameterList = ParameterList
    def get_Unit(self):
        return self.Unit
    def set_Unit(self, Unit):
        self.Unit = Unit
    def add_Unit(self, value):
        self.Unit.append(value)
    def insert_Unit_at(self, index, value):
        self.Unit.insert(index, value)
    def replace_Unit_at(self, index, value):
        self.Unit[index] = value
    def get_Handle(self):
        return self.Handle
    def set_Handle(self, Handle):
        self.Handle = Handle
    def _hasContent(self):
        if (
            self.ParameterList is not None or
            self.Unit
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='UnitsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('UnitsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'UnitsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='UnitsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='UnitsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='UnitsType'):
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='UnitsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ParameterList is not None:
            namespaceprefix_ = self.ParameterList_nsprefix_ + ':' if (UseCapturedNS_ and self.ParameterList_nsprefix_) else ''
            self.ParameterList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParameterList', pretty_print=pretty_print)
        for Unit_ in self.Unit:
            namespaceprefix_ = self.Unit_nsprefix_ + ':' if (UseCapturedNS_ and self.Unit_nsprefix_) else ''
            Unit_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Unit', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='UnitsType', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        if self.Handle is not None:
            element.set('Handle', self.gds_format_string(self.Handle))
        if self.ParameterList is not None:
            ParameterList_ = self.ParameterList
            ParameterList_.to_etree(element, name_='ParameterList', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        for Unit_ in self.Unit:
            Unit_.to_etree(element, name_='Unit', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        if reverse_mapping_ is not None:
            reverse_mapping_[element] = self
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Handle', node)
        if value is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            self.Handle = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ParameterList':
            obj_ = ParameterListType1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParameterList = obj_
            obj_.original_tagname_ = 'ParameterList'
        elif nodeName_ == 'Unit':
            obj_ = UnitType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Unit.append(obj_)
            obj_.original_tagname_ = 'Unit'
# end class UnitsType


class ParameterListType1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Parameter=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Parameter is None:
            self.Parameter = []
        else:
            self.Parameter = Parameter
        self.Parameter_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParameterListType1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParameterListType1.subclass:
            return ParameterListType1.subclass(*args_, **kwargs_)
        else:
            return ParameterListType1(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Parameter(self):
        return self.Parameter
    def set_Parameter(self, Parameter):
        self.Parameter = Parameter
    def add_Parameter(self, value):
        self.Parameter.append(value)
    def insert_Parameter_at(self, index, value):
        self.Parameter.insert(index, value)
    def replace_Parameter_at(self, index, value):
        self.Parameter[index] = value
    def _hasContent(self):
        if (
            self.Parameter
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ParameterListType1', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParameterListType1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParameterListType1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParameterListType1')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParameterListType1', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParameterListType1'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ParameterListType1', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Parameter_ in self.Parameter:
            namespaceprefix_ = self.Parameter_nsprefix_ + ':' if (UseCapturedNS_ and self.Parameter_nsprefix_) else ''
            Parameter_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Parameter', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ParameterListType1', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        for Parameter_ in self.Parameter:
            Parameter_.to_etree(element, name_='Parameter', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        if reverse_mapping_ is not None:
            reverse_mapping_[element] = self
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Parameter':
            obj_ = ParameterType2.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Parameter.append(obj_)
            obj_.original_tagname_ = 'Parameter'
# end class ParameterListType1


class ParameterType2(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, Type=None, Value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Type = _cast(None, Type)
        self.Type_nsprefix_ = None
        self.Value = Value
        self.Value_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParameterType2)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParameterType2.subclass:
            return ParameterType2.subclass(*args_, **kwargs_)
        else:
            return ParameterType2(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Value(self):
        return self.Value
    def set_Value(self, Value):
        self.Value = Value
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def get_Type(self):
        return self.Type
    def set_Type(self, Type):
        self.Type = Type
    def _hasContent(self):
        if (
            self.Value is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ParameterType2', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParameterType2')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParameterType2':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParameterType2')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParameterType2', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParameterType2'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Type is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            outfile.write(' Type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Type), input_name='Type')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ParameterType2', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Value is not None:
            namespaceprefix_ = self.Value_nsprefix_ + ':' if (UseCapturedNS_ and self.Value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValue>%s</%sValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Value), input_name='Value')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='ParameterType2', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        if self.Name is not None:
            element.set('Name', self.gds_format_string(self.Name))
        if self.Type is not None:
            element.set('Type', self.gds_format_string(self.Type))
        if self.Value is not None:
            Value_ = self.Value
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Value').text = self.gds_format_string(Value_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        if reverse_mapping_ is not None:
            reverse_mapping_[element] = self
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Name', node)
        if value is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            self.Name = value
        value = find_attr_value_('Type', node)
        if value is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            self.Type = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Value':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Value')
            value_ = self.gds_validate_string(value_, node, 'Value')
            self.Value = value_
            self.Value_nsprefix_ = child_.prefix
# end class ParameterType2


class UnitType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, Mneumonic=None, Shorthand=None, Concept=None, ActualsVariable=None, Type=None, ToSimInd=None, SimCVStructural=None, SimCVPerPeriod=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Position = _cast(int, Position)
        self.Position_nsprefix_ = None
        self.Mneumonic = Mneumonic
        self.Mneumonic_nsprefix_ = None
        self.Shorthand = Shorthand
        self.Shorthand_nsprefix_ = None
        self.Concept = Concept
        self.Concept_nsprefix_ = None
        self.ActualsVariable = ActualsVariable
        self.ActualsVariable_nsprefix_ = None
        self.Type = Type
        self.Type_nsprefix_ = None
        self.ToSimInd = ToSimInd
        self.ToSimInd_nsprefix_ = None
        self.SimCVStructural = SimCVStructural
        self.SimCVStructural_nsprefix_ = None
        self.SimCVPerPeriod = SimCVPerPeriod
        self.SimCVPerPeriod_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, UnitType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if UnitType.subclass:
            return UnitType.subclass(*args_, **kwargs_)
        else:
            return UnitType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Mneumonic(self):
        return self.Mneumonic
    def set_Mneumonic(self, Mneumonic):
        self.Mneumonic = Mneumonic
    def get_Shorthand(self):
        return self.Shorthand
    def set_Shorthand(self, Shorthand):
        self.Shorthand = Shorthand
    def get_Concept(self):
        return self.Concept
    def set_Concept(self, Concept):
        self.Concept = Concept
    def get_ActualsVariable(self):
        return self.ActualsVariable
    def set_ActualsVariable(self, ActualsVariable):
        self.ActualsVariable = ActualsVariable
    def get_Type(self):
        return self.Type
    def set_Type(self, Type):
        self.Type = Type
    def get_ToSimInd(self):
        return self.ToSimInd
    def set_ToSimInd(self, ToSimInd):
        self.ToSimInd = ToSimInd
    def get_SimCVStructural(self):
        return self.SimCVStructural
    def set_SimCVStructural(self, SimCVStructural):
        self.SimCVStructural = SimCVStructural
    def get_SimCVPerPeriod(self):
        return self.SimCVPerPeriod
    def set_SimCVPerPeriod(self, SimCVPerPeriod):
        self.SimCVPerPeriod = SimCVPerPeriod
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def _hasContent(self):
        if (
            self.Mneumonic is not None or
            self.Shorthand is not None or
            self.Concept is not None or
            self.ActualsVariable is not None or
            self.Type is not None or
            self.ToSimInd is not None or
            self.SimCVStructural is not None or
            self.SimCVPerPeriod is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='UnitType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('UnitType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'UnitType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='UnitType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='UnitType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='UnitType'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position="%s"' % self.gds_format_integer(self.Position, input_name='Position'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='UnitType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Mneumonic is not None:
            namespaceprefix_ = self.Mneumonic_nsprefix_ + ':' if (UseCapturedNS_ and self.Mneumonic_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMneumonic>%s</%sMneumonic>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Mneumonic), input_name='Mneumonic')), namespaceprefix_ , eol_))
        if self.Shorthand is not None:
            namespaceprefix_ = self.Shorthand_nsprefix_ + ':' if (UseCapturedNS_ and self.Shorthand_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sShorthand>%s</%sShorthand>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Shorthand), input_name='Shorthand')), namespaceprefix_ , eol_))
        if self.Concept is not None:
            namespaceprefix_ = self.Concept_nsprefix_ + ':' if (UseCapturedNS_ and self.Concept_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sConcept>%s</%sConcept>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Concept), input_name='Concept')), namespaceprefix_ , eol_))
        if self.ActualsVariable is not None:
            namespaceprefix_ = self.ActualsVariable_nsprefix_ + ':' if (UseCapturedNS_ and self.ActualsVariable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sActualsVariable>%s</%sActualsVariable>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ActualsVariable), input_name='ActualsVariable')), namespaceprefix_ , eol_))
        if self.Type is not None:
            namespaceprefix_ = self.Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sType>%s</%sType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Type), input_name='Type')), namespaceprefix_ , eol_))
        if self.ToSimInd is not None:
            namespaceprefix_ = self.ToSimInd_nsprefix_ + ':' if (UseCapturedNS_ and self.ToSimInd_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sToSimInd>%s</%sToSimInd>%s' % (namespaceprefix_ , self.gds_format_integer(self.ToSimInd, input_name='ToSimInd'), namespaceprefix_ , eol_))
        if self.SimCVStructural is not None:
            namespaceprefix_ = self.SimCVStructural_nsprefix_ + ':' if (UseCapturedNS_ and self.SimCVStructural_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSimCVStructural>%s</%sSimCVStructural>%s' % (namespaceprefix_ , self.gds_format_double(self.SimCVStructural, input_name='SimCVStructural'), namespaceprefix_ , eol_))
        if self.SimCVPerPeriod is not None:
            namespaceprefix_ = self.SimCVPerPeriod_nsprefix_ + ':' if (UseCapturedNS_ and self.SimCVPerPeriod_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSimCVPerPeriod>%s</%sSimCVPerPeriod>%s' % (namespaceprefix_ , self.gds_format_double(self.SimCVPerPeriod, input_name='SimCVPerPeriod'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='UnitType', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        if self.Position is not None:
            element.set('Position', self.gds_format_integer(self.Position))
        if self.Mneumonic is not None:
            Mneumonic_ = self.Mneumonic
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Mneumonic').text = self.gds_format_string(Mneumonic_)
        if self.Shorthand is not None:
            Shorthand_ = self.Shorthand
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Shorthand').text = self.gds_format_string(Shorthand_)
        if self.Concept is not None:
            Concept_ = self.Concept
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Concept').text = self.gds_format_string(Concept_)
        if self.ActualsVariable is not None:
            ActualsVariable_ = self.ActualsVariable
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}ActualsVariable').text = self.gds_format_string(ActualsVariable_)
        if self.Type is not None:
            Type_ = self.Type
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Type').text = self.gds_format_string(Type_)
        if self.ToSimInd is not None:
            ToSimInd_ = self.ToSimInd
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}ToSimInd').text = self.gds_format_integer(ToSimInd_)
        if self.SimCVStructural is not None:
            SimCVStructural_ = self.SimCVStructural
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}SimCVStructural').text = self.gds_format_double(SimCVStructural_)
        if self.SimCVPerPeriod is not None:
            SimCVPerPeriod_ = self.SimCVPerPeriod
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}SimCVPerPeriod').text = self.gds_format_double(SimCVPerPeriod_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        if reverse_mapping_ is not None:
            reverse_mapping_[element] = self
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Position', node)
        if value is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            self.Position = self.gds_parse_integer(value, node, 'Position')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Mneumonic':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Mneumonic')
            value_ = self.gds_validate_string(value_, node, 'Mneumonic')
            self.Mneumonic = value_
            self.Mneumonic_nsprefix_ = child_.prefix
        elif nodeName_ == 'Shorthand':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Shorthand')
            value_ = self.gds_validate_string(value_, node, 'Shorthand')
            self.Shorthand = value_
            self.Shorthand_nsprefix_ = child_.prefix
        elif nodeName_ == 'Concept':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Concept')
            value_ = self.gds_validate_string(value_, node, 'Concept')
            self.Concept = value_
            self.Concept_nsprefix_ = child_.prefix
        elif nodeName_ == 'ActualsVariable':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ActualsVariable')
            value_ = self.gds_validate_string(value_, node, 'ActualsVariable')
            self.ActualsVariable = value_
            self.ActualsVariable_nsprefix_ = child_.prefix
        elif nodeName_ == 'Type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Type')
            value_ = self.gds_validate_string(value_, node, 'Type')
            self.Type = value_
            self.Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'ToSimInd' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'ToSimInd')
            ival_ = self.gds_validate_integer(ival_, node, 'ToSimInd')
            self.ToSimInd = ival_
            self.ToSimInd_nsprefix_ = child_.prefix
        elif nodeName_ == 'SimCVStructural' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'SimCVStructural')
            fval_ = self.gds_validate_double(fval_, node, 'SimCVStructural')
            self.SimCVStructural = fval_
            self.SimCVStructural_nsprefix_ = child_.prefix
        elif nodeName_ == 'SimCVPerPeriod' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'SimCVPerPeriod')
            fval_ = self.gds_validate_double(fval_, node, 'SimCVPerPeriod')
            self.SimCVPerPeriod = fval_
            self.SimCVPerPeriod_nsprefix_ = child_.prefix
# end class UnitType


class StocksType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Handle=None, Number=None, MacroReturnNumber=None, FunctionReturnNumber=None, ParameterList=None, Stock=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        self.Number = Number
        self.Number_nsprefix_ = None
        self.MacroReturnNumber = MacroReturnNumber
        self.MacroReturnNumber_nsprefix_ = None
        self.FunctionReturnNumber = FunctionReturnNumber
        self.FunctionReturnNumber_nsprefix_ = None
        self.ParameterList = ParameterList
        self.ParameterList_nsprefix_ = None
        if Stock is None:
            self.Stock = []
        else:
            self.Stock = Stock
        self.Stock_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, StocksType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if StocksType.subclass:
            return StocksType.subclass(*args_, **kwargs_)
        else:
            return StocksType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Number(self):
        return self.Number
    def set_Number(self, Number):
        self.Number = Number
    def get_MacroReturnNumber(self):
        return self.MacroReturnNumber
    def set_MacroReturnNumber(self, MacroReturnNumber):
        self.MacroReturnNumber = MacroReturnNumber
    def get_FunctionReturnNumber(self):
        return self.FunctionReturnNumber
    def set_FunctionReturnNumber(self, FunctionReturnNumber):
        self.FunctionReturnNumber = FunctionReturnNumber
    def get_ParameterList(self):
        return self.ParameterList
    def set_ParameterList(self, ParameterList):
        self.ParameterList = ParameterList
    def get_Stock(self):
        return self.Stock
    def set_Stock(self, Stock):
        self.Stock = Stock
    def add_Stock(self, value):
        self.Stock.append(value)
    def insert_Stock_at(self, index, value):
        self.Stock.insert(index, value)
    def replace_Stock_at(self, index, value):
        self.Stock[index] = value
    def get_Handle(self):
        return self.Handle
    def set_Handle(self, Handle):
        self.Handle = Handle
    def _hasContent(self):
        if (
            self.Number is not None or
            self.MacroReturnNumber is not None or
            self.FunctionReturnNumber is not None or
            self.ParameterList is not None or
            self.Stock
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='StocksType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('StocksType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'StocksType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='StocksType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='StocksType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='StocksType'):
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='StocksType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Number is not None:
            namespaceprefix_ = self.Number_nsprefix_ + ':' if (UseCapturedNS_ and self.Number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumber>%s</%sNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.Number, input_name='Number'), namespaceprefix_ , eol_))
        if self.MacroReturnNumber is not None:
            namespaceprefix_ = self.MacroReturnNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.MacroReturnNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMacroReturnNumber>%s</%sMacroReturnNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.MacroReturnNumber, input_name='MacroReturnNumber'), namespaceprefix_ , eol_))
        if self.FunctionReturnNumber is not None:
            namespaceprefix_ = self.FunctionReturnNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.FunctionReturnNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sFunctionReturnNumber>%s</%sFunctionReturnNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.FunctionReturnNumber, input_name='FunctionReturnNumber'), namespaceprefix_ , eol_))
        if self.ParameterList is not None:
            namespaceprefix_ = self.ParameterList_nsprefix_ + ':' if (UseCapturedNS_ and self.ParameterList_nsprefix_) else ''
            self.ParameterList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParameterList', pretty_print=pretty_print)
        for Stock_ in self.Stock:
            namespaceprefix_ = self.Stock_nsprefix_ + ':' if (UseCapturedNS_ and self.Stock_nsprefix_) else ''
            Stock_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Stock', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='StocksType', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        if self.Handle is not None:
            element.set('Handle', self.gds_format_string(self.Handle))
        if self.Number is not None:
            Number_ = self.Number
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Number').text = self.gds_format_integer(Number_)
        if self.MacroReturnNumber is not None:
            MacroReturnNumber_ = self.MacroReturnNumber
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}MacroReturnNumber').text = self.gds_format_integer(MacroReturnNumber_)
        if self.FunctionReturnNumber is not None:
            FunctionReturnNumber_ = self.FunctionReturnNumber
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}FunctionReturnNumber').text = self.gds_format_integer(FunctionReturnNumber_)
        if self.ParameterList is not None:
            ParameterList_ = self.ParameterList
            ParameterList_.to_etree(element, name_='ParameterList', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        for Stock_ in self.Stock:
            Stock_.to_etree(element, name_='Stock', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        if reverse_mapping_ is not None:
            reverse_mapping_[element] = self
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Handle', node)
        if value is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            self.Handle = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Number' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Number')
            ival_ = self.gds_validate_integer(ival_, node, 'Number')
            self.Number = ival_
            self.Number_nsprefix_ = child_.prefix
        elif nodeName_ == 'MacroReturnNumber' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'MacroReturnNumber')
            ival_ = self.gds_validate_integer(ival_, node, 'MacroReturnNumber')
            self.MacroReturnNumber = ival_
            self.MacroReturnNumber_nsprefix_ = child_.prefix
        elif nodeName_ == 'FunctionReturnNumber' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'FunctionReturnNumber')
            ival_ = self.gds_validate_integer(ival_, node, 'FunctionReturnNumber')
            self.FunctionReturnNumber = ival_
            self.FunctionReturnNumber_nsprefix_ = child_.prefix
        elif nodeName_ == 'ParameterList':
            obj_ = ParameterListType3.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParameterList = obj_
            obj_.original_tagname_ = 'ParameterList'
        elif nodeName_ == 'Stock':
            obj_ = StockType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Stock.append(obj_)
            obj_.original_tagname_ = 'Stock'
# end class StocksType


class ParameterListType3(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Parameter=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Parameter is None:
            self.Parameter = []
        else:
            self.Parameter = Parameter
        self.Parameter_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParameterListType3)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParameterListType3.subclass:
            return ParameterListType3.subclass(*args_, **kwargs_)
        else:
            return ParameterListType3(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Parameter(self):
        return self.Parameter
    def set_Parameter(self, Parameter):
        self.Parameter = Parameter
    def add_Parameter(self, value):
        self.Parameter.append(value)
    def insert_Parameter_at(self, index, value):
        self.Parameter.insert(index, value)
    def replace_Parameter_at(self, index, value):
        self.Parameter[index] = value
    def _hasContent(self):
        if (
            self.Parameter
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ParameterListType3', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParameterListType3')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParameterListType3':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParameterListType3')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParameterListType3', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParameterListType3'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ParameterListType3', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Parameter_ in self.Parameter:
            namespaceprefix_ = self.Parameter_nsprefix_ + ':' if (UseCapturedNS_ and self.Parameter_nsprefix_) else ''
            Parameter_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Parameter', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ParameterListType3', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        for Parameter_ in self.Parameter:
            Parameter_.to_etree(element, name_='Parameter', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        if reverse_mapping_ is not None:
            reverse_mapping_[element] = self
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Parameter':
            obj_ = ParameterType4.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Parameter.append(obj_)
            obj_.original_tagname_ = 'Parameter'
# end class ParameterListType3


class ParameterType4(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, Type=None, Value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Type = _cast(None, Type)
        self.Type_nsprefix_ = None
        self.Value = Value
        self.Value_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParameterType4)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParameterType4.subclass:
            return ParameterType4.subclass(*args_, **kwargs_)
        else:
            return ParameterType4(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Value(self):
        return self.Value
    def set_Value(self, Value):
        self.Value = Value
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def get_Type(self):
        return self.Type
    def set_Type(self, Type):
        self.Type = Type
    def _hasContent(self):
        if (
            self.Value is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ParameterType4', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParameterType4')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParameterType4':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParameterType4')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParameterType4', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParameterType4'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Type is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            outfile.write(' Type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Type), input_name='Type')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ParameterType4', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Value is not None:
            namespaceprefix_ = self.Value_nsprefix_ + ':' if (UseCapturedNS_ and self.Value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValue>%s</%sValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Value), input_name='Value')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='ParameterType4', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        if self.Name is not None:
            element.set('Name', self.gds_format_string(self.Name))
        if self.Type is not None:
            element.set('Type', self.gds_format_string(self.Type))
        if self.Value is not None:
            Value_ = self.Value
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Value').text = self.gds_format_string(Value_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        if reverse_mapping_ is not None:
            reverse_mapping_[element] = self
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Name', node)
        if value is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            self.Name = value
        value = find_attr_value_('Type', node)
        if value is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            self.Type = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Value':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Value')
            value_ = self.gds_validate_string(value_, node, 'Value')
            self.Value = value_
            self.Value_nsprefix_ = child_.prefix
# end class ParameterType4


class StockType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, Mneumonic=None, Shorthand=None, Concept=None, ActualsVariable=None, Type=None, LaterUse=None, Treatment=None, FOutput=None, MOutput=None, ToSimInd=None, SimCV=None, NumberOfBases=None, Base1Type=None, Base1Variable=None, Base1IndexOrCode=None, Base1Weighting=None, Base2Type=None, Base2Variable=None, Base2IndexOrCode=None, Base2Weighting=None, Base3Type=None, Base3Variable=None, Base3IndexOrCode=None, Base3Weighting=None, Base4Type=None, Base4Variable=None, Base4IndexOrCode=None, Base4Weighting=None, Base5Type=None, Base5Variable=None, Base5IndexOrCode=None, Base5Weighting=None, Base6Type=None, Base6Variable=None, Base6IndexOrCode=None, Base6Weighting=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Position = _cast(int, Position)
        self.Position_nsprefix_ = None
        self.Mneumonic = Mneumonic
        self.Mneumonic_nsprefix_ = None
        self.Shorthand = Shorthand
        self.Shorthand_nsprefix_ = None
        self.Concept = Concept
        self.Concept_nsprefix_ = None
        self.ActualsVariable = ActualsVariable
        self.ActualsVariable_nsprefix_ = None
        self.Type = Type
        self.Type_nsprefix_ = None
        self.LaterUse = LaterUse
        self.LaterUse_nsprefix_ = None
        self.Treatment = Treatment
        self.Treatment_nsprefix_ = None
        self.FOutput = FOutput
        self.FOutput_nsprefix_ = None
        self.MOutput = MOutput
        self.MOutput_nsprefix_ = None
        self.ToSimInd = ToSimInd
        self.ToSimInd_nsprefix_ = None
        self.SimCV = SimCV
        self.SimCV_nsprefix_ = None
        self.NumberOfBases = NumberOfBases
        self.NumberOfBases_nsprefix_ = None
        self.Base1Type = Base1Type
        self.Base1Type_nsprefix_ = None
        self.Base1Variable = Base1Variable
        self.Base1Variable_nsprefix_ = None
        self.Base1IndexOrCode = Base1IndexOrCode
        self.Base1IndexOrCode_nsprefix_ = None
        self.Base1Weighting = Base1Weighting
        self.Base1Weighting_nsprefix_ = None
        self.Base2Type = Base2Type
        self.Base2Type_nsprefix_ = None
        self.Base2Variable = Base2Variable
        self.Base2Variable_nsprefix_ = None
        self.Base2IndexOrCode = Base2IndexOrCode
        self.Base2IndexOrCode_nsprefix_ = None
        self.Base2Weighting = Base2Weighting
        self.Base2Weighting_nsprefix_ = None
        self.Base3Type = Base3Type
        self.Base3Type_nsprefix_ = None
        self.Base3Variable = Base3Variable
        self.Base3Variable_nsprefix_ = None
        self.Base3IndexOrCode = Base3IndexOrCode
        self.Base3IndexOrCode_nsprefix_ = None
        self.Base3Weighting = Base3Weighting
        self.Base3Weighting_nsprefix_ = None
        self.Base4Type = Base4Type
        self.Base4Type_nsprefix_ = None
        self.Base4Variable = Base4Variable
        self.Base4Variable_nsprefix_ = None
        self.Base4IndexOrCode = Base4IndexOrCode
        self.Base4IndexOrCode_nsprefix_ = None
        self.Base4Weighting = Base4Weighting
        self.Base4Weighting_nsprefix_ = None
        self.Base5Type = Base5Type
        self.Base5Type_nsprefix_ = None
        self.Base5Variable = Base5Variable
        self.Base5Variable_nsprefix_ = None
        self.Base5IndexOrCode = Base5IndexOrCode
        self.Base5IndexOrCode_nsprefix_ = None
        self.Base5Weighting = Base5Weighting
        self.Base5Weighting_nsprefix_ = None
        self.Base6Type = Base6Type
        self.Base6Type_nsprefix_ = None
        self.Base6Variable = Base6Variable
        self.Base6Variable_nsprefix_ = None
        self.Base6IndexOrCode = Base6IndexOrCode
        self.Base6IndexOrCode_nsprefix_ = None
        self.Base6Weighting = Base6Weighting
        self.Base6Weighting_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, StockType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if StockType.subclass:
            return StockType.subclass(*args_, **kwargs_)
        else:
            return StockType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Mneumonic(self):
        return self.Mneumonic
    def set_Mneumonic(self, Mneumonic):
        self.Mneumonic = Mneumonic
    def get_Shorthand(self):
        return self.Shorthand
    def set_Shorthand(self, Shorthand):
        self.Shorthand = Shorthand
    def get_Concept(self):
        return self.Concept
    def set_Concept(self, Concept):
        self.Concept = Concept
    def get_ActualsVariable(self):
        return self.ActualsVariable
    def set_ActualsVariable(self, ActualsVariable):
        self.ActualsVariable = ActualsVariable
    def get_Type(self):
        return self.Type
    def set_Type(self, Type):
        self.Type = Type
    def get_LaterUse(self):
        return self.LaterUse
    def set_LaterUse(self, LaterUse):
        self.LaterUse = LaterUse
    def get_Treatment(self):
        return self.Treatment
    def set_Treatment(self, Treatment):
        self.Treatment = Treatment
    def get_FOutput(self):
        return self.FOutput
    def set_FOutput(self, FOutput):
        self.FOutput = FOutput
    def get_MOutput(self):
        return self.MOutput
    def set_MOutput(self, MOutput):
        self.MOutput = MOutput
    def get_ToSimInd(self):
        return self.ToSimInd
    def set_ToSimInd(self, ToSimInd):
        self.ToSimInd = ToSimInd
    def get_SimCV(self):
        return self.SimCV
    def set_SimCV(self, SimCV):
        self.SimCV = SimCV
    def get_NumberOfBases(self):
        return self.NumberOfBases
    def set_NumberOfBases(self, NumberOfBases):
        self.NumberOfBases = NumberOfBases
    def get_Base1Type(self):
        return self.Base1Type
    def set_Base1Type(self, Base1Type):
        self.Base1Type = Base1Type
    def get_Base1Variable(self):
        return self.Base1Variable
    def set_Base1Variable(self, Base1Variable):
        self.Base1Variable = Base1Variable
    def get_Base1IndexOrCode(self):
        return self.Base1IndexOrCode
    def set_Base1IndexOrCode(self, Base1IndexOrCode):
        self.Base1IndexOrCode = Base1IndexOrCode
    def get_Base1Weighting(self):
        return self.Base1Weighting
    def set_Base1Weighting(self, Base1Weighting):
        self.Base1Weighting = Base1Weighting
    def get_Base2Type(self):
        return self.Base2Type
    def set_Base2Type(self, Base2Type):
        self.Base2Type = Base2Type
    def get_Base2Variable(self):
        return self.Base2Variable
    def set_Base2Variable(self, Base2Variable):
        self.Base2Variable = Base2Variable
    def get_Base2IndexOrCode(self):
        return self.Base2IndexOrCode
    def set_Base2IndexOrCode(self, Base2IndexOrCode):
        self.Base2IndexOrCode = Base2IndexOrCode
    def get_Base2Weighting(self):
        return self.Base2Weighting
    def set_Base2Weighting(self, Base2Weighting):
        self.Base2Weighting = Base2Weighting
    def get_Base3Type(self):
        return self.Base3Type
    def set_Base3Type(self, Base3Type):
        self.Base3Type = Base3Type
    def get_Base3Variable(self):
        return self.Base3Variable
    def set_Base3Variable(self, Base3Variable):
        self.Base3Variable = Base3Variable
    def get_Base3IndexOrCode(self):
        return self.Base3IndexOrCode
    def set_Base3IndexOrCode(self, Base3IndexOrCode):
        self.Base3IndexOrCode = Base3IndexOrCode
    def get_Base3Weighting(self):
        return self.Base3Weighting
    def set_Base3Weighting(self, Base3Weighting):
        self.Base3Weighting = Base3Weighting
    def get_Base4Type(self):
        return self.Base4Type
    def set_Base4Type(self, Base4Type):
        self.Base4Type = Base4Type
    def get_Base4Variable(self):
        return self.Base4Variable
    def set_Base4Variable(self, Base4Variable):
        self.Base4Variable = Base4Variable
    def get_Base4IndexOrCode(self):
        return self.Base4IndexOrCode
    def set_Base4IndexOrCode(self, Base4IndexOrCode):
        self.Base4IndexOrCode = Base4IndexOrCode
    def get_Base4Weighting(self):
        return self.Base4Weighting
    def set_Base4Weighting(self, Base4Weighting):
        self.Base4Weighting = Base4Weighting
    def get_Base5Type(self):
        return self.Base5Type
    def set_Base5Type(self, Base5Type):
        self.Base5Type = Base5Type
    def get_Base5Variable(self):
        return self.Base5Variable
    def set_Base5Variable(self, Base5Variable):
        self.Base5Variable = Base5Variable
    def get_Base5IndexOrCode(self):
        return self.Base5IndexOrCode
    def set_Base5IndexOrCode(self, Base5IndexOrCode):
        self.Base5IndexOrCode = Base5IndexOrCode
    def get_Base5Weighting(self):
        return self.Base5Weighting
    def set_Base5Weighting(self, Base5Weighting):
        self.Base5Weighting = Base5Weighting
    def get_Base6Type(self):
        return self.Base6Type
    def set_Base6Type(self, Base6Type):
        self.Base6Type = Base6Type
    def get_Base6Variable(self):
        return self.Base6Variable
    def set_Base6Variable(self, Base6Variable):
        self.Base6Variable = Base6Variable
    def get_Base6IndexOrCode(self):
        return self.Base6IndexOrCode
    def set_Base6IndexOrCode(self, Base6IndexOrCode):
        self.Base6IndexOrCode = Base6IndexOrCode
    def get_Base6Weighting(self):
        return self.Base6Weighting
    def set_Base6Weighting(self, Base6Weighting):
        self.Base6Weighting = Base6Weighting
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def _hasContent(self):
        if (
            self.Mneumonic is not None or
            self.Shorthand is not None or
            self.Concept is not None or
            self.ActualsVariable is not None or
            self.Type is not None or
            self.LaterUse is not None or
            self.Treatment is not None or
            self.FOutput is not None or
            self.MOutput is not None or
            self.ToSimInd is not None or
            self.SimCV is not None or
            self.NumberOfBases is not None or
            self.Base1Type is not None or
            self.Base1Variable is not None or
            self.Base1IndexOrCode is not None or
            self.Base1Weighting is not None or
            self.Base2Type is not None or
            self.Base2Variable is not None or
            self.Base2IndexOrCode is not None or
            self.Base2Weighting is not None or
            self.Base3Type is not None or
            self.Base3Variable is not None or
            self.Base3IndexOrCode is not None or
            self.Base3Weighting is not None or
            self.Base4Type is not None or
            self.Base4Variable is not None or
            self.Base4IndexOrCode is not None or
            self.Base4Weighting is not None or
            self.Base5Type is not None or
            self.Base5Variable is not None or
            self.Base5IndexOrCode is not None or
            self.Base5Weighting is not None or
            self.Base6Type is not None or
            self.Base6Variable is not None or
            self.Base6IndexOrCode is not None or
            self.Base6Weighting is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='StockType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('StockType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'StockType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='StockType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='StockType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='StockType'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position="%s"' % self.gds_format_integer(self.Position, input_name='Position'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='StockType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Mneumonic is not None:
            namespaceprefix_ = self.Mneumonic_nsprefix_ + ':' if (UseCapturedNS_ and self.Mneumonic_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMneumonic>%s</%sMneumonic>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Mneumonic), input_name='Mneumonic')), namespaceprefix_ , eol_))
        if self.Shorthand is not None:
            namespaceprefix_ = self.Shorthand_nsprefix_ + ':' if (UseCapturedNS_ and self.Shorthand_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sShorthand>%s</%sShorthand>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Shorthand), input_name='Shorthand')), namespaceprefix_ , eol_))
        if self.Concept is not None:
            namespaceprefix_ = self.Concept_nsprefix_ + ':' if (UseCapturedNS_ and self.Concept_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sConcept>%s</%sConcept>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Concept), input_name='Concept')), namespaceprefix_ , eol_))
        if self.ActualsVariable is not None:
            namespaceprefix_ = self.ActualsVariable_nsprefix_ + ':' if (UseCapturedNS_ and self.ActualsVariable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sActualsVariable>%s</%sActualsVariable>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ActualsVariable), input_name='ActualsVariable')), namespaceprefix_ , eol_))
        if self.Type is not None:
            namespaceprefix_ = self.Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sType>%s</%sType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Type), input_name='Type')), namespaceprefix_ , eol_))
        if self.LaterUse is not None:
            namespaceprefix_ = self.LaterUse_nsprefix_ + ':' if (UseCapturedNS_ and self.LaterUse_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sLaterUse>%s</%sLaterUse>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.LaterUse), input_name='LaterUse')), namespaceprefix_ , eol_))
        if self.Treatment is not None:
            namespaceprefix_ = self.Treatment_nsprefix_ + ':' if (UseCapturedNS_ and self.Treatment_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTreatment>%s</%sTreatment>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Treatment), input_name='Treatment')), namespaceprefix_ , eol_))
        if self.FOutput is not None:
            namespaceprefix_ = self.FOutput_nsprefix_ + ':' if (UseCapturedNS_ and self.FOutput_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sFOutput>%s</%sFOutput>%s' % (namespaceprefix_ , self.gds_format_integer(self.FOutput, input_name='FOutput'), namespaceprefix_ , eol_))
        if self.MOutput is not None:
            namespaceprefix_ = self.MOutput_nsprefix_ + ':' if (UseCapturedNS_ and self.MOutput_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMOutput>%s</%sMOutput>%s' % (namespaceprefix_ , self.gds_format_integer(self.MOutput, input_name='MOutput'), namespaceprefix_ , eol_))
        if self.ToSimInd is not None:
            namespaceprefix_ = self.ToSimInd_nsprefix_ + ':' if (UseCapturedNS_ and self.ToSimInd_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sToSimInd>%s</%sToSimInd>%s' % (namespaceprefix_ , self.gds_format_integer(self.ToSimInd, input_name='ToSimInd'), namespaceprefix_ , eol_))
        if self.SimCV is not None:
            namespaceprefix_ = self.SimCV_nsprefix_ + ':' if (UseCapturedNS_ and self.SimCV_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSimCV>%s</%sSimCV>%s' % (namespaceprefix_ , self.gds_format_double(self.SimCV, input_name='SimCV'), namespaceprefix_ , eol_))
        if self.NumberOfBases is not None:
            namespaceprefix_ = self.NumberOfBases_nsprefix_ + ':' if (UseCapturedNS_ and self.NumberOfBases_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumberOfBases>%s</%sNumberOfBases>%s' % (namespaceprefix_ , self.gds_format_integer(self.NumberOfBases, input_name='NumberOfBases'), namespaceprefix_ , eol_))
        if self.Base1Type is not None:
            namespaceprefix_ = self.Base1Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Base1Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase1Type>%s</%sBase1Type>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base1Type, input_name='Base1Type'), namespaceprefix_ , eol_))
        if self.Base1Variable is not None:
            namespaceprefix_ = self.Base1Variable_nsprefix_ + ':' if (UseCapturedNS_ and self.Base1Variable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase1Variable>%s</%sBase1Variable>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Base1Variable), input_name='Base1Variable')), namespaceprefix_ , eol_))
        if self.Base1IndexOrCode is not None:
            namespaceprefix_ = self.Base1IndexOrCode_nsprefix_ + ':' if (UseCapturedNS_ and self.Base1IndexOrCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase1IndexOrCode>%s</%sBase1IndexOrCode>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base1IndexOrCode, input_name='Base1IndexOrCode'), namespaceprefix_ , eol_))
        if self.Base1Weighting is not None:
            namespaceprefix_ = self.Base1Weighting_nsprefix_ + ':' if (UseCapturedNS_ and self.Base1Weighting_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase1Weighting>%s</%sBase1Weighting>%s' % (namespaceprefix_ , self.gds_format_double(self.Base1Weighting, input_name='Base1Weighting'), namespaceprefix_ , eol_))
        if self.Base2Type is not None:
            namespaceprefix_ = self.Base2Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Base2Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase2Type>%s</%sBase2Type>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base2Type, input_name='Base2Type'), namespaceprefix_ , eol_))
        if self.Base2Variable is not None:
            namespaceprefix_ = self.Base2Variable_nsprefix_ + ':' if (UseCapturedNS_ and self.Base2Variable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase2Variable>%s</%sBase2Variable>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Base2Variable), input_name='Base2Variable')), namespaceprefix_ , eol_))
        if self.Base2IndexOrCode is not None:
            namespaceprefix_ = self.Base2IndexOrCode_nsprefix_ + ':' if (UseCapturedNS_ and self.Base2IndexOrCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase2IndexOrCode>%s</%sBase2IndexOrCode>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base2IndexOrCode, input_name='Base2IndexOrCode'), namespaceprefix_ , eol_))
        if self.Base2Weighting is not None:
            namespaceprefix_ = self.Base2Weighting_nsprefix_ + ':' if (UseCapturedNS_ and self.Base2Weighting_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase2Weighting>%s</%sBase2Weighting>%s' % (namespaceprefix_ , self.gds_format_double(self.Base2Weighting, input_name='Base2Weighting'), namespaceprefix_ , eol_))
        if self.Base3Type is not None:
            namespaceprefix_ = self.Base3Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Base3Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase3Type>%s</%sBase3Type>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base3Type, input_name='Base3Type'), namespaceprefix_ , eol_))
        if self.Base3Variable is not None:
            namespaceprefix_ = self.Base3Variable_nsprefix_ + ':' if (UseCapturedNS_ and self.Base3Variable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase3Variable>%s</%sBase3Variable>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Base3Variable), input_name='Base3Variable')), namespaceprefix_ , eol_))
        if self.Base3IndexOrCode is not None:
            namespaceprefix_ = self.Base3IndexOrCode_nsprefix_ + ':' if (UseCapturedNS_ and self.Base3IndexOrCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase3IndexOrCode>%s</%sBase3IndexOrCode>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base3IndexOrCode, input_name='Base3IndexOrCode'), namespaceprefix_ , eol_))
        if self.Base3Weighting is not None:
            namespaceprefix_ = self.Base3Weighting_nsprefix_ + ':' if (UseCapturedNS_ and self.Base3Weighting_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase3Weighting>%s</%sBase3Weighting>%s' % (namespaceprefix_ , self.gds_format_double(self.Base3Weighting, input_name='Base3Weighting'), namespaceprefix_ , eol_))
        if self.Base4Type is not None:
            namespaceprefix_ = self.Base4Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Base4Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase4Type>%s</%sBase4Type>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base4Type, input_name='Base4Type'), namespaceprefix_ , eol_))
        if self.Base4Variable is not None:
            namespaceprefix_ = self.Base4Variable_nsprefix_ + ':' if (UseCapturedNS_ and self.Base4Variable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase4Variable>%s</%sBase4Variable>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Base4Variable), input_name='Base4Variable')), namespaceprefix_ , eol_))
        if self.Base4IndexOrCode is not None:
            namespaceprefix_ = self.Base4IndexOrCode_nsprefix_ + ':' if (UseCapturedNS_ and self.Base4IndexOrCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase4IndexOrCode>%s</%sBase4IndexOrCode>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base4IndexOrCode, input_name='Base4IndexOrCode'), namespaceprefix_ , eol_))
        if self.Base4Weighting is not None:
            namespaceprefix_ = self.Base4Weighting_nsprefix_ + ':' if (UseCapturedNS_ and self.Base4Weighting_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase4Weighting>%s</%sBase4Weighting>%s' % (namespaceprefix_ , self.gds_format_double(self.Base4Weighting, input_name='Base4Weighting'), namespaceprefix_ , eol_))
        if self.Base5Type is not None:
            namespaceprefix_ = self.Base5Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Base5Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase5Type>%s</%sBase5Type>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base5Type, input_name='Base5Type'), namespaceprefix_ , eol_))
        if self.Base5Variable is not None:
            namespaceprefix_ = self.Base5Variable_nsprefix_ + ':' if (UseCapturedNS_ and self.Base5Variable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase5Variable>%s</%sBase5Variable>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Base5Variable), input_name='Base5Variable')), namespaceprefix_ , eol_))
        if self.Base5IndexOrCode is not None:
            namespaceprefix_ = self.Base5IndexOrCode_nsprefix_ + ':' if (UseCapturedNS_ and self.Base5IndexOrCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase5IndexOrCode>%s</%sBase5IndexOrCode>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base5IndexOrCode, input_name='Base5IndexOrCode'), namespaceprefix_ , eol_))
        if self.Base5Weighting is not None:
            namespaceprefix_ = self.Base5Weighting_nsprefix_ + ':' if (UseCapturedNS_ and self.Base5Weighting_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase5Weighting>%s</%sBase5Weighting>%s' % (namespaceprefix_ , self.gds_format_double(self.Base5Weighting, input_name='Base5Weighting'), namespaceprefix_ , eol_))
        if self.Base6Type is not None:
            namespaceprefix_ = self.Base6Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Base6Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase6Type>%s</%sBase6Type>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base6Type, input_name='Base6Type'), namespaceprefix_ , eol_))
        if self.Base6Variable is not None:
            namespaceprefix_ = self.Base6Variable_nsprefix_ + ':' if (UseCapturedNS_ and self.Base6Variable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase6Variable>%s</%sBase6Variable>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Base6Variable), input_name='Base6Variable')), namespaceprefix_ , eol_))
        if self.Base6IndexOrCode is not None:
            namespaceprefix_ = self.Base6IndexOrCode_nsprefix_ + ':' if (UseCapturedNS_ and self.Base6IndexOrCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase6IndexOrCode>%s</%sBase6IndexOrCode>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base6IndexOrCode, input_name='Base6IndexOrCode'), namespaceprefix_ , eol_))
        if self.Base6Weighting is not None:
            namespaceprefix_ = self.Base6Weighting_nsprefix_ + ':' if (UseCapturedNS_ and self.Base6Weighting_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase6Weighting>%s</%sBase6Weighting>%s' % (namespaceprefix_ , self.gds_format_double(self.Base6Weighting, input_name='Base6Weighting'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='StockType', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        if self.Position is not None:
            element.set('Position', self.gds_format_integer(self.Position))
        if self.Mneumonic is not None:
            Mneumonic_ = self.Mneumonic
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Mneumonic').text = self.gds_format_string(Mneumonic_)
        if self.Shorthand is not None:
            Shorthand_ = self.Shorthand
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Shorthand').text = self.gds_format_string(Shorthand_)
        if self.Concept is not None:
            Concept_ = self.Concept
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Concept').text = self.gds_format_string(Concept_)
        if self.ActualsVariable is not None:
            ActualsVariable_ = self.ActualsVariable
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}ActualsVariable').text = self.gds_format_string(ActualsVariable_)
        if self.Type is not None:
            Type_ = self.Type
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Type').text = self.gds_format_string(Type_)
        if self.LaterUse is not None:
            LaterUse_ = self.LaterUse
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}LaterUse').text = self.gds_format_string(LaterUse_)
        if self.Treatment is not None:
            Treatment_ = self.Treatment
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Treatment').text = self.gds_format_string(Treatment_)
        if self.FOutput is not None:
            FOutput_ = self.FOutput
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}FOutput').text = self.gds_format_integer(FOutput_)
        if self.MOutput is not None:
            MOutput_ = self.MOutput
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}MOutput').text = self.gds_format_integer(MOutput_)
        if self.ToSimInd is not None:
            ToSimInd_ = self.ToSimInd
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}ToSimInd').text = self.gds_format_integer(ToSimInd_)
        if self.SimCV is not None:
            SimCV_ = self.SimCV
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}SimCV').text = self.gds_format_double(SimCV_)
        if self.NumberOfBases is not None:
            NumberOfBases_ = self.NumberOfBases
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}NumberOfBases').text = self.gds_format_integer(NumberOfBases_)
        if self.Base1Type is not None:
            Base1Type_ = self.Base1Type
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base1Type').text = self.gds_format_integer(Base1Type_)
        if self.Base1Variable is not None:
            Base1Variable_ = self.Base1Variable
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base1Variable').text = self.gds_format_string(Base1Variable_)
        if self.Base1IndexOrCode is not None:
            Base1IndexOrCode_ = self.Base1IndexOrCode
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base1IndexOrCode').text = self.gds_format_integer(Base1IndexOrCode_)
        if self.Base1Weighting is not None:
            Base1Weighting_ = self.Base1Weighting
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base1Weighting').text = self.gds_format_double(Base1Weighting_)
        if self.Base2Type is not None:
            Base2Type_ = self.Base2Type
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base2Type').text = self.gds_format_integer(Base2Type_)
        if self.Base2Variable is not None:
            Base2Variable_ = self.Base2Variable
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base2Variable').text = self.gds_format_string(Base2Variable_)
        if self.Base2IndexOrCode is not None:
            Base2IndexOrCode_ = self.Base2IndexOrCode
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base2IndexOrCode').text = self.gds_format_integer(Base2IndexOrCode_)
        if self.Base2Weighting is not None:
            Base2Weighting_ = self.Base2Weighting
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base2Weighting').text = self.gds_format_double(Base2Weighting_)
        if self.Base3Type is not None:
            Base3Type_ = self.Base3Type
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base3Type').text = self.gds_format_integer(Base3Type_)
        if self.Base3Variable is not None:
            Base3Variable_ = self.Base3Variable
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base3Variable').text = self.gds_format_string(Base3Variable_)
        if self.Base3IndexOrCode is not None:
            Base3IndexOrCode_ = self.Base3IndexOrCode
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base3IndexOrCode').text = self.gds_format_integer(Base3IndexOrCode_)
        if self.Base3Weighting is not None:
            Base3Weighting_ = self.Base3Weighting
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base3Weighting').text = self.gds_format_double(Base3Weighting_)
        if self.Base4Type is not None:
            Base4Type_ = self.Base4Type
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base4Type').text = self.gds_format_integer(Base4Type_)
        if self.Base4Variable is not None:
            Base4Variable_ = self.Base4Variable
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base4Variable').text = self.gds_format_string(Base4Variable_)
        if self.Base4IndexOrCode is not None:
            Base4IndexOrCode_ = self.Base4IndexOrCode
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base4IndexOrCode').text = self.gds_format_integer(Base4IndexOrCode_)
        if self.Base4Weighting is not None:
            Base4Weighting_ = self.Base4Weighting
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base4Weighting').text = self.gds_format_double(Base4Weighting_)
        if self.Base5Type is not None:
            Base5Type_ = self.Base5Type
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base5Type').text = self.gds_format_integer(Base5Type_)
        if self.Base5Variable is not None:
            Base5Variable_ = self.Base5Variable
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base5Variable').text = self.gds_format_string(Base5Variable_)
        if self.Base5IndexOrCode is not None:
            Base5IndexOrCode_ = self.Base5IndexOrCode
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base5IndexOrCode').text = self.gds_format_integer(Base5IndexOrCode_)
        if self.Base5Weighting is not None:
            Base5Weighting_ = self.Base5Weighting
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base5Weighting').text = self.gds_format_double(Base5Weighting_)
        if self.Base6Type is not None:
            Base6Type_ = self.Base6Type
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base6Type').text = self.gds_format_integer(Base6Type_)
        if self.Base6Variable is not None:
            Base6Variable_ = self.Base6Variable
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base6Variable').text = self.gds_format_string(Base6Variable_)
        if self.Base6IndexOrCode is not None:
            Base6IndexOrCode_ = self.Base6IndexOrCode
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base6IndexOrCode').text = self.gds_format_integer(Base6IndexOrCode_)
        if self.Base6Weighting is not None:
            Base6Weighting_ = self.Base6Weighting
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base6Weighting').text = self.gds_format_double(Base6Weighting_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        if reverse_mapping_ is not None:
            reverse_mapping_[element] = self
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Position', node)
        if value is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            self.Position = self.gds_parse_integer(value, node, 'Position')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Mneumonic':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Mneumonic')
            value_ = self.gds_validate_string(value_, node, 'Mneumonic')
            self.Mneumonic = value_
            self.Mneumonic_nsprefix_ = child_.prefix
        elif nodeName_ == 'Shorthand':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Shorthand')
            value_ = self.gds_validate_string(value_, node, 'Shorthand')
            self.Shorthand = value_
            self.Shorthand_nsprefix_ = child_.prefix
        elif nodeName_ == 'Concept':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Concept')
            value_ = self.gds_validate_string(value_, node, 'Concept')
            self.Concept = value_
            self.Concept_nsprefix_ = child_.prefix
        elif nodeName_ == 'ActualsVariable':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ActualsVariable')
            value_ = self.gds_validate_string(value_, node, 'ActualsVariable')
            self.ActualsVariable = value_
            self.ActualsVariable_nsprefix_ = child_.prefix
        elif nodeName_ == 'Type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Type')
            value_ = self.gds_validate_string(value_, node, 'Type')
            self.Type = value_
            self.Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'LaterUse':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'LaterUse')
            value_ = self.gds_validate_string(value_, node, 'LaterUse')
            self.LaterUse = value_
            self.LaterUse_nsprefix_ = child_.prefix
        elif nodeName_ == 'Treatment':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Treatment')
            value_ = self.gds_validate_string(value_, node, 'Treatment')
            self.Treatment = value_
            self.Treatment_nsprefix_ = child_.prefix
        elif nodeName_ == 'FOutput' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'FOutput')
            ival_ = self.gds_validate_integer(ival_, node, 'FOutput')
            self.FOutput = ival_
            self.FOutput_nsprefix_ = child_.prefix
        elif nodeName_ == 'MOutput' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'MOutput')
            ival_ = self.gds_validate_integer(ival_, node, 'MOutput')
            self.MOutput = ival_
            self.MOutput_nsprefix_ = child_.prefix
        elif nodeName_ == 'ToSimInd' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'ToSimInd')
            ival_ = self.gds_validate_integer(ival_, node, 'ToSimInd')
            self.ToSimInd = ival_
            self.ToSimInd_nsprefix_ = child_.prefix
        elif nodeName_ == 'SimCV' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'SimCV')
            fval_ = self.gds_validate_double(fval_, node, 'SimCV')
            self.SimCV = fval_
            self.SimCV_nsprefix_ = child_.prefix
        elif nodeName_ == 'NumberOfBases' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NumberOfBases')
            ival_ = self.gds_validate_integer(ival_, node, 'NumberOfBases')
            self.NumberOfBases = ival_
            self.NumberOfBases_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base1Type' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base1Type')
            ival_ = self.gds_validate_integer(ival_, node, 'Base1Type')
            self.Base1Type = ival_
            self.Base1Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base1Variable':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Base1Variable')
            value_ = self.gds_validate_string(value_, node, 'Base1Variable')
            self.Base1Variable = value_
            self.Base1Variable_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base1IndexOrCode' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base1IndexOrCode')
            ival_ = self.gds_validate_integer(ival_, node, 'Base1IndexOrCode')
            self.Base1IndexOrCode = ival_
            self.Base1IndexOrCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base1Weighting' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Base1Weighting')
            fval_ = self.gds_validate_double(fval_, node, 'Base1Weighting')
            self.Base1Weighting = fval_
            self.Base1Weighting_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base2Type' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base2Type')
            ival_ = self.gds_validate_integer(ival_, node, 'Base2Type')
            self.Base2Type = ival_
            self.Base2Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base2Variable':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Base2Variable')
            value_ = self.gds_validate_string(value_, node, 'Base2Variable')
            self.Base2Variable = value_
            self.Base2Variable_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base2IndexOrCode' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base2IndexOrCode')
            ival_ = self.gds_validate_integer(ival_, node, 'Base2IndexOrCode')
            self.Base2IndexOrCode = ival_
            self.Base2IndexOrCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base2Weighting' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Base2Weighting')
            fval_ = self.gds_validate_double(fval_, node, 'Base2Weighting')
            self.Base2Weighting = fval_
            self.Base2Weighting_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base3Type' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base3Type')
            ival_ = self.gds_validate_integer(ival_, node, 'Base3Type')
            self.Base3Type = ival_
            self.Base3Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base3Variable':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Base3Variable')
            value_ = self.gds_validate_string(value_, node, 'Base3Variable')
            self.Base3Variable = value_
            self.Base3Variable_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base3IndexOrCode' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base3IndexOrCode')
            ival_ = self.gds_validate_integer(ival_, node, 'Base3IndexOrCode')
            self.Base3IndexOrCode = ival_
            self.Base3IndexOrCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base3Weighting' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Base3Weighting')
            fval_ = self.gds_validate_double(fval_, node, 'Base3Weighting')
            self.Base3Weighting = fval_
            self.Base3Weighting_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base4Type' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base4Type')
            ival_ = self.gds_validate_integer(ival_, node, 'Base4Type')
            self.Base4Type = ival_
            self.Base4Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base4Variable':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Base4Variable')
            value_ = self.gds_validate_string(value_, node, 'Base4Variable')
            self.Base4Variable = value_
            self.Base4Variable_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base4IndexOrCode' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base4IndexOrCode')
            ival_ = self.gds_validate_integer(ival_, node, 'Base4IndexOrCode')
            self.Base4IndexOrCode = ival_
            self.Base4IndexOrCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base4Weighting' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Base4Weighting')
            fval_ = self.gds_validate_double(fval_, node, 'Base4Weighting')
            self.Base4Weighting = fval_
            self.Base4Weighting_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base5Type' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base5Type')
            ival_ = self.gds_validate_integer(ival_, node, 'Base5Type')
            self.Base5Type = ival_
            self.Base5Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base5Variable':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Base5Variable')
            value_ = self.gds_validate_string(value_, node, 'Base5Variable')
            self.Base5Variable = value_
            self.Base5Variable_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base5IndexOrCode' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base5IndexOrCode')
            ival_ = self.gds_validate_integer(ival_, node, 'Base5IndexOrCode')
            self.Base5IndexOrCode = ival_
            self.Base5IndexOrCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base5Weighting' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Base5Weighting')
            fval_ = self.gds_validate_double(fval_, node, 'Base5Weighting')
            self.Base5Weighting = fval_
            self.Base5Weighting_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base6Type' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base6Type')
            ival_ = self.gds_validate_integer(ival_, node, 'Base6Type')
            self.Base6Type = ival_
            self.Base6Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base6Variable':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Base6Variable')
            value_ = self.gds_validate_string(value_, node, 'Base6Variable')
            self.Base6Variable = value_
            self.Base6Variable_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base6IndexOrCode' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base6IndexOrCode')
            ival_ = self.gds_validate_integer(ival_, node, 'Base6IndexOrCode')
            self.Base6IndexOrCode = ival_
            self.Base6IndexOrCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base6Weighting' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Base6Weighting')
            fval_ = self.gds_validate_double(fval_, node, 'Base6Weighting')
            self.Base6Weighting = fval_
            self.Base6Weighting_nsprefix_ = child_.prefix
# end class StockType


class FlowsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Handle=None, Number=None, MacroReturnNumber=None, FunctionReturnNumber=None, ParameterList=None, Flow=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        self.Number = Number
        self.Number_nsprefix_ = None
        self.MacroReturnNumber = MacroReturnNumber
        self.MacroReturnNumber_nsprefix_ = None
        self.FunctionReturnNumber = FunctionReturnNumber
        self.FunctionReturnNumber_nsprefix_ = None
        self.ParameterList = ParameterList
        self.ParameterList_nsprefix_ = None
        if Flow is None:
            self.Flow = []
        else:
            self.Flow = Flow
        self.Flow_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, FlowsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if FlowsType.subclass:
            return FlowsType.subclass(*args_, **kwargs_)
        else:
            return FlowsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Number(self):
        return self.Number
    def set_Number(self, Number):
        self.Number = Number
    def get_MacroReturnNumber(self):
        return self.MacroReturnNumber
    def set_MacroReturnNumber(self, MacroReturnNumber):
        self.MacroReturnNumber = MacroReturnNumber
    def get_FunctionReturnNumber(self):
        return self.FunctionReturnNumber
    def set_FunctionReturnNumber(self, FunctionReturnNumber):
        self.FunctionReturnNumber = FunctionReturnNumber
    def get_ParameterList(self):
        return self.ParameterList
    def set_ParameterList(self, ParameterList):
        self.ParameterList = ParameterList
    def get_Flow(self):
        return self.Flow
    def set_Flow(self, Flow):
        self.Flow = Flow
    def add_Flow(self, value):
        self.Flow.append(value)
    def insert_Flow_at(self, index, value):
        self.Flow.insert(index, value)
    def replace_Flow_at(self, index, value):
        self.Flow[index] = value
    def get_Handle(self):
        return self.Handle
    def set_Handle(self, Handle):
        self.Handle = Handle
    def _hasContent(self):
        if (
            self.Number is not None or
            self.MacroReturnNumber is not None or
            self.FunctionReturnNumber is not None or
            self.ParameterList is not None or
            self.Flow
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='FlowsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('FlowsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'FlowsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='FlowsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='FlowsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='FlowsType'):
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='FlowsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Number is not None:
            namespaceprefix_ = self.Number_nsprefix_ + ':' if (UseCapturedNS_ and self.Number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumber>%s</%sNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.Number, input_name='Number'), namespaceprefix_ , eol_))
        if self.MacroReturnNumber is not None:
            namespaceprefix_ = self.MacroReturnNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.MacroReturnNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMacroReturnNumber>%s</%sMacroReturnNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.MacroReturnNumber, input_name='MacroReturnNumber'), namespaceprefix_ , eol_))
        if self.FunctionReturnNumber is not None:
            namespaceprefix_ = self.FunctionReturnNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.FunctionReturnNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sFunctionReturnNumber>%s</%sFunctionReturnNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.FunctionReturnNumber, input_name='FunctionReturnNumber'), namespaceprefix_ , eol_))
        if self.ParameterList is not None:
            namespaceprefix_ = self.ParameterList_nsprefix_ + ':' if (UseCapturedNS_ and self.ParameterList_nsprefix_) else ''
            self.ParameterList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParameterList', pretty_print=pretty_print)
        for Flow_ in self.Flow:
            namespaceprefix_ = self.Flow_nsprefix_ + ':' if (UseCapturedNS_ and self.Flow_nsprefix_) else ''
            Flow_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Flow', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='FlowsType', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        if self.Handle is not None:
            element.set('Handle', self.gds_format_string(self.Handle))
        if self.Number is not None:
            Number_ = self.Number
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Number').text = self.gds_format_integer(Number_)
        if self.MacroReturnNumber is not None:
            MacroReturnNumber_ = self.MacroReturnNumber
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}MacroReturnNumber').text = self.gds_format_integer(MacroReturnNumber_)
        if self.FunctionReturnNumber is not None:
            FunctionReturnNumber_ = self.FunctionReturnNumber
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}FunctionReturnNumber').text = self.gds_format_integer(FunctionReturnNumber_)
        if self.ParameterList is not None:
            ParameterList_ = self.ParameterList
            ParameterList_.to_etree(element, name_='ParameterList', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        for Flow_ in self.Flow:
            Flow_.to_etree(element, name_='Flow', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        if reverse_mapping_ is not None:
            reverse_mapping_[element] = self
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Handle', node)
        if value is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            self.Handle = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Number' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Number')
            ival_ = self.gds_validate_integer(ival_, node, 'Number')
            self.Number = ival_
            self.Number_nsprefix_ = child_.prefix
        elif nodeName_ == 'MacroReturnNumber' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'MacroReturnNumber')
            ival_ = self.gds_validate_integer(ival_, node, 'MacroReturnNumber')
            self.MacroReturnNumber = ival_
            self.MacroReturnNumber_nsprefix_ = child_.prefix
        elif nodeName_ == 'FunctionReturnNumber' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'FunctionReturnNumber')
            ival_ = self.gds_validate_integer(ival_, node, 'FunctionReturnNumber')
            self.FunctionReturnNumber = ival_
            self.FunctionReturnNumber_nsprefix_ = child_.prefix
        elif nodeName_ == 'ParameterList':
            obj_ = ParameterListType5.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParameterList = obj_
            obj_.original_tagname_ = 'ParameterList'
        elif nodeName_ == 'Flow':
            obj_ = FlowType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Flow.append(obj_)
            obj_.original_tagname_ = 'Flow'
# end class FlowsType


class ParameterListType5(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Parameter=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Parameter is None:
            self.Parameter = []
        else:
            self.Parameter = Parameter
        self.Parameter_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParameterListType5)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParameterListType5.subclass:
            return ParameterListType5.subclass(*args_, **kwargs_)
        else:
            return ParameterListType5(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Parameter(self):
        return self.Parameter
    def set_Parameter(self, Parameter):
        self.Parameter = Parameter
    def add_Parameter(self, value):
        self.Parameter.append(value)
    def insert_Parameter_at(self, index, value):
        self.Parameter.insert(index, value)
    def replace_Parameter_at(self, index, value):
        self.Parameter[index] = value
    def _hasContent(self):
        if (
            self.Parameter
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ParameterListType5', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParameterListType5')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParameterListType5':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParameterListType5')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParameterListType5', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParameterListType5'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ParameterListType5', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Parameter_ in self.Parameter:
            namespaceprefix_ = self.Parameter_nsprefix_ + ':' if (UseCapturedNS_ and self.Parameter_nsprefix_) else ''
            Parameter_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Parameter', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ParameterListType5', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        for Parameter_ in self.Parameter:
            Parameter_.to_etree(element, name_='Parameter', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        if reverse_mapping_ is not None:
            reverse_mapping_[element] = self
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Parameter':
            obj_ = ParameterType6.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Parameter.append(obj_)
            obj_.original_tagname_ = 'Parameter'
# end class ParameterListType5


class ParameterType6(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, Type=None, Value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Type = _cast(None, Type)
        self.Type_nsprefix_ = None
        self.Value = Value
        self.Value_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParameterType6)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParameterType6.subclass:
            return ParameterType6.subclass(*args_, **kwargs_)
        else:
            return ParameterType6(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Value(self):
        return self.Value
    def set_Value(self, Value):
        self.Value = Value
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def get_Type(self):
        return self.Type
    def set_Type(self, Type):
        self.Type = Type
    def _hasContent(self):
        if (
            self.Value is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ParameterType6', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParameterType6')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParameterType6':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParameterType6')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParameterType6', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParameterType6'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Type is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            outfile.write(' Type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Type), input_name='Type')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ParameterType6', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Value is not None:
            namespaceprefix_ = self.Value_nsprefix_ + ':' if (UseCapturedNS_ and self.Value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValue>%s</%sValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Value), input_name='Value')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='ParameterType6', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        if self.Name is not None:
            element.set('Name', self.gds_format_string(self.Name))
        if self.Type is not None:
            element.set('Type', self.gds_format_string(self.Type))
        if self.Value is not None:
            Value_ = self.Value
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Value').text = self.gds_format_string(Value_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        if reverse_mapping_ is not None:
            reverse_mapping_[element] = self
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Name', node)
        if value is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            self.Name = value
        value = find_attr_value_('Type', node)
        if value is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            self.Type = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Value':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Value')
            value_ = self.gds_validate_string(value_, node, 'Value')
            self.Value = value_
            self.Value_nsprefix_ = child_.prefix
# end class ParameterType6


class FlowType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, Mneumonic=None, Shorthand=None, Concept=None, PrePost=None, AorS=None, RollWeighting=None, ActualsVariable=None, NumberOfFlowMatrices=None, ToSimInd=None, SimCV=None, NumberOfBases=None, Base1Type=None, Base1Variable=None, Base1IndexOrCode=None, Base1Weighting=None, Base2Type=None, Base2Variable=None, Base2IndexOrCode=None, Base2Weighting=None, Base3Type=None, Base3Variable=None, Base3IndexOrCode=None, Base3Weighting=None, Base4Type=None, Base4Variable=None, Base4IndexOrCode=None, Base4Weighting=None, Base5Type=None, Base5Variable=None, Base5IndexOrCode=None, Base5Weighting=None, Base6Type=None, Base6Variable=None, Base6IndexOrCode=None, Base6Weighting=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Position = _cast(int, Position)
        self.Position_nsprefix_ = None
        self.Mneumonic = Mneumonic
        self.Mneumonic_nsprefix_ = None
        self.Shorthand = Shorthand
        self.Shorthand_nsprefix_ = None
        self.Concept = Concept
        self.Concept_nsprefix_ = None
        self.PrePost = PrePost
        self.PrePost_nsprefix_ = None
        self.AorS = AorS
        self.AorS_nsprefix_ = None
        self.RollWeighting = RollWeighting
        self.RollWeighting_nsprefix_ = None
        self.ActualsVariable = ActualsVariable
        self.ActualsVariable_nsprefix_ = None
        self.NumberOfFlowMatrices = NumberOfFlowMatrices
        self.NumberOfFlowMatrices_nsprefix_ = None
        self.ToSimInd = ToSimInd
        self.ToSimInd_nsprefix_ = None
        self.SimCV = SimCV
        self.SimCV_nsprefix_ = None
        self.NumberOfBases = NumberOfBases
        self.NumberOfBases_nsprefix_ = None
        self.Base1Type = Base1Type
        self.Base1Type_nsprefix_ = None
        self.Base1Variable = Base1Variable
        self.Base1Variable_nsprefix_ = None
        self.Base1IndexOrCode = Base1IndexOrCode
        self.Base1IndexOrCode_nsprefix_ = None
        self.Base1Weighting = Base1Weighting
        self.Base1Weighting_nsprefix_ = None
        self.Base2Type = Base2Type
        self.Base2Type_nsprefix_ = None
        self.Base2Variable = Base2Variable
        self.Base2Variable_nsprefix_ = None
        self.Base2IndexOrCode = Base2IndexOrCode
        self.Base2IndexOrCode_nsprefix_ = None
        self.Base2Weighting = Base2Weighting
        self.Base2Weighting_nsprefix_ = None
        self.Base3Type = Base3Type
        self.Base3Type_nsprefix_ = None
        self.Base3Variable = Base3Variable
        self.Base3Variable_nsprefix_ = None
        self.Base3IndexOrCode = Base3IndexOrCode
        self.Base3IndexOrCode_nsprefix_ = None
        self.Base3Weighting = Base3Weighting
        self.Base3Weighting_nsprefix_ = None
        self.Base4Type = Base4Type
        self.Base4Type_nsprefix_ = None
        self.Base4Variable = Base4Variable
        self.Base4Variable_nsprefix_ = None
        self.Base4IndexOrCode = Base4IndexOrCode
        self.Base4IndexOrCode_nsprefix_ = None
        self.Base4Weighting = Base4Weighting
        self.Base4Weighting_nsprefix_ = None
        self.Base5Type = Base5Type
        self.Base5Type_nsprefix_ = None
        self.Base5Variable = Base5Variable
        self.Base5Variable_nsprefix_ = None
        self.Base5IndexOrCode = Base5IndexOrCode
        self.Base5IndexOrCode_nsprefix_ = None
        self.Base5Weighting = Base5Weighting
        self.Base5Weighting_nsprefix_ = None
        self.Base6Type = Base6Type
        self.Base6Type_nsprefix_ = None
        self.Base6Variable = Base6Variable
        self.Base6Variable_nsprefix_ = None
        self.Base6IndexOrCode = Base6IndexOrCode
        self.Base6IndexOrCode_nsprefix_ = None
        self.Base6Weighting = Base6Weighting
        self.Base6Weighting_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, FlowType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if FlowType.subclass:
            return FlowType.subclass(*args_, **kwargs_)
        else:
            return FlowType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Mneumonic(self):
        return self.Mneumonic
    def set_Mneumonic(self, Mneumonic):
        self.Mneumonic = Mneumonic
    def get_Shorthand(self):
        return self.Shorthand
    def set_Shorthand(self, Shorthand):
        self.Shorthand = Shorthand
    def get_Concept(self):
        return self.Concept
    def set_Concept(self, Concept):
        self.Concept = Concept
    def get_PrePost(self):
        return self.PrePost
    def set_PrePost(self, PrePost):
        self.PrePost = PrePost
    def get_AorS(self):
        return self.AorS
    def set_AorS(self, AorS):
        self.AorS = AorS
    def get_RollWeighting(self):
        return self.RollWeighting
    def set_RollWeighting(self, RollWeighting):
        self.RollWeighting = RollWeighting
    def get_ActualsVariable(self):
        return self.ActualsVariable
    def set_ActualsVariable(self, ActualsVariable):
        self.ActualsVariable = ActualsVariable
    def get_NumberOfFlowMatrices(self):
        return self.NumberOfFlowMatrices
    def set_NumberOfFlowMatrices(self, NumberOfFlowMatrices):
        self.NumberOfFlowMatrices = NumberOfFlowMatrices
    def get_ToSimInd(self):
        return self.ToSimInd
    def set_ToSimInd(self, ToSimInd):
        self.ToSimInd = ToSimInd
    def get_SimCV(self):
        return self.SimCV
    def set_SimCV(self, SimCV):
        self.SimCV = SimCV
    def get_NumberOfBases(self):
        return self.NumberOfBases
    def set_NumberOfBases(self, NumberOfBases):
        self.NumberOfBases = NumberOfBases
    def get_Base1Type(self):
        return self.Base1Type
    def set_Base1Type(self, Base1Type):
        self.Base1Type = Base1Type
    def get_Base1Variable(self):
        return self.Base1Variable
    def set_Base1Variable(self, Base1Variable):
        self.Base1Variable = Base1Variable
    def get_Base1IndexOrCode(self):
        return self.Base1IndexOrCode
    def set_Base1IndexOrCode(self, Base1IndexOrCode):
        self.Base1IndexOrCode = Base1IndexOrCode
    def get_Base1Weighting(self):
        return self.Base1Weighting
    def set_Base1Weighting(self, Base1Weighting):
        self.Base1Weighting = Base1Weighting
    def get_Base2Type(self):
        return self.Base2Type
    def set_Base2Type(self, Base2Type):
        self.Base2Type = Base2Type
    def get_Base2Variable(self):
        return self.Base2Variable
    def set_Base2Variable(self, Base2Variable):
        self.Base2Variable = Base2Variable
    def get_Base2IndexOrCode(self):
        return self.Base2IndexOrCode
    def set_Base2IndexOrCode(self, Base2IndexOrCode):
        self.Base2IndexOrCode = Base2IndexOrCode
    def get_Base2Weighting(self):
        return self.Base2Weighting
    def set_Base2Weighting(self, Base2Weighting):
        self.Base2Weighting = Base2Weighting
    def get_Base3Type(self):
        return self.Base3Type
    def set_Base3Type(self, Base3Type):
        self.Base3Type = Base3Type
    def get_Base3Variable(self):
        return self.Base3Variable
    def set_Base3Variable(self, Base3Variable):
        self.Base3Variable = Base3Variable
    def get_Base3IndexOrCode(self):
        return self.Base3IndexOrCode
    def set_Base3IndexOrCode(self, Base3IndexOrCode):
        self.Base3IndexOrCode = Base3IndexOrCode
    def get_Base3Weighting(self):
        return self.Base3Weighting
    def set_Base3Weighting(self, Base3Weighting):
        self.Base3Weighting = Base3Weighting
    def get_Base4Type(self):
        return self.Base4Type
    def set_Base4Type(self, Base4Type):
        self.Base4Type = Base4Type
    def get_Base4Variable(self):
        return self.Base4Variable
    def set_Base4Variable(self, Base4Variable):
        self.Base4Variable = Base4Variable
    def get_Base4IndexOrCode(self):
        return self.Base4IndexOrCode
    def set_Base4IndexOrCode(self, Base4IndexOrCode):
        self.Base4IndexOrCode = Base4IndexOrCode
    def get_Base4Weighting(self):
        return self.Base4Weighting
    def set_Base4Weighting(self, Base4Weighting):
        self.Base4Weighting = Base4Weighting
    def get_Base5Type(self):
        return self.Base5Type
    def set_Base5Type(self, Base5Type):
        self.Base5Type = Base5Type
    def get_Base5Variable(self):
        return self.Base5Variable
    def set_Base5Variable(self, Base5Variable):
        self.Base5Variable = Base5Variable
    def get_Base5IndexOrCode(self):
        return self.Base5IndexOrCode
    def set_Base5IndexOrCode(self, Base5IndexOrCode):
        self.Base5IndexOrCode = Base5IndexOrCode
    def get_Base5Weighting(self):
        return self.Base5Weighting
    def set_Base5Weighting(self, Base5Weighting):
        self.Base5Weighting = Base5Weighting
    def get_Base6Type(self):
        return self.Base6Type
    def set_Base6Type(self, Base6Type):
        self.Base6Type = Base6Type
    def get_Base6Variable(self):
        return self.Base6Variable
    def set_Base6Variable(self, Base6Variable):
        self.Base6Variable = Base6Variable
    def get_Base6IndexOrCode(self):
        return self.Base6IndexOrCode
    def set_Base6IndexOrCode(self, Base6IndexOrCode):
        self.Base6IndexOrCode = Base6IndexOrCode
    def get_Base6Weighting(self):
        return self.Base6Weighting
    def set_Base6Weighting(self, Base6Weighting):
        self.Base6Weighting = Base6Weighting
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def _hasContent(self):
        if (
            self.Mneumonic is not None or
            self.Shorthand is not None or
            self.Concept is not None or
            self.PrePost is not None or
            self.AorS is not None or
            self.RollWeighting is not None or
            self.ActualsVariable is not None or
            self.NumberOfFlowMatrices is not None or
            self.ToSimInd is not None or
            self.SimCV is not None or
            self.NumberOfBases is not None or
            self.Base1Type is not None or
            self.Base1Variable is not None or
            self.Base1IndexOrCode is not None or
            self.Base1Weighting is not None or
            self.Base2Type is not None or
            self.Base2Variable is not None or
            self.Base2IndexOrCode is not None or
            self.Base2Weighting is not None or
            self.Base3Type is not None or
            self.Base3Variable is not None or
            self.Base3IndexOrCode is not None or
            self.Base3Weighting is not None or
            self.Base4Type is not None or
            self.Base4Variable is not None or
            self.Base4IndexOrCode is not None or
            self.Base4Weighting is not None or
            self.Base5Type is not None or
            self.Base5Variable is not None or
            self.Base5IndexOrCode is not None or
            self.Base5Weighting is not None or
            self.Base6Type is not None or
            self.Base6Variable is not None or
            self.Base6IndexOrCode is not None or
            self.Base6Weighting is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='FlowType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('FlowType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'FlowType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='FlowType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='FlowType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='FlowType'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position="%s"' % self.gds_format_integer(self.Position, input_name='Position'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='FlowType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Mneumonic is not None:
            namespaceprefix_ = self.Mneumonic_nsprefix_ + ':' if (UseCapturedNS_ and self.Mneumonic_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMneumonic>%s</%sMneumonic>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Mneumonic), input_name='Mneumonic')), namespaceprefix_ , eol_))
        if self.Shorthand is not None:
            namespaceprefix_ = self.Shorthand_nsprefix_ + ':' if (UseCapturedNS_ and self.Shorthand_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sShorthand>%s</%sShorthand>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Shorthand), input_name='Shorthand')), namespaceprefix_ , eol_))
        if self.Concept is not None:
            namespaceprefix_ = self.Concept_nsprefix_ + ':' if (UseCapturedNS_ and self.Concept_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sConcept>%s</%sConcept>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Concept), input_name='Concept')), namespaceprefix_ , eol_))
        if self.PrePost is not None:
            namespaceprefix_ = self.PrePost_nsprefix_ + ':' if (UseCapturedNS_ and self.PrePost_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPrePost>%s</%sPrePost>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PrePost), input_name='PrePost')), namespaceprefix_ , eol_))
        if self.AorS is not None:
            namespaceprefix_ = self.AorS_nsprefix_ + ':' if (UseCapturedNS_ and self.AorS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAorS>%s</%sAorS>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.AorS), input_name='AorS')), namespaceprefix_ , eol_))
        if self.RollWeighting is not None:
            namespaceprefix_ = self.RollWeighting_nsprefix_ + ':' if (UseCapturedNS_ and self.RollWeighting_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRollWeighting>%s</%sRollWeighting>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RollWeighting), input_name='RollWeighting')), namespaceprefix_ , eol_))
        if self.ActualsVariable is not None:
            namespaceprefix_ = self.ActualsVariable_nsprefix_ + ':' if (UseCapturedNS_ and self.ActualsVariable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sActualsVariable>%s</%sActualsVariable>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ActualsVariable), input_name='ActualsVariable')), namespaceprefix_ , eol_))
        if self.NumberOfFlowMatrices is not None:
            namespaceprefix_ = self.NumberOfFlowMatrices_nsprefix_ + ':' if (UseCapturedNS_ and self.NumberOfFlowMatrices_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumberOfFlowMatrices>%s</%sNumberOfFlowMatrices>%s' % (namespaceprefix_ , self.gds_format_integer(self.NumberOfFlowMatrices, input_name='NumberOfFlowMatrices'), namespaceprefix_ , eol_))
        if self.ToSimInd is not None:
            namespaceprefix_ = self.ToSimInd_nsprefix_ + ':' if (UseCapturedNS_ and self.ToSimInd_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sToSimInd>%s</%sToSimInd>%s' % (namespaceprefix_ , self.gds_format_integer(self.ToSimInd, input_name='ToSimInd'), namespaceprefix_ , eol_))
        if self.SimCV is not None:
            namespaceprefix_ = self.SimCV_nsprefix_ + ':' if (UseCapturedNS_ and self.SimCV_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSimCV>%s</%sSimCV>%s' % (namespaceprefix_ , self.gds_format_double(self.SimCV, input_name='SimCV'), namespaceprefix_ , eol_))
        if self.NumberOfBases is not None:
            namespaceprefix_ = self.NumberOfBases_nsprefix_ + ':' if (UseCapturedNS_ and self.NumberOfBases_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumberOfBases>%s</%sNumberOfBases>%s' % (namespaceprefix_ , self.gds_format_integer(self.NumberOfBases, input_name='NumberOfBases'), namespaceprefix_ , eol_))
        if self.Base1Type is not None:
            namespaceprefix_ = self.Base1Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Base1Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase1Type>%s</%sBase1Type>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base1Type, input_name='Base1Type'), namespaceprefix_ , eol_))
        if self.Base1Variable is not None:
            namespaceprefix_ = self.Base1Variable_nsprefix_ + ':' if (UseCapturedNS_ and self.Base1Variable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase1Variable>%s</%sBase1Variable>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Base1Variable), input_name='Base1Variable')), namespaceprefix_ , eol_))
        if self.Base1IndexOrCode is not None:
            namespaceprefix_ = self.Base1IndexOrCode_nsprefix_ + ':' if (UseCapturedNS_ and self.Base1IndexOrCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase1IndexOrCode>%s</%sBase1IndexOrCode>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base1IndexOrCode, input_name='Base1IndexOrCode'), namespaceprefix_ , eol_))
        if self.Base1Weighting is not None:
            namespaceprefix_ = self.Base1Weighting_nsprefix_ + ':' if (UseCapturedNS_ and self.Base1Weighting_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase1Weighting>%s</%sBase1Weighting>%s' % (namespaceprefix_ , self.gds_format_double(self.Base1Weighting, input_name='Base1Weighting'), namespaceprefix_ , eol_))
        if self.Base2Type is not None:
            namespaceprefix_ = self.Base2Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Base2Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase2Type>%s</%sBase2Type>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base2Type, input_name='Base2Type'), namespaceprefix_ , eol_))
        if self.Base2Variable is not None:
            namespaceprefix_ = self.Base2Variable_nsprefix_ + ':' if (UseCapturedNS_ and self.Base2Variable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase2Variable>%s</%sBase2Variable>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Base2Variable), input_name='Base2Variable')), namespaceprefix_ , eol_))
        if self.Base2IndexOrCode is not None:
            namespaceprefix_ = self.Base2IndexOrCode_nsprefix_ + ':' if (UseCapturedNS_ and self.Base2IndexOrCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase2IndexOrCode>%s</%sBase2IndexOrCode>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base2IndexOrCode, input_name='Base2IndexOrCode'), namespaceprefix_ , eol_))
        if self.Base2Weighting is not None:
            namespaceprefix_ = self.Base2Weighting_nsprefix_ + ':' if (UseCapturedNS_ and self.Base2Weighting_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase2Weighting>%s</%sBase2Weighting>%s' % (namespaceprefix_ , self.gds_format_double(self.Base2Weighting, input_name='Base2Weighting'), namespaceprefix_ , eol_))
        if self.Base3Type is not None:
            namespaceprefix_ = self.Base3Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Base3Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase3Type>%s</%sBase3Type>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base3Type, input_name='Base3Type'), namespaceprefix_ , eol_))
        if self.Base3Variable is not None:
            namespaceprefix_ = self.Base3Variable_nsprefix_ + ':' if (UseCapturedNS_ and self.Base3Variable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase3Variable>%s</%sBase3Variable>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Base3Variable), input_name='Base3Variable')), namespaceprefix_ , eol_))
        if self.Base3IndexOrCode is not None:
            namespaceprefix_ = self.Base3IndexOrCode_nsprefix_ + ':' if (UseCapturedNS_ and self.Base3IndexOrCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase3IndexOrCode>%s</%sBase3IndexOrCode>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base3IndexOrCode, input_name='Base3IndexOrCode'), namespaceprefix_ , eol_))
        if self.Base3Weighting is not None:
            namespaceprefix_ = self.Base3Weighting_nsprefix_ + ':' if (UseCapturedNS_ and self.Base3Weighting_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase3Weighting>%s</%sBase3Weighting>%s' % (namespaceprefix_ , self.gds_format_double(self.Base3Weighting, input_name='Base3Weighting'), namespaceprefix_ , eol_))
        if self.Base4Type is not None:
            namespaceprefix_ = self.Base4Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Base4Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase4Type>%s</%sBase4Type>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base4Type, input_name='Base4Type'), namespaceprefix_ , eol_))
        if self.Base4Variable is not None:
            namespaceprefix_ = self.Base4Variable_nsprefix_ + ':' if (UseCapturedNS_ and self.Base4Variable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase4Variable>%s</%sBase4Variable>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Base4Variable), input_name='Base4Variable')), namespaceprefix_ , eol_))
        if self.Base4IndexOrCode is not None:
            namespaceprefix_ = self.Base4IndexOrCode_nsprefix_ + ':' if (UseCapturedNS_ and self.Base4IndexOrCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase4IndexOrCode>%s</%sBase4IndexOrCode>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base4IndexOrCode, input_name='Base4IndexOrCode'), namespaceprefix_ , eol_))
        if self.Base4Weighting is not None:
            namespaceprefix_ = self.Base4Weighting_nsprefix_ + ':' if (UseCapturedNS_ and self.Base4Weighting_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase4Weighting>%s</%sBase4Weighting>%s' % (namespaceprefix_ , self.gds_format_double(self.Base4Weighting, input_name='Base4Weighting'), namespaceprefix_ , eol_))
        if self.Base5Type is not None:
            namespaceprefix_ = self.Base5Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Base5Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase5Type>%s</%sBase5Type>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base5Type, input_name='Base5Type'), namespaceprefix_ , eol_))
        if self.Base5Variable is not None:
            namespaceprefix_ = self.Base5Variable_nsprefix_ + ':' if (UseCapturedNS_ and self.Base5Variable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase5Variable>%s</%sBase5Variable>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Base5Variable), input_name='Base5Variable')), namespaceprefix_ , eol_))
        if self.Base5IndexOrCode is not None:
            namespaceprefix_ = self.Base5IndexOrCode_nsprefix_ + ':' if (UseCapturedNS_ and self.Base5IndexOrCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase5IndexOrCode>%s</%sBase5IndexOrCode>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base5IndexOrCode, input_name='Base5IndexOrCode'), namespaceprefix_ , eol_))
        if self.Base5Weighting is not None:
            namespaceprefix_ = self.Base5Weighting_nsprefix_ + ':' if (UseCapturedNS_ and self.Base5Weighting_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase5Weighting>%s</%sBase5Weighting>%s' % (namespaceprefix_ , self.gds_format_double(self.Base5Weighting, input_name='Base5Weighting'), namespaceprefix_ , eol_))
        if self.Base6Type is not None:
            namespaceprefix_ = self.Base6Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Base6Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase6Type>%s</%sBase6Type>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base6Type, input_name='Base6Type'), namespaceprefix_ , eol_))
        if self.Base6Variable is not None:
            namespaceprefix_ = self.Base6Variable_nsprefix_ + ':' if (UseCapturedNS_ and self.Base6Variable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase6Variable>%s</%sBase6Variable>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Base6Variable), input_name='Base6Variable')), namespaceprefix_ , eol_))
        if self.Base6IndexOrCode is not None:
            namespaceprefix_ = self.Base6IndexOrCode_nsprefix_ + ':' if (UseCapturedNS_ and self.Base6IndexOrCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase6IndexOrCode>%s</%sBase6IndexOrCode>%s' % (namespaceprefix_ , self.gds_format_integer(self.Base6IndexOrCode, input_name='Base6IndexOrCode'), namespaceprefix_ , eol_))
        if self.Base6Weighting is not None:
            namespaceprefix_ = self.Base6Weighting_nsprefix_ + ':' if (UseCapturedNS_ and self.Base6Weighting_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBase6Weighting>%s</%sBase6Weighting>%s' % (namespaceprefix_ , self.gds_format_double(self.Base6Weighting, input_name='Base6Weighting'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='FlowType', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        if self.Position is not None:
            element.set('Position', self.gds_format_integer(self.Position))
        if self.Mneumonic is not None:
            Mneumonic_ = self.Mneumonic
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Mneumonic').text = self.gds_format_string(Mneumonic_)
        if self.Shorthand is not None:
            Shorthand_ = self.Shorthand
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Shorthand').text = self.gds_format_string(Shorthand_)
        if self.Concept is not None:
            Concept_ = self.Concept
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Concept').text = self.gds_format_string(Concept_)
        if self.PrePost is not None:
            PrePost_ = self.PrePost
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}PrePost').text = self.gds_format_string(PrePost_)
        if self.AorS is not None:
            AorS_ = self.AorS
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}AorS').text = self.gds_format_string(AorS_)
        if self.RollWeighting is not None:
            RollWeighting_ = self.RollWeighting
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}RollWeighting').text = self.gds_format_string(RollWeighting_)
        if self.ActualsVariable is not None:
            ActualsVariable_ = self.ActualsVariable
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}ActualsVariable').text = self.gds_format_string(ActualsVariable_)
        if self.NumberOfFlowMatrices is not None:
            NumberOfFlowMatrices_ = self.NumberOfFlowMatrices
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}NumberOfFlowMatrices').text = self.gds_format_integer(NumberOfFlowMatrices_)
        if self.ToSimInd is not None:
            ToSimInd_ = self.ToSimInd
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}ToSimInd').text = self.gds_format_integer(ToSimInd_)
        if self.SimCV is not None:
            SimCV_ = self.SimCV
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}SimCV').text = self.gds_format_double(SimCV_)
        if self.NumberOfBases is not None:
            NumberOfBases_ = self.NumberOfBases
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}NumberOfBases').text = self.gds_format_integer(NumberOfBases_)
        if self.Base1Type is not None:
            Base1Type_ = self.Base1Type
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base1Type').text = self.gds_format_integer(Base1Type_)
        if self.Base1Variable is not None:
            Base1Variable_ = self.Base1Variable
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base1Variable').text = self.gds_format_string(Base1Variable_)
        if self.Base1IndexOrCode is not None:
            Base1IndexOrCode_ = self.Base1IndexOrCode
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base1IndexOrCode').text = self.gds_format_integer(Base1IndexOrCode_)
        if self.Base1Weighting is not None:
            Base1Weighting_ = self.Base1Weighting
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base1Weighting').text = self.gds_format_double(Base1Weighting_)
        if self.Base2Type is not None:
            Base2Type_ = self.Base2Type
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base2Type').text = self.gds_format_integer(Base2Type_)
        if self.Base2Variable is not None:
            Base2Variable_ = self.Base2Variable
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base2Variable').text = self.gds_format_string(Base2Variable_)
        if self.Base2IndexOrCode is not None:
            Base2IndexOrCode_ = self.Base2IndexOrCode
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base2IndexOrCode').text = self.gds_format_integer(Base2IndexOrCode_)
        if self.Base2Weighting is not None:
            Base2Weighting_ = self.Base2Weighting
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base2Weighting').text = self.gds_format_double(Base2Weighting_)
        if self.Base3Type is not None:
            Base3Type_ = self.Base3Type
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base3Type').text = self.gds_format_integer(Base3Type_)
        if self.Base3Variable is not None:
            Base3Variable_ = self.Base3Variable
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base3Variable').text = self.gds_format_string(Base3Variable_)
        if self.Base3IndexOrCode is not None:
            Base3IndexOrCode_ = self.Base3IndexOrCode
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base3IndexOrCode').text = self.gds_format_integer(Base3IndexOrCode_)
        if self.Base3Weighting is not None:
            Base3Weighting_ = self.Base3Weighting
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base3Weighting').text = self.gds_format_double(Base3Weighting_)
        if self.Base4Type is not None:
            Base4Type_ = self.Base4Type
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base4Type').text = self.gds_format_integer(Base4Type_)
        if self.Base4Variable is not None:
            Base4Variable_ = self.Base4Variable
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base4Variable').text = self.gds_format_string(Base4Variable_)
        if self.Base4IndexOrCode is not None:
            Base4IndexOrCode_ = self.Base4IndexOrCode
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base4IndexOrCode').text = self.gds_format_integer(Base4IndexOrCode_)
        if self.Base4Weighting is not None:
            Base4Weighting_ = self.Base4Weighting
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base4Weighting').text = self.gds_format_double(Base4Weighting_)
        if self.Base5Type is not None:
            Base5Type_ = self.Base5Type
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base5Type').text = self.gds_format_integer(Base5Type_)
        if self.Base5Variable is not None:
            Base5Variable_ = self.Base5Variable
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base5Variable').text = self.gds_format_string(Base5Variable_)
        if self.Base5IndexOrCode is not None:
            Base5IndexOrCode_ = self.Base5IndexOrCode
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base5IndexOrCode').text = self.gds_format_integer(Base5IndexOrCode_)
        if self.Base5Weighting is not None:
            Base5Weighting_ = self.Base5Weighting
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base5Weighting').text = self.gds_format_double(Base5Weighting_)
        if self.Base6Type is not None:
            Base6Type_ = self.Base6Type
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base6Type').text = self.gds_format_integer(Base6Type_)
        if self.Base6Variable is not None:
            Base6Variable_ = self.Base6Variable
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base6Variable').text = self.gds_format_string(Base6Variable_)
        if self.Base6IndexOrCode is not None:
            Base6IndexOrCode_ = self.Base6IndexOrCode
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base6IndexOrCode').text = self.gds_format_integer(Base6IndexOrCode_)
        if self.Base6Weighting is not None:
            Base6Weighting_ = self.Base6Weighting
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Base6Weighting').text = self.gds_format_double(Base6Weighting_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        if reverse_mapping_ is not None:
            reverse_mapping_[element] = self
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Position', node)
        if value is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            self.Position = self.gds_parse_integer(value, node, 'Position')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Mneumonic':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Mneumonic')
            value_ = self.gds_validate_string(value_, node, 'Mneumonic')
            self.Mneumonic = value_
            self.Mneumonic_nsprefix_ = child_.prefix
        elif nodeName_ == 'Shorthand':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Shorthand')
            value_ = self.gds_validate_string(value_, node, 'Shorthand')
            self.Shorthand = value_
            self.Shorthand_nsprefix_ = child_.prefix
        elif nodeName_ == 'Concept':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Concept')
            value_ = self.gds_validate_string(value_, node, 'Concept')
            self.Concept = value_
            self.Concept_nsprefix_ = child_.prefix
        elif nodeName_ == 'PrePost':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PrePost')
            value_ = self.gds_validate_string(value_, node, 'PrePost')
            self.PrePost = value_
            self.PrePost_nsprefix_ = child_.prefix
        elif nodeName_ == 'AorS':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'AorS')
            value_ = self.gds_validate_string(value_, node, 'AorS')
            self.AorS = value_
            self.AorS_nsprefix_ = child_.prefix
        elif nodeName_ == 'RollWeighting':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RollWeighting')
            value_ = self.gds_validate_string(value_, node, 'RollWeighting')
            self.RollWeighting = value_
            self.RollWeighting_nsprefix_ = child_.prefix
        elif nodeName_ == 'ActualsVariable':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ActualsVariable')
            value_ = self.gds_validate_string(value_, node, 'ActualsVariable')
            self.ActualsVariable = value_
            self.ActualsVariable_nsprefix_ = child_.prefix
        elif nodeName_ == 'NumberOfFlowMatrices' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NumberOfFlowMatrices')
            ival_ = self.gds_validate_integer(ival_, node, 'NumberOfFlowMatrices')
            self.NumberOfFlowMatrices = ival_
            self.NumberOfFlowMatrices_nsprefix_ = child_.prefix
        elif nodeName_ == 'ToSimInd' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'ToSimInd')
            ival_ = self.gds_validate_integer(ival_, node, 'ToSimInd')
            self.ToSimInd = ival_
            self.ToSimInd_nsprefix_ = child_.prefix
        elif nodeName_ == 'SimCV' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'SimCV')
            fval_ = self.gds_validate_double(fval_, node, 'SimCV')
            self.SimCV = fval_
            self.SimCV_nsprefix_ = child_.prefix
        elif nodeName_ == 'NumberOfBases' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NumberOfBases')
            ival_ = self.gds_validate_integer(ival_, node, 'NumberOfBases')
            self.NumberOfBases = ival_
            self.NumberOfBases_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base1Type' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base1Type')
            ival_ = self.gds_validate_integer(ival_, node, 'Base1Type')
            self.Base1Type = ival_
            self.Base1Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base1Variable':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Base1Variable')
            value_ = self.gds_validate_string(value_, node, 'Base1Variable')
            self.Base1Variable = value_
            self.Base1Variable_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base1IndexOrCode' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base1IndexOrCode')
            ival_ = self.gds_validate_integer(ival_, node, 'Base1IndexOrCode')
            self.Base1IndexOrCode = ival_
            self.Base1IndexOrCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base1Weighting' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Base1Weighting')
            fval_ = self.gds_validate_double(fval_, node, 'Base1Weighting')
            self.Base1Weighting = fval_
            self.Base1Weighting_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base2Type' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base2Type')
            ival_ = self.gds_validate_integer(ival_, node, 'Base2Type')
            self.Base2Type = ival_
            self.Base2Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base2Variable':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Base2Variable')
            value_ = self.gds_validate_string(value_, node, 'Base2Variable')
            self.Base2Variable = value_
            self.Base2Variable_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base2IndexOrCode' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base2IndexOrCode')
            ival_ = self.gds_validate_integer(ival_, node, 'Base2IndexOrCode')
            self.Base2IndexOrCode = ival_
            self.Base2IndexOrCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base2Weighting' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Base2Weighting')
            fval_ = self.gds_validate_double(fval_, node, 'Base2Weighting')
            self.Base2Weighting = fval_
            self.Base2Weighting_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base3Type' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base3Type')
            ival_ = self.gds_validate_integer(ival_, node, 'Base3Type')
            self.Base3Type = ival_
            self.Base3Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base3Variable':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Base3Variable')
            value_ = self.gds_validate_string(value_, node, 'Base3Variable')
            self.Base3Variable = value_
            self.Base3Variable_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base3IndexOrCode' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base3IndexOrCode')
            ival_ = self.gds_validate_integer(ival_, node, 'Base3IndexOrCode')
            self.Base3IndexOrCode = ival_
            self.Base3IndexOrCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base3Weighting' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Base3Weighting')
            fval_ = self.gds_validate_double(fval_, node, 'Base3Weighting')
            self.Base3Weighting = fval_
            self.Base3Weighting_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base4Type' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base4Type')
            ival_ = self.gds_validate_integer(ival_, node, 'Base4Type')
            self.Base4Type = ival_
            self.Base4Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base4Variable':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Base4Variable')
            value_ = self.gds_validate_string(value_, node, 'Base4Variable')
            self.Base4Variable = value_
            self.Base4Variable_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base4IndexOrCode' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base4IndexOrCode')
            ival_ = self.gds_validate_integer(ival_, node, 'Base4IndexOrCode')
            self.Base4IndexOrCode = ival_
            self.Base4IndexOrCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base4Weighting' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Base4Weighting')
            fval_ = self.gds_validate_double(fval_, node, 'Base4Weighting')
            self.Base4Weighting = fval_
            self.Base4Weighting_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base5Type' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base5Type')
            ival_ = self.gds_validate_integer(ival_, node, 'Base5Type')
            self.Base5Type = ival_
            self.Base5Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base5Variable':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Base5Variable')
            value_ = self.gds_validate_string(value_, node, 'Base5Variable')
            self.Base5Variable = value_
            self.Base5Variable_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base5IndexOrCode' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base5IndexOrCode')
            ival_ = self.gds_validate_integer(ival_, node, 'Base5IndexOrCode')
            self.Base5IndexOrCode = ival_
            self.Base5IndexOrCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base5Weighting' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Base5Weighting')
            fval_ = self.gds_validate_double(fval_, node, 'Base5Weighting')
            self.Base5Weighting = fval_
            self.Base5Weighting_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base6Type' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base6Type')
            ival_ = self.gds_validate_integer(ival_, node, 'Base6Type')
            self.Base6Type = ival_
            self.Base6Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base6Variable':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Base6Variable')
            value_ = self.gds_validate_string(value_, node, 'Base6Variable')
            self.Base6Variable = value_
            self.Base6Variable_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base6IndexOrCode' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Base6IndexOrCode')
            ival_ = self.gds_validate_integer(ival_, node, 'Base6IndexOrCode')
            self.Base6IndexOrCode = ival_
            self.Base6IndexOrCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'Base6Weighting' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Base6Weighting')
            fval_ = self.gds_validate_double(fval_, node, 'Base6Weighting')
            self.Base6Weighting = fval_
            self.Base6Weighting_nsprefix_ = child_.prefix
# end class FlowType


class OrdersType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Handle=None, Order=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        if Order is None:
            self.Order = []
        else:
            self.Order = Order
        self.Order_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OrdersType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OrdersType.subclass:
            return OrdersType.subclass(*args_, **kwargs_)
        else:
            return OrdersType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Order(self):
        return self.Order
    def set_Order(self, Order):
        self.Order = Order
    def add_Order(self, value):
        self.Order.append(value)
    def insert_Order_at(self, index, value):
        self.Order.insert(index, value)
    def replace_Order_at(self, index, value):
        self.Order[index] = value
    def get_Handle(self):
        return self.Handle
    def set_Handle(self, Handle):
        self.Handle = Handle
    def _hasContent(self):
        if (
            self.Order
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='OrdersType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OrdersType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'OrdersType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OrdersType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OrdersType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='OrdersType'):
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='OrdersType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Order_ in self.Order:
            namespaceprefix_ = self.Order_nsprefix_ + ':' if (UseCapturedNS_ and self.Order_nsprefix_) else ''
            Order_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Order', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='OrdersType', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        if self.Handle is not None:
            element.set('Handle', self.gds_format_string(self.Handle))
        for Order_ in self.Order:
            Order_.to_etree(element, name_='Order', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        if reverse_mapping_ is not None:
            reverse_mapping_[element] = self
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Handle', node)
        if value is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            self.Handle = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Order':
            obj_ = OrderType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Order.append(obj_)
            obj_.original_tagname_ = 'Order'
# end class OrdersType


class OrderType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, Mneumonic=None, USF=None, IndexOrCode=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Position = _cast(int, Position)
        self.Position_nsprefix_ = None
        self.Mneumonic = Mneumonic
        self.Mneumonic_nsprefix_ = None
        self.USF = USF
        self.USF_nsprefix_ = None
        self.IndexOrCode = IndexOrCode
        self.IndexOrCode_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OrderType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OrderType.subclass:
            return OrderType.subclass(*args_, **kwargs_)
        else:
            return OrderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Mneumonic(self):
        return self.Mneumonic
    def set_Mneumonic(self, Mneumonic):
        self.Mneumonic = Mneumonic
    def get_USF(self):
        return self.USF
    def set_USF(self, USF):
        self.USF = USF
    def get_IndexOrCode(self):
        return self.IndexOrCode
    def set_IndexOrCode(self, IndexOrCode):
        self.IndexOrCode = IndexOrCode
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def _hasContent(self):
        if (
            self.Mneumonic is not None or
            self.USF is not None or
            self.IndexOrCode is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='OrderType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OrderType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'OrderType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OrderType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OrderType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='OrderType'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position="%s"' % self.gds_format_integer(self.Position, input_name='Position'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='OrderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Mneumonic is not None:
            namespaceprefix_ = self.Mneumonic_nsprefix_ + ':' if (UseCapturedNS_ and self.Mneumonic_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMneumonic>%s</%sMneumonic>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Mneumonic), input_name='Mneumonic')), namespaceprefix_ , eol_))
        if self.USF is not None:
            namespaceprefix_ = self.USF_nsprefix_ + ':' if (UseCapturedNS_ and self.USF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sUSF>%s</%sUSF>%s' % (namespaceprefix_ , self.gds_format_integer(self.USF, input_name='USF'), namespaceprefix_ , eol_))
        if self.IndexOrCode is not None:
            namespaceprefix_ = self.IndexOrCode_nsprefix_ + ':' if (UseCapturedNS_ and self.IndexOrCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sIndexOrCode>%s</%sIndexOrCode>%s' % (namespaceprefix_ , self.gds_format_integer(self.IndexOrCode, input_name='IndexOrCode'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='OrderType', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        if self.Position is not None:
            element.set('Position', self.gds_format_integer(self.Position))
        if self.Mneumonic is not None:
            Mneumonic_ = self.Mneumonic
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Mneumonic').text = self.gds_format_string(Mneumonic_)
        if self.USF is not None:
            USF_ = self.USF
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}USF').text = self.gds_format_integer(USF_)
        if self.IndexOrCode is not None:
            IndexOrCode_ = self.IndexOrCode
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}IndexOrCode').text = self.gds_format_integer(IndexOrCode_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        if reverse_mapping_ is not None:
            reverse_mapping_[element] = self
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Position', node)
        if value is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            self.Position = self.gds_parse_integer(value, node, 'Position')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Mneumonic':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Mneumonic')
            value_ = self.gds_validate_string(value_, node, 'Mneumonic')
            self.Mneumonic = value_
            self.Mneumonic_nsprefix_ = child_.prefix
        elif nodeName_ == 'USF' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'USF')
            ival_ = self.gds_validate_integer(ival_, node, 'USF')
            self.USF = ival_
            self.USF_nsprefix_ = child_.prefix
        elif nodeName_ == 'IndexOrCode' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'IndexOrCode')
            ival_ = self.gds_validate_integer(ival_, node, 'IndexOrCode')
            self.IndexOrCode = ival_
            self.IndexOrCode_nsprefix_ = child_.prefix
# end class OrderType


GDSClassesMapping = {
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    prefix_tag = TagNamePrefix + tag
    rootClass = GDSClassesMapping.get(prefix_tag)
    if rootClass is None:
        rootClass = globals().get(prefix_tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'WDSStocksAndFlows'
        rootClass = WDSStocksAndFlows
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, reverse_mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'WDSStocksAndFlows'
        rootClass = WDSStocksAndFlows
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if mapping is None:
        mapping = {}
    if reverse_mapping is None:
        reverse_mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping,
        reverse_mapping_=reverse_mapping, nsmap_=nsmap)
    reverse_node_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_node_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'WDSStocksAndFlows'
        rootClass = WDSStocksAndFlows
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'WDSStocksAndFlows'
        rootClass = WDSStocksAndFlows
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from gWDSStocksAndFlowsSpec import *\n\n')
        sys.stdout.write('import gWDSStocksAndFlowsSpec as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'https://github.com/wdatasci/WDS-ModelSpec': []}

__all__ = [
    "FlowType",
    "FlowsType",
    "OrderType",
    "OrdersType",
    "ParameterListType",
    "ParameterListType1",
    "ParameterListType3",
    "ParameterListType5",
    "ParameterType",
    "ParameterType2",
    "ParameterType4",
    "ParameterType6",
    "StockType",
    "StocksType",
    "UnitType",
    "UnitsType",
    "WDSStocksAndFlows"
]
