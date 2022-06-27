#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Mon Jun 27 09:20:27 2022 by generateDS.py version 2.40.13.
# Python 3.9.5 (default, Nov 23 2021, 15:27:38)  [GCC 9.3.0]
#
# Command line options:
#   ('--mixed-case-enums', '')
#   ('-f', '')
#   ('--export', 'write etree')
#   ('-o', './WDS-Python/WDS/Wranglers/gXMLParsers/gWDSStatesAndStagesSpec.py')
#
# Command line arguments:
#   ./WDS-XML/XSD/WDSStatesAndStagesSpec.xsd
#
# Command line:
#   ./WDS-Python/scripts/generateDS_unsnaked --mixed-case-enums -f --export="write etree" -o "./WDS-Python/WDS/Wranglers/gXMLParsers/gWDSStatesAndStagesSpec.py" ./WDS-XML/XSD/WDSStatesAndStagesSpec.xsd
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


class WDSStateSpace(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, Handle=None, ParameterList=None, States=None, Stages=None, Bridges=None, gds_collector_=None, **kwargs_):
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
        self.States = States
        self.States_nsprefix_ = "wds"
        self.Stages = Stages
        self.Stages_nsprefix_ = "wds"
        self.Bridges = Bridges
        self.Bridges_nsprefix_ = "wds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, WDSStateSpace)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if WDSStateSpace.subclass:
            return WDSStateSpace.subclass(*args_, **kwargs_)
        else:
            return WDSStateSpace(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ParameterList(self):
        return self.ParameterList
    def set_ParameterList(self, ParameterList):
        self.ParameterList = ParameterList
    def get_States(self):
        return self.States
    def set_States(self, States):
        self.States = States
    def get_Stages(self):
        return self.Stages
    def set_Stages(self, Stages):
        self.Stages = Stages
    def get_Bridges(self):
        return self.Bridges
    def set_Bridges(self, Bridges):
        self.Bridges = Bridges
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
            self.States is not None or
            self.Stages is not None or
            self.Bridges is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='WDSStateSpace', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('WDSStateSpace')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'WDSStateSpace':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='WDSStateSpace')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='WDSStateSpace', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='WDSStateSpace'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='WDSStateSpace', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ParameterList is not None:
            namespaceprefix_ = self.ParameterList_nsprefix_ + ':' if (UseCapturedNS_ and self.ParameterList_nsprefix_) else ''
            self.ParameterList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParameterList', pretty_print=pretty_print)
        if self.States is not None:
            namespaceprefix_ = self.States_nsprefix_ + ':' if (UseCapturedNS_ and self.States_nsprefix_) else ''
            self.States.export(outfile, level, namespaceprefix_, namespacedef_='', name_='States', pretty_print=pretty_print)
        if self.Stages is not None:
            namespaceprefix_ = self.Stages_nsprefix_ + ':' if (UseCapturedNS_ and self.Stages_nsprefix_) else ''
            self.Stages.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Stages', pretty_print=pretty_print)
        if self.Bridges is not None:
            namespaceprefix_ = self.Bridges_nsprefix_ + ':' if (UseCapturedNS_ and self.Bridges_nsprefix_) else ''
            self.Bridges.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Bridges', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='WDSStateSpace', mapping_=None, reverse_mapping_=None, nsmap_=None):
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
        if self.States is not None:
            States_ = self.States
            States_.to_etree(element, name_='States', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        if self.Stages is not None:
            Stages_ = self.Stages
            Stages_.to_etree(element, name_='Stages', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        if self.Bridges is not None:
            Bridges_ = self.Bridges
            Bridges_.to_etree(element, name_='Bridges', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
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
        elif nodeName_ == 'States':
            obj_ = StatesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.States = obj_
            obj_.original_tagname_ = 'States'
        elif nodeName_ == 'Stages':
            obj_ = StagesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Stages = obj_
            obj_.original_tagname_ = 'Stages'
        elif nodeName_ == 'Bridges':
            obj_ = BridgesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Bridges = obj_
            obj_.original_tagname_ = 'Bridges'
# end class WDSStateSpace


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


class StatesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Handle=None, Number=None, NumberOfBaseDimensions=None, NumberOfAgePages=None, Axis1LimitDefault=None, Axis2LimitDefault=None, Axis3LimitDefault=None, Axis4LimitDefault=None, ParameterList=None, State=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        self.Number = Number
        self.Number_nsprefix_ = None
        self.NumberOfBaseDimensions = NumberOfBaseDimensions
        self.NumberOfBaseDimensions_nsprefix_ = None
        self.NumberOfAgePages = NumberOfAgePages
        self.NumberOfAgePages_nsprefix_ = None
        self.Axis1LimitDefault = Axis1LimitDefault
        self.Axis1LimitDefault_nsprefix_ = None
        self.Axis2LimitDefault = Axis2LimitDefault
        self.Axis2LimitDefault_nsprefix_ = None
        self.Axis3LimitDefault = Axis3LimitDefault
        self.Axis3LimitDefault_nsprefix_ = None
        self.Axis4LimitDefault = Axis4LimitDefault
        self.Axis4LimitDefault_nsprefix_ = None
        self.ParameterList = ParameterList
        self.ParameterList_nsprefix_ = None
        if State is None:
            self.State = []
        else:
            self.State = State
        self.State_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, StatesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if StatesType.subclass:
            return StatesType.subclass(*args_, **kwargs_)
        else:
            return StatesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Number(self):
        return self.Number
    def set_Number(self, Number):
        self.Number = Number
    def get_NumberOfBaseDimensions(self):
        return self.NumberOfBaseDimensions
    def set_NumberOfBaseDimensions(self, NumberOfBaseDimensions):
        self.NumberOfBaseDimensions = NumberOfBaseDimensions
    def get_NumberOfAgePages(self):
        return self.NumberOfAgePages
    def set_NumberOfAgePages(self, NumberOfAgePages):
        self.NumberOfAgePages = NumberOfAgePages
    def get_Axis1LimitDefault(self):
        return self.Axis1LimitDefault
    def set_Axis1LimitDefault(self, Axis1LimitDefault):
        self.Axis1LimitDefault = Axis1LimitDefault
    def get_Axis2LimitDefault(self):
        return self.Axis2LimitDefault
    def set_Axis2LimitDefault(self, Axis2LimitDefault):
        self.Axis2LimitDefault = Axis2LimitDefault
    def get_Axis3LimitDefault(self):
        return self.Axis3LimitDefault
    def set_Axis3LimitDefault(self, Axis3LimitDefault):
        self.Axis3LimitDefault = Axis3LimitDefault
    def get_Axis4LimitDefault(self):
        return self.Axis4LimitDefault
    def set_Axis4LimitDefault(self, Axis4LimitDefault):
        self.Axis4LimitDefault = Axis4LimitDefault
    def get_ParameterList(self):
        return self.ParameterList
    def set_ParameterList(self, ParameterList):
        self.ParameterList = ParameterList
    def get_State(self):
        return self.State
    def set_State(self, State):
        self.State = State
    def add_State(self, value):
        self.State.append(value)
    def insert_State_at(self, index, value):
        self.State.insert(index, value)
    def replace_State_at(self, index, value):
        self.State[index] = value
    def get_Handle(self):
        return self.Handle
    def set_Handle(self, Handle):
        self.Handle = Handle
    def _hasContent(self):
        if (
            self.Number is not None or
            self.NumberOfBaseDimensions is not None or
            self.NumberOfAgePages is not None or
            self.Axis1LimitDefault is not None or
            self.Axis2LimitDefault is not None or
            self.Axis3LimitDefault is not None or
            self.Axis4LimitDefault is not None or
            self.ParameterList is not None or
            self.State
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='StatesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('StatesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'StatesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='StatesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='StatesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='StatesType'):
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='StatesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Number is not None:
            namespaceprefix_ = self.Number_nsprefix_ + ':' if (UseCapturedNS_ and self.Number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumber>%s</%sNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.Number, input_name='Number'), namespaceprefix_ , eol_))
        if self.NumberOfBaseDimensions is not None:
            namespaceprefix_ = self.NumberOfBaseDimensions_nsprefix_ + ':' if (UseCapturedNS_ and self.NumberOfBaseDimensions_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumberOfBaseDimensions>%s</%sNumberOfBaseDimensions>%s' % (namespaceprefix_ , self.gds_format_integer(self.NumberOfBaseDimensions, input_name='NumberOfBaseDimensions'), namespaceprefix_ , eol_))
        if self.NumberOfAgePages is not None:
            namespaceprefix_ = self.NumberOfAgePages_nsprefix_ + ':' if (UseCapturedNS_ and self.NumberOfAgePages_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumberOfAgePages>%s</%sNumberOfAgePages>%s' % (namespaceprefix_ , self.gds_format_integer(self.NumberOfAgePages, input_name='NumberOfAgePages'), namespaceprefix_ , eol_))
        if self.Axis1LimitDefault is not None:
            namespaceprefix_ = self.Axis1LimitDefault_nsprefix_ + ':' if (UseCapturedNS_ and self.Axis1LimitDefault_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAxis1LimitDefault>%s</%sAxis1LimitDefault>%s' % (namespaceprefix_ , self.gds_format_integer(self.Axis1LimitDefault, input_name='Axis1LimitDefault'), namespaceprefix_ , eol_))
        if self.Axis2LimitDefault is not None:
            namespaceprefix_ = self.Axis2LimitDefault_nsprefix_ + ':' if (UseCapturedNS_ and self.Axis2LimitDefault_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAxis2LimitDefault>%s</%sAxis2LimitDefault>%s' % (namespaceprefix_ , self.gds_format_integer(self.Axis2LimitDefault, input_name='Axis2LimitDefault'), namespaceprefix_ , eol_))
        if self.Axis3LimitDefault is not None:
            namespaceprefix_ = self.Axis3LimitDefault_nsprefix_ + ':' if (UseCapturedNS_ and self.Axis3LimitDefault_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAxis3LimitDefault>%s</%sAxis3LimitDefault>%s' % (namespaceprefix_ , self.gds_format_integer(self.Axis3LimitDefault, input_name='Axis3LimitDefault'), namespaceprefix_ , eol_))
        if self.Axis4LimitDefault is not None:
            namespaceprefix_ = self.Axis4LimitDefault_nsprefix_ + ':' if (UseCapturedNS_ and self.Axis4LimitDefault_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAxis4LimitDefault>%s</%sAxis4LimitDefault>%s' % (namespaceprefix_ , self.gds_format_integer(self.Axis4LimitDefault, input_name='Axis4LimitDefault'), namespaceprefix_ , eol_))
        if self.ParameterList is not None:
            namespaceprefix_ = self.ParameterList_nsprefix_ + ':' if (UseCapturedNS_ and self.ParameterList_nsprefix_) else ''
            self.ParameterList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParameterList', pretty_print=pretty_print)
        for State_ in self.State:
            namespaceprefix_ = self.State_nsprefix_ + ':' if (UseCapturedNS_ and self.State_nsprefix_) else ''
            State_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='State', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='StatesType', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        if self.Handle is not None:
            element.set('Handle', self.gds_format_string(self.Handle))
        if self.Number is not None:
            Number_ = self.Number
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Number').text = self.gds_format_integer(Number_)
        if self.NumberOfBaseDimensions is not None:
            NumberOfBaseDimensions_ = self.NumberOfBaseDimensions
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}NumberOfBaseDimensions').text = self.gds_format_integer(NumberOfBaseDimensions_)
        if self.NumberOfAgePages is not None:
            NumberOfAgePages_ = self.NumberOfAgePages
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}NumberOfAgePages').text = self.gds_format_integer(NumberOfAgePages_)
        if self.Axis1LimitDefault is not None:
            Axis1LimitDefault_ = self.Axis1LimitDefault
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Axis1LimitDefault').text = self.gds_format_integer(Axis1LimitDefault_)
        if self.Axis2LimitDefault is not None:
            Axis2LimitDefault_ = self.Axis2LimitDefault
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Axis2LimitDefault').text = self.gds_format_integer(Axis2LimitDefault_)
        if self.Axis3LimitDefault is not None:
            Axis3LimitDefault_ = self.Axis3LimitDefault
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Axis3LimitDefault').text = self.gds_format_integer(Axis3LimitDefault_)
        if self.Axis4LimitDefault is not None:
            Axis4LimitDefault_ = self.Axis4LimitDefault
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Axis4LimitDefault').text = self.gds_format_integer(Axis4LimitDefault_)
        if self.ParameterList is not None:
            ParameterList_ = self.ParameterList
            ParameterList_.to_etree(element, name_='ParameterList', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        for State_ in self.State:
            State_.to_etree(element, name_='State', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
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
        elif nodeName_ == 'NumberOfBaseDimensions' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NumberOfBaseDimensions')
            ival_ = self.gds_validate_integer(ival_, node, 'NumberOfBaseDimensions')
            self.NumberOfBaseDimensions = ival_
            self.NumberOfBaseDimensions_nsprefix_ = child_.prefix
        elif nodeName_ == 'NumberOfAgePages' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NumberOfAgePages')
            ival_ = self.gds_validate_integer(ival_, node, 'NumberOfAgePages')
            self.NumberOfAgePages = ival_
            self.NumberOfAgePages_nsprefix_ = child_.prefix
        elif nodeName_ == 'Axis1LimitDefault' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Axis1LimitDefault')
            ival_ = self.gds_validate_integer(ival_, node, 'Axis1LimitDefault')
            self.Axis1LimitDefault = ival_
            self.Axis1LimitDefault_nsprefix_ = child_.prefix
        elif nodeName_ == 'Axis2LimitDefault' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Axis2LimitDefault')
            ival_ = self.gds_validate_integer(ival_, node, 'Axis2LimitDefault')
            self.Axis2LimitDefault = ival_
            self.Axis2LimitDefault_nsprefix_ = child_.prefix
        elif nodeName_ == 'Axis3LimitDefault' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Axis3LimitDefault')
            ival_ = self.gds_validate_integer(ival_, node, 'Axis3LimitDefault')
            self.Axis3LimitDefault = ival_
            self.Axis3LimitDefault_nsprefix_ = child_.prefix
        elif nodeName_ == 'Axis4LimitDefault' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Axis4LimitDefault')
            ival_ = self.gds_validate_integer(ival_, node, 'Axis4LimitDefault')
            self.Axis4LimitDefault = ival_
            self.Axis4LimitDefault_nsprefix_ = child_.prefix
        elif nodeName_ == 'ParameterList':
            obj_ = ParameterListType1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParameterList = obj_
            obj_.original_tagname_ = 'ParameterList'
        elif nodeName_ == 'State':
            obj_ = StateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.State.append(obj_)
            obj_.original_tagname_ = 'State'
# end class StatesType


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


class StateType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, Mneumonic=None, Shorthand=None, Concept=None, NullInd=None, Type=None, NotionalDelq=None, gds_collector_=None, **kwargs_):
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
        self.NullInd = NullInd
        self.NullInd_nsprefix_ = None
        self.Type = Type
        self.Type_nsprefix_ = None
        self.NotionalDelq = NotionalDelq
        self.NotionalDelq_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, StateType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if StateType.subclass:
            return StateType.subclass(*args_, **kwargs_)
        else:
            return StateType(*args_, **kwargs_)
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
    def get_NullInd(self):
        return self.NullInd
    def set_NullInd(self, NullInd):
        self.NullInd = NullInd
    def get_Type(self):
        return self.Type
    def set_Type(self, Type):
        self.Type = Type
    def get_NotionalDelq(self):
        return self.NotionalDelq
    def set_NotionalDelq(self, NotionalDelq):
        self.NotionalDelq = NotionalDelq
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def _hasContent(self):
        if (
            self.Mneumonic is not None or
            self.Shorthand is not None or
            self.Concept is not None or
            self.NullInd is not None or
            self.Type is not None or
            self.NotionalDelq is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='StateType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('StateType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'StateType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='StateType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='StateType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='StateType'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position="%s"' % self.gds_format_integer(self.Position, input_name='Position'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='StateType', fromsubclass_=False, pretty_print=True):
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
        if self.NullInd is not None:
            namespaceprefix_ = self.NullInd_nsprefix_ + ':' if (UseCapturedNS_ and self.NullInd_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNullInd>%s</%sNullInd>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.NullInd), input_name='NullInd')), namespaceprefix_ , eol_))
        if self.Type is not None:
            namespaceprefix_ = self.Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sType>%s</%sType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Type), input_name='Type')), namespaceprefix_ , eol_))
        if self.NotionalDelq is not None:
            namespaceprefix_ = self.NotionalDelq_nsprefix_ + ':' if (UseCapturedNS_ and self.NotionalDelq_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNotionalDelq>%s</%sNotionalDelq>%s' % (namespaceprefix_ , self.gds_format_integer(self.NotionalDelq, input_name='NotionalDelq'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='StateType', mapping_=None, reverse_mapping_=None, nsmap_=None):
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
        if self.NullInd is not None:
            NullInd_ = self.NullInd
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}NullInd').text = self.gds_format_string(NullInd_)
        if self.Type is not None:
            Type_ = self.Type
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Type').text = self.gds_format_string(Type_)
        if self.NotionalDelq is not None:
            NotionalDelq_ = self.NotionalDelq
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}NotionalDelq').text = self.gds_format_integer(NotionalDelq_)
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
        elif nodeName_ == 'NullInd':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'NullInd')
            value_ = self.gds_validate_string(value_, node, 'NullInd')
            self.NullInd = value_
            self.NullInd_nsprefix_ = child_.prefix
        elif nodeName_ == 'Type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Type')
            value_ = self.gds_validate_string(value_, node, 'Type')
            self.Type = value_
            self.Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'NotionalDelq' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NotionalDelq')
            ival_ = self.gds_validate_integer(ival_, node, 'NotionalDelq')
            self.NotionalDelq = ival_
            self.NotionalDelq_nsprefix_ = child_.prefix
# end class StateType


class StagesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Handle=None, Number=None, ParameterList=None, Stage=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        self.Number = Number
        self.Number_nsprefix_ = None
        self.ParameterList = ParameterList
        self.ParameterList_nsprefix_ = None
        if Stage is None:
            self.Stage = []
        else:
            self.Stage = Stage
        self.Stage_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, StagesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if StagesType.subclass:
            return StagesType.subclass(*args_, **kwargs_)
        else:
            return StagesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Number(self):
        return self.Number
    def set_Number(self, Number):
        self.Number = Number
    def get_ParameterList(self):
        return self.ParameterList
    def set_ParameterList(self, ParameterList):
        self.ParameterList = ParameterList
    def get_Stage(self):
        return self.Stage
    def set_Stage(self, Stage):
        self.Stage = Stage
    def add_Stage(self, value):
        self.Stage.append(value)
    def insert_Stage_at(self, index, value):
        self.Stage.insert(index, value)
    def replace_Stage_at(self, index, value):
        self.Stage[index] = value
    def get_Handle(self):
        return self.Handle
    def set_Handle(self, Handle):
        self.Handle = Handle
    def _hasContent(self):
        if (
            self.Number is not None or
            self.ParameterList is not None or
            self.Stage
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='StagesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('StagesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'StagesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='StagesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='StagesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='StagesType'):
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='StagesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Number is not None:
            namespaceprefix_ = self.Number_nsprefix_ + ':' if (UseCapturedNS_ and self.Number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumber>%s</%sNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.Number, input_name='Number'), namespaceprefix_ , eol_))
        if self.ParameterList is not None:
            namespaceprefix_ = self.ParameterList_nsprefix_ + ':' if (UseCapturedNS_ and self.ParameterList_nsprefix_) else ''
            self.ParameterList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParameterList', pretty_print=pretty_print)
        for Stage_ in self.Stage:
            namespaceprefix_ = self.Stage_nsprefix_ + ':' if (UseCapturedNS_ and self.Stage_nsprefix_) else ''
            Stage_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Stage', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='StagesType', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        if self.Handle is not None:
            element.set('Handle', self.gds_format_string(self.Handle))
        if self.Number is not None:
            Number_ = self.Number
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Number').text = self.gds_format_integer(Number_)
        if self.ParameterList is not None:
            ParameterList_ = self.ParameterList
            ParameterList_.to_etree(element, name_='ParameterList', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        for Stage_ in self.Stage:
            Stage_.to_etree(element, name_='Stage', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
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
        elif nodeName_ == 'ParameterList':
            obj_ = ParameterListType3.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParameterList = obj_
            obj_.original_tagname_ = 'ParameterList'
        elif nodeName_ == 'Stage':
            obj_ = StageType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Stage.append(obj_)
            obj_.original_tagname_ = 'Stage'
# end class StagesType


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


class StageType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, Mneumonic=None, Shorthand=None, Concept=None, Type=None, ModelHandle=None, gds_collector_=None, **kwargs_):
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
        self.Type = Type
        self.Type_nsprefix_ = None
        self.ModelHandle = ModelHandle
        self.ModelHandle_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, StageType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if StageType.subclass:
            return StageType.subclass(*args_, **kwargs_)
        else:
            return StageType(*args_, **kwargs_)
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
    def get_Type(self):
        return self.Type
    def set_Type(self, Type):
        self.Type = Type
    def get_ModelHandle(self):
        return self.ModelHandle
    def set_ModelHandle(self, ModelHandle):
        self.ModelHandle = ModelHandle
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def _hasContent(self):
        if (
            self.Mneumonic is not None or
            self.Shorthand is not None or
            self.Concept is not None or
            self.Type is not None or
            self.ModelHandle is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='StageType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('StageType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'StageType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='StageType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='StageType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='StageType'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position="%s"' % self.gds_format_integer(self.Position, input_name='Position'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='StageType', fromsubclass_=False, pretty_print=True):
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
        if self.Type is not None:
            namespaceprefix_ = self.Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sType>%s</%sType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Type), input_name='Type')), namespaceprefix_ , eol_))
        if self.ModelHandle is not None:
            namespaceprefix_ = self.ModelHandle_nsprefix_ + ':' if (UseCapturedNS_ and self.ModelHandle_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sModelHandle>%s</%sModelHandle>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ModelHandle), input_name='ModelHandle')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='StageType', mapping_=None, reverse_mapping_=None, nsmap_=None):
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
        if self.Type is not None:
            Type_ = self.Type
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Type').text = self.gds_format_string(Type_)
        if self.ModelHandle is not None:
            ModelHandle_ = self.ModelHandle
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}ModelHandle').text = self.gds_format_string(ModelHandle_)
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
        elif nodeName_ == 'Type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Type')
            value_ = self.gds_validate_string(value_, node, 'Type')
            self.Type = value_
            self.Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'ModelHandle':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ModelHandle')
            value_ = self.gds_validate_string(value_, node, 'ModelHandle')
            self.ModelHandle = value_
            self.ModelHandle_nsprefix_ = child_.prefix
# end class StageType


class BridgesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Handle=None, Number=None, ParameterList=None, Bridge=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        self.Number = Number
        self.Number_nsprefix_ = None
        self.ParameterList = ParameterList
        self.ParameterList_nsprefix_ = None
        if Bridge is None:
            self.Bridge = []
        else:
            self.Bridge = Bridge
        self.Bridge_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BridgesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BridgesType.subclass:
            return BridgesType.subclass(*args_, **kwargs_)
        else:
            return BridgesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Number(self):
        return self.Number
    def set_Number(self, Number):
        self.Number = Number
    def get_ParameterList(self):
        return self.ParameterList
    def set_ParameterList(self, ParameterList):
        self.ParameterList = ParameterList
    def get_Bridge(self):
        return self.Bridge
    def set_Bridge(self, Bridge):
        self.Bridge = Bridge
    def add_Bridge(self, value):
        self.Bridge.append(value)
    def insert_Bridge_at(self, index, value):
        self.Bridge.insert(index, value)
    def replace_Bridge_at(self, index, value):
        self.Bridge[index] = value
    def get_Handle(self):
        return self.Handle
    def set_Handle(self, Handle):
        self.Handle = Handle
    def _hasContent(self):
        if (
            self.Number is not None or
            self.ParameterList is not None or
            self.Bridge
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='BridgesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BridgesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BridgesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='BridgesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='BridgesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='BridgesType'):
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='BridgesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Number is not None:
            namespaceprefix_ = self.Number_nsprefix_ + ':' if (UseCapturedNS_ and self.Number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumber>%s</%sNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.Number, input_name='Number'), namespaceprefix_ , eol_))
        if self.ParameterList is not None:
            namespaceprefix_ = self.ParameterList_nsprefix_ + ':' if (UseCapturedNS_ and self.ParameterList_nsprefix_) else ''
            self.ParameterList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParameterList', pretty_print=pretty_print)
        for Bridge_ in self.Bridge:
            namespaceprefix_ = self.Bridge_nsprefix_ + ':' if (UseCapturedNS_ and self.Bridge_nsprefix_) else ''
            Bridge_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Bridge', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='BridgesType', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        if self.Handle is not None:
            element.set('Handle', self.gds_format_string(self.Handle))
        if self.Number is not None:
            Number_ = self.Number
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Number').text = self.gds_format_integer(Number_)
        if self.ParameterList is not None:
            ParameterList_ = self.ParameterList
            ParameterList_.to_etree(element, name_='ParameterList', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
        for Bridge_ in self.Bridge:
            Bridge_.to_etree(element, name_='Bridge', mapping_=mapping_, reverse_mapping_=reverse_mapping_, nsmap_=nsmap_)
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
        elif nodeName_ == 'ParameterList':
            obj_ = ParameterListType5.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParameterList = obj_
            obj_.original_tagname_ = 'ParameterList'
        elif nodeName_ == 'Bridge':
            obj_ = BridgeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Bridge.append(obj_)
            obj_.original_tagname_ = 'Bridge'
# end class BridgesType


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


class BridgeType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, StatePosition=None, From=None, To=None, Type=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Position = _cast(int, Position)
        self.Position_nsprefix_ = None
        self.StatePosition = StatePosition
        self.StatePosition_nsprefix_ = None
        self.From = From
        self.From_nsprefix_ = None
        self.To = To
        self.To_nsprefix_ = None
        self.Type = Type
        self.Type_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BridgeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BridgeType.subclass:
            return BridgeType.subclass(*args_, **kwargs_)
        else:
            return BridgeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_StatePosition(self):
        return self.StatePosition
    def set_StatePosition(self, StatePosition):
        self.StatePosition = StatePosition
    def get_From(self):
        return self.From
    def set_From(self, From):
        self.From = From
    def get_To(self):
        return self.To
    def set_To(self, To):
        self.To = To
    def get_Type(self):
        return self.Type
    def set_Type(self, Type):
        self.Type = Type
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def _hasContent(self):
        if (
            self.StatePosition is not None or
            self.From is not None or
            self.To is not None or
            self.Type is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='BridgeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BridgeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BridgeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='BridgeType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='BridgeType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='BridgeType'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position="%s"' % self.gds_format_integer(self.Position, input_name='Position'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='BridgeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.StatePosition is not None:
            namespaceprefix_ = self.StatePosition_nsprefix_ + ':' if (UseCapturedNS_ and self.StatePosition_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sStatePosition>%s</%sStatePosition>%s' % (namespaceprefix_ , self.gds_format_integer(self.StatePosition, input_name='StatePosition'), namespaceprefix_ , eol_))
        if self.From is not None:
            namespaceprefix_ = self.From_nsprefix_ + ':' if (UseCapturedNS_ and self.From_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sFrom>%s</%sFrom>%s' % (namespaceprefix_ , self.gds_format_integer(self.From, input_name='From'), namespaceprefix_ , eol_))
        if self.To is not None:
            namespaceprefix_ = self.To_nsprefix_ + ':' if (UseCapturedNS_ and self.To_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTo>%s</%sTo>%s' % (namespaceprefix_ , self.gds_format_integer(self.To, input_name='To'), namespaceprefix_ , eol_))
        if self.Type is not None:
            namespaceprefix_ = self.Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sType>%s</%sType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Type), input_name='Type')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='BridgeType', mapping_=None, reverse_mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://github.com/wdatasci/WDS-ModelSpec}' + name_, nsmap=nsmap_)
        if self.Position is not None:
            element.set('Position', self.gds_format_integer(self.Position))
        if self.StatePosition is not None:
            StatePosition_ = self.StatePosition
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}StatePosition').text = self.gds_format_integer(StatePosition_)
        if self.From is not None:
            From_ = self.From
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}From').text = self.gds_format_integer(From_)
        if self.To is not None:
            To_ = self.To
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}To').text = self.gds_format_integer(To_)
        if self.Type is not None:
            Type_ = self.Type
            etree_.SubElement(element, '{https://github.com/wdatasci/WDS-ModelSpec}Type').text = self.gds_format_string(Type_)
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
        if nodeName_ == 'StatePosition' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'StatePosition')
            ival_ = self.gds_validate_integer(ival_, node, 'StatePosition')
            self.StatePosition = ival_
            self.StatePosition_nsprefix_ = child_.prefix
        elif nodeName_ == 'From' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'From')
            ival_ = self.gds_validate_integer(ival_, node, 'From')
            self.From = ival_
            self.From_nsprefix_ = child_.prefix
        elif nodeName_ == 'To' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'To')
            ival_ = self.gds_validate_integer(ival_, node, 'To')
            self.To = ival_
            self.To_nsprefix_ = child_.prefix
        elif nodeName_ == 'Type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Type')
            value_ = self.gds_validate_string(value_, node, 'Type')
            self.Type = value_
            self.Type_nsprefix_ = child_.prefix
# end class BridgeType


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
        rootTag = 'WDSStateSpace'
        rootClass = WDSStateSpace
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
        rootTag = 'WDSStateSpace'
        rootClass = WDSStateSpace
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
        rootTag = 'WDSStateSpace'
        rootClass = WDSStateSpace
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
        rootTag = 'WDSStateSpace'
        rootClass = WDSStateSpace
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from gWDSStatesAndStagesSpec import *\n\n')
        sys.stdout.write('import gWDSStatesAndStagesSpec as model_\n\n')
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
    "BridgeType",
    "BridgesType",
    "ParameterListType",
    "ParameterListType1",
    "ParameterListType3",
    "ParameterListType5",
    "ParameterType",
    "ParameterType2",
    "ParameterType4",
    "ParameterType6",
    "StageType",
    "StagesType",
    "StateType",
    "StatesType",
    "WDSStateSpace"
]
