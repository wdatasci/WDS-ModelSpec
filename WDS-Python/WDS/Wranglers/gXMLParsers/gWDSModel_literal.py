#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Mon Jun 27 09:20:27 2022 by generateDS.py version 2.40.13.
# Python 3.9.5 (default, Nov 23 2021, 15:27:38)  [GCC 9.3.0]
#
# Command line options:
#   ('--mixed-case-enums', '')
#   ('-f', '')
#   ('--export', 'write literal')
#   ('-o', './WDS-Python/WDS/Wranglers/gXMLParsers/gWDSModel_literal.py')
#
# Command line arguments:
#   ./WDS-XML/XSD/WDSModel.xsd
#
# Command line:
#   ./WDS-Python/scripts/generateDS_unsnaked --mixed-case-enums -f --export="write literal" -o "./WDS-Python/WDS/Wranglers/gXMLParsers/gWDSModel_literal.py" ./WDS-XML/XSD/WDSModel.xsd
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


class DTypType(str, Enum):
    Unk='Unk'
    Dbl='Dbl'
    Lng='Lng'
    Int='Int'
    Dte='Dte'
    DTm='DTm'
    Str='Str'
    VLS='VLS'
    Byt='Byt'
    Bln='Bln'
    Any='Any'


class Annotation(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, AppInfo=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if AppInfo is None:
            self.AppInfo = []
        else:
            self.AppInfo = AppInfo
        self.AppInfo_nsprefix_ = None
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Annotation)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Annotation.subclass:
            return Annotation.subclass(*args_, **kwargs_)
        else:
            return Annotation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_AppInfo(self):
        return self.AppInfo
    def set_AppInfo(self, AppInfo):
        self.AppInfo = AppInfo
    def add_AppInfo(self, value):
        self.AppInfo.append(value)
    def insert_AppInfo_at(self, index, value):
        self.AppInfo.insert(index, value)
    def replace_AppInfo_at(self, index, value):
        self.AppInfo[index] = value
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            self.AppInfo or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Annotation', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Annotation')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Annotation':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Annotation')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Annotation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Annotation'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Annotation', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for AppInfo_ in self.AppInfo:
            namespaceprefix_ = self.AppInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.AppInfo_nsprefix_) else ''
            AppInfo_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AppInfo', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Annotation'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('],\n')
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'AppInfo':
            obj_ = AppInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'AppInfo', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_AppInfo'):
              self.add_AppInfo(obj_.value)
            elif hasattr(self, 'set_AppInfo'):
              self.set_AppInfo(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class Annotation


class Column(GeneratedsSuper):
    """  
    * Column --
      Used in signatures, parameter sets, and table definitions.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, BlockID=None, RowID=None, Static=None, Name=None, Handle=None, DTyp=None, Length=None, Default=None, MetaDataXRef=None, ProjectHandleXRef=None, Use=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.BlockID = _cast(None, BlockID)
        self.BlockID_nsprefix_ = None
        self.RowID = _cast(None, RowID)
        self.RowID_nsprefix_ = None
        self.Static = _cast(None, Static)
        self.Static_nsprefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        self.DTyp = _cast(None, DTyp)
        self.DTyp_nsprefix_ = None
        self.Length = _cast(int, Length)
        self.Length_nsprefix_ = None
        self.Default = _cast(None, Default)
        self.Default_nsprefix_ = None
        self.MetaDataXRef = _cast(None, MetaDataXRef)
        self.MetaDataXRef_nsprefix_ = None
        self.ProjectHandleXRef = _cast(None, ProjectHandleXRef)
        self.ProjectHandleXRef_nsprefix_ = None
        self.Use = _cast(None, Use)
        self.Use_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Column)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Column.subclass:
            return Column.subclass(*args_, **kwargs_)
        else:
            return Column(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_BlockID(self):
        return self.BlockID
    def set_BlockID(self, BlockID):
        self.BlockID = BlockID
    def get_RowID(self):
        return self.RowID
    def set_RowID(self, RowID):
        self.RowID = RowID
    def get_Static(self):
        return self.Static
    def set_Static(self, Static):
        self.Static = Static
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def get_Handle(self):
        return self.Handle
    def set_Handle(self, Handle):
        self.Handle = Handle
    def get_DTyp(self):
        return self.DTyp
    def set_DTyp(self, DTyp):
        self.DTyp = DTyp
    def get_Length(self):
        return self.Length
    def set_Length(self, Length):
        self.Length = Length
    def get_Default(self):
        return self.Default
    def set_Default(self, Default):
        self.Default = Default
    def get_MetaDataXRef(self):
        return self.MetaDataXRef
    def set_MetaDataXRef(self, MetaDataXRef):
        self.MetaDataXRef = MetaDataXRef
    def get_ProjectHandleXRef(self):
        return self.ProjectHandleXRef
    def set_ProjectHandleXRef(self, ProjectHandleXRef):
        self.ProjectHandleXRef = ProjectHandleXRef
    def get_Use(self):
        return self.Use
    def set_Use(self, Use):
        self.Use = Use
    def validate_DTypType(self, value):
        # Validate type DTypType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Unk', 'Dbl', 'Lng', 'Int', 'Dte', 'DTm', 'Str', 'VLS', 'Byt', 'Bln', 'Any']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on DTypType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Column', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Column')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Column':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Column')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Column', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Column'):
        if self.BlockID is not None and 'BlockID' not in already_processed:
            already_processed.add('BlockID')
            outfile.write(' BlockID=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.BlockID), input_name='BlockID')), ))
        if self.RowID is not None and 'RowID' not in already_processed:
            already_processed.add('RowID')
            outfile.write(' RowID=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.RowID), input_name='RowID')), ))
        if self.Static is not None and 'Static' not in already_processed:
            already_processed.add('Static')
            outfile.write(' Static=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Static), input_name='Static')), ))
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
        if self.DTyp is not None and 'DTyp' not in already_processed:
            already_processed.add('DTyp')
            outfile.write(' DTyp=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.DTyp), input_name='DTyp')), ))
        if self.Length is not None and 'Length' not in already_processed:
            already_processed.add('Length')
            outfile.write(' Length="%s"' % self.gds_format_integer(self.Length, input_name='Length'))
        if self.Default is not None and 'Default' not in already_processed:
            already_processed.add('Default')
            outfile.write(' Default=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Default), input_name='Default')), ))
        if self.MetaDataXRef is not None and 'MetaDataXRef' not in already_processed:
            already_processed.add('MetaDataXRef')
            outfile.write(' MetaDataXRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.MetaDataXRef), input_name='MetaDataXRef')), ))
        if self.ProjectHandleXRef is not None and 'ProjectHandleXRef' not in already_processed:
            already_processed.add('ProjectHandleXRef')
            outfile.write(' ProjectHandleXRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ProjectHandleXRef), input_name='ProjectHandleXRef')), ))
        if self.Use is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            outfile.write(' Use=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Use), input_name='Use')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Column', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='Column'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.BlockID is not None and 'BlockID' not in already_processed:
            already_processed.add('BlockID')
            showIndent(outfile, level)
            outfile.write('BlockID="%s",\n' % (self.BlockID,))
        if self.RowID is not None and 'RowID' not in already_processed:
            already_processed.add('RowID')
            showIndent(outfile, level)
            outfile.write('RowID="%s",\n' % (self.RowID,))
        if self.Static is not None and 'Static' not in already_processed:
            already_processed.add('Static')
            showIndent(outfile, level)
            outfile.write('Static="%s",\n' % (self.Static,))
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            showIndent(outfile, level)
            outfile.write('Handle="%s",\n' % (self.Handle,))
        if self.DTyp is not None and 'DTyp' not in already_processed:
            already_processed.add('DTyp')
            showIndent(outfile, level)
            outfile.write('DTyp="%s",\n' % (self.DTyp,))
        if self.Length is not None and 'Length' not in already_processed:
            already_processed.add('Length')
            showIndent(outfile, level)
            outfile.write('Length=%d,\n' % (self.Length,))
        if self.Default is not None and 'Default' not in already_processed:
            already_processed.add('Default')
            showIndent(outfile, level)
            outfile.write('Default="%s",\n' % (self.Default,))
        if self.MetaDataXRef is not None and 'MetaDataXRef' not in already_processed:
            already_processed.add('MetaDataXRef')
            showIndent(outfile, level)
            outfile.write('MetaDataXRef="%s",\n' % (self.MetaDataXRef,))
        if self.ProjectHandleXRef is not None and 'ProjectHandleXRef' not in already_processed:
            already_processed.add('ProjectHandleXRef')
            showIndent(outfile, level)
            outfile.write('ProjectHandleXRef="%s",\n' % (self.ProjectHandleXRef,))
        if self.Use is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            showIndent(outfile, level)
            outfile.write('Use="%s",\n' % (self.Use,))
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
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
        value = find_attr_value_('BlockID', node)
        if value is not None and 'BlockID' not in already_processed:
            already_processed.add('BlockID')
            self.BlockID = value
        value = find_attr_value_('RowID', node)
        if value is not None and 'RowID' not in already_processed:
            already_processed.add('RowID')
            self.RowID = value
        value = find_attr_value_('Static', node)
        if value is not None and 'Static' not in already_processed:
            already_processed.add('Static')
            self.Static = value
        value = find_attr_value_('Name', node)
        if value is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            self.Name = value
        value = find_attr_value_('Handle', node)
        if value is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            self.Handle = value
        value = find_attr_value_('DTyp', node)
        if value is not None and 'DTyp' not in already_processed:
            already_processed.add('DTyp')
            self.DTyp = value
            self.validate_DTypType(self.DTyp)    # validate type DTypType
        value = find_attr_value_('Length', node)
        if value is not None and 'Length' not in already_processed:
            already_processed.add('Length')
            self.Length = self.gds_parse_integer(value, node, 'Length')
        value = find_attr_value_('Default', node)
        if value is not None and 'Default' not in already_processed:
            already_processed.add('Default')
            self.Default = value
        value = find_attr_value_('MetaDataXRef', node)
        if value is not None and 'MetaDataXRef' not in already_processed:
            already_processed.add('MetaDataXRef')
            self.MetaDataXRef = value
        value = find_attr_value_('ProjectHandleXRef', node)
        if value is not None and 'ProjectHandleXRef' not in already_processed:
            already_processed.add('ProjectHandleXRef')
            self.ProjectHandleXRef = value
        value = find_attr_value_('Use', node)
        if value is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            self.Use = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Column


class Parameter(GeneratedsSuper):
    """Parameter --
    Used in signatures, parameter sets, and table definitions.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, Handle=None, DTyp=None, Length=None, Default=None, MetaDataXRef=None, ProjectHandleXRef=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        self.DTyp = _cast(None, DTyp)
        self.DTyp_nsprefix_ = None
        self.Length = _cast(int, Length)
        self.Length_nsprefix_ = None
        self.Default = _cast(None, Default)
        self.Default_nsprefix_ = None
        self.MetaDataXRef = _cast(None, MetaDataXRef)
        self.MetaDataXRef_nsprefix_ = None
        self.ProjectHandleXRef = _cast(None, ProjectHandleXRef)
        self.ProjectHandleXRef_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Parameter)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Parameter.subclass:
            return Parameter.subclass(*args_, **kwargs_)
        else:
            return Parameter(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def get_Handle(self):
        return self.Handle
    def set_Handle(self, Handle):
        self.Handle = Handle
    def get_DTyp(self):
        return self.DTyp
    def set_DTyp(self, DTyp):
        self.DTyp = DTyp
    def get_Length(self):
        return self.Length
    def set_Length(self, Length):
        self.Length = Length
    def get_Default(self):
        return self.Default
    def set_Default(self, Default):
        self.Default = Default
    def get_MetaDataXRef(self):
        return self.MetaDataXRef
    def set_MetaDataXRef(self, MetaDataXRef):
        self.MetaDataXRef = MetaDataXRef
    def get_ProjectHandleXRef(self):
        return self.ProjectHandleXRef
    def set_ProjectHandleXRef(self, ProjectHandleXRef):
        self.ProjectHandleXRef = ProjectHandleXRef
    def validate_DTypType(self, value):
        # Validate type DTypType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Unk', 'Dbl', 'Lng', 'Int', 'Dte', 'DTm', 'Str', 'VLS', 'Byt', 'Bln', 'Any']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on DTypType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Parameter', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Parameter')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Parameter':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Parameter')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Parameter', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Parameter'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
        if self.DTyp is not None and 'DTyp' not in already_processed:
            already_processed.add('DTyp')
            outfile.write(' DTyp=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.DTyp), input_name='DTyp')), ))
        if self.Length is not None and 'Length' not in already_processed:
            already_processed.add('Length')
            outfile.write(' Length="%s"' % self.gds_format_integer(self.Length, input_name='Length'))
        if self.Default is not None and 'Default' not in already_processed:
            already_processed.add('Default')
            outfile.write(' Default=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Default), input_name='Default')), ))
        if self.MetaDataXRef is not None and 'MetaDataXRef' not in already_processed:
            already_processed.add('MetaDataXRef')
            outfile.write(' MetaDataXRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.MetaDataXRef), input_name='MetaDataXRef')), ))
        if self.ProjectHandleXRef is not None and 'ProjectHandleXRef' not in already_processed:
            already_processed.add('ProjectHandleXRef')
            outfile.write(' ProjectHandleXRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ProjectHandleXRef), input_name='ProjectHandleXRef')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Parameter', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='Parameter'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            showIndent(outfile, level)
            outfile.write('Handle="%s",\n' % (self.Handle,))
        if self.DTyp is not None and 'DTyp' not in already_processed:
            already_processed.add('DTyp')
            showIndent(outfile, level)
            outfile.write('DTyp="%s",\n' % (self.DTyp,))
        if self.Length is not None and 'Length' not in already_processed:
            already_processed.add('Length')
            showIndent(outfile, level)
            outfile.write('Length=%d,\n' % (self.Length,))
        if self.Default is not None and 'Default' not in already_processed:
            already_processed.add('Default')
            showIndent(outfile, level)
            outfile.write('Default="%s",\n' % (self.Default,))
        if self.MetaDataXRef is not None and 'MetaDataXRef' not in already_processed:
            already_processed.add('MetaDataXRef')
            showIndent(outfile, level)
            outfile.write('MetaDataXRef="%s",\n' % (self.MetaDataXRef,))
        if self.ProjectHandleXRef is not None and 'ProjectHandleXRef' not in already_processed:
            already_processed.add('ProjectHandleXRef')
            showIndent(outfile, level)
            outfile.write('ProjectHandleXRef="%s",\n' % (self.ProjectHandleXRef,))
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
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
        value = find_attr_value_('DTyp', node)
        if value is not None and 'DTyp' not in already_processed:
            already_processed.add('DTyp')
            self.DTyp = value
            self.validate_DTypType(self.DTyp)    # validate type DTypType
        value = find_attr_value_('Length', node)
        if value is not None and 'Length' not in already_processed:
            already_processed.add('Length')
            self.Length = self.gds_parse_integer(value, node, 'Length')
        value = find_attr_value_('Default', node)
        if value is not None and 'Default' not in already_processed:
            already_processed.add('Default')
            self.Default = value
        value = find_attr_value_('MetaDataXRef', node)
        if value is not None and 'MetaDataXRef' not in already_processed:
            already_processed.add('MetaDataXRef')
            self.MetaDataXRef = value
        value = find_attr_value_('ProjectHandleXRef', node)
        if value is not None and 'ProjectHandleXRef' not in already_processed:
            already_processed.add('ProjectHandleXRef')
            self.ProjectHandleXRef = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Parameter


class Columns(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Column=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Column is None:
            self.Column = []
        else:
            self.Column = Column
        self.Column_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Columns)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Columns.subclass:
            return Columns.subclass(*args_, **kwargs_)
        else:
            return Columns(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Column(self):
        return self.Column
    def set_Column(self, Column):
        self.Column = Column
    def add_Column(self, value):
        self.Column.append(value)
    def insert_Column_at(self, index, value):
        self.Column.insert(index, value)
    def replace_Column_at(self, index, value):
        self.Column[index] = value
    def _hasContent(self):
        if (
            self.Column
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Columns', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Columns')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Columns':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Columns')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Columns', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Columns'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Columns', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Column_ in self.Column:
            namespaceprefix_ = self.Column_nsprefix_ + ':' if (UseCapturedNS_ and self.Column_nsprefix_) else ''
            Column_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Column', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Columns'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Column=[\n')
        level += 1
        for Column_ in self.Column:
            showIndent(outfile, level)
            outfile.write('model_.Column(\n')
            Column_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'Column':
            obj_ = Column.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Column.append(obj_)
            obj_.original_tagname_ = 'Column'
# end class Columns


class Parameters(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Column=None, Parameter=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Column is None:
            self.Column = []
        else:
            self.Column = Column
        self.Column_nsprefix_ = None
        if Parameter is None:
            self.Parameter = []
        else:
            self.Parameter = Parameter
        self.Parameter_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Parameters)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Parameters.subclass:
            return Parameters.subclass(*args_, **kwargs_)
        else:
            return Parameters(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Column(self):
        return self.Column
    def set_Column(self, Column):
        self.Column = Column
    def add_Column(self, value):
        self.Column.append(value)
    def insert_Column_at(self, index, value):
        self.Column.insert(index, value)
    def replace_Column_at(self, index, value):
        self.Column[index] = value
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
            self.Column or
            self.Parameter
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Parameters', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Parameters')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Parameters':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Parameters')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Parameters', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Parameters'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Parameters', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Column_ in self.Column:
            namespaceprefix_ = self.Column_nsprefix_ + ':' if (UseCapturedNS_ and self.Column_nsprefix_) else ''
            Column_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Column', pretty_print=pretty_print)
        for Parameter_ in self.Parameter:
            namespaceprefix_ = self.Parameter_nsprefix_ + ':' if (UseCapturedNS_ and self.Parameter_nsprefix_) else ''
            Parameter_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Parameter', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Parameters'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Column=[\n')
        level += 1
        for Column_ in self.Column:
            showIndent(outfile, level)
            outfile.write('model_.Column(\n')
            Column_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('Parameter=[\n')
        level += 1
        for Parameter_ in self.Parameter:
            showIndent(outfile, level)
            outfile.write('model_.Parameter(\n')
            Parameter_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'Column':
            obj_ = Column.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Column.append(obj_)
            obj_.original_tagname_ = 'Column'
        elif nodeName_ == 'Parameter':
            obj_ = Parameter.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Parameter.append(obj_)
            obj_.original_tagname_ = 'Parameter'
# end class Parameters


class EnumValue(GeneratedsSuper):
    """EnumValue --
    The enum value for each element is taken from its name.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.anyAttributes_ = {}
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EnumValue)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EnumValue.subclass:
            return EnumValue.subclass(*args_, **kwargs_)
        else:
            return EnumValue(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def get_anyAttributes_(self): return self.anyAttributes_
    def set_anyAttributes_(self, anyAttributes_): self.anyAttributes_ = anyAttributes_
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='EnumValue', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EnumValue')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EnumValue':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EnumValue')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EnumValue', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EnumValue'):
        unique_counter = 0
        for name, value in self.anyAttributes_.items():
            xsinamespaceprefix = 'xsi'
            xsinamespace1 = 'http://www.w3.org/2001/XMLSchema-instance'
            xsinamespace2 = '{%s}' % (xsinamespace1, )
            if name.startswith(xsinamespace2):
                name1 = name[len(xsinamespace2):]
                name2 = '%s:%s' % (xsinamespaceprefix, name1, )
                if name2 not in already_processed:
                    already_processed.add(name2)
                    outfile.write(' %s=%s' % (name2, quote_attrib(value), ))
            else:
                mo = re_.match(Namespace_extract_pat_, name)
                if mo is not None:
                    namespace, name = mo.group(1, 2)
                    if name not in already_processed:
                        already_processed.add(name)
                        if namespace == 'http://www.w3.org/XML/1998/namespace':
                            outfile.write(' %s=%s' % (
                                name, quote_attrib(value), ))
                        else:
                            unique_counter += 1
                            outfile.write(' xmlns:%d="%s"' % (
                                unique_counter, namespace, ))
                            outfile.write(' %d:%s=%s' % (
                                unique_counter, name, quote_attrib(value), ))
                else:
                    if name not in already_processed:
                        already_processed.add(name)
                        outfile.write(' %s=%s' % (
                            name, quote_attrib(value), ))
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='EnumValue', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='EnumValue'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
        for name, value in self.anyAttributes_.items():
            showIndent(outfile, level)
            outfile.write('%s="%s",\n' % (name, value,))
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
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
        self.anyAttributes_ = {}
        for name, value in attrs.items():
            if name not in already_processed:
                self.anyAttributes_[name] = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class EnumValue


class EnumValues(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, EnumValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if EnumValue is None:
            self.EnumValue = []
        else:
            self.EnumValue = EnumValue
        self.EnumValue_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EnumValues)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EnumValues.subclass:
            return EnumValues.subclass(*args_, **kwargs_)
        else:
            return EnumValues(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_EnumValue(self):
        return self.EnumValue
    def set_EnumValue(self, EnumValue):
        self.EnumValue = EnumValue
    def add_EnumValue(self, value):
        self.EnumValue.append(value)
    def insert_EnumValue_at(self, index, value):
        self.EnumValue.insert(index, value)
    def replace_EnumValue_at(self, index, value):
        self.EnumValue[index] = value
    def _hasContent(self):
        if (
            self.EnumValue
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='EnumValues', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EnumValues')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EnumValues':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EnumValues')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EnumValues', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EnumValues'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='EnumValues', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for EnumValue_ in self.EnumValue:
            namespaceprefix_ = self.EnumValue_nsprefix_ + ':' if (UseCapturedNS_ and self.EnumValue_nsprefix_) else ''
            EnumValue_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EnumValue', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='EnumValues'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('EnumValue=[\n')
        level += 1
        for EnumValue_ in self.EnumValue:
            showIndent(outfile, level)
            outfile.write('model_.EnumValue(\n')
            EnumValue_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'EnumValue':
            obj_ = EnumValue.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EnumValue.append(obj_)
            obj_.original_tagname_ = 'EnumValue'
# end class EnumValues


class Enum(GeneratedsSuper):
    """EnumMD --
    The EnumMD is the unordered collection of EnumAttrMD elements for the EnumValue elements.
    Specification of EnumMD beside the EnumValues collection is for programmatic purposes of generating additional methods linked to the enum values.
    This is to balance the needs of enum code in C++/C#/Java/Python/ect where it may or may not be natural to extend a basic enum class.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, EnumMD=None, EnumValue=None, EnumValues=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.EnumMD = EnumMD
        self.EnumMD_nsprefix_ = None
        if EnumValue is None:
            self.EnumValue = []
        else:
            self.EnumValue = EnumValue
        self.EnumValue_nsprefix_ = None
        self.EnumValues = EnumValues
        self.EnumValues_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Enum)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Enum.subclass:
            return Enum.subclass(*args_, **kwargs_)
        else:
            return Enum(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_EnumMD(self):
        return self.EnumMD
    def set_EnumMD(self, EnumMD):
        self.EnumMD = EnumMD
    def get_EnumValue(self):
        return self.EnumValue
    def set_EnumValue(self, EnumValue):
        self.EnumValue = EnumValue
    def add_EnumValue(self, value):
        self.EnumValue.append(value)
    def insert_EnumValue_at(self, index, value):
        self.EnumValue.insert(index, value)
    def replace_EnumValue_at(self, index, value):
        self.EnumValue[index] = value
    def get_EnumValues(self):
        return self.EnumValues
    def set_EnumValues(self, EnumValues):
        self.EnumValues = EnumValues
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def _hasContent(self):
        if (
            self.EnumMD is not None or
            self.EnumValue or
            self.EnumValues is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Enum', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Enum')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Enum':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Enum')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Enum', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Enum'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Enum', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.EnumMD is not None:
            namespaceprefix_ = self.EnumMD_nsprefix_ + ':' if (UseCapturedNS_ and self.EnumMD_nsprefix_) else ''
            self.EnumMD.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EnumMD', pretty_print=pretty_print)
        for EnumValue_ in self.EnumValue:
            namespaceprefix_ = self.EnumValue_nsprefix_ + ':' if (UseCapturedNS_ and self.EnumValue_nsprefix_) else ''
            EnumValue_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EnumValue', pretty_print=pretty_print)
        if self.EnumValues is not None:
            namespaceprefix_ = self.EnumValues_nsprefix_ + ':' if (UseCapturedNS_ and self.EnumValues_nsprefix_) else ''
            self.EnumValues.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EnumValues', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Enum'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.EnumMD is not None:
            showIndent(outfile, level)
            outfile.write('EnumMD=model_.EnumMDType(\n')
            self.EnumMD.exportLiteral(outfile, level, name_='EnumMD')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('EnumValue=[\n')
        level += 1
        for EnumValue_ in self.EnumValue:
            showIndent(outfile, level)
            outfile.write('model_.EnumValue(\n')
            EnumValue_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.EnumValues is not None:
            showIndent(outfile, level)
            outfile.write('EnumValues=model_.EnumValues(\n')
            self.EnumValues.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
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
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'EnumMD':
            obj_ = EnumMDType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EnumMD = obj_
            obj_.original_tagname_ = 'EnumMD'
        elif nodeName_ == 'EnumValue':
            obj_ = EnumValue.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EnumValue.append(obj_)
            obj_.original_tagname_ = 'EnumValue'
        elif nodeName_ == 'EnumValues':
            obj_ = EnumValues.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EnumValues = obj_
            obj_.original_tagname_ = 'EnumValues'
# end class Enum


class Enums(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Enum=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Enum is None:
            self.Enum = []
        else:
            self.Enum = Enum
        self.Enum_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Enums)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Enums.subclass:
            return Enums.subclass(*args_, **kwargs_)
        else:
            return Enums(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Enum(self):
        return self.Enum
    def set_Enum(self, Enum):
        self.Enum = Enum
    def add_Enum(self, value):
        self.Enum.append(value)
    def insert_Enum_at(self, index, value):
        self.Enum.insert(index, value)
    def replace_Enum_at(self, index, value):
        self.Enum[index] = value
    def _hasContent(self):
        if (
            self.Enum
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Enums', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Enums')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Enums':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Enums')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Enums', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Enums'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Enums', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Enum_ in self.Enum:
            namespaceprefix_ = self.Enum_nsprefix_ + ':' if (UseCapturedNS_ and self.Enum_nsprefix_) else ''
            Enum_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Enum', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Enums'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Enum=[\n')
        level += 1
        for Enum_ in self.Enum:
            showIndent(outfile, level)
            outfile.write('model_.Enum(\n')
            Enum_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'Enum':
            obj_ = Enum.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Enum.append(obj_)
            obj_.original_tagname_ = 'Enum'
# end class Enums


class UDxInfo(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Cpp=None, Java=None, Python=None, SQL=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Cpp = Cpp
        self.Cpp_nsprefix_ = None
        self.Java = Java
        self.Java_nsprefix_ = None
        self.Python = Python
        self.Python_nsprefix_ = None
        self.SQL = SQL
        self.SQL_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, UDxInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if UDxInfo.subclass:
            return UDxInfo.subclass(*args_, **kwargs_)
        else:
            return UDxInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Cpp(self):
        return self.Cpp
    def set_Cpp(self, Cpp):
        self.Cpp = Cpp
    def get_Java(self):
        return self.Java
    def set_Java(self, Java):
        self.Java = Java
    def get_Python(self):
        return self.Python
    def set_Python(self, Python):
        self.Python = Python
    def get_SQL(self):
        return self.SQL
    def set_SQL(self, SQL):
        self.SQL = SQL
    def _hasContent(self):
        if (
            self.Cpp is not None or
            self.Java is not None or
            self.Python is not None or
            self.SQL is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='UDxInfo', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('UDxInfo')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'UDxInfo':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='UDxInfo')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='UDxInfo', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='UDxInfo'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='UDxInfo', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Cpp is not None:
            namespaceprefix_ = self.Cpp_nsprefix_ + ':' if (UseCapturedNS_ and self.Cpp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCpp>%s</%sCpp>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Cpp), input_name='Cpp')), namespaceprefix_ , eol_))
        if self.Java is not None:
            namespaceprefix_ = self.Java_nsprefix_ + ':' if (UseCapturedNS_ and self.Java_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sJava>%s</%sJava>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Java), input_name='Java')), namespaceprefix_ , eol_))
        if self.Python is not None:
            namespaceprefix_ = self.Python_nsprefix_ + ':' if (UseCapturedNS_ and self.Python_nsprefix_) else ''
            self.Python.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Python', pretty_print=pretty_print)
        if self.SQL is not None:
            namespaceprefix_ = self.SQL_nsprefix_ + ':' if (UseCapturedNS_ and self.SQL_nsprefix_) else ''
            self.SQL.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SQL', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='UDxInfo'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.Cpp is not None:
            showIndent(outfile, level)
            outfile.write('Cpp=%s,\n' % self.gds_encode(quote_python(self.Cpp)))
        if self.Java is not None:
            showIndent(outfile, level)
            outfile.write('Java=%s,\n' % self.gds_encode(quote_python(self.Java)))
        if self.Python is not None:
            showIndent(outfile, level)
            outfile.write('Python=model_.PythonType(\n')
            self.Python.exportLiteral(outfile, level, name_='Python')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.SQL is not None:
            showIndent(outfile, level)
            outfile.write('SQL=model_.SQLType(\n')
            self.SQL.exportLiteral(outfile, level, name_='SQL')
            showIndent(outfile, level)
            outfile.write('),\n')
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
        if nodeName_ == 'Cpp':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Cpp')
            value_ = self.gds_validate_string(value_, node, 'Cpp')
            self.Cpp = value_
            self.Cpp_nsprefix_ = child_.prefix
        elif nodeName_ == 'Java':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Java')
            value_ = self.gds_validate_string(value_, node, 'Java')
            self.Java = value_
            self.Java_nsprefix_ = child_.prefix
        elif nodeName_ == 'Python':
            obj_ = PythonType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Python = obj_
            obj_.original_tagname_ = 'Python'
        elif nodeName_ == 'SQL':
            obj_ = SQLType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SQL = obj_
            obj_.original_tagname_ = 'SQL'
# end class UDxInfo


class UDxs(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, UDF=None, UDTF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if UDF is None:
            self.UDF = []
        else:
            self.UDF = UDF
        self.UDF_nsprefix_ = None
        if UDTF is None:
            self.UDTF = []
        else:
            self.UDTF = UDTF
        self.UDTF_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, UDxs)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if UDxs.subclass:
            return UDxs.subclass(*args_, **kwargs_)
        else:
            return UDxs(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_UDF(self):
        return self.UDF
    def set_UDF(self, UDF):
        self.UDF = UDF
    def add_UDF(self, value):
        self.UDF.append(value)
    def insert_UDF_at(self, index, value):
        self.UDF.insert(index, value)
    def replace_UDF_at(self, index, value):
        self.UDF[index] = value
    def get_UDTF(self):
        return self.UDTF
    def set_UDTF(self, UDTF):
        self.UDTF = UDTF
    def add_UDTF(self, value):
        self.UDTF.append(value)
    def insert_UDTF_at(self, index, value):
        self.UDTF.insert(index, value)
    def replace_UDTF_at(self, index, value):
        self.UDTF[index] = value
    def _hasContent(self):
        if (
            self.UDF or
            self.UDTF
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='UDxs', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('UDxs')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'UDxs':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='UDxs')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='UDxs', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='UDxs'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='UDxs', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for UDF_ in self.UDF:
            namespaceprefix_ = self.UDF_nsprefix_ + ':' if (UseCapturedNS_ and self.UDF_nsprefix_) else ''
            UDF_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UDF', pretty_print=pretty_print)
        for UDTF_ in self.UDTF:
            namespaceprefix_ = self.UDTF_nsprefix_ + ':' if (UseCapturedNS_ and self.UDTF_nsprefix_) else ''
            UDTF_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UDTF', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='UDxs'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('UDF=[\n')
        level += 1
        for UDF_ in self.UDF:
            showIndent(outfile, level)
            outfile.write('model_.UDFType(\n')
            UDF_.exportLiteral(outfile, level, name_='UDFType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('UDTF=[\n')
        level += 1
        for UDTF_ in self.UDTF:
            showIndent(outfile, level)
            outfile.write('model_.UDTFType(\n')
            UDTF_.exportLiteral(outfile, level, name_='UDTFType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'UDF':
            obj_ = UDFType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UDF.append(obj_)
            obj_.original_tagname_ = 'UDF'
        elif nodeName_ == 'UDTF':
            obj_ = UDTFType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UDTF.append(obj_)
            obj_.original_tagname_ = 'UDTF'
# end class UDxs


class Source(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, MetaDataXRef=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.MetaDataXRef = _cast(None, MetaDataXRef)
        self.MetaDataXRef_nsprefix_ = None
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Source)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Source.subclass:
            return Source.subclass(*args_, **kwargs_)
        else:
            return Source(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_MetaDataXRef(self):
        return self.MetaDataXRef
    def set_MetaDataXRef(self, MetaDataXRef):
        self.MetaDataXRef = MetaDataXRef
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Source', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Source')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Source':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Source')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Source'):
        if self.MetaDataXRef is not None and 'MetaDataXRef' not in already_processed:
            already_processed.add('MetaDataXRef')
            outfile.write(' MetaDataXRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.MetaDataXRef), input_name='MetaDataXRef')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Source', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='Source'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.MetaDataXRef is not None and 'MetaDataXRef' not in already_processed:
            already_processed.add('MetaDataXRef')
            showIndent(outfile, level)
            outfile.write('MetaDataXRef="%s",\n' % (self.MetaDataXRef,))
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('MetaDataXRef', node)
        if value is not None and 'MetaDataXRef' not in already_processed:
            already_processed.add('MetaDataXRef')
            self.MetaDataXRef = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        pass
# end class Source


class Sources(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Source=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Source is None:
            self.Source = []
        else:
            self.Source = Source
        self.Source_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Sources)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Sources.subclass:
            return Sources.subclass(*args_, **kwargs_)
        else:
            return Sources(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Source(self):
        return self.Source
    def set_Source(self, Source):
        self.Source = Source
    def add_Source(self, value):
        self.Source.append(value)
    def insert_Source_at(self, index, value):
        self.Source.insert(index, value)
    def replace_Source_at(self, index, value):
        self.Source[index] = value
    def _hasContent(self):
        if (
            self.Source
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Sources', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Sources')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Sources':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Sources')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Sources', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Sources'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Sources', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Source_ in self.Source:
            namespaceprefix_ = self.Source_nsprefix_ + ':' if (UseCapturedNS_ and self.Source_nsprefix_) else ''
            Source_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Source', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Sources'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Source=[\n')
        level += 1
        for Source_ in self.Source:
            showIndent(outfile, level)
            outfile.write('model_.Source(\n')
            Source_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'Source':
            obj_ = Source.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Source.append(obj_)
            obj_.original_tagname_ = 'Source'
# end class Sources


class Transformations(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Transformation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Transformation is None:
            self.Transformation = []
        else:
            self.Transformation = Transformation
        self.Transformation_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Transformations)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Transformations.subclass:
            return Transformations.subclass(*args_, **kwargs_)
        else:
            return Transformations(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Transformation(self):
        return self.Transformation
    def set_Transformation(self, Transformation):
        self.Transformation = Transformation
    def add_Transformation(self, value):
        self.Transformation.append(value)
    def insert_Transformation_at(self, index, value):
        self.Transformation.insert(index, value)
    def replace_Transformation_at(self, index, value):
        self.Transformation[index] = value
    def _hasContent(self):
        if (
            self.Transformation
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Transformations', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Transformations')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Transformations':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Transformations')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Transformations', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Transformations'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Transformations', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Transformation_ in self.Transformation:
            namespaceprefix_ = self.Transformation_nsprefix_ + ':' if (UseCapturedNS_ and self.Transformation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTransformation>%s</%sTransformation>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(Transformation_), input_name='Transformation')), namespaceprefix_ , eol_))
    def exportLiteral(self, outfile, level, name_='Transformations'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Transformation=[\n')
        level += 1
        for Transformation_ in self.Transformation:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(Transformation_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'Transformation':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Transformation')
            value_ = self.gds_validate_string(value_, node, 'Transformation')
            self.Transformation.append(value_)
            self.Transformation_nsprefix_ = child_.prefix
# end class Transformations


class Constants(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Constant=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Constant is None:
            self.Constant = []
        else:
            self.Constant = Constant
        self.Constant_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Constants)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Constants.subclass:
            return Constants.subclass(*args_, **kwargs_)
        else:
            return Constants(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Constant(self):
        return self.Constant
    def set_Constant(self, Constant):
        self.Constant = Constant
    def add_Constant(self, value):
        self.Constant.append(value)
    def insert_Constant_at(self, index, value):
        self.Constant.insert(index, value)
    def replace_Constant_at(self, index, value):
        self.Constant[index] = value
    def _hasContent(self):
        if (
            self.Constant
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Constants', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Constants')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Constants':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Constants')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Constants', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Constants'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Constants', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Constant_ in self.Constant:
            namespaceprefix_ = self.Constant_nsprefix_ + ':' if (UseCapturedNS_ and self.Constant_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sConstant>%s</%sConstant>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(Constant_), input_name='Constant')), namespaceprefix_ , eol_))
    def exportLiteral(self, outfile, level, name_='Constants'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Constant=[\n')
        level += 1
        for Constant_ in self.Constant:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(Constant_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'Constant':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Constant')
            value_ = self.gds_validate_string(value_, node, 'Constant')
            self.Constant.append(value_)
            self.Constant_nsprefix_ = child_.prefix
# end class Constants


class FieldMD(GeneratedsSuper):
    """FieldMD --
    Since FieldMD is an attribute structure, multiple valued attribues are allowable as elements.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, Handle=None, DTyp=None, Length=None, Default=None, MetaDataXRef=None, ProjectHandleXRef=None, Source=None, Sources=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        self.DTyp = _cast(None, DTyp)
        self.DTyp_nsprefix_ = None
        self.Length = _cast(int, Length)
        self.Length_nsprefix_ = None
        self.Default = _cast(None, Default)
        self.Default_nsprefix_ = None
        self.MetaDataXRef = _cast(None, MetaDataXRef)
        self.MetaDataXRef_nsprefix_ = None
        self.ProjectHandleXRef = _cast(None, ProjectHandleXRef)
        self.ProjectHandleXRef_nsprefix_ = None
        if Source is None:
            self.Source = []
        else:
            self.Source = Source
        self.Source_nsprefix_ = None
        self.Sources = Sources
        self.Sources_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, FieldMD)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if FieldMD.subclass:
            return FieldMD.subclass(*args_, **kwargs_)
        else:
            return FieldMD(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Source(self):
        return self.Source
    def set_Source(self, Source):
        self.Source = Source
    def add_Source(self, value):
        self.Source.append(value)
    def insert_Source_at(self, index, value):
        self.Source.insert(index, value)
    def replace_Source_at(self, index, value):
        self.Source[index] = value
    def get_Sources(self):
        return self.Sources
    def set_Sources(self, Sources):
        self.Sources = Sources
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def get_Handle(self):
        return self.Handle
    def set_Handle(self, Handle):
        self.Handle = Handle
    def get_DTyp(self):
        return self.DTyp
    def set_DTyp(self, DTyp):
        self.DTyp = DTyp
    def get_Length(self):
        return self.Length
    def set_Length(self, Length):
        self.Length = Length
    def get_Default(self):
        return self.Default
    def set_Default(self, Default):
        self.Default = Default
    def get_MetaDataXRef(self):
        return self.MetaDataXRef
    def set_MetaDataXRef(self, MetaDataXRef):
        self.MetaDataXRef = MetaDataXRef
    def get_ProjectHandleXRef(self):
        return self.ProjectHandleXRef
    def set_ProjectHandleXRef(self, ProjectHandleXRef):
        self.ProjectHandleXRef = ProjectHandleXRef
    def validate_DTypType(self, value):
        # Validate type DTypType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Unk', 'Dbl', 'Lng', 'Int', 'Dte', 'DTm', 'Str', 'VLS', 'Byt', 'Bln', 'Any']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on DTypType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (
            self.Source or
            self.Sources is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='FieldMD', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('FieldMD')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'FieldMD':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='FieldMD')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='FieldMD', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='FieldMD'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
        if self.DTyp is not None and 'DTyp' not in already_processed:
            already_processed.add('DTyp')
            outfile.write(' DTyp=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.DTyp), input_name='DTyp')), ))
        if self.Length is not None and 'Length' not in already_processed:
            already_processed.add('Length')
            outfile.write(' Length="%s"' % self.gds_format_integer(self.Length, input_name='Length'))
        if self.Default is not None and 'Default' not in already_processed:
            already_processed.add('Default')
            outfile.write(' Default=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Default), input_name='Default')), ))
        if self.MetaDataXRef is not None and 'MetaDataXRef' not in already_processed:
            already_processed.add('MetaDataXRef')
            outfile.write(' MetaDataXRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.MetaDataXRef), input_name='MetaDataXRef')), ))
        if self.ProjectHandleXRef is not None and 'ProjectHandleXRef' not in already_processed:
            already_processed.add('ProjectHandleXRef')
            outfile.write(' ProjectHandleXRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ProjectHandleXRef), input_name='ProjectHandleXRef')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='FieldMD', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Source_ in self.Source:
            namespaceprefix_ = self.Source_nsprefix_ + ':' if (UseCapturedNS_ and self.Source_nsprefix_) else ''
            Source_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Source', pretty_print=pretty_print)
        if self.Sources is not None:
            namespaceprefix_ = self.Sources_nsprefix_ + ':' if (UseCapturedNS_ and self.Sources_nsprefix_) else ''
            self.Sources.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Sources', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='FieldMD'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            showIndent(outfile, level)
            outfile.write('Handle="%s",\n' % (self.Handle,))
        if self.DTyp is not None and 'DTyp' not in already_processed:
            already_processed.add('DTyp')
            showIndent(outfile, level)
            outfile.write('DTyp="%s",\n' % (self.DTyp,))
        if self.Length is not None and 'Length' not in already_processed:
            already_processed.add('Length')
            showIndent(outfile, level)
            outfile.write('Length=%d,\n' % (self.Length,))
        if self.Default is not None and 'Default' not in already_processed:
            already_processed.add('Default')
            showIndent(outfile, level)
            outfile.write('Default="%s",\n' % (self.Default,))
        if self.MetaDataXRef is not None and 'MetaDataXRef' not in already_processed:
            already_processed.add('MetaDataXRef')
            showIndent(outfile, level)
            outfile.write('MetaDataXRef="%s",\n' % (self.MetaDataXRef,))
        if self.ProjectHandleXRef is not None and 'ProjectHandleXRef' not in already_processed:
            already_processed.add('ProjectHandleXRef')
            showIndent(outfile, level)
            outfile.write('ProjectHandleXRef="%s",\n' % (self.ProjectHandleXRef,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Source=[\n')
        level += 1
        for Source_ in self.Source:
            showIndent(outfile, level)
            outfile.write('model_.Source(\n')
            Source_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Sources is not None:
            showIndent(outfile, level)
            outfile.write('Sources=model_.Sources(\n')
            self.Sources.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
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
        value = find_attr_value_('DTyp', node)
        if value is not None and 'DTyp' not in already_processed:
            already_processed.add('DTyp')
            self.DTyp = value
            self.validate_DTypType(self.DTyp)    # validate type DTypType
        value = find_attr_value_('Length', node)
        if value is not None and 'Length' not in already_processed:
            already_processed.add('Length')
            self.Length = self.gds_parse_integer(value, node, 'Length')
        value = find_attr_value_('Default', node)
        if value is not None and 'Default' not in already_processed:
            already_processed.add('Default')
            self.Default = value
        value = find_attr_value_('MetaDataXRef', node)
        if value is not None and 'MetaDataXRef' not in already_processed:
            already_processed.add('MetaDataXRef')
            self.MetaDataXRef = value
        value = find_attr_value_('ProjectHandleXRef', node)
        if value is not None and 'ProjectHandleXRef' not in already_processed:
            already_processed.add('ProjectHandleXRef')
            self.ProjectHandleXRef = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Source':
            obj_ = Source.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Source.append(obj_)
            obj_.original_tagname_ = 'Source'
        elif nodeName_ == 'Sources':
            obj_ = Sources.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Sources = obj_
            obj_.original_tagname_ = 'Sources'
# end class FieldMD


class FieldExtMD(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, Handle=None, DTyp=None, Length=None, Default=None, MetaDataXRef=None, ProjectHandleXRef=None, Source=None, Sources=None, Constant=None, Constants=None, Transformation=None, Transformations=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        self.DTyp = _cast(None, DTyp)
        self.DTyp_nsprefix_ = None
        self.Length = _cast(int, Length)
        self.Length_nsprefix_ = None
        self.Default = _cast(None, Default)
        self.Default_nsprefix_ = None
        self.MetaDataXRef = _cast(None, MetaDataXRef)
        self.MetaDataXRef_nsprefix_ = None
        self.ProjectHandleXRef = _cast(None, ProjectHandleXRef)
        self.ProjectHandleXRef_nsprefix_ = None
        if Source is None:
            self.Source = []
        else:
            self.Source = Source
        self.Source_nsprefix_ = None
        self.Sources = Sources
        self.Sources_nsprefix_ = None
        if Constant is None:
            self.Constant = []
        else:
            self.Constant = Constant
        self.Constant_nsprefix_ = None
        self.Constants = Constants
        self.Constants_nsprefix_ = None
        if Transformation is None:
            self.Transformation = []
        else:
            self.Transformation = Transformation
        self.Transformation_nsprefix_ = None
        self.Transformations = Transformations
        self.Transformations_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, FieldExtMD)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if FieldExtMD.subclass:
            return FieldExtMD.subclass(*args_, **kwargs_)
        else:
            return FieldExtMD(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Source(self):
        return self.Source
    def set_Source(self, Source):
        self.Source = Source
    def add_Source(self, value):
        self.Source.append(value)
    def insert_Source_at(self, index, value):
        self.Source.insert(index, value)
    def replace_Source_at(self, index, value):
        self.Source[index] = value
    def get_Sources(self):
        return self.Sources
    def set_Sources(self, Sources):
        self.Sources = Sources
    def get_Constant(self):
        return self.Constant
    def set_Constant(self, Constant):
        self.Constant = Constant
    def add_Constant(self, value):
        self.Constant.append(value)
    def insert_Constant_at(self, index, value):
        self.Constant.insert(index, value)
    def replace_Constant_at(self, index, value):
        self.Constant[index] = value
    def get_Constants(self):
        return self.Constants
    def set_Constants(self, Constants):
        self.Constants = Constants
    def get_Transformation(self):
        return self.Transformation
    def set_Transformation(self, Transformation):
        self.Transformation = Transformation
    def add_Transformation(self, value):
        self.Transformation.append(value)
    def insert_Transformation_at(self, index, value):
        self.Transformation.insert(index, value)
    def replace_Transformation_at(self, index, value):
        self.Transformation[index] = value
    def get_Transformations(self):
        return self.Transformations
    def set_Transformations(self, Transformations):
        self.Transformations = Transformations
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def get_Handle(self):
        return self.Handle
    def set_Handle(self, Handle):
        self.Handle = Handle
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def get_Handle(self):
        return self.Handle
    def set_Handle(self, Handle):
        self.Handle = Handle
    def get_DTyp(self):
        return self.DTyp
    def set_DTyp(self, DTyp):
        self.DTyp = DTyp
    def get_Length(self):
        return self.Length
    def set_Length(self, Length):
        self.Length = Length
    def get_Default(self):
        return self.Default
    def set_Default(self, Default):
        self.Default = Default
    def get_MetaDataXRef(self):
        return self.MetaDataXRef
    def set_MetaDataXRef(self, MetaDataXRef):
        self.MetaDataXRef = MetaDataXRef
    def get_ProjectHandleXRef(self):
        return self.ProjectHandleXRef
    def set_ProjectHandleXRef(self, ProjectHandleXRef):
        self.ProjectHandleXRef = ProjectHandleXRef
    def validate_DTypType(self, value):
        # Validate type DTypType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Unk', 'Dbl', 'Lng', 'Int', 'Dte', 'DTm', 'Str', 'VLS', 'Byt', 'Bln', 'Any']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on DTypType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (
            self.Source or
            self.Sources is not None or
            self.Constant or
            self.Constants is not None or
            self.Transformation or
            self.Transformations is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='FieldExtMD', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('FieldExtMD')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'FieldExtMD':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='FieldExtMD')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='FieldExtMD', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='FieldExtMD'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
        if self.DTyp is not None and 'DTyp' not in already_processed:
            already_processed.add('DTyp')
            outfile.write(' DTyp=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.DTyp), input_name='DTyp')), ))
        if self.Length is not None and 'Length' not in already_processed:
            already_processed.add('Length')
            outfile.write(' Length="%s"' % self.gds_format_integer(self.Length, input_name='Length'))
        if self.Default is not None and 'Default' not in already_processed:
            already_processed.add('Default')
            outfile.write(' Default=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Default), input_name='Default')), ))
        if self.MetaDataXRef is not None and 'MetaDataXRef' not in already_processed:
            already_processed.add('MetaDataXRef')
            outfile.write(' MetaDataXRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.MetaDataXRef), input_name='MetaDataXRef')), ))
        if self.ProjectHandleXRef is not None and 'ProjectHandleXRef' not in already_processed:
            already_processed.add('ProjectHandleXRef')
            outfile.write(' ProjectHandleXRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ProjectHandleXRef), input_name='ProjectHandleXRef')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='FieldExtMD', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Source_ in self.Source:
            namespaceprefix_ = self.Source_nsprefix_ + ':' if (UseCapturedNS_ and self.Source_nsprefix_) else ''
            Source_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Source', pretty_print=pretty_print)
        if self.Sources is not None:
            namespaceprefix_ = self.Sources_nsprefix_ + ':' if (UseCapturedNS_ and self.Sources_nsprefix_) else ''
            self.Sources.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Sources', pretty_print=pretty_print)
        for Constant_ in self.Constant:
            namespaceprefix_ = self.Constant_nsprefix_ + ':' if (UseCapturedNS_ and self.Constant_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sConstant>%s</%sConstant>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(Constant_), input_name='Constant')), namespaceprefix_ , eol_))
        if self.Constants is not None:
            namespaceprefix_ = self.Constants_nsprefix_ + ':' if (UseCapturedNS_ and self.Constants_nsprefix_) else ''
            self.Constants.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Constants', pretty_print=pretty_print)
        for Transformation_ in self.Transformation:
            namespaceprefix_ = self.Transformation_nsprefix_ + ':' if (UseCapturedNS_ and self.Transformation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTransformation>%s</%sTransformation>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(Transformation_), input_name='Transformation')), namespaceprefix_ , eol_))
        if self.Transformations is not None:
            namespaceprefix_ = self.Transformations_nsprefix_ + ':' if (UseCapturedNS_ and self.Transformations_nsprefix_) else ''
            self.Transformations.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Transformations', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='FieldExtMD'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            showIndent(outfile, level)
            outfile.write('Handle="%s",\n' % (self.Handle,))
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            showIndent(outfile, level)
            outfile.write('Handle="%s",\n' % (self.Handle,))
        if self.DTyp is not None and 'DTyp' not in already_processed:
            already_processed.add('DTyp')
            showIndent(outfile, level)
            outfile.write('DTyp="%s",\n' % (self.DTyp,))
        if self.Length is not None and 'Length' not in already_processed:
            already_processed.add('Length')
            showIndent(outfile, level)
            outfile.write('Length=%d,\n' % (self.Length,))
        if self.Default is not None and 'Default' not in already_processed:
            already_processed.add('Default')
            showIndent(outfile, level)
            outfile.write('Default="%s",\n' % (self.Default,))
        if self.MetaDataXRef is not None and 'MetaDataXRef' not in already_processed:
            already_processed.add('MetaDataXRef')
            showIndent(outfile, level)
            outfile.write('MetaDataXRef="%s",\n' % (self.MetaDataXRef,))
        if self.ProjectHandleXRef is not None and 'ProjectHandleXRef' not in already_processed:
            already_processed.add('ProjectHandleXRef')
            showIndent(outfile, level)
            outfile.write('ProjectHandleXRef="%s",\n' % (self.ProjectHandleXRef,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Source=[\n')
        level += 1
        for Source_ in self.Source:
            showIndent(outfile, level)
            outfile.write('model_.Source(\n')
            Source_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Sources is not None:
            showIndent(outfile, level)
            outfile.write('Sources=model_.Sources(\n')
            self.Sources.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Constant=[\n')
        level += 1
        for Constant_ in self.Constant:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(Constant_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Constants is not None:
            showIndent(outfile, level)
            outfile.write('Constants=model_.Constants(\n')
            self.Constants.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Transformation=[\n')
        level += 1
        for Transformation_ in self.Transformation:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(Transformation_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Transformations is not None:
            showIndent(outfile, level)
            outfile.write('Transformations=model_.Transformations(\n')
            self.Transformations.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
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
        value = find_attr_value_('Name', node)
        if value is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            self.Name = value
        value = find_attr_value_('Handle', node)
        if value is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            self.Handle = value
        value = find_attr_value_('DTyp', node)
        if value is not None and 'DTyp' not in already_processed:
            already_processed.add('DTyp')
            self.DTyp = value
            self.validate_DTypType(self.DTyp)    # validate type DTypType
        value = find_attr_value_('Length', node)
        if value is not None and 'Length' not in already_processed:
            already_processed.add('Length')
            self.Length = self.gds_parse_integer(value, node, 'Length')
        value = find_attr_value_('Default', node)
        if value is not None and 'Default' not in already_processed:
            already_processed.add('Default')
            self.Default = value
        value = find_attr_value_('MetaDataXRef', node)
        if value is not None and 'MetaDataXRef' not in already_processed:
            already_processed.add('MetaDataXRef')
            self.MetaDataXRef = value
        value = find_attr_value_('ProjectHandleXRef', node)
        if value is not None and 'ProjectHandleXRef' not in already_processed:
            already_processed.add('ProjectHandleXRef')
            self.ProjectHandleXRef = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Source':
            obj_ = Source.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Source.append(obj_)
            obj_.original_tagname_ = 'Source'
        elif nodeName_ == 'Sources':
            obj_ = Sources.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Sources = obj_
            obj_.original_tagname_ = 'Sources'
        elif nodeName_ == 'Constant':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Constant')
            value_ = self.gds_validate_string(value_, node, 'Constant')
            self.Constant.append(value_)
            self.Constant_nsprefix_ = child_.prefix
        elif nodeName_ == 'Constants':
            obj_ = Constants.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Constants = obj_
            obj_.original_tagname_ = 'Constants'
        elif nodeName_ == 'Transformation':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Transformation')
            value_ = self.gds_validate_string(value_, node, 'Transformation')
            self.Transformation.append(value_)
            self.Transformation_nsprefix_ = child_.prefix
        elif nodeName_ == 'Transformations':
            obj_ = Transformations.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transformations = obj_
            obj_.original_tagname_ = 'Transformations'
# end class FieldExtMD


class Dictionary(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, FieldMD=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if FieldMD is None:
            self.FieldMD = []
        else:
            self.FieldMD = FieldMD
        self.FieldMD_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Dictionary)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Dictionary.subclass:
            return Dictionary.subclass(*args_, **kwargs_)
        else:
            return Dictionary(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_FieldMD(self):
        return self.FieldMD
    def set_FieldMD(self, FieldMD):
        self.FieldMD = FieldMD
    def add_FieldMD(self, value):
        self.FieldMD.append(value)
    def insert_FieldMD_at(self, index, value):
        self.FieldMD.insert(index, value)
    def replace_FieldMD_at(self, index, value):
        self.FieldMD[index] = value
    def _hasContent(self):
        if (
            self.FieldMD
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Dictionary', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Dictionary')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Dictionary':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Dictionary')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Dictionary', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Dictionary'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Dictionary', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for FieldMD_ in self.FieldMD:
            namespaceprefix_ = self.FieldMD_nsprefix_ + ':' if (UseCapturedNS_ and self.FieldMD_nsprefix_) else ''
            FieldMD_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='FieldMD', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Dictionary'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('FieldMD=[\n')
        level += 1
        for FieldMD_ in self.FieldMD:
            showIndent(outfile, level)
            outfile.write('model_.FieldMD(\n')
            FieldMD_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'FieldMD':
            obj_ = FieldMD.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.FieldMD.append(obj_)
            obj_.original_tagname_ = 'FieldMD'
# end class Dictionary


class Signature(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, Use=None, Column=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Use = _cast(None, Use)
        self.Use_nsprefix_ = None
        if Column is None:
            self.Column = []
        else:
            self.Column = Column
        self.Column_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Signature)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Signature.subclass:
            return Signature.subclass(*args_, **kwargs_)
        else:
            return Signature(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Column(self):
        return self.Column
    def set_Column(self, Column):
        self.Column = Column
    def add_Column(self, value):
        self.Column.append(value)
    def insert_Column_at(self, index, value):
        self.Column.insert(index, value)
    def replace_Column_at(self, index, value):
        self.Column[index] = value
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def get_Use(self):
        return self.Use
    def set_Use(self, Use):
        self.Use = Use
    def _hasContent(self):
        if (
            self.Column
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Signature', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Signature')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Signature':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Signature')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Signature', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Signature'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Use is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            outfile.write(' Use=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Use), input_name='Use')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Signature', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Column_ in self.Column:
            namespaceprefix_ = self.Column_nsprefix_ + ':' if (UseCapturedNS_ and self.Column_nsprefix_) else ''
            Column_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Column', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Signature'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
        if self.Use is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            showIndent(outfile, level)
            outfile.write('Use="%s",\n' % (self.Use,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Column=[\n')
        level += 1
        for Column_ in self.Column:
            showIndent(outfile, level)
            outfile.write('model_.Column(\n')
            Column_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        value = find_attr_value_('Use', node)
        if value is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            self.Use = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Column':
            obj_ = Column.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Column.append(obj_)
            obj_.original_tagname_ = 'Column'
# end class Signature


class Signatures(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Signature is None:
            self.Signature = []
        else:
            self.Signature = Signature
        self.Signature_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Signatures)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Signatures.subclass:
            return Signatures.subclass(*args_, **kwargs_)
        else:
            return Signatures(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Signature(self):
        return self.Signature
    def set_Signature(self, Signature):
        self.Signature = Signature
    def add_Signature(self, value):
        self.Signature.append(value)
    def insert_Signature_at(self, index, value):
        self.Signature.insert(index, value)
    def replace_Signature_at(self, index, value):
        self.Signature[index] = value
    def _hasContent(self):
        if (
            self.Signature
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Signatures', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Signatures')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Signatures':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Signatures')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Signatures', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Signatures'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Signatures', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Signature_ in self.Signature:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            Signature_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Signature', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Signatures'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Signature=[\n')
        level += 1
        for Signature_ in self.Signature:
            showIndent(outfile, level)
            outfile.write('model_.Signature(\n')
            Signature_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'Signature':
            obj_ = Signature.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Signature.append(obj_)
            obj_.original_tagname_ = 'Signature'
# end class Signatures


class Documentation(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Date=None, Version=None, Text=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Date = Date
        self.Date_nsprefix_ = None
        self.Version = Version
        self.Version_nsprefix_ = None
        self.Text = Text
        self.Text_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Documentation)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Documentation.subclass:
            return Documentation.subclass(*args_, **kwargs_)
        else:
            return Documentation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Date(self):
        return self.Date
    def set_Date(self, Date):
        self.Date = Date
    def get_Version(self):
        return self.Version
    def set_Version(self, Version):
        self.Version = Version
    def get_Text(self):
        return self.Text
    def set_Text(self, Text):
        self.Text = Text
    def _hasContent(self):
        if (
            self.Date is not None or
            self.Version is not None or
            self.Text is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Documentation', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Documentation')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Documentation':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Documentation')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Documentation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Documentation'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Documentation', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Date is not None:
            namespaceprefix_ = self.Date_nsprefix_ + ':' if (UseCapturedNS_ and self.Date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDate>%s</%sDate>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Date), input_name='Date')), namespaceprefix_ , eol_))
        if self.Version is not None:
            namespaceprefix_ = self.Version_nsprefix_ + ':' if (UseCapturedNS_ and self.Version_nsprefix_) else ''
            self.Version.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Version', pretty_print=pretty_print)
        if self.Text is not None:
            namespaceprefix_ = self.Text_nsprefix_ + ':' if (UseCapturedNS_ and self.Text_nsprefix_) else ''
            self.Text.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Text', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Documentation'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.Date is not None:
            showIndent(outfile, level)
            outfile.write('Date=%s,\n' % self.gds_encode(quote_python(self.Date)))
        if self.Version is not None:
            showIndent(outfile, level)
            outfile.write('Version=model_.VersionType(\n')
            self.Version.exportLiteral(outfile, level, name_='Version')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Text is not None:
            showIndent(outfile, level)
            outfile.write('Text=model_.TextType(\n')
            self.Text.exportLiteral(outfile, level, name_='Text')
            showIndent(outfile, level)
            outfile.write('),\n')
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
        if nodeName_ == 'Date':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Date')
            value_ = self.gds_validate_string(value_, node, 'Date')
            self.Date = value_
            self.Date_nsprefix_ = child_.prefix
        elif nodeName_ == 'Version':
            obj_ = VersionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Version = obj_
            obj_.original_tagname_ = 'Version'
        elif nodeName_ == 'Text':
            obj_ = TextType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Text = obj_
            obj_.original_tagname_ = 'Text'
# end class Documentation


class Projects(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, Handle=None, Project=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        if Project is None:
            self.Project = []
        else:
            self.Project = Project
        self.Project_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Projects)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Projects.subclass:
            return Projects.subclass(*args_, **kwargs_)
        else:
            return Projects(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Project(self):
        return self.Project
    def set_Project(self, Project):
        self.Project = Project
    def add_Project(self, value):
        self.Project.append(value)
    def insert_Project_at(self, index, value):
        self.Project.insert(index, value)
    def replace_Project_at(self, index, value):
        self.Project[index] = value
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
            self.Project
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Projects', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Projects')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Projects':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Projects')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Projects', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Projects'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Projects', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Project_ in self.Project:
            namespaceprefix_ = self.Project_nsprefix_ + ':' if (UseCapturedNS_ and self.Project_nsprefix_) else ''
            Project_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Project', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Projects'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            showIndent(outfile, level)
            outfile.write('Handle="%s",\n' % (self.Handle,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Project=[\n')
        level += 1
        for Project_ in self.Project:
            showIndent(outfile, level)
            outfile.write('model_.Project(\n')
            Project_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'Project':
            obj_ = Project.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Project.append(obj_)
            obj_.original_tagname_ = 'Project'
# end class Projects


class Project(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, Handle=None, Documentation=None, Dictionary=None, Models=None, Model=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        if Documentation is None:
            self.Documentation = []
        else:
            self.Documentation = Documentation
        self.Documentation_nsprefix_ = None
        if Dictionary is None:
            self.Dictionary = []
        else:
            self.Dictionary = Dictionary
        self.Dictionary_nsprefix_ = None
        self.Models = Models
        self.Models_nsprefix_ = None
        if Model is None:
            self.Model = []
        else:
            self.Model = Model
        self.Model_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Project)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Project.subclass:
            return Project.subclass(*args_, **kwargs_)
        else:
            return Project(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Documentation(self):
        return self.Documentation
    def set_Documentation(self, Documentation):
        self.Documentation = Documentation
    def add_Documentation(self, value):
        self.Documentation.append(value)
    def insert_Documentation_at(self, index, value):
        self.Documentation.insert(index, value)
    def replace_Documentation_at(self, index, value):
        self.Documentation[index] = value
    def get_Dictionary(self):
        return self.Dictionary
    def set_Dictionary(self, Dictionary):
        self.Dictionary = Dictionary
    def add_Dictionary(self, value):
        self.Dictionary.append(value)
    def insert_Dictionary_at(self, index, value):
        self.Dictionary.insert(index, value)
    def replace_Dictionary_at(self, index, value):
        self.Dictionary[index] = value
    def get_Models(self):
        return self.Models
    def set_Models(self, Models):
        self.Models = Models
    def get_Model(self):
        return self.Model
    def set_Model(self, Model):
        self.Model = Model
    def add_Model(self, value):
        self.Model.append(value)
    def insert_Model_at(self, index, value):
        self.Model.insert(index, value)
    def replace_Model_at(self, index, value):
        self.Model[index] = value
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
            self.Documentation or
            self.Dictionary or
            self.Models is not None or
            self.Model
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Project', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Project')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Project':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Project')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Project', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Project'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Project', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Documentation_ in self.Documentation:
            namespaceprefix_ = self.Documentation_nsprefix_ + ':' if (UseCapturedNS_ and self.Documentation_nsprefix_) else ''
            Documentation_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Documentation', pretty_print=pretty_print)
        for Dictionary_ in self.Dictionary:
            namespaceprefix_ = self.Dictionary_nsprefix_ + ':' if (UseCapturedNS_ and self.Dictionary_nsprefix_) else ''
            Dictionary_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Dictionary', pretty_print=pretty_print)
        if self.Models is not None:
            namespaceprefix_ = self.Models_nsprefix_ + ':' if (UseCapturedNS_ and self.Models_nsprefix_) else ''
            self.Models.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Models', pretty_print=pretty_print)
        for Model_ in self.Model:
            namespaceprefix_ = self.Model_nsprefix_ + ':' if (UseCapturedNS_ and self.Model_nsprefix_) else ''
            Model_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Model', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Project'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            showIndent(outfile, level)
            outfile.write('Handle="%s",\n' % (self.Handle,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Documentation=[\n')
        level += 1
        for Documentation_ in self.Documentation:
            showIndent(outfile, level)
            outfile.write('model_.Documentation(\n')
            Documentation_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('Dictionary=[\n')
        level += 1
        for Dictionary_ in self.Dictionary:
            showIndent(outfile, level)
            outfile.write('model_.Dictionary(\n')
            Dictionary_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Models is not None:
            showIndent(outfile, level)
            outfile.write('Models=model_.Models(\n')
            self.Models.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Model=[\n')
        level += 1
        for Model_ in self.Model:
            showIndent(outfile, level)
            outfile.write('model_.Model(\n')
            Model_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'Documentation':
            obj_ = Documentation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Documentation.append(obj_)
            obj_.original_tagname_ = 'Documentation'
        elif nodeName_ == 'Dictionary':
            obj_ = Dictionary.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Dictionary.append(obj_)
            obj_.original_tagname_ = 'Dictionary'
        elif nodeName_ == 'Models':
            obj_ = Models.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Models = obj_
            obj_.original_tagname_ = 'Models'
        elif nodeName_ == 'Model':
            obj_ = Model.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Model.append(obj_)
            obj_.original_tagname_ = 'Model'
# end class Project


class Response(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Position = _cast(None, Position)
        self.Position_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Response)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Response.subclass:
            return Response.subclass(*args_, **kwargs_)
        else:
            return Response(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Response', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Response')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Response':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Response')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Response', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Response'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Position), input_name='Position')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Response', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='Response'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            showIndent(outfile, level)
            outfile.write('Position="%s",\n' % (self.Position,))
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Position', node)
        if value is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            self.Position = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Response


class Responses(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Response=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Response is None:
            self.Response = []
        else:
            self.Response = Response
        self.Response_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Responses)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Responses.subclass:
            return Responses.subclass(*args_, **kwargs_)
        else:
            return Responses(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Response(self):
        return self.Response
    def set_Response(self, Response):
        self.Response = Response
    def add_Response(self, value):
        self.Response.append(value)
    def insert_Response_at(self, index, value):
        self.Response.insert(index, value)
    def replace_Response_at(self, index, value):
        self.Response[index] = value
    def _hasContent(self):
        if (
            self.Response
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Responses', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Responses')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Responses':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Responses')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Responses', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Responses'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Responses', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Response_ in self.Response:
            namespaceprefix_ = self.Response_nsprefix_ + ':' if (UseCapturedNS_ and self.Response_nsprefix_) else ''
            Response_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Response', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Responses'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Response=[\n')
        level += 1
        for Response_ in self.Response:
            showIndent(outfile, level)
            outfile.write('model_.Response(\n')
            Response_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'Response':
            obj_ = Response.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Response.append(obj_)
            obj_.original_tagname_ = 'Response'
# end class Responses


class ModelDirectives(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Annotation=None, Type=None, Response=None, Responses=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Annotation is None:
            self.Annotation = []
        else:
            self.Annotation = Annotation
        self.Annotation_nsprefix_ = None
        self.Type = Type
        self.Type_nsprefix_ = None
        if Response is None:
            self.Response = []
        else:
            self.Response = Response
        self.Response_nsprefix_ = None
        self.Responses = Responses
        self.Responses_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ModelDirectives)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ModelDirectives.subclass:
            return ModelDirectives.subclass(*args_, **kwargs_)
        else:
            return ModelDirectives(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Annotation(self):
        return self.Annotation
    def set_Annotation(self, Annotation):
        self.Annotation = Annotation
    def add_Annotation(self, value):
        self.Annotation.append(value)
    def insert_Annotation_at(self, index, value):
        self.Annotation.insert(index, value)
    def replace_Annotation_at(self, index, value):
        self.Annotation[index] = value
    def get_Type(self):
        return self.Type
    def set_Type(self, Type):
        self.Type = Type
    def get_Response(self):
        return self.Response
    def set_Response(self, Response):
        self.Response = Response
    def add_Response(self, value):
        self.Response.append(value)
    def insert_Response_at(self, index, value):
        self.Response.insert(index, value)
    def replace_Response_at(self, index, value):
        self.Response[index] = value
    def get_Responses(self):
        return self.Responses
    def set_Responses(self, Responses):
        self.Responses = Responses
    def _hasContent(self):
        if (
            self.Annotation or
            self.Type is not None or
            self.Response or
            self.Responses is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ModelDirectives', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ModelDirectives')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ModelDirectives':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ModelDirectives')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ModelDirectives', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ModelDirectives'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ModelDirectives', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Annotation_ in self.Annotation:
            namespaceprefix_ = self.Annotation_nsprefix_ + ':' if (UseCapturedNS_ and self.Annotation_nsprefix_) else ''
            Annotation_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Annotation', pretty_print=pretty_print)
        if self.Type is not None:
            namespaceprefix_ = self.Type_nsprefix_ + ':' if (UseCapturedNS_ and self.Type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sType>%s</%sType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Type), input_name='Type')), namespaceprefix_ , eol_))
        for Response_ in self.Response:
            namespaceprefix_ = self.Response_nsprefix_ + ':' if (UseCapturedNS_ and self.Response_nsprefix_) else ''
            Response_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Response', pretty_print=pretty_print)
        if self.Responses is not None:
            namespaceprefix_ = self.Responses_nsprefix_ + ':' if (UseCapturedNS_ and self.Responses_nsprefix_) else ''
            self.Responses.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Responses', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ModelDirectives'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Annotation=[\n')
        level += 1
        for Annotation_ in self.Annotation:
            showIndent(outfile, level)
            outfile.write('model_.Annotation(\n')
            Annotation_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Type is not None:
            showIndent(outfile, level)
            outfile.write('Type=%s,\n' % self.gds_encode(quote_python(self.Type)))
        showIndent(outfile, level)
        outfile.write('Response=[\n')
        level += 1
        for Response_ in self.Response:
            showIndent(outfile, level)
            outfile.write('model_.Response(\n')
            Response_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Responses is not None:
            showIndent(outfile, level)
            outfile.write('Responses=model_.Responses(\n')
            self.Responses.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
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
        if nodeName_ == 'Annotation':
            obj_ = Annotation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Annotation.append(obj_)
            obj_.original_tagname_ = 'Annotation'
        elif nodeName_ == 'Type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Type')
            value_ = self.gds_validate_string(value_, node, 'Type')
            self.Type = value_
            self.Type_nsprefix_ = child_.prefix
        elif nodeName_ == 'Response':
            obj_ = Response.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Response.append(obj_)
            obj_.original_tagname_ = 'Response'
        elif nodeName_ == 'Responses':
            obj_ = Responses.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Responses = obj_
            obj_.original_tagname_ = 'Responses'
# end class ModelDirectives


class Models(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, Handle=None, Annotation=None, Model=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        if Annotation is None:
            self.Annotation = []
        else:
            self.Annotation = Annotation
        self.Annotation_nsprefix_ = None
        if Model is None:
            self.Model = []
        else:
            self.Model = Model
        self.Model_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Models)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Models.subclass:
            return Models.subclass(*args_, **kwargs_)
        else:
            return Models(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Annotation(self):
        return self.Annotation
    def set_Annotation(self, Annotation):
        self.Annotation = Annotation
    def add_Annotation(self, value):
        self.Annotation.append(value)
    def insert_Annotation_at(self, index, value):
        self.Annotation.insert(index, value)
    def replace_Annotation_at(self, index, value):
        self.Annotation[index] = value
    def get_Model(self):
        return self.Model
    def set_Model(self, Model):
        self.Model = Model
    def add_Model(self, value):
        self.Model.append(value)
    def insert_Model_at(self, index, value):
        self.Model.insert(index, value)
    def replace_Model_at(self, index, value):
        self.Model[index] = value
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
            self.Annotation or
            self.Model
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Models', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Models')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Models':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Models')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Models', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Models'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Models', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Annotation_ in self.Annotation:
            namespaceprefix_ = self.Annotation_nsprefix_ + ':' if (UseCapturedNS_ and self.Annotation_nsprefix_) else ''
            Annotation_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Annotation', pretty_print=pretty_print)
        for Model_ in self.Model:
            namespaceprefix_ = self.Model_nsprefix_ + ':' if (UseCapturedNS_ and self.Model_nsprefix_) else ''
            Model_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Model', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Models'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            showIndent(outfile, level)
            outfile.write('Handle="%s",\n' % (self.Handle,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Annotation=[\n')
        level += 1
        for Annotation_ in self.Annotation:
            showIndent(outfile, level)
            outfile.write('model_.Annotation(\n')
            Annotation_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('Model=[\n')
        level += 1
        for Model_ in self.Model:
            showIndent(outfile, level)
            outfile.write('model_.Model(\n')
            Model_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'Annotation':
            obj_ = Annotation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Annotation.append(obj_)
            obj_.original_tagname_ = 'Annotation'
        elif nodeName_ == 'Model':
            obj_ = Model.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Model.append(obj_)
            obj_.original_tagname_ = 'Model'
# end class Models


class Model(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Use=None, Name=None, Handle=None, Annotation=None, Signatures=None, Dictionary=None, ModelDirectives=None, ComponentModels=None, ComponentModel=None, Variables=None, Variable=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Use = _cast(None, Use)
        self.Use_nsprefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        if Annotation is None:
            self.Annotation = []
        else:
            self.Annotation = Annotation
        self.Annotation_nsprefix_ = None
        self.Signatures = Signatures
        self.Signatures_nsprefix_ = None
        self.Dictionary = Dictionary
        self.Dictionary_nsprefix_ = None
        self.ModelDirectives = ModelDirectives
        self.ModelDirectives_nsprefix_ = None
        self.ComponentModels = ComponentModels
        self.ComponentModels_nsprefix_ = None
        if ComponentModel is None:
            self.ComponentModel = []
        else:
            self.ComponentModel = ComponentModel
        self.ComponentModel_nsprefix_ = None
        self.Variables = Variables
        self.Variables_nsprefix_ = None
        if Variable is None:
            self.Variable = []
        else:
            self.Variable = Variable
        self.Variable_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Model)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Model.subclass:
            return Model.subclass(*args_, **kwargs_)
        else:
            return Model(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Annotation(self):
        return self.Annotation
    def set_Annotation(self, Annotation):
        self.Annotation = Annotation
    def add_Annotation(self, value):
        self.Annotation.append(value)
    def insert_Annotation_at(self, index, value):
        self.Annotation.insert(index, value)
    def replace_Annotation_at(self, index, value):
        self.Annotation[index] = value
    def get_Signatures(self):
        return self.Signatures
    def set_Signatures(self, Signatures):
        self.Signatures = Signatures
    def get_Dictionary(self):
        return self.Dictionary
    def set_Dictionary(self, Dictionary):
        self.Dictionary = Dictionary
    def get_ModelDirectives(self):
        return self.ModelDirectives
    def set_ModelDirectives(self, ModelDirectives):
        self.ModelDirectives = ModelDirectives
    def get_ComponentModels(self):
        return self.ComponentModels
    def set_ComponentModels(self, ComponentModels):
        self.ComponentModels = ComponentModels
    def get_ComponentModel(self):
        return self.ComponentModel
    def set_ComponentModel(self, ComponentModel):
        self.ComponentModel = ComponentModel
    def add_ComponentModel(self, value):
        self.ComponentModel.append(value)
    def insert_ComponentModel_at(self, index, value):
        self.ComponentModel.insert(index, value)
    def replace_ComponentModel_at(self, index, value):
        self.ComponentModel[index] = value
    def get_Variables(self):
        return self.Variables
    def set_Variables(self, Variables):
        self.Variables = Variables
    def get_Variable(self):
        return self.Variable
    def set_Variable(self, Variable):
        self.Variable = Variable
    def add_Variable(self, value):
        self.Variable.append(value)
    def insert_Variable_at(self, index, value):
        self.Variable.insert(index, value)
    def replace_Variable_at(self, index, value):
        self.Variable[index] = value
    def get_Use(self):
        return self.Use
    def set_Use(self, Use):
        self.Use = Use
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
            self.Annotation or
            self.Signatures is not None or
            self.Dictionary is not None or
            self.ModelDirectives is not None or
            self.ComponentModels is not None or
            self.ComponentModel or
            self.Variables is not None or
            self.Variable
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Model', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Model')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Model':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Model')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Model', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Model'):
        if self.Use is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            outfile.write(' Use=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Use), input_name='Use')), ))
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Model', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Annotation_ in self.Annotation:
            namespaceprefix_ = self.Annotation_nsprefix_ + ':' if (UseCapturedNS_ and self.Annotation_nsprefix_) else ''
            Annotation_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Annotation', pretty_print=pretty_print)
        if self.Signatures is not None:
            namespaceprefix_ = self.Signatures_nsprefix_ + ':' if (UseCapturedNS_ and self.Signatures_nsprefix_) else ''
            self.Signatures.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Signatures', pretty_print=pretty_print)
        if self.Dictionary is not None:
            namespaceprefix_ = self.Dictionary_nsprefix_ + ':' if (UseCapturedNS_ and self.Dictionary_nsprefix_) else ''
            self.Dictionary.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Dictionary', pretty_print=pretty_print)
        if self.ModelDirectives is not None:
            namespaceprefix_ = self.ModelDirectives_nsprefix_ + ':' if (UseCapturedNS_ and self.ModelDirectives_nsprefix_) else ''
            self.ModelDirectives.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ModelDirectives', pretty_print=pretty_print)
        if self.ComponentModels is not None:
            namespaceprefix_ = self.ComponentModels_nsprefix_ + ':' if (UseCapturedNS_ and self.ComponentModels_nsprefix_) else ''
            self.ComponentModels.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ComponentModels', pretty_print=pretty_print)
        for ComponentModel_ in self.ComponentModel:
            namespaceprefix_ = self.ComponentModel_nsprefix_ + ':' if (UseCapturedNS_ and self.ComponentModel_nsprefix_) else ''
            ComponentModel_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ComponentModel', pretty_print=pretty_print)
        if self.Variables is not None:
            namespaceprefix_ = self.Variables_nsprefix_ + ':' if (UseCapturedNS_ and self.Variables_nsprefix_) else ''
            self.Variables.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Variables', pretty_print=pretty_print)
        for Variable_ in self.Variable:
            namespaceprefix_ = self.Variable_nsprefix_ + ':' if (UseCapturedNS_ and self.Variable_nsprefix_) else ''
            Variable_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Variable', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Model'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Use is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            showIndent(outfile, level)
            outfile.write('Use="%s",\n' % (self.Use,))
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            showIndent(outfile, level)
            outfile.write('Handle="%s",\n' % (self.Handle,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Annotation=[\n')
        level += 1
        for Annotation_ in self.Annotation:
            showIndent(outfile, level)
            outfile.write('model_.Annotation(\n')
            Annotation_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Signatures is not None:
            showIndent(outfile, level)
            outfile.write('Signatures=model_.Signatures(\n')
            self.Signatures.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Dictionary is not None:
            showIndent(outfile, level)
            outfile.write('Dictionary=model_.Dictionary(\n')
            self.Dictionary.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ModelDirectives is not None:
            showIndent(outfile, level)
            outfile.write('ModelDirectives=model_.ModelDirectives(\n')
            self.ModelDirectives.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ComponentModels is not None:
            showIndent(outfile, level)
            outfile.write('ComponentModels=model_.ComponentModels(\n')
            self.ComponentModels.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('ComponentModel=[\n')
        level += 1
        for ComponentModel_ in self.ComponentModel:
            showIndent(outfile, level)
            outfile.write('model_.ComponentModel(\n')
            ComponentModel_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Variables is not None:
            showIndent(outfile, level)
            outfile.write('Variables=model_.Variables(\n')
            self.Variables.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Variable=[\n')
        level += 1
        for Variable_ in self.Variable:
            showIndent(outfile, level)
            outfile.write('model_.Variable(\n')
            Variable_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        value = find_attr_value_('Use', node)
        if value is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            self.Use = value
        value = find_attr_value_('Name', node)
        if value is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            self.Name = value
        value = find_attr_value_('Handle', node)
        if value is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            self.Handle = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Annotation':
            obj_ = Annotation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Annotation.append(obj_)
            obj_.original_tagname_ = 'Annotation'
        elif nodeName_ == 'Signatures':
            obj_ = Signatures.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Signatures = obj_
            obj_.original_tagname_ = 'Signatures'
        elif nodeName_ == 'Dictionary':
            obj_ = Dictionary.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Dictionary = obj_
            obj_.original_tagname_ = 'Dictionary'
        elif nodeName_ == 'ModelDirectives':
            obj_ = ModelDirectives.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ModelDirectives = obj_
            obj_.original_tagname_ = 'ModelDirectives'
        elif nodeName_ == 'ComponentModels':
            obj_ = ComponentModels.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ComponentModels = obj_
            obj_.original_tagname_ = 'ComponentModels'
        elif nodeName_ == 'ComponentModel':
            obj_ = ComponentModel.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ComponentModel.append(obj_)
            obj_.original_tagname_ = 'ComponentModel'
        elif nodeName_ == 'Variables':
            obj_ = Variables.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Variables = obj_
            obj_.original_tagname_ = 'Variables'
        elif nodeName_ == 'Variable':
            obj_ = Variable.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Variable.append(obj_)
            obj_.original_tagname_ = 'Variable'
# end class Model


class ComponentModels(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Annotation=None, ComponentModel=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Annotation is None:
            self.Annotation = []
        else:
            self.Annotation = Annotation
        self.Annotation_nsprefix_ = None
        if ComponentModel is None:
            self.ComponentModel = []
        else:
            self.ComponentModel = ComponentModel
        self.ComponentModel_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ComponentModels)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ComponentModels.subclass:
            return ComponentModels.subclass(*args_, **kwargs_)
        else:
            return ComponentModels(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Annotation(self):
        return self.Annotation
    def set_Annotation(self, Annotation):
        self.Annotation = Annotation
    def add_Annotation(self, value):
        self.Annotation.append(value)
    def insert_Annotation_at(self, index, value):
        self.Annotation.insert(index, value)
    def replace_Annotation_at(self, index, value):
        self.Annotation[index] = value
    def get_ComponentModel(self):
        return self.ComponentModel
    def set_ComponentModel(self, ComponentModel):
        self.ComponentModel = ComponentModel
    def add_ComponentModel(self, value):
        self.ComponentModel.append(value)
    def insert_ComponentModel_at(self, index, value):
        self.ComponentModel.insert(index, value)
    def replace_ComponentModel_at(self, index, value):
        self.ComponentModel[index] = value
    def _hasContent(self):
        if (
            self.Annotation or
            self.ComponentModel
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ComponentModels', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ComponentModels')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ComponentModels':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ComponentModels')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ComponentModels', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ComponentModels'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ComponentModels', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Annotation_ in self.Annotation:
            namespaceprefix_ = self.Annotation_nsprefix_ + ':' if (UseCapturedNS_ and self.Annotation_nsprefix_) else ''
            Annotation_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Annotation', pretty_print=pretty_print)
        for ComponentModel_ in self.ComponentModel:
            namespaceprefix_ = self.ComponentModel_nsprefix_ + ':' if (UseCapturedNS_ and self.ComponentModel_nsprefix_) else ''
            ComponentModel_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ComponentModel', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ComponentModels'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Annotation=[\n')
        level += 1
        for Annotation_ in self.Annotation:
            showIndent(outfile, level)
            outfile.write('model_.Annotation(\n')
            Annotation_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('ComponentModel=[\n')
        level += 1
        for ComponentModel_ in self.ComponentModel:
            showIndent(outfile, level)
            outfile.write('model_.ComponentModel(\n')
            ComponentModel_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'Annotation':
            obj_ = Annotation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Annotation.append(obj_)
            obj_.original_tagname_ = 'Annotation'
        elif nodeName_ == 'ComponentModel':
            obj_ = ComponentModel.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ComponentModel.append(obj_)
            obj_.original_tagname_ = 'ComponentModel'
# end class ComponentModels


class ComponentModel(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Use=None, Name=None, Handle=None, Annotation=None, Signatures=None, ModelDirectives=None, Variables=None, Variable=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Use = _cast(None, Use)
        self.Use_nsprefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        if Annotation is None:
            self.Annotation = []
        else:
            self.Annotation = Annotation
        self.Annotation_nsprefix_ = None
        self.Signatures = Signatures
        self.Signatures_nsprefix_ = None
        self.ModelDirectives = ModelDirectives
        self.ModelDirectives_nsprefix_ = None
        self.Variables = Variables
        self.Variables_nsprefix_ = None
        if Variable is None:
            self.Variable = []
        else:
            self.Variable = Variable
        self.Variable_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ComponentModel)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ComponentModel.subclass:
            return ComponentModel.subclass(*args_, **kwargs_)
        else:
            return ComponentModel(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Annotation(self):
        return self.Annotation
    def set_Annotation(self, Annotation):
        self.Annotation = Annotation
    def add_Annotation(self, value):
        self.Annotation.append(value)
    def insert_Annotation_at(self, index, value):
        self.Annotation.insert(index, value)
    def replace_Annotation_at(self, index, value):
        self.Annotation[index] = value
    def get_Signatures(self):
        return self.Signatures
    def set_Signatures(self, Signatures):
        self.Signatures = Signatures
    def get_ModelDirectives(self):
        return self.ModelDirectives
    def set_ModelDirectives(self, ModelDirectives):
        self.ModelDirectives = ModelDirectives
    def get_Variables(self):
        return self.Variables
    def set_Variables(self, Variables):
        self.Variables = Variables
    def get_Variable(self):
        return self.Variable
    def set_Variable(self, Variable):
        self.Variable = Variable
    def add_Variable(self, value):
        self.Variable.append(value)
    def insert_Variable_at(self, index, value):
        self.Variable.insert(index, value)
    def replace_Variable_at(self, index, value):
        self.Variable[index] = value
    def get_Use(self):
        return self.Use
    def set_Use(self, Use):
        self.Use = Use
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
            self.Annotation or
            self.Signatures is not None or
            self.ModelDirectives is not None or
            self.Variables is not None or
            self.Variable
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ComponentModel', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ComponentModel')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ComponentModel':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ComponentModel')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ComponentModel', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ComponentModel'):
        if self.Use is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            outfile.write(' Use=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Use), input_name='Use')), ))
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ComponentModel', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Annotation_ in self.Annotation:
            namespaceprefix_ = self.Annotation_nsprefix_ + ':' if (UseCapturedNS_ and self.Annotation_nsprefix_) else ''
            Annotation_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Annotation', pretty_print=pretty_print)
        if self.Signatures is not None:
            namespaceprefix_ = self.Signatures_nsprefix_ + ':' if (UseCapturedNS_ and self.Signatures_nsprefix_) else ''
            self.Signatures.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Signatures', pretty_print=pretty_print)
        if self.ModelDirectives is not None:
            namespaceprefix_ = self.ModelDirectives_nsprefix_ + ':' if (UseCapturedNS_ and self.ModelDirectives_nsprefix_) else ''
            self.ModelDirectives.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ModelDirectives', pretty_print=pretty_print)
        if self.Variables is not None:
            namespaceprefix_ = self.Variables_nsprefix_ + ':' if (UseCapturedNS_ and self.Variables_nsprefix_) else ''
            self.Variables.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Variables', pretty_print=pretty_print)
        for Variable_ in self.Variable:
            namespaceprefix_ = self.Variable_nsprefix_ + ':' if (UseCapturedNS_ and self.Variable_nsprefix_) else ''
            Variable_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Variable', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ComponentModel'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Use is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            showIndent(outfile, level)
            outfile.write('Use="%s",\n' % (self.Use,))
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            showIndent(outfile, level)
            outfile.write('Handle="%s",\n' % (self.Handle,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Annotation=[\n')
        level += 1
        for Annotation_ in self.Annotation:
            showIndent(outfile, level)
            outfile.write('model_.Annotation(\n')
            Annotation_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Signatures is not None:
            showIndent(outfile, level)
            outfile.write('Signatures=model_.Signatures(\n')
            self.Signatures.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ModelDirectives is not None:
            showIndent(outfile, level)
            outfile.write('ModelDirectives=model_.ModelDirectives(\n')
            self.ModelDirectives.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Variables is not None:
            showIndent(outfile, level)
            outfile.write('Variables=model_.Variables(\n')
            self.Variables.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Variable=[\n')
        level += 1
        for Variable_ in self.Variable:
            showIndent(outfile, level)
            outfile.write('model_.Variable(\n')
            Variable_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        value = find_attr_value_('Use', node)
        if value is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            self.Use = value
        value = find_attr_value_('Name', node)
        if value is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            self.Name = value
        value = find_attr_value_('Handle', node)
        if value is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            self.Handle = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Annotation':
            obj_ = Annotation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Annotation.append(obj_)
            obj_.original_tagname_ = 'Annotation'
        elif nodeName_ == 'Signatures':
            obj_ = Signatures.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Signatures = obj_
            obj_.original_tagname_ = 'Signatures'
        elif nodeName_ == 'ModelDirectives':
            obj_ = ModelDirectives.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ModelDirectives = obj_
            obj_.original_tagname_ = 'ModelDirectives'
        elif nodeName_ == 'Variables':
            obj_ = Variables.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Variables = obj_
            obj_.original_tagname_ = 'Variables'
        elif nodeName_ == 'Variable':
            obj_ = Variable.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Variable.append(obj_)
            obj_.original_tagname_ = 'Variable'
# end class ComponentModel


class Variables(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Annotation=None, Variable=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Annotation is None:
            self.Annotation = []
        else:
            self.Annotation = Annotation
        self.Annotation_nsprefix_ = None
        if Variable is None:
            self.Variable = []
        else:
            self.Variable = Variable
        self.Variable_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Variables)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Variables.subclass:
            return Variables.subclass(*args_, **kwargs_)
        else:
            return Variables(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Annotation(self):
        return self.Annotation
    def set_Annotation(self, Annotation):
        self.Annotation = Annotation
    def add_Annotation(self, value):
        self.Annotation.append(value)
    def insert_Annotation_at(self, index, value):
        self.Annotation.insert(index, value)
    def replace_Annotation_at(self, index, value):
        self.Annotation[index] = value
    def get_Variable(self):
        return self.Variable
    def set_Variable(self, Variable):
        self.Variable = Variable
    def add_Variable(self, value):
        self.Variable.append(value)
    def insert_Variable_at(self, index, value):
        self.Variable.insert(index, value)
    def replace_Variable_at(self, index, value):
        self.Variable[index] = value
    def _hasContent(self):
        if (
            self.Annotation or
            self.Variable
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Variables', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Variables')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Variables':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Variables')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Variables', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Variables'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Variables', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Annotation_ in self.Annotation:
            namespaceprefix_ = self.Annotation_nsprefix_ + ':' if (UseCapturedNS_ and self.Annotation_nsprefix_) else ''
            Annotation_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Annotation', pretty_print=pretty_print)
        for Variable_ in self.Variable:
            namespaceprefix_ = self.Variable_nsprefix_ + ':' if (UseCapturedNS_ and self.Variable_nsprefix_) else ''
            Variable_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Variable', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Variables'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Annotation=[\n')
        level += 1
        for Annotation_ in self.Annotation:
            showIndent(outfile, level)
            outfile.write('model_.Annotation(\n')
            Annotation_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('Variable=[\n')
        level += 1
        for Variable_ in self.Variable:
            showIndent(outfile, level)
            outfile.write('model_.Variable(\n')
            Variable_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'Annotation':
            obj_ = Annotation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Annotation.append(obj_)
            obj_.original_tagname_ = 'Annotation'
        elif nodeName_ == 'Variable':
            obj_ = Variable.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Variable.append(obj_)
            obj_.original_tagname_ = 'Variable'
# end class Variables


class v(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, i=None, j=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Position = _cast(int, Position)
        self.Position_nsprefix_ = None
        self.i = _cast(int, i)
        self.i_nsprefix_ = None
        self.j = _cast(int, j)
        self.j_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, v)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if v.subclass:
            return v.subclass(*args_, **kwargs_)
        else:
            return v(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def get_i(self):
        return self.i
    def set_i(self, i):
        self.i = i
    def get_j(self):
        return self.j
    def set_j(self, j):
        self.j = j
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_Dbl(self, value):
        result = True
        # Validate type Dbl, a restriction on None.
        pass
        return result
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='v', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('v')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'v':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='v')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='v', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='v'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position="%s"' % self.gds_format_integer(self.Position, input_name='Position'))
        if self.i is not None and 'i' not in already_processed:
            already_processed.add('i')
            outfile.write(' i="%s"' % self.gds_format_integer(self.i, input_name='i'))
        if self.j is not None and 'j' not in already_processed:
            already_processed.add('j')
            outfile.write(' j="%s"' % self.gds_format_integer(self.j, input_name='j'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='v', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='v'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            showIndent(outfile, level)
            outfile.write('Position=%d,\n' % (self.Position,))
        if self.i is not None and 'i' not in already_processed:
            already_processed.add('i')
            showIndent(outfile, level)
            outfile.write('i=%d,\n' % (self.i,))
        if self.j is not None and 'j' not in already_processed:
            already_processed.add('j')
            showIndent(outfile, level)
            outfile.write('j=%d,\n' % (self.j,))
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Position', node)
        if value is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            self.Position = self.gds_parse_integer(value, node, 'Position')
        value = find_attr_value_('i', node)
        if value is not None and 'i' not in already_processed:
            already_processed.add('i')
            self.i = self.gds_parse_integer(value, node, 'i')
        value = find_attr_value_('j', node)
        if value is not None and 'j' not in already_processed:
            already_processed.add('j')
            self.j = self.gds_parse_integer(value, node, 'j')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class v


class w(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, i=None, j=None, dlm=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Position = _cast(int, Position)
        self.Position_nsprefix_ = None
        self.i = _cast(int, i)
        self.i_nsprefix_ = None
        self.j = _cast(int, j)
        self.j_nsprefix_ = None
        self.dlm = _cast(None, dlm)
        self.dlm_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, w)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if w.subclass:
            return w.subclass(*args_, **kwargs_)
        else:
            return w(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def get_i(self):
        return self.i
    def set_i(self, i):
        self.i = i
    def get_j(self):
        return self.j
    def set_j(self, j):
        self.j = j
    def get_dlm(self):
        return self.dlm
    def set_dlm(self, dlm):
        self.dlm = dlm
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_Any(self, value):
        result = True
        # Validate type Any, a restriction on None.
        pass
        return result
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='w', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('w')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'w':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='w')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='w', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='w'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position="%s"' % self.gds_format_integer(self.Position, input_name='Position'))
        if self.i is not None and 'i' not in already_processed:
            already_processed.add('i')
            outfile.write(' i="%s"' % self.gds_format_integer(self.i, input_name='i'))
        if self.j is not None and 'j' not in already_processed:
            already_processed.add('j')
            outfile.write(' j="%s"' % self.gds_format_integer(self.j, input_name='j'))
        if self.dlm is not None and 'dlm' not in already_processed:
            already_processed.add('dlm')
            outfile.write(' dlm=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.dlm), input_name='dlm')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='w', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='w'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            showIndent(outfile, level)
            outfile.write('Position=%d,\n' % (self.Position,))
        if self.i is not None and 'i' not in already_processed:
            already_processed.add('i')
            showIndent(outfile, level)
            outfile.write('i=%d,\n' % (self.i,))
        if self.j is not None and 'j' not in already_processed:
            already_processed.add('j')
            showIndent(outfile, level)
            outfile.write('j=%d,\n' % (self.j,))
        if self.dlm is not None and 'dlm' not in already_processed:
            already_processed.add('dlm')
            showIndent(outfile, level)
            outfile.write('dlm="%s",\n' % (self.dlm,))
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Position', node)
        if value is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            self.Position = self.gds_parse_integer(value, node, 'Position')
        value = find_attr_value_('i', node)
        if value is not None and 'i' not in already_processed:
            already_processed.add('i')
            self.i = self.gds_parse_integer(value, node, 'i')
        value = find_attr_value_('j', node)
        if value is not None and 'j' not in already_processed:
            already_processed.add('j')
            self.j = self.gds_parse_integer(value, node, 'j')
        value = find_attr_value_('dlm', node)
        if value is not None and 'dlm' not in already_processed:
            already_processed.add('dlm')
            self.dlm = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class w


class RowDbl(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, length=None, v=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.length = _cast(int, length)
        self.length_nsprefix_ = None
        if v is None:
            self.v = []
        else:
            self.v = v
        self.v_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RowDbl)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RowDbl.subclass:
            return RowDbl.subclass(*args_, **kwargs_)
        else:
            return RowDbl(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_v(self):
        return self.v
    def set_v(self, v):
        self.v = v
    def add_v(self, value):
        self.v.append(value)
    def insert_v_at(self, index, value):
        self.v.insert(index, value)
    def replace_v_at(self, index, value):
        self.v[index] = value
    def get_length(self):
        return self.length
    def set_length(self, length):
        self.length = length
    def _hasContent(self):
        if (
            self.v
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='RowDbl', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RowDbl')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RowDbl':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RowDbl')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RowDbl', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RowDbl'):
        if self.length is not None and 'length' not in already_processed:
            already_processed.add('length')
            outfile.write(' length="%s"' % self.gds_format_integer(self.length, input_name='length'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='RowDbl', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for v_ in self.v:
            namespaceprefix_ = self.v_nsprefix_ + ':' if (UseCapturedNS_ and self.v_nsprefix_) else ''
            v_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='v', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='RowDbl'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.length is not None and 'length' not in already_processed:
            already_processed.add('length')
            showIndent(outfile, level)
            outfile.write('length=%d,\n' % (self.length,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('v=[\n')
        level += 1
        for v_ in self.v:
            showIndent(outfile, level)
            outfile.write('model_.v(\n')
            v_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        value = find_attr_value_('length', node)
        if value is not None and 'length' not in already_processed:
            already_processed.add('length')
            self.length = self.gds_parse_integer(value, node, 'length')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'v':
            obj_ = v.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.v.append(obj_)
            obj_.original_tagname_ = 'v'
# end class RowDbl


class RowStr(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, length=None, w=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.length = _cast(int, length)
        self.length_nsprefix_ = None
        if w is None:
            self.w = []
        else:
            self.w = w
        self.w_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RowStr)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RowStr.subclass:
            return RowStr.subclass(*args_, **kwargs_)
        else:
            return RowStr(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_w(self):
        return self.w
    def set_w(self, w):
        self.w = w
    def add_w(self, value):
        self.w.append(value)
    def insert_w_at(self, index, value):
        self.w.insert(index, value)
    def replace_w_at(self, index, value):
        self.w[index] = value
    def get_length(self):
        return self.length
    def set_length(self, length):
        self.length = length
    def _hasContent(self):
        if (
            self.w
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='RowStr', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RowStr')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RowStr':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RowStr')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RowStr', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RowStr'):
        if self.length is not None and 'length' not in already_processed:
            already_processed.add('length')
            outfile.write(' length="%s"' % self.gds_format_integer(self.length, input_name='length'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='RowStr', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for w_ in self.w:
            namespaceprefix_ = self.w_nsprefix_ + ':' if (UseCapturedNS_ and self.w_nsprefix_) else ''
            w_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='w', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='RowStr'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.length is not None and 'length' not in already_processed:
            already_processed.add('length')
            showIndent(outfile, level)
            outfile.write('length=%d,\n' % (self.length,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('w=[\n')
        level += 1
        for w_ in self.w:
            showIndent(outfile, level)
            outfile.write('model_.w(\n')
            w_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        value = find_attr_value_('length', node)
        if value is not None and 'length' not in already_processed:
            already_processed.add('length')
            self.length = self.gds_parse_integer(value, node, 'length')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'w':
            obj_ = w.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.w.append(obj_)
            obj_.original_tagname_ = 'w'
# end class RowStr


class ColumnDbl(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, length=None, v=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.length = _cast(int, length)
        self.length_nsprefix_ = None
        if v is None:
            self.v = []
        else:
            self.v = v
        self.v_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ColumnDbl)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ColumnDbl.subclass:
            return ColumnDbl.subclass(*args_, **kwargs_)
        else:
            return ColumnDbl(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_v(self):
        return self.v
    def set_v(self, v):
        self.v = v
    def add_v(self, value):
        self.v.append(value)
    def insert_v_at(self, index, value):
        self.v.insert(index, value)
    def replace_v_at(self, index, value):
        self.v[index] = value
    def get_length(self):
        return self.length
    def set_length(self, length):
        self.length = length
    def _hasContent(self):
        if (
            self.v
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ColumnDbl', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ColumnDbl')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ColumnDbl':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ColumnDbl')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ColumnDbl', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ColumnDbl'):
        if self.length is not None and 'length' not in already_processed:
            already_processed.add('length')
            outfile.write(' length="%s"' % self.gds_format_integer(self.length, input_name='length'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ColumnDbl', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for v_ in self.v:
            namespaceprefix_ = self.v_nsprefix_ + ':' if (UseCapturedNS_ and self.v_nsprefix_) else ''
            v_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='v', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ColumnDbl'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.length is not None and 'length' not in already_processed:
            already_processed.add('length')
            showIndent(outfile, level)
            outfile.write('length=%d,\n' % (self.length,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('v=[\n')
        level += 1
        for v_ in self.v:
            showIndent(outfile, level)
            outfile.write('model_.v(\n')
            v_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        value = find_attr_value_('length', node)
        if value is not None and 'length' not in already_processed:
            already_processed.add('length')
            self.length = self.gds_parse_integer(value, node, 'length')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'v':
            obj_ = v.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.v.append(obj_)
            obj_.original_tagname_ = 'v'
# end class ColumnDbl


class ColumnStr(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, length=None, w=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.length = _cast(int, length)
        self.length_nsprefix_ = None
        if w is None:
            self.w = []
        else:
            self.w = w
        self.w_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ColumnStr)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ColumnStr.subclass:
            return ColumnStr.subclass(*args_, **kwargs_)
        else:
            return ColumnStr(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_w(self):
        return self.w
    def set_w(self, w):
        self.w = w
    def add_w(self, value):
        self.w.append(value)
    def insert_w_at(self, index, value):
        self.w.insert(index, value)
    def replace_w_at(self, index, value):
        self.w[index] = value
    def get_length(self):
        return self.length
    def set_length(self, length):
        self.length = length
    def _hasContent(self):
        if (
            self.w
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ColumnStr', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ColumnStr')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ColumnStr':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ColumnStr')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ColumnStr', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ColumnStr'):
        if self.length is not None and 'length' not in already_processed:
            already_processed.add('length')
            outfile.write(' length="%s"' % self.gds_format_integer(self.length, input_name='length'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ColumnStr', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for w_ in self.w:
            namespaceprefix_ = self.w_nsprefix_ + ':' if (UseCapturedNS_ and self.w_nsprefix_) else ''
            w_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='w', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ColumnStr'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.length is not None and 'length' not in already_processed:
            already_processed.add('length')
            showIndent(outfile, level)
            outfile.write('length=%d,\n' % (self.length,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('w=[\n')
        level += 1
        for w_ in self.w:
            showIndent(outfile, level)
            outfile.write('model_.w(\n')
            w_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        value = find_attr_value_('length', node)
        if value is not None and 'length' not in already_processed:
            already_processed.add('length')
            self.length = self.gds_parse_integer(value, node, 'length')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'w':
            obj_ = w.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.w.append(obj_)
            obj_.original_tagname_ = 'w'
# end class ColumnStr


class ElemMD(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, Position=None, i=None, j=None, VariableHandle=None, Response=None, Index=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Position = _cast(int, Position)
        self.Position_nsprefix_ = None
        self.i = _cast(int, i)
        self.i_nsprefix_ = None
        self.j = _cast(int, j)
        self.j_nsprefix_ = None
        self.VariableHandle = _cast(None, VariableHandle)
        self.VariableHandle_nsprefix_ = None
        self.Response = _cast(None, Response)
        self.Response_nsprefix_ = None
        self.Index = _cast(None, Index)
        self.Index_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ElemMD)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ElemMD.subclass:
            return ElemMD.subclass(*args_, **kwargs_)
        else:
            return ElemMD(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def get_i(self):
        return self.i
    def set_i(self, i):
        self.i = i
    def get_j(self):
        return self.j
    def set_j(self, j):
        self.j = j
    def get_VariableHandle(self):
        return self.VariableHandle
    def set_VariableHandle(self, VariableHandle):
        self.VariableHandle = VariableHandle
    def get_Response(self):
        return self.Response
    def set_Response(self, Response):
        self.Response = Response
    def get_Index(self):
        return self.Index
    def set_Index(self, Index):
        self.Index = Index
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ElemMD', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ElemMD')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ElemMD':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ElemMD')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ElemMD', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ElemMD'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position="%s"' % self.gds_format_integer(self.Position, input_name='Position'))
        if self.i is not None and 'i' not in already_processed:
            already_processed.add('i')
            outfile.write(' i="%s"' % self.gds_format_integer(self.i, input_name='i'))
        if self.j is not None and 'j' not in already_processed:
            already_processed.add('j')
            outfile.write(' j="%s"' % self.gds_format_integer(self.j, input_name='j'))
        if self.VariableHandle is not None and 'VariableHandle' not in already_processed:
            already_processed.add('VariableHandle')
            outfile.write(' VariableHandle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.VariableHandle), input_name='VariableHandle')), ))
        if self.Response is not None and 'Response' not in already_processed:
            already_processed.add('Response')
            outfile.write(' Response=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Response), input_name='Response')), ))
        if self.Index is not None and 'Index' not in already_processed:
            already_processed.add('Index')
            outfile.write(' Index=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Index), input_name='Index')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='ElemMD', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='ElemMD'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            showIndent(outfile, level)
            outfile.write('Position=%d,\n' % (self.Position,))
        if self.i is not None and 'i' not in already_processed:
            already_processed.add('i')
            showIndent(outfile, level)
            outfile.write('i=%d,\n' % (self.i,))
        if self.j is not None and 'j' not in already_processed:
            already_processed.add('j')
            showIndent(outfile, level)
            outfile.write('j=%d,\n' % (self.j,))
        if self.VariableHandle is not None and 'VariableHandle' not in already_processed:
            already_processed.add('VariableHandle')
            showIndent(outfile, level)
            outfile.write('VariableHandle="%s",\n' % (self.VariableHandle,))
        if self.Response is not None and 'Response' not in already_processed:
            already_processed.add('Response')
            showIndent(outfile, level)
            outfile.write('Response="%s",\n' % (self.Response,))
        if self.Index is not None and 'Index' not in already_processed:
            already_processed.add('Index')
            showIndent(outfile, level)
            outfile.write('Index="%s",\n' % (self.Index,))
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
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
        value = find_attr_value_('Position', node)
        if value is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            self.Position = self.gds_parse_integer(value, node, 'Position')
        value = find_attr_value_('i', node)
        if value is not None and 'i' not in already_processed:
            already_processed.add('i')
            self.i = self.gds_parse_integer(value, node, 'i')
        value = find_attr_value_('j', node)
        if value is not None and 'j' not in already_processed:
            already_processed.add('j')
            self.j = self.gds_parse_integer(value, node, 'j')
        value = find_attr_value_('VariableHandle', node)
        if value is not None and 'VariableHandle' not in already_processed:
            already_processed.add('VariableHandle')
            self.VariableHandle = value
        value = find_attr_value_('Response', node)
        if value is not None and 'Response' not in already_processed:
            already_processed.add('Response')
            self.Response = value
        value = find_attr_value_('Index', node)
        if value is not None and 'Index' not in already_processed:
            already_processed.add('Index')
            self.Index = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ElemMD


class MatrixRowMD(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ElemMD=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if ElemMD is None:
            self.ElemMD = []
        else:
            self.ElemMD = ElemMD
        self.ElemMD_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MatrixRowMD)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MatrixRowMD.subclass:
            return MatrixRowMD.subclass(*args_, **kwargs_)
        else:
            return MatrixRowMD(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ElemMD(self):
        return self.ElemMD
    def set_ElemMD(self, ElemMD):
        self.ElemMD = ElemMD
    def add_ElemMD(self, value):
        self.ElemMD.append(value)
    def insert_ElemMD_at(self, index, value):
        self.ElemMD.insert(index, value)
    def replace_ElemMD_at(self, index, value):
        self.ElemMD[index] = value
    def _hasContent(self):
        if (
            self.ElemMD
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='MatrixRowMD', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MatrixRowMD')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MatrixRowMD':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MatrixRowMD')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MatrixRowMD', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MatrixRowMD'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='MatrixRowMD', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for ElemMD_ in self.ElemMD:
            namespaceprefix_ = self.ElemMD_nsprefix_ + ':' if (UseCapturedNS_ and self.ElemMD_nsprefix_) else ''
            ElemMD_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ElemMD', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='MatrixRowMD'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('ElemMD=[\n')
        level += 1
        for ElemMD_ in self.ElemMD:
            showIndent(outfile, level)
            outfile.write('model_.ElemMD(\n')
            ElemMD_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'ElemMD':
            obj_ = ElemMD.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ElemMD.append(obj_)
            obj_.original_tagname_ = 'ElemMD'
# end class MatrixRowMD


class MatrixColMD(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ElemMD=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if ElemMD is None:
            self.ElemMD = []
        else:
            self.ElemMD = ElemMD
        self.ElemMD_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MatrixColMD)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MatrixColMD.subclass:
            return MatrixColMD.subclass(*args_, **kwargs_)
        else:
            return MatrixColMD(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ElemMD(self):
        return self.ElemMD
    def set_ElemMD(self, ElemMD):
        self.ElemMD = ElemMD
    def add_ElemMD(self, value):
        self.ElemMD.append(value)
    def insert_ElemMD_at(self, index, value):
        self.ElemMD.insert(index, value)
    def replace_ElemMD_at(self, index, value):
        self.ElemMD[index] = value
    def _hasContent(self):
        if (
            self.ElemMD
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='MatrixColMD', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MatrixColMD')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MatrixColMD':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MatrixColMD')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MatrixColMD', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MatrixColMD'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='MatrixColMD', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for ElemMD_ in self.ElemMD:
            namespaceprefix_ = self.ElemMD_nsprefix_ + ':' if (UseCapturedNS_ and self.ElemMD_nsprefix_) else ''
            ElemMD_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ElemMD', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='MatrixColMD'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('ElemMD=[\n')
        level += 1
        for ElemMD_ in self.ElemMD:
            showIndent(outfile, level)
            outfile.write('model_.ElemMD(\n')
            ElemMD_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'ElemMD':
            obj_ = ElemMD.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ElemMD.append(obj_)
            obj_.original_tagname_ = 'ElemMD'
# end class MatrixColMD


class MatrixDbl(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, RowMD_eq_ColMD=None, nrows=None, ncols=None, MatrixRowMD=None, MatrixColMD=None, RowDbl=None, ColumnDbl=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.RowMD_eq_ColMD = _cast(int, RowMD_eq_ColMD)
        self.RowMD_eq_ColMD_nsprefix_ = None
        self.nrows = _cast(int, nrows)
        self.nrows_nsprefix_ = None
        self.ncols = _cast(int, ncols)
        self.ncols_nsprefix_ = None
        self.MatrixRowMD = MatrixRowMD
        self.MatrixRowMD_nsprefix_ = None
        self.MatrixColMD = MatrixColMD
        self.MatrixColMD_nsprefix_ = None
        if RowDbl is None:
            self.RowDbl = []
        else:
            self.RowDbl = RowDbl
        self.RowDbl_nsprefix_ = None
        if ColumnDbl is None:
            self.ColumnDbl = []
        else:
            self.ColumnDbl = ColumnDbl
        self.ColumnDbl_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MatrixDbl)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MatrixDbl.subclass:
            return MatrixDbl.subclass(*args_, **kwargs_)
        else:
            return MatrixDbl(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_MatrixRowMD(self):
        return self.MatrixRowMD
    def set_MatrixRowMD(self, MatrixRowMD):
        self.MatrixRowMD = MatrixRowMD
    def get_MatrixColMD(self):
        return self.MatrixColMD
    def set_MatrixColMD(self, MatrixColMD):
        self.MatrixColMD = MatrixColMD
    def get_RowDbl(self):
        return self.RowDbl
    def set_RowDbl(self, RowDbl):
        self.RowDbl = RowDbl
    def add_RowDbl(self, value):
        self.RowDbl.append(value)
    def insert_RowDbl_at(self, index, value):
        self.RowDbl.insert(index, value)
    def replace_RowDbl_at(self, index, value):
        self.RowDbl[index] = value
    def get_ColumnDbl(self):
        return self.ColumnDbl
    def set_ColumnDbl(self, ColumnDbl):
        self.ColumnDbl = ColumnDbl
    def add_ColumnDbl(self, value):
        self.ColumnDbl.append(value)
    def insert_ColumnDbl_at(self, index, value):
        self.ColumnDbl.insert(index, value)
    def replace_ColumnDbl_at(self, index, value):
        self.ColumnDbl[index] = value
    def get_RowMD_eq_ColMD(self):
        return self.RowMD_eq_ColMD
    def set_RowMD_eq_ColMD(self, RowMD_eq_ColMD):
        self.RowMD_eq_ColMD = RowMD_eq_ColMD
    def get_nrows(self):
        return self.nrows
    def set_nrows(self, nrows):
        self.nrows = nrows
    def get_ncols(self):
        return self.ncols
    def set_ncols(self, ncols):
        self.ncols = ncols
    def _hasContent(self):
        if (
            self.MatrixRowMD is not None or
            self.MatrixColMD is not None or
            self.RowDbl or
            self.ColumnDbl
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='MatrixDbl', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MatrixDbl')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MatrixDbl':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MatrixDbl')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MatrixDbl', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MatrixDbl'):
        if self.RowMD_eq_ColMD is not None and 'RowMD_eq_ColMD' not in already_processed:
            already_processed.add('RowMD_eq_ColMD')
            outfile.write(' RowMD_eq_ColMD="%s"' % self.gds_format_integer(self.RowMD_eq_ColMD, input_name='RowMD_eq_ColMD'))
        if self.nrows is not None and 'nrows' not in already_processed:
            already_processed.add('nrows')
            outfile.write(' nrows="%s"' % self.gds_format_integer(self.nrows, input_name='nrows'))
        if self.ncols is not None and 'ncols' not in already_processed:
            already_processed.add('ncols')
            outfile.write(' ncols="%s"' % self.gds_format_integer(self.ncols, input_name='ncols'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='MatrixDbl', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.MatrixRowMD is not None:
            namespaceprefix_ = self.MatrixRowMD_nsprefix_ + ':' if (UseCapturedNS_ and self.MatrixRowMD_nsprefix_) else ''
            self.MatrixRowMD.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MatrixRowMD', pretty_print=pretty_print)
        if self.MatrixColMD is not None:
            namespaceprefix_ = self.MatrixColMD_nsprefix_ + ':' if (UseCapturedNS_ and self.MatrixColMD_nsprefix_) else ''
            self.MatrixColMD.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MatrixColMD', pretty_print=pretty_print)
        for RowDbl_ in self.RowDbl:
            namespaceprefix_ = self.RowDbl_nsprefix_ + ':' if (UseCapturedNS_ and self.RowDbl_nsprefix_) else ''
            RowDbl_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RowDbl', pretty_print=pretty_print)
        for ColumnDbl_ in self.ColumnDbl:
            namespaceprefix_ = self.ColumnDbl_nsprefix_ + ':' if (UseCapturedNS_ and self.ColumnDbl_nsprefix_) else ''
            ColumnDbl_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ColumnDbl', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='MatrixDbl'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.RowMD_eq_ColMD is not None and 'RowMD_eq_ColMD' not in already_processed:
            already_processed.add('RowMD_eq_ColMD')
            showIndent(outfile, level)
            outfile.write('RowMD_eq_ColMD=%d,\n' % (self.RowMD_eq_ColMD,))
        if self.nrows is not None and 'nrows' not in already_processed:
            already_processed.add('nrows')
            showIndent(outfile, level)
            outfile.write('nrows=%d,\n' % (self.nrows,))
        if self.ncols is not None and 'ncols' not in already_processed:
            already_processed.add('ncols')
            showIndent(outfile, level)
            outfile.write('ncols=%d,\n' % (self.ncols,))
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.MatrixRowMD is not None:
            showIndent(outfile, level)
            outfile.write('MatrixRowMD=model_.MatrixRowMD(\n')
            self.MatrixRowMD.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.MatrixColMD is not None:
            showIndent(outfile, level)
            outfile.write('MatrixColMD=model_.MatrixColMD(\n')
            self.MatrixColMD.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('RowDbl=[\n')
        level += 1
        for RowDbl_ in self.RowDbl:
            showIndent(outfile, level)
            outfile.write('model_.RowDbl(\n')
            RowDbl_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('ColumnDbl=[\n')
        level += 1
        for ColumnDbl_ in self.ColumnDbl:
            showIndent(outfile, level)
            outfile.write('model_.ColumnDbl(\n')
            ColumnDbl_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        value = find_attr_value_('RowMD_eq_ColMD', node)
        if value is not None and 'RowMD_eq_ColMD' not in already_processed:
            already_processed.add('RowMD_eq_ColMD')
            self.RowMD_eq_ColMD = self.gds_parse_integer(value, node, 'RowMD_eq_ColMD')
        value = find_attr_value_('nrows', node)
        if value is not None and 'nrows' not in already_processed:
            already_processed.add('nrows')
            self.nrows = self.gds_parse_integer(value, node, 'nrows')
        value = find_attr_value_('ncols', node)
        if value is not None and 'ncols' not in already_processed:
            already_processed.add('ncols')
            self.ncols = self.gds_parse_integer(value, node, 'ncols')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'MatrixRowMD':
            obj_ = MatrixRowMD.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MatrixRowMD = obj_
            obj_.original_tagname_ = 'MatrixRowMD'
        elif nodeName_ == 'MatrixColMD':
            obj_ = MatrixColMD.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MatrixColMD = obj_
            obj_.original_tagname_ = 'MatrixColMD'
        elif nodeName_ == 'RowDbl':
            obj_ = RowDbl.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RowDbl.append(obj_)
            obj_.original_tagname_ = 'RowDbl'
        elif nodeName_ == 'ColumnDbl':
            obj_ = ColumnDbl.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ColumnDbl.append(obj_)
            obj_.original_tagname_ = 'ColumnDbl'
# end class MatrixDbl


class MatrixStr(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, RowMD_eq_ColMD=None, nrows=None, ncols=None, MatrixRowMD=None, MatrixColMD=None, RowStr=None, ColumnStr=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.RowMD_eq_ColMD = _cast(int, RowMD_eq_ColMD)
        self.RowMD_eq_ColMD_nsprefix_ = None
        self.nrows = _cast(int, nrows)
        self.nrows_nsprefix_ = None
        self.ncols = _cast(int, ncols)
        self.ncols_nsprefix_ = None
        self.MatrixRowMD = MatrixRowMD
        self.MatrixRowMD_nsprefix_ = None
        self.MatrixColMD = MatrixColMD
        self.MatrixColMD_nsprefix_ = None
        if RowStr is None:
            self.RowStr = []
        else:
            self.RowStr = RowStr
        self.RowStr_nsprefix_ = None
        if ColumnStr is None:
            self.ColumnStr = []
        else:
            self.ColumnStr = ColumnStr
        self.ColumnStr_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MatrixStr)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MatrixStr.subclass:
            return MatrixStr.subclass(*args_, **kwargs_)
        else:
            return MatrixStr(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_MatrixRowMD(self):
        return self.MatrixRowMD
    def set_MatrixRowMD(self, MatrixRowMD):
        self.MatrixRowMD = MatrixRowMD
    def get_MatrixColMD(self):
        return self.MatrixColMD
    def set_MatrixColMD(self, MatrixColMD):
        self.MatrixColMD = MatrixColMD
    def get_RowStr(self):
        return self.RowStr
    def set_RowStr(self, RowStr):
        self.RowStr = RowStr
    def add_RowStr(self, value):
        self.RowStr.append(value)
    def insert_RowStr_at(self, index, value):
        self.RowStr.insert(index, value)
    def replace_RowStr_at(self, index, value):
        self.RowStr[index] = value
    def get_ColumnStr(self):
        return self.ColumnStr
    def set_ColumnStr(self, ColumnStr):
        self.ColumnStr = ColumnStr
    def add_ColumnStr(self, value):
        self.ColumnStr.append(value)
    def insert_ColumnStr_at(self, index, value):
        self.ColumnStr.insert(index, value)
    def replace_ColumnStr_at(self, index, value):
        self.ColumnStr[index] = value
    def get_RowMD_eq_ColMD(self):
        return self.RowMD_eq_ColMD
    def set_RowMD_eq_ColMD(self, RowMD_eq_ColMD):
        self.RowMD_eq_ColMD = RowMD_eq_ColMD
    def get_nrows(self):
        return self.nrows
    def set_nrows(self, nrows):
        self.nrows = nrows
    def get_ncols(self):
        return self.ncols
    def set_ncols(self, ncols):
        self.ncols = ncols
    def _hasContent(self):
        if (
            self.MatrixRowMD is not None or
            self.MatrixColMD is not None or
            self.RowStr or
            self.ColumnStr
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='MatrixStr', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MatrixStr')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MatrixStr':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MatrixStr')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MatrixStr', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MatrixStr'):
        if self.RowMD_eq_ColMD is not None and 'RowMD_eq_ColMD' not in already_processed:
            already_processed.add('RowMD_eq_ColMD')
            outfile.write(' RowMD_eq_ColMD="%s"' % self.gds_format_integer(self.RowMD_eq_ColMD, input_name='RowMD_eq_ColMD'))
        if self.nrows is not None and 'nrows' not in already_processed:
            already_processed.add('nrows')
            outfile.write(' nrows="%s"' % self.gds_format_integer(self.nrows, input_name='nrows'))
        if self.ncols is not None and 'ncols' not in already_processed:
            already_processed.add('ncols')
            outfile.write(' ncols="%s"' % self.gds_format_integer(self.ncols, input_name='ncols'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='MatrixStr', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.MatrixRowMD is not None:
            namespaceprefix_ = self.MatrixRowMD_nsprefix_ + ':' if (UseCapturedNS_ and self.MatrixRowMD_nsprefix_) else ''
            self.MatrixRowMD.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MatrixRowMD', pretty_print=pretty_print)
        if self.MatrixColMD is not None:
            namespaceprefix_ = self.MatrixColMD_nsprefix_ + ':' if (UseCapturedNS_ and self.MatrixColMD_nsprefix_) else ''
            self.MatrixColMD.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MatrixColMD', pretty_print=pretty_print)
        for RowStr_ in self.RowStr:
            namespaceprefix_ = self.RowStr_nsprefix_ + ':' if (UseCapturedNS_ and self.RowStr_nsprefix_) else ''
            RowStr_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RowStr', pretty_print=pretty_print)
        for ColumnStr_ in self.ColumnStr:
            namespaceprefix_ = self.ColumnStr_nsprefix_ + ':' if (UseCapturedNS_ and self.ColumnStr_nsprefix_) else ''
            ColumnStr_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ColumnStr', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='MatrixStr'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.RowMD_eq_ColMD is not None and 'RowMD_eq_ColMD' not in already_processed:
            already_processed.add('RowMD_eq_ColMD')
            showIndent(outfile, level)
            outfile.write('RowMD_eq_ColMD=%d,\n' % (self.RowMD_eq_ColMD,))
        if self.nrows is not None and 'nrows' not in already_processed:
            already_processed.add('nrows')
            showIndent(outfile, level)
            outfile.write('nrows=%d,\n' % (self.nrows,))
        if self.ncols is not None and 'ncols' not in already_processed:
            already_processed.add('ncols')
            showIndent(outfile, level)
            outfile.write('ncols=%d,\n' % (self.ncols,))
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.MatrixRowMD is not None:
            showIndent(outfile, level)
            outfile.write('MatrixRowMD=model_.MatrixRowMD(\n')
            self.MatrixRowMD.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.MatrixColMD is not None:
            showIndent(outfile, level)
            outfile.write('MatrixColMD=model_.MatrixColMD(\n')
            self.MatrixColMD.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('RowStr=[\n')
        level += 1
        for RowStr_ in self.RowStr:
            showIndent(outfile, level)
            outfile.write('model_.RowStr(\n')
            RowStr_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('ColumnStr=[\n')
        level += 1
        for ColumnStr_ in self.ColumnStr:
            showIndent(outfile, level)
            outfile.write('model_.ColumnStr(\n')
            ColumnStr_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        value = find_attr_value_('RowMD_eq_ColMD', node)
        if value is not None and 'RowMD_eq_ColMD' not in already_processed:
            already_processed.add('RowMD_eq_ColMD')
            self.RowMD_eq_ColMD = self.gds_parse_integer(value, node, 'RowMD_eq_ColMD')
        value = find_attr_value_('nrows', node)
        if value is not None and 'nrows' not in already_processed:
            already_processed.add('nrows')
            self.nrows = self.gds_parse_integer(value, node, 'nrows')
        value = find_attr_value_('ncols', node)
        if value is not None and 'ncols' not in already_processed:
            already_processed.add('ncols')
            self.ncols = self.gds_parse_integer(value, node, 'ncols')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'MatrixRowMD':
            obj_ = MatrixRowMD.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MatrixRowMD = obj_
            obj_.original_tagname_ = 'MatrixRowMD'
        elif nodeName_ == 'MatrixColMD':
            obj_ = MatrixColMD.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MatrixColMD = obj_
            obj_.original_tagname_ = 'MatrixColMD'
        elif nodeName_ == 'RowStr':
            obj_ = RowStr.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RowStr.append(obj_)
            obj_.original_tagname_ = 'RowStr'
        elif nodeName_ == 'ColumnStr':
            obj_ = ColumnStr.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ColumnStr.append(obj_)
            obj_.original_tagname_ = 'ColumnStr'
# end class MatrixStr


class CleanLimit(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Position = _cast(None, Position)
        self.Position_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CleanLimit)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CleanLimit.subclass:
            return CleanLimit.subclass(*args_, **kwargs_)
        else:
            return CleanLimit(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_Dbl(self, value):
        result = True
        # Validate type Dbl, a restriction on None.
        pass
        return result
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CleanLimit', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CleanLimit')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CleanLimit':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CleanLimit')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CleanLimit', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CleanLimit'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Position), input_name='Position')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CleanLimit', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='CleanLimit'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            showIndent(outfile, level)
            outfile.write('Position="%s",\n' % (self.Position,))
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Position', node)
        if value is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            self.Position = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class CleanLimit


class LeftLimit(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LeftLimit)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LeftLimit.subclass:
            return LeftLimit.subclass(*args_, **kwargs_)
        else:
            return LeftLimit(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_Dbl(self, value):
        result = True
        # Validate type Dbl, a restriction on None.
        pass
        return result
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='LeftLimit', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LeftLimit')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LeftLimit':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LeftLimit')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LeftLimit', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LeftLimit'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='LeftLimit', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='LeftLimit'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class LeftLimit


class RightLimit(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RightLimit)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RightLimit.subclass:
            return RightLimit.subclass(*args_, **kwargs_)
        else:
            return RightLimit(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_Dbl(self, value):
        result = True
        # Validate type Dbl, a restriction on None.
        pass
        return result
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='RightLimit', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RightLimit')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RightLimit':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RightLimit')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RightLimit', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RightLimit'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='RightLimit', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='RightLimit'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class RightLimit


class CleanLimits(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, v=None, CleanLimit=None, LeftLimit=None, RightLimit=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if v is None:
            self.v = []
        else:
            self.v = v
        self.v_nsprefix_ = None
        if CleanLimit is None:
            self.CleanLimit = []
        else:
            self.CleanLimit = CleanLimit
        self.CleanLimit_nsprefix_ = None
        self.LeftLimit = LeftLimit
        self.LeftLimit_nsprefix_ = None
        self.RightLimit = RightLimit
        self.RightLimit_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CleanLimits)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CleanLimits.subclass:
            return CleanLimits.subclass(*args_, **kwargs_)
        else:
            return CleanLimits(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_v(self):
        return self.v
    def set_v(self, v):
        self.v = v
    def add_v(self, value):
        self.v.append(value)
    def insert_v_at(self, index, value):
        self.v.insert(index, value)
    def replace_v_at(self, index, value):
        self.v[index] = value
    def get_CleanLimit(self):
        return self.CleanLimit
    def set_CleanLimit(self, CleanLimit):
        self.CleanLimit = CleanLimit
    def add_CleanLimit(self, value):
        self.CleanLimit.append(value)
    def insert_CleanLimit_at(self, index, value):
        self.CleanLimit.insert(index, value)
    def replace_CleanLimit_at(self, index, value):
        self.CleanLimit[index] = value
    def get_LeftLimit(self):
        return self.LeftLimit
    def set_LeftLimit(self, LeftLimit):
        self.LeftLimit = LeftLimit
    def get_RightLimit(self):
        return self.RightLimit
    def set_RightLimit(self, RightLimit):
        self.RightLimit = RightLimit
    def _hasContent(self):
        if (
            self.v or
            self.CleanLimit or
            self.LeftLimit is not None or
            self.RightLimit is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CleanLimits', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CleanLimits')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CleanLimits':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CleanLimits')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CleanLimits', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CleanLimits'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CleanLimits', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for v_ in self.v:
            namespaceprefix_ = self.v_nsprefix_ + ':' if (UseCapturedNS_ and self.v_nsprefix_) else ''
            v_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='v', pretty_print=pretty_print)
        for CleanLimit_ in self.CleanLimit:
            namespaceprefix_ = self.CleanLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.CleanLimit_nsprefix_) else ''
            CleanLimit_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CleanLimit', pretty_print=pretty_print)
        if self.LeftLimit is not None:
            namespaceprefix_ = self.LeftLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.LeftLimit_nsprefix_) else ''
            self.LeftLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='LeftLimit', pretty_print=pretty_print)
        if self.RightLimit is not None:
            namespaceprefix_ = self.RightLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.RightLimit_nsprefix_) else ''
            self.RightLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RightLimit', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='CleanLimits'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('v=[\n')
        level += 1
        for v_ in self.v:
            showIndent(outfile, level)
            outfile.write('model_.v(\n')
            v_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('CleanLimit=[\n')
        level += 1
        for CleanLimit_ in self.CleanLimit:
            showIndent(outfile, level)
            outfile.write('model_.CleanLimit(\n')
            CleanLimit_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.LeftLimit is not None:
            showIndent(outfile, level)
            outfile.write('LeftLimit=model_.LeftLimit(\n')
            self.LeftLimit.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.RightLimit is not None:
            showIndent(outfile, level)
            outfile.write('RightLimit=model_.RightLimit(\n')
            self.RightLimit.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
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
        if nodeName_ == 'v':
            obj_ = v.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.v.append(obj_)
            obj_.original_tagname_ = 'v'
        elif nodeName_ == 'CleanLimit':
            obj_ = CleanLimit.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CleanLimit.append(obj_)
            obj_.original_tagname_ = 'CleanLimit'
        elif nodeName_ == 'LeftLimit':
            obj_ = LeftLimit.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.LeftLimit = obj_
            obj_.original_tagname_ = 'LeftLimit'
        elif nodeName_ == 'RightLimit':
            obj_ = RightLimit.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RightLimit = obj_
            obj_.original_tagname_ = 'RightLimit'
# end class CleanLimits


class DropIndices(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, DropIndex=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if DropIndex is None:
            self.DropIndex = []
        else:
            self.DropIndex = DropIndex
        self.DropIndex_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DropIndices)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DropIndices.subclass:
            return DropIndices.subclass(*args_, **kwargs_)
        else:
            return DropIndices(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_DropIndex(self):
        return self.DropIndex
    def set_DropIndex(self, DropIndex):
        self.DropIndex = DropIndex
    def add_DropIndex(self, value):
        self.DropIndex.append(value)
    def insert_DropIndex_at(self, index, value):
        self.DropIndex.insert(index, value)
    def replace_DropIndex_at(self, index, value):
        self.DropIndex[index] = value
    def _hasContent(self):
        if (
            self.DropIndex
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='DropIndices', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DropIndices')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DropIndices':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DropIndices')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DropIndices', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DropIndices'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='DropIndices', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for DropIndex_ in self.DropIndex:
            namespaceprefix_ = self.DropIndex_nsprefix_ + ':' if (UseCapturedNS_ and self.DropIndex_nsprefix_) else ''
            DropIndex_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DropIndex', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='DropIndices'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('DropIndex=[\n')
        level += 1
        for DropIndex_ in self.DropIndex:
            showIndent(outfile, level)
            outfile.write('model_.DropIndex(\n')
            DropIndex_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'DropIndex':
            obj_ = Int.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DropIndex.append(obj_)
            obj_.original_tagname_ = 'DropIndex'
# end class DropIndices


class CriticalValue(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Position = _cast(None, Position)
        self.Position_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CriticalValue)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CriticalValue.subclass:
            return CriticalValue.subclass(*args_, **kwargs_)
        else:
            return CriticalValue(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_Dbl(self, value):
        result = True
        # Validate type Dbl, a restriction on None.
        pass
        return result
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CriticalValue', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CriticalValue')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CriticalValue':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CriticalValue')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CriticalValue', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CriticalValue'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Position), input_name='Position')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CriticalValue', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='CriticalValue'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            showIndent(outfile, level)
            outfile.write('Position="%s",\n' % (self.Position,))
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Position', node)
        if value is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            self.Position = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class CriticalValue


class CriticalValues(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, v=None, CriticalValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if v is None:
            self.v = []
        else:
            self.v = v
        self.v_nsprefix_ = None
        if CriticalValue is None:
            self.CriticalValue = []
        else:
            self.CriticalValue = CriticalValue
        self.CriticalValue_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CriticalValues)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CriticalValues.subclass:
            return CriticalValues.subclass(*args_, **kwargs_)
        else:
            return CriticalValues(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_v(self):
        return self.v
    def set_v(self, v):
        self.v = v
    def add_v(self, value):
        self.v.append(value)
    def insert_v_at(self, index, value):
        self.v.insert(index, value)
    def replace_v_at(self, index, value):
        self.v[index] = value
    def get_CriticalValue(self):
        return self.CriticalValue
    def set_CriticalValue(self, CriticalValue):
        self.CriticalValue = CriticalValue
    def add_CriticalValue(self, value):
        self.CriticalValue.append(value)
    def insert_CriticalValue_at(self, index, value):
        self.CriticalValue.insert(index, value)
    def replace_CriticalValue_at(self, index, value):
        self.CriticalValue[index] = value
    def _hasContent(self):
        if (
            self.v or
            self.CriticalValue
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CriticalValues', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CriticalValues')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CriticalValues':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CriticalValues')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CriticalValues', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CriticalValues'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CriticalValues', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for v_ in self.v:
            namespaceprefix_ = self.v_nsprefix_ + ':' if (UseCapturedNS_ and self.v_nsprefix_) else ''
            v_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='v', pretty_print=pretty_print)
        for CriticalValue_ in self.CriticalValue:
            namespaceprefix_ = self.CriticalValue_nsprefix_ + ':' if (UseCapturedNS_ and self.CriticalValue_nsprefix_) else ''
            CriticalValue_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CriticalValue', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='CriticalValues'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('v=[\n')
        level += 1
        for v_ in self.v:
            showIndent(outfile, level)
            outfile.write('model_.v(\n')
            v_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('CriticalValue=[\n')
        level += 1
        for CriticalValue_ in self.CriticalValue:
            showIndent(outfile, level)
            outfile.write('model_.CriticalValue(\n')
            CriticalValue_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'v':
            obj_ = v.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.v.append(obj_)
            obj_.original_tagname_ = 'v'
        elif nodeName_ == 'CriticalValue':
            obj_ = CriticalValue.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CriticalValue.append(obj_)
            obj_.original_tagname_ = 'CriticalValue'
# end class CriticalValues


class CriticalWord(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Dlm=None, Position=None, w=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Dlm = _cast(None, Dlm)
        self.Dlm_nsprefix_ = None
        self.Position = _cast(None, Position)
        self.Position_nsprefix_ = None
        if w is None:
            self.w = []
        else:
            self.w = w
        self.w_nsprefix_ = None
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CriticalWord)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CriticalWord.subclass:
            return CriticalWord.subclass(*args_, **kwargs_)
        else:
            return CriticalWord(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_w(self):
        return self.w
    def set_w(self, w):
        self.w = w
    def add_w(self, value):
        self.w.append(value)
    def insert_w_at(self, index, value):
        self.w.insert(index, value)
    def replace_w_at(self, index, value):
        self.w[index] = value
    def get_Dlm(self):
        return self.Dlm
    def set_Dlm(self, Dlm):
        self.Dlm = Dlm
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            self.w or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CriticalWord', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CriticalWord')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CriticalWord':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CriticalWord')
        if self._hasContent():
            outfile.write('>')
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CriticalWord', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CriticalWord'):
        if self.Dlm is not None and 'Dlm' not in already_processed:
            already_processed.add('Dlm')
            outfile.write(' Dlm=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Dlm), input_name='Dlm')), ))
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position=%s' % (quote_attrib(self.Position), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CriticalWord', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for w_ in self.w:
            namespaceprefix_ = self.w_nsprefix_ + ':' if (UseCapturedNS_ and self.w_nsprefix_) else ''
            w_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='w', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='CriticalWord'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Dlm is not None and 'Dlm' not in already_processed:
            already_processed.add('Dlm')
            showIndent(outfile, level)
            outfile.write('Dlm="%s",\n' % (self.Dlm,))
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            showIndent(outfile, level)
            outfile.write('Position=%s,\n' % (self.Position,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('],\n')
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Dlm', node)
        if value is not None and 'Dlm' not in already_processed:
            already_processed.add('Dlm')
            self.Dlm = value
        value = find_attr_value_('Position', node)
        if value is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            self.Position = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'w':
            obj_ = w.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'w', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_w'):
              self.add_w(obj_.value)
            elif hasattr(self, 'set_w'):
              self.set_w(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class CriticalWord


class CriticalWordList(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Dlm=None, WordDlm=None, Position=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Dlm = _cast(None, Dlm)
        self.Dlm_nsprefix_ = None
        self.WordDlm = _cast(None, WordDlm)
        self.WordDlm_nsprefix_ = None
        self.Position = _cast(None, Position)
        self.Position_nsprefix_ = None
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CriticalWordList)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CriticalWordList.subclass:
            return CriticalWordList.subclass(*args_, **kwargs_)
        else:
            return CriticalWordList(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Dlm(self):
        return self.Dlm
    def set_Dlm(self, Dlm):
        self.Dlm = Dlm
    def get_WordDlm(self):
        return self.WordDlm
    def set_WordDlm(self, WordDlm):
        self.WordDlm = WordDlm
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CriticalWordList', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CriticalWordList')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CriticalWordList':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CriticalWordList')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CriticalWordList'):
        if self.Dlm is not None and 'Dlm' not in already_processed:
            already_processed.add('Dlm')
            outfile.write(' Dlm=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Dlm), input_name='Dlm')), ))
        if self.WordDlm is not None and 'WordDlm' not in already_processed:
            already_processed.add('WordDlm')
            outfile.write(' WordDlm=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.WordDlm), input_name='WordDlm')), ))
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position=%s' % (quote_attrib(self.Position), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CriticalWordList', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='CriticalWordList'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Dlm is not None and 'Dlm' not in already_processed:
            already_processed.add('Dlm')
            showIndent(outfile, level)
            outfile.write('Dlm="%s",\n' % (self.Dlm,))
        if self.WordDlm is not None and 'WordDlm' not in already_processed:
            already_processed.add('WordDlm')
            showIndent(outfile, level)
            outfile.write('WordDlm="%s",\n' % (self.WordDlm,))
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            showIndent(outfile, level)
            outfile.write('Position=%s,\n' % (self.Position,))
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Dlm', node)
        if value is not None and 'Dlm' not in already_processed:
            already_processed.add('Dlm')
            self.Dlm = value
        value = find_attr_value_('WordDlm', node)
        if value is not None and 'WordDlm' not in already_processed:
            already_processed.add('WordDlm')
            self.WordDlm = value
        value = find_attr_value_('Position', node)
        if value is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            self.Position = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        pass
# end class CriticalWordList


class CriticalWords(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, CriticalWord=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if CriticalWord is None:
            self.CriticalWord = []
        else:
            self.CriticalWord = CriticalWord
        self.CriticalWord_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CriticalWords)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CriticalWords.subclass:
            return CriticalWords.subclass(*args_, **kwargs_)
        else:
            return CriticalWords(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CriticalWord(self):
        return self.CriticalWord
    def set_CriticalWord(self, CriticalWord):
        self.CriticalWord = CriticalWord
    def add_CriticalWord(self, value):
        self.CriticalWord.append(value)
    def insert_CriticalWord_at(self, index, value):
        self.CriticalWord.insert(index, value)
    def replace_CriticalWord_at(self, index, value):
        self.CriticalWord[index] = value
    def _hasContent(self):
        if (
            self.CriticalWord
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CriticalWords', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CriticalWords')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CriticalWords':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CriticalWords')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CriticalWords', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CriticalWords'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CriticalWords', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for CriticalWord_ in self.CriticalWord:
            namespaceprefix_ = self.CriticalWord_nsprefix_ + ':' if (UseCapturedNS_ and self.CriticalWord_nsprefix_) else ''
            CriticalWord_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CriticalWord', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='CriticalWords'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('CriticalWord=[\n')
        level += 1
        for CriticalWord_ in self.CriticalWord:
            showIndent(outfile, level)
            outfile.write('model_.CriticalWord(\n')
            CriticalWord_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'CriticalWord':
            obj_ = CriticalWord.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CriticalWord.append(obj_)
            obj_.original_tagname_ = 'CriticalWord'
# end class CriticalWords


class CriticalWordSet(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, CriticalWord=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if CriticalWord is None:
            self.CriticalWord = []
        else:
            self.CriticalWord = CriticalWord
        self.CriticalWord_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CriticalWordSet)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CriticalWordSet.subclass:
            return CriticalWordSet.subclass(*args_, **kwargs_)
        else:
            return CriticalWordSet(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CriticalWord(self):
        return self.CriticalWord
    def set_CriticalWord(self, CriticalWord):
        self.CriticalWord = CriticalWord
    def add_CriticalWord(self, value):
        self.CriticalWord.append(value)
    def insert_CriticalWord_at(self, index, value):
        self.CriticalWord.insert(index, value)
    def replace_CriticalWord_at(self, index, value):
        self.CriticalWord[index] = value
    def _hasContent(self):
        if (
            self.CriticalWord
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CriticalWordSet', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CriticalWordSet')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CriticalWordSet':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CriticalWordSet')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CriticalWordSet', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CriticalWordSet'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CriticalWordSet', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for CriticalWord_ in self.CriticalWord:
            namespaceprefix_ = self.CriticalWord_nsprefix_ + ':' if (UseCapturedNS_ and self.CriticalWord_nsprefix_) else ''
            CriticalWord_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CriticalWord', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='CriticalWordSet'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('CriticalWord=[\n')
        level += 1
        for CriticalWord_ in self.CriticalWord:
            showIndent(outfile, level)
            outfile.write('model_.CriticalWord(\n')
            CriticalWord_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'CriticalWord':
            obj_ = CriticalWord.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CriticalWord.append(obj_)
            obj_.original_tagname_ = 'CriticalWord'
# end class CriticalWordSet


class Coefficient(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Position = _cast(None, Position)
        self.Position_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Coefficient)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Coefficient.subclass:
            return Coefficient.subclass(*args_, **kwargs_)
        else:
            return Coefficient(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_Dbl(self, value):
        result = True
        # Validate type Dbl, a restriction on None.
        pass
        return result
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Coefficient', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Coefficient')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Coefficient':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Coefficient')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Coefficient', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Coefficient'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Position), input_name='Position')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Coefficient', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='Coefficient'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            showIndent(outfile, level)
            outfile.write('Position="%s",\n' % (self.Position,))
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Position', node)
        if value is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            self.Position = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Coefficient


class Coefficients(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Response=None, Coefficient=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Response = _cast(None, Response)
        self.Response_nsprefix_ = None
        if Coefficient is None:
            self.Coefficient = []
        else:
            self.Coefficient = Coefficient
        self.Coefficient_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Coefficients)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Coefficients.subclass:
            return Coefficients.subclass(*args_, **kwargs_)
        else:
            return Coefficients(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Coefficient(self):
        return self.Coefficient
    def set_Coefficient(self, Coefficient):
        self.Coefficient = Coefficient
    def add_Coefficient(self, value):
        self.Coefficient.append(value)
    def insert_Coefficient_at(self, index, value):
        self.Coefficient.insert(index, value)
    def replace_Coefficient_at(self, index, value):
        self.Coefficient[index] = value
    def get_Response(self):
        return self.Response
    def set_Response(self, Response):
        self.Response = Response
    def _hasContent(self):
        if (
            self.Coefficient
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Coefficients', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Coefficients')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Coefficients':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Coefficients')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Coefficients', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Coefficients'):
        if self.Response is not None and 'Response' not in already_processed:
            already_processed.add('Response')
            outfile.write(' Response=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Response), input_name='Response')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Coefficients', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Coefficient_ in self.Coefficient:
            namespaceprefix_ = self.Coefficient_nsprefix_ + ':' if (UseCapturedNS_ and self.Coefficient_nsprefix_) else ''
            Coefficient_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Coefficient', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Coefficients'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Response is not None and 'Response' not in already_processed:
            already_processed.add('Response')
            showIndent(outfile, level)
            outfile.write('Response="%s",\n' % (self.Response,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Coefficient=[\n')
        level += 1
        for Coefficient_ in self.Coefficient:
            showIndent(outfile, level)
            outfile.write('model_.Coefficient(\n')
            Coefficient_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        value = find_attr_value_('Response', node)
        if value is not None and 'Response' not in already_processed:
            already_processed.add('Response')
            self.Response = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Coefficient':
            obj_ = Coefficient.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Coefficient.append(obj_)
            obj_.original_tagname_ = 'Coefficient'
# end class Coefficients


class CoefficientSet(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Response=None, CoefficientList=None, Coefficients=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Response = _cast(None, Response)
        self.Response_nsprefix_ = None
        if CoefficientList is None:
            self.CoefficientList = []
        else:
            self.CoefficientList = CoefficientList
        self.CoefficientList_nsprefix_ = None
        if Coefficients is None:
            self.Coefficients = []
        else:
            self.Coefficients = Coefficients
        self.Coefficients_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CoefficientSet)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CoefficientSet.subclass:
            return CoefficientSet.subclass(*args_, **kwargs_)
        else:
            return CoefficientSet(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CoefficientList(self):
        return self.CoefficientList
    def set_CoefficientList(self, CoefficientList):
        self.CoefficientList = CoefficientList
    def add_CoefficientList(self, value):
        self.CoefficientList.append(value)
    def insert_CoefficientList_at(self, index, value):
        self.CoefficientList.insert(index, value)
    def replace_CoefficientList_at(self, index, value):
        self.CoefficientList[index] = value
    def get_Coefficients(self):
        return self.Coefficients
    def set_Coefficients(self, Coefficients):
        self.Coefficients = Coefficients
    def add_Coefficients(self, value):
        self.Coefficients.append(value)
    def insert_Coefficients_at(self, index, value):
        self.Coefficients.insert(index, value)
    def replace_Coefficients_at(self, index, value):
        self.Coefficients[index] = value
    def get_Response(self):
        return self.Response
    def set_Response(self, Response):
        self.Response = Response
    def _hasContent(self):
        if (
            self.CoefficientList or
            self.Coefficients
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CoefficientSet', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CoefficientSet')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CoefficientSet':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CoefficientSet')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CoefficientSet', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CoefficientSet'):
        if self.Response is not None and 'Response' not in already_processed:
            already_processed.add('Response')
            outfile.write(' Response=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Response), input_name='Response')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CoefficientSet', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for CoefficientList_ in self.CoefficientList:
            namespaceprefix_ = self.CoefficientList_nsprefix_ + ':' if (UseCapturedNS_ and self.CoefficientList_nsprefix_) else ''
            CoefficientList_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CoefficientList', pretty_print=pretty_print)
        for Coefficients_ in self.Coefficients:
            namespaceprefix_ = self.Coefficients_nsprefix_ + ':' if (UseCapturedNS_ and self.Coefficients_nsprefix_) else ''
            Coefficients_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Coefficients', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='CoefficientSet'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Response is not None and 'Response' not in already_processed:
            already_processed.add('Response')
            showIndent(outfile, level)
            outfile.write('Response="%s",\n' % (self.Response,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('CoefficientList=[\n')
        level += 1
        for CoefficientList_ in self.CoefficientList:
            showIndent(outfile, level)
            outfile.write('model_.CoefficientList(\n')
            CoefficientList_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('Coefficients=[\n')
        level += 1
        for Coefficients_ in self.Coefficients:
            showIndent(outfile, level)
            outfile.write('model_.Coefficients(\n')
            Coefficients_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        value = find_attr_value_('Response', node)
        if value is not None and 'Response' not in already_processed:
            already_processed.add('Response')
            self.Response = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CoefficientList':
            obj_ = CoefficientList.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CoefficientList.append(obj_)
            obj_.original_tagname_ = 'CoefficientList'
        elif nodeName_ == 'Coefficients':
            obj_ = Coefficients.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Coefficients.append(obj_)
            obj_.original_tagname_ = 'Coefficients'
# end class CoefficientSet


class CoefficientSets(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Use=None, Coefficients=None, CoefficientSet=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Use = _cast(None, Use)
        self.Use_nsprefix_ = None
        if Coefficients is None:
            self.Coefficients = []
        else:
            self.Coefficients = Coefficients
        self.Coefficients_nsprefix_ = None
        if CoefficientSet is None:
            self.CoefficientSet = []
        else:
            self.CoefficientSet = CoefficientSet
        self.CoefficientSet_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CoefficientSets)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CoefficientSets.subclass:
            return CoefficientSets.subclass(*args_, **kwargs_)
        else:
            return CoefficientSets(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Coefficients(self):
        return self.Coefficients
    def set_Coefficients(self, Coefficients):
        self.Coefficients = Coefficients
    def add_Coefficients(self, value):
        self.Coefficients.append(value)
    def insert_Coefficients_at(self, index, value):
        self.Coefficients.insert(index, value)
    def replace_Coefficients_at(self, index, value):
        self.Coefficients[index] = value
    def get_CoefficientSet(self):
        return self.CoefficientSet
    def set_CoefficientSet(self, CoefficientSet):
        self.CoefficientSet = CoefficientSet
    def add_CoefficientSet(self, value):
        self.CoefficientSet.append(value)
    def insert_CoefficientSet_at(self, index, value):
        self.CoefficientSet.insert(index, value)
    def replace_CoefficientSet_at(self, index, value):
        self.CoefficientSet[index] = value
    def get_Use(self):
        return self.Use
    def set_Use(self, Use):
        self.Use = Use
    def _hasContent(self):
        if (
            self.Coefficients or
            self.CoefficientSet
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CoefficientSets', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CoefficientSets')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CoefficientSets':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CoefficientSets')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CoefficientSets', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CoefficientSets'):
        if self.Use is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            outfile.write(' Use=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Use), input_name='Use')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CoefficientSets', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Coefficients_ in self.Coefficients:
            namespaceprefix_ = self.Coefficients_nsprefix_ + ':' if (UseCapturedNS_ and self.Coefficients_nsprefix_) else ''
            Coefficients_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Coefficients', pretty_print=pretty_print)
        for CoefficientSet_ in self.CoefficientSet:
            namespaceprefix_ = self.CoefficientSet_nsprefix_ + ':' if (UseCapturedNS_ and self.CoefficientSet_nsprefix_) else ''
            CoefficientSet_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CoefficientSet', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='CoefficientSets'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Use is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            showIndent(outfile, level)
            outfile.write('Use="%s",\n' % (self.Use,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Coefficients=[\n')
        level += 1
        for Coefficients_ in self.Coefficients:
            showIndent(outfile, level)
            outfile.write('model_.Coefficients(\n')
            Coefficients_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('CoefficientSet=[\n')
        level += 1
        for CoefficientSet_ in self.CoefficientSet:
            showIndent(outfile, level)
            outfile.write('model_.CoefficientSet(\n')
            CoefficientSet_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        value = find_attr_value_('Use', node)
        if value is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            self.Use = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Coefficients':
            obj_ = Coefficients.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Coefficients.append(obj_)
            obj_.original_tagname_ = 'Coefficients'
        elif nodeName_ == 'CoefficientSet':
            obj_ = CoefficientSet.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CoefficientSet.append(obj_)
            obj_.original_tagname_ = 'CoefficientSet'
# end class CoefficientSets


class Variable(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, Handle=None, SegmentedBy=None, Treatment=None, Source=None, Sources=None, Constant=None, Constants=None, Transformation=None, Transformations=None, CleanLimit=None, LeftLimit=None, RightLimit=None, CleanLimits=None, CleanLimitList=None, CriticalValue=None, CriticalValues=None, CriticalValuesList=None, CriticalWord=None, CriticalWords=None, CriticalWordList=None, DropIndex=None, DropIndexs=None, DropIndexList=None, DropIndices=None, CoefficientSet=None, CoefficientSets=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.Handle = _cast(None, Handle)
        self.Handle_nsprefix_ = None
        self.SegmentedBy = SegmentedBy
        self.SegmentedBy_nsprefix_ = None
        self.Treatment = Treatment
        self.Treatment_nsprefix_ = None
        if Source is None:
            self.Source = []
        else:
            self.Source = Source
        self.Source_nsprefix_ = None
        self.Sources = Sources
        self.Sources_nsprefix_ = None
        if Constant is None:
            self.Constant = []
        else:
            self.Constant = Constant
        self.Constant_nsprefix_ = None
        self.Constants = Constants
        self.Constants_nsprefix_ = None
        if Transformation is None:
            self.Transformation = []
        else:
            self.Transformation = Transformation
        self.Transformation_nsprefix_ = None
        self.Transformations = Transformations
        self.Transformations_nsprefix_ = None
        if CleanLimit is None:
            self.CleanLimit = []
        else:
            self.CleanLimit = CleanLimit
        self.CleanLimit_nsprefix_ = None
        self.LeftLimit = LeftLimit
        self.LeftLimit_nsprefix_ = None
        self.RightLimit = RightLimit
        self.RightLimit_nsprefix_ = None
        self.CleanLimits = CleanLimits
        self.CleanLimits_nsprefix_ = None
        self.CleanLimitList = CleanLimitList
        self.CleanLimitList_nsprefix_ = None
        if CriticalValue is None:
            self.CriticalValue = []
        else:
            self.CriticalValue = CriticalValue
        self.CriticalValue_nsprefix_ = None
        self.CriticalValues = CriticalValues
        self.CriticalValues_nsprefix_ = None
        self.CriticalValuesList = CriticalValuesList
        self.CriticalValuesList_nsprefix_ = None
        if CriticalWord is None:
            self.CriticalWord = []
        else:
            self.CriticalWord = CriticalWord
        self.CriticalWord_nsprefix_ = None
        self.CriticalWords = CriticalWords
        self.CriticalWords_nsprefix_ = None
        self.CriticalWordList = CriticalWordList
        self.CriticalWordList_nsprefix_ = None
        if DropIndex is None:
            self.DropIndex = []
        else:
            self.DropIndex = DropIndex
        self.DropIndex_nsprefix_ = None
        self.DropIndexs = DropIndexs
        self.DropIndexs_nsprefix_ = None
        self.DropIndexList = DropIndexList
        self.DropIndexList_nsprefix_ = None
        self.DropIndices = DropIndices
        self.DropIndices_nsprefix_ = None
        if CoefficientSet is None:
            self.CoefficientSet = []
        else:
            self.CoefficientSet = CoefficientSet
        self.CoefficientSet_nsprefix_ = None
        self.CoefficientSets = CoefficientSets
        self.CoefficientSets_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Variable)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Variable.subclass:
            return Variable.subclass(*args_, **kwargs_)
        else:
            return Variable(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SegmentedBy(self):
        return self.SegmentedBy
    def set_SegmentedBy(self, SegmentedBy):
        self.SegmentedBy = SegmentedBy
    def get_Treatment(self):
        return self.Treatment
    def set_Treatment(self, Treatment):
        self.Treatment = Treatment
    def get_Source(self):
        return self.Source
    def set_Source(self, Source):
        self.Source = Source
    def add_Source(self, value):
        self.Source.append(value)
    def insert_Source_at(self, index, value):
        self.Source.insert(index, value)
    def replace_Source_at(self, index, value):
        self.Source[index] = value
    def get_Sources(self):
        return self.Sources
    def set_Sources(self, Sources):
        self.Sources = Sources
    def get_Constant(self):
        return self.Constant
    def set_Constant(self, Constant):
        self.Constant = Constant
    def add_Constant(self, value):
        self.Constant.append(value)
    def insert_Constant_at(self, index, value):
        self.Constant.insert(index, value)
    def replace_Constant_at(self, index, value):
        self.Constant[index] = value
    def get_Constants(self):
        return self.Constants
    def set_Constants(self, Constants):
        self.Constants = Constants
    def get_Transformation(self):
        return self.Transformation
    def set_Transformation(self, Transformation):
        self.Transformation = Transformation
    def add_Transformation(self, value):
        self.Transformation.append(value)
    def insert_Transformation_at(self, index, value):
        self.Transformation.insert(index, value)
    def replace_Transformation_at(self, index, value):
        self.Transformation[index] = value
    def get_Transformations(self):
        return self.Transformations
    def set_Transformations(self, Transformations):
        self.Transformations = Transformations
    def get_CleanLimit(self):
        return self.CleanLimit
    def set_CleanLimit(self, CleanLimit):
        self.CleanLimit = CleanLimit
    def add_CleanLimit(self, value):
        self.CleanLimit.append(value)
    def insert_CleanLimit_at(self, index, value):
        self.CleanLimit.insert(index, value)
    def replace_CleanLimit_at(self, index, value):
        self.CleanLimit[index] = value
    def get_LeftLimit(self):
        return self.LeftLimit
    def set_LeftLimit(self, LeftLimit):
        self.LeftLimit = LeftLimit
    def get_RightLimit(self):
        return self.RightLimit
    def set_RightLimit(self, RightLimit):
        self.RightLimit = RightLimit
    def get_CleanLimits(self):
        return self.CleanLimits
    def set_CleanLimits(self, CleanLimits):
        self.CleanLimits = CleanLimits
    def get_CleanLimitList(self):
        return self.CleanLimitList
    def set_CleanLimitList(self, CleanLimitList):
        self.CleanLimitList = CleanLimitList
    def get_CriticalValue(self):
        return self.CriticalValue
    def set_CriticalValue(self, CriticalValue):
        self.CriticalValue = CriticalValue
    def add_CriticalValue(self, value):
        self.CriticalValue.append(value)
    def insert_CriticalValue_at(self, index, value):
        self.CriticalValue.insert(index, value)
    def replace_CriticalValue_at(self, index, value):
        self.CriticalValue[index] = value
    def get_CriticalValues(self):
        return self.CriticalValues
    def set_CriticalValues(self, CriticalValues):
        self.CriticalValues = CriticalValues
    def get_CriticalValuesList(self):
        return self.CriticalValuesList
    def set_CriticalValuesList(self, CriticalValuesList):
        self.CriticalValuesList = CriticalValuesList
    def get_CriticalWord(self):
        return self.CriticalWord
    def set_CriticalWord(self, CriticalWord):
        self.CriticalWord = CriticalWord
    def add_CriticalWord(self, value):
        self.CriticalWord.append(value)
    def insert_CriticalWord_at(self, index, value):
        self.CriticalWord.insert(index, value)
    def replace_CriticalWord_at(self, index, value):
        self.CriticalWord[index] = value
    def get_CriticalWords(self):
        return self.CriticalWords
    def set_CriticalWords(self, CriticalWords):
        self.CriticalWords = CriticalWords
    def get_CriticalWordList(self):
        return self.CriticalWordList
    def set_CriticalWordList(self, CriticalWordList):
        self.CriticalWordList = CriticalWordList
    def get_DropIndex(self):
        return self.DropIndex
    def set_DropIndex(self, DropIndex):
        self.DropIndex = DropIndex
    def add_DropIndex(self, value):
        self.DropIndex.append(value)
    def insert_DropIndex_at(self, index, value):
        self.DropIndex.insert(index, value)
    def replace_DropIndex_at(self, index, value):
        self.DropIndex[index] = value
    def get_DropIndexs(self):
        return self.DropIndexs
    def set_DropIndexs(self, DropIndexs):
        self.DropIndexs = DropIndexs
    def get_DropIndexList(self):
        return self.DropIndexList
    def set_DropIndexList(self, DropIndexList):
        self.DropIndexList = DropIndexList
    def get_DropIndices(self):
        return self.DropIndices
    def set_DropIndices(self, DropIndices):
        self.DropIndices = DropIndices
    def get_CoefficientSet(self):
        return self.CoefficientSet
    def set_CoefficientSet(self, CoefficientSet):
        self.CoefficientSet = CoefficientSet
    def add_CoefficientSet(self, value):
        self.CoefficientSet.append(value)
    def insert_CoefficientSet_at(self, index, value):
        self.CoefficientSet.insert(index, value)
    def replace_CoefficientSet_at(self, index, value):
        self.CoefficientSet[index] = value
    def get_CoefficientSets(self):
        return self.CoefficientSets
    def set_CoefficientSets(self, CoefficientSets):
        self.CoefficientSets = CoefficientSets
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
            self.SegmentedBy is not None or
            self.Treatment is not None or
            self.Source or
            self.Sources is not None or
            self.Constant or
            self.Constants is not None or
            self.Transformation or
            self.Transformations is not None or
            self.CleanLimit or
            self.LeftLimit is not None or
            self.RightLimit is not None or
            self.CleanLimits is not None or
            self.CleanLimitList is not None or
            self.CriticalValue or
            self.CriticalValues is not None or
            self.CriticalValuesList is not None or
            self.CriticalWord or
            self.CriticalWords is not None or
            self.CriticalWordList is not None or
            self.DropIndex or
            self.DropIndexs is not None or
            self.DropIndexList is not None or
            self.DropIndices is not None or
            self.CoefficientSet or
            self.CoefficientSets is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Variable', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Variable')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Variable':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Variable')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Variable', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Variable'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            outfile.write(' Handle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Handle), input_name='Handle')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Variable', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SegmentedBy is not None:
            namespaceprefix_ = self.SegmentedBy_nsprefix_ + ':' if (UseCapturedNS_ and self.SegmentedBy_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSegmentedBy>%s</%sSegmentedBy>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SegmentedBy), input_name='SegmentedBy')), namespaceprefix_ , eol_))
        if self.Treatment is not None:
            namespaceprefix_ = self.Treatment_nsprefix_ + ':' if (UseCapturedNS_ and self.Treatment_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTreatment>%s</%sTreatment>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Treatment), input_name='Treatment')), namespaceprefix_ , eol_))
        for Source_ in self.Source:
            namespaceprefix_ = self.Source_nsprefix_ + ':' if (UseCapturedNS_ and self.Source_nsprefix_) else ''
            Source_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Source', pretty_print=pretty_print)
        if self.Sources is not None:
            namespaceprefix_ = self.Sources_nsprefix_ + ':' if (UseCapturedNS_ and self.Sources_nsprefix_) else ''
            self.Sources.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Sources', pretty_print=pretty_print)
        for Constant_ in self.Constant:
            namespaceprefix_ = self.Constant_nsprefix_ + ':' if (UseCapturedNS_ and self.Constant_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sConstant>%s</%sConstant>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(Constant_), input_name='Constant')), namespaceprefix_ , eol_))
        if self.Constants is not None:
            namespaceprefix_ = self.Constants_nsprefix_ + ':' if (UseCapturedNS_ and self.Constants_nsprefix_) else ''
            self.Constants.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Constants', pretty_print=pretty_print)
        for Transformation_ in self.Transformation:
            namespaceprefix_ = self.Transformation_nsprefix_ + ':' if (UseCapturedNS_ and self.Transformation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTransformation>%s</%sTransformation>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(Transformation_), input_name='Transformation')), namespaceprefix_ , eol_))
        if self.Transformations is not None:
            namespaceprefix_ = self.Transformations_nsprefix_ + ':' if (UseCapturedNS_ and self.Transformations_nsprefix_) else ''
            self.Transformations.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Transformations', pretty_print=pretty_print)
        for CleanLimit_ in self.CleanLimit:
            namespaceprefix_ = self.CleanLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.CleanLimit_nsprefix_) else ''
            CleanLimit_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CleanLimit', pretty_print=pretty_print)
        if self.LeftLimit is not None:
            namespaceprefix_ = self.LeftLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.LeftLimit_nsprefix_) else ''
            self.LeftLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='LeftLimit', pretty_print=pretty_print)
        if self.RightLimit is not None:
            namespaceprefix_ = self.RightLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.RightLimit_nsprefix_) else ''
            self.RightLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RightLimit', pretty_print=pretty_print)
        if self.CleanLimits is not None:
            namespaceprefix_ = self.CleanLimits_nsprefix_ + ':' if (UseCapturedNS_ and self.CleanLimits_nsprefix_) else ''
            self.CleanLimits.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CleanLimits', pretty_print=pretty_print)
        if self.CleanLimitList is not None:
            namespaceprefix_ = self.CleanLimitList_nsprefix_ + ':' if (UseCapturedNS_ and self.CleanLimitList_nsprefix_) else ''
            self.CleanLimitList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CleanLimitList', pretty_print=pretty_print)
        for CriticalValue_ in self.CriticalValue:
            namespaceprefix_ = self.CriticalValue_nsprefix_ + ':' if (UseCapturedNS_ and self.CriticalValue_nsprefix_) else ''
            CriticalValue_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CriticalValue', pretty_print=pretty_print)
        if self.CriticalValues is not None:
            namespaceprefix_ = self.CriticalValues_nsprefix_ + ':' if (UseCapturedNS_ and self.CriticalValues_nsprefix_) else ''
            self.CriticalValues.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CriticalValues', pretty_print=pretty_print)
        if self.CriticalValuesList is not None:
            namespaceprefix_ = self.CriticalValuesList_nsprefix_ + ':' if (UseCapturedNS_ and self.CriticalValuesList_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCriticalValuesList>%s</%sCriticalValuesList>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CriticalValuesList), input_name='CriticalValuesList')), namespaceprefix_ , eol_))
        for CriticalWord_ in self.CriticalWord:
            namespaceprefix_ = self.CriticalWord_nsprefix_ + ':' if (UseCapturedNS_ and self.CriticalWord_nsprefix_) else ''
            CriticalWord_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CriticalWord', pretty_print=pretty_print)
        if self.CriticalWords is not None:
            namespaceprefix_ = self.CriticalWords_nsprefix_ + ':' if (UseCapturedNS_ and self.CriticalWords_nsprefix_) else ''
            self.CriticalWords.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CriticalWords', pretty_print=pretty_print)
        if self.CriticalWordList is not None:
            namespaceprefix_ = self.CriticalWordList_nsprefix_ + ':' if (UseCapturedNS_ and self.CriticalWordList_nsprefix_) else ''
            self.CriticalWordList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CriticalWordList', pretty_print=pretty_print)
        for DropIndex_ in self.DropIndex:
            namespaceprefix_ = self.DropIndex_nsprefix_ + ':' if (UseCapturedNS_ and self.DropIndex_nsprefix_) else ''
            DropIndex_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DropIndex', pretty_print=pretty_print)
        if self.DropIndexs is not None:
            namespaceprefix_ = self.DropIndexs_nsprefix_ + ':' if (UseCapturedNS_ and self.DropIndexs_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDropIndexs>%s</%sDropIndexs>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DropIndexs), input_name='DropIndexs')), namespaceprefix_ , eol_))
        if self.DropIndexList is not None:
            namespaceprefix_ = self.DropIndexList_nsprefix_ + ':' if (UseCapturedNS_ and self.DropIndexList_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDropIndexList>%s</%sDropIndexList>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DropIndexList), input_name='DropIndexList')), namespaceprefix_ , eol_))
        if self.DropIndices is not None:
            namespaceprefix_ = self.DropIndices_nsprefix_ + ':' if (UseCapturedNS_ and self.DropIndices_nsprefix_) else ''
            self.DropIndices.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DropIndices', pretty_print=pretty_print)
        for CoefficientSet_ in self.CoefficientSet:
            namespaceprefix_ = self.CoefficientSet_nsprefix_ + ':' if (UseCapturedNS_ and self.CoefficientSet_nsprefix_) else ''
            CoefficientSet_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CoefficientSet', pretty_print=pretty_print)
        if self.CoefficientSets is not None:
            namespaceprefix_ = self.CoefficientSets_nsprefix_ + ':' if (UseCapturedNS_ and self.CoefficientSets_nsprefix_) else ''
            self.CoefficientSets.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CoefficientSets', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='Variable'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
        if self.Handle is not None and 'Handle' not in already_processed:
            already_processed.add('Handle')
            showIndent(outfile, level)
            outfile.write('Handle="%s",\n' % (self.Handle,))
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.SegmentedBy is not None:
            showIndent(outfile, level)
            outfile.write('SegmentedBy=%s,\n' % self.gds_encode(quote_python(self.SegmentedBy)))
        if self.Treatment is not None:
            showIndent(outfile, level)
            outfile.write('Treatment=%s,\n' % self.gds_encode(quote_python(self.Treatment)))
        showIndent(outfile, level)
        outfile.write('Source=[\n')
        level += 1
        for Source_ in self.Source:
            showIndent(outfile, level)
            outfile.write('model_.Source(\n')
            Source_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Sources is not None:
            showIndent(outfile, level)
            outfile.write('Sources=model_.Sources(\n')
            self.Sources.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Constant=[\n')
        level += 1
        for Constant_ in self.Constant:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(Constant_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Constants is not None:
            showIndent(outfile, level)
            outfile.write('Constants=model_.Constants(\n')
            self.Constants.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Transformation=[\n')
        level += 1
        for Transformation_ in self.Transformation:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(Transformation_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Transformations is not None:
            showIndent(outfile, level)
            outfile.write('Transformations=model_.Transformations(\n')
            self.Transformations.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('CleanLimit=[\n')
        level += 1
        for CleanLimit_ in self.CleanLimit:
            showIndent(outfile, level)
            outfile.write('model_.CleanLimit(\n')
            CleanLimit_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.LeftLimit is not None:
            showIndent(outfile, level)
            outfile.write('LeftLimit=model_.LeftLimit(\n')
            self.LeftLimit.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.RightLimit is not None:
            showIndent(outfile, level)
            outfile.write('RightLimit=model_.RightLimit(\n')
            self.RightLimit.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.CleanLimits is not None:
            showIndent(outfile, level)
            outfile.write('CleanLimits=model_.CleanLimits(\n')
            self.CleanLimits.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.CleanLimitList is not None:
            showIndent(outfile, level)
            outfile.write('CleanLimitList=model_.CleanLimitList(\n')
            self.CleanLimitList.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('CriticalValue=[\n')
        level += 1
        for CriticalValue_ in self.CriticalValue:
            showIndent(outfile, level)
            outfile.write('model_.CriticalValue(\n')
            CriticalValue_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.CriticalValues is not None:
            showIndent(outfile, level)
            outfile.write('CriticalValues=model_.CriticalValues(\n')
            self.CriticalValues.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.CriticalValuesList is not None:
            showIndent(outfile, level)
            outfile.write('CriticalValuesList=%s,\n' % self.gds_encode(quote_python(self.CriticalValuesList)))
        showIndent(outfile, level)
        outfile.write('CriticalWord=[\n')
        level += 1
        for CriticalWord_ in self.CriticalWord:
            showIndent(outfile, level)
            outfile.write('model_.CriticalWord(\n')
            CriticalWord_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.CriticalWords is not None:
            showIndent(outfile, level)
            outfile.write('CriticalWords=model_.CriticalWords(\n')
            self.CriticalWords.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.CriticalWordList is not None:
            showIndent(outfile, level)
            outfile.write('CriticalWordList=model_.CriticalWordList(\n')
            self.CriticalWordList.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('DropIndex=[\n')
        level += 1
        for DropIndex_ in self.DropIndex:
            showIndent(outfile, level)
            outfile.write('model_.DropIndex(\n')
            DropIndex_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.DropIndexs is not None:
            showIndent(outfile, level)
            outfile.write('DropIndexs=%s,\n' % self.gds_encode(quote_python(self.DropIndexs)))
        if self.DropIndexList is not None:
            showIndent(outfile, level)
            outfile.write('DropIndexList=%s,\n' % self.gds_encode(quote_python(self.DropIndexList)))
        if self.DropIndices is not None:
            showIndent(outfile, level)
            outfile.write('DropIndices=model_.DropIndices(\n')
            self.DropIndices.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('CoefficientSet=[\n')
        level += 1
        for CoefficientSet_ in self.CoefficientSet:
            showIndent(outfile, level)
            outfile.write('model_.CoefficientSet(\n')
            CoefficientSet_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.CoefficientSets is not None:
            showIndent(outfile, level)
            outfile.write('CoefficientSets=model_.CoefficientSets(\n')
            self.CoefficientSets.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
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
        if nodeName_ == 'SegmentedBy':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SegmentedBy')
            value_ = self.gds_validate_string(value_, node, 'SegmentedBy')
            self.SegmentedBy = value_
            self.SegmentedBy_nsprefix_ = child_.prefix
        elif nodeName_ == 'Treatment':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Treatment')
            value_ = self.gds_validate_string(value_, node, 'Treatment')
            self.Treatment = value_
            self.Treatment_nsprefix_ = child_.prefix
        elif nodeName_ == 'Source':
            obj_ = Source.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Source.append(obj_)
            obj_.original_tagname_ = 'Source'
        elif nodeName_ == 'Sources':
            obj_ = Sources.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Sources = obj_
            obj_.original_tagname_ = 'Sources'
        elif nodeName_ == 'Constant':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Constant')
            value_ = self.gds_validate_string(value_, node, 'Constant')
            self.Constant.append(value_)
            self.Constant_nsprefix_ = child_.prefix
        elif nodeName_ == 'Constants':
            obj_ = Constants.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Constants = obj_
            obj_.original_tagname_ = 'Constants'
        elif nodeName_ == 'Transformation':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Transformation')
            value_ = self.gds_validate_string(value_, node, 'Transformation')
            self.Transformation.append(value_)
            self.Transformation_nsprefix_ = child_.prefix
        elif nodeName_ == 'Transformations':
            obj_ = Transformations.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transformations = obj_
            obj_.original_tagname_ = 'Transformations'
        elif nodeName_ == 'CleanLimit':
            obj_ = CleanLimit.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CleanLimit.append(obj_)
            obj_.original_tagname_ = 'CleanLimit'
        elif nodeName_ == 'LeftLimit':
            obj_ = LeftLimit.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.LeftLimit = obj_
            obj_.original_tagname_ = 'LeftLimit'
        elif nodeName_ == 'RightLimit':
            obj_ = RightLimit.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RightLimit = obj_
            obj_.original_tagname_ = 'RightLimit'
        elif nodeName_ == 'CleanLimits':
            obj_ = CleanLimits.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CleanLimits = obj_
            obj_.original_tagname_ = 'CleanLimits'
        elif nodeName_ == 'CleanLimitList':
            obj_ = CleanLimitList.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CleanLimitList = obj_
            obj_.original_tagname_ = 'CleanLimitList'
        elif nodeName_ == 'CriticalValue':
            obj_ = CriticalValue.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CriticalValue.append(obj_)
            obj_.original_tagname_ = 'CriticalValue'
        elif nodeName_ == 'CriticalValues':
            obj_ = CriticalValues.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CriticalValues = obj_
            obj_.original_tagname_ = 'CriticalValues'
        elif nodeName_ == 'CriticalValuesList':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CriticalValuesList')
            value_ = self.gds_validate_string(value_, node, 'CriticalValuesList')
            self.CriticalValuesList = value_
            self.CriticalValuesList_nsprefix_ = child_.prefix
        elif nodeName_ == 'CriticalWord':
            obj_ = CriticalWord.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CriticalWord.append(obj_)
            obj_.original_tagname_ = 'CriticalWord'
        elif nodeName_ == 'CriticalWords':
            obj_ = CriticalWords.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CriticalWords = obj_
            obj_.original_tagname_ = 'CriticalWords'
        elif nodeName_ == 'CriticalWordList':
            obj_ = CriticalWordList.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CriticalWordList = obj_
            obj_.original_tagname_ = 'CriticalWordList'
        elif nodeName_ == 'DropIndex':
            obj_ = Int.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DropIndex.append(obj_)
            obj_.original_tagname_ = 'DropIndex'
        elif nodeName_ == 'DropIndexs':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DropIndexs')
            value_ = self.gds_validate_string(value_, node, 'DropIndexs')
            self.DropIndexs = value_
            self.DropIndexs_nsprefix_ = child_.prefix
        elif nodeName_ == 'DropIndexList':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DropIndexList')
            value_ = self.gds_validate_string(value_, node, 'DropIndexList')
            self.DropIndexList = value_
            self.DropIndexList_nsprefix_ = child_.prefix
        elif nodeName_ == 'DropIndices':
            obj_ = DropIndices.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DropIndices = obj_
            obj_.original_tagname_ = 'DropIndices'
        elif nodeName_ == 'CoefficientSet':
            obj_ = CoefficientSet.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CoefficientSet.append(obj_)
            obj_.original_tagname_ = 'CoefficientSet'
        elif nodeName_ == 'CoefficientSets':
            obj_ = CoefficientSets.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CoefficientSets = obj_
            obj_.original_tagname_ = 'CoefficientSets'
# end class Variable


class Int(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Int)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Int.subclass:
            return Int.subclass(*args_, **kwargs_)
        else:
            return Int(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_Int_impl(self, value):
        result = True
        # Validate type Int_impl, a restriction on None.
        pass
        return result
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Int', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Int')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Int':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Int')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Int', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Int'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='Int', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='Int'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Int


class DblList(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, valueOf_=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.valueOf_ = valueOf_
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DblList)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DblList.subclass:
            return DblList.subclass(*args_, **kwargs_)
        else:
            return DblList(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def validate_DblList_impl(self, value):
        result = True
        # Validate type DblList_impl, a restriction on xs:double.
        pass
        return result
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='DblList', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DblList')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DblList':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DblList')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DblList', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DblList'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='DblList', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='DblList'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DblList


class AppInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Use=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Use = _cast(None, Use)
        self.Use_nsprefix_ = None
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AppInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AppInfoType.subclass:
            return AppInfoType.subclass(*args_, **kwargs_)
        else:
            return AppInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Use(self):
        return self.Use
    def set_Use(self, Use):
        self.Use = Use
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='AppInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AppInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AppInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AppInfoType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AppInfoType'):
        if self.Use is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            outfile.write(' Use=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Use), input_name='Use')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='AppInfoType', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='AppInfoType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Use is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            showIndent(outfile, level)
            outfile.write('Use="%s",\n' % (self.Use,))
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Use', node)
        if value is not None and 'Use' not in already_processed:
            already_processed.add('Use')
            self.Use = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        pass
# end class AppInfoType


class EnumMDType(GeneratedsSuper):
    """EnumMDType --
    The EnumMD is the unordered collection of EnumAttrMD elements for the EnumValue elements.
    Specification of EnumMD beside the EnumValues collection is for programmatic purposes of generating additional methods linked to the enum values.
    This is to balance the needs of enum code in C++/C#/Java/Python/ect where it may or may not be natural to extend a basic enum class.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, EnumAttrMD=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if EnumAttrMD is None:
            self.EnumAttrMD = []
        else:
            self.EnumAttrMD = EnumAttrMD
        self.EnumAttrMD_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EnumMDType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EnumMDType.subclass:
            return EnumMDType.subclass(*args_, **kwargs_)
        else:
            return EnumMDType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_EnumAttrMD(self):
        return self.EnumAttrMD
    def set_EnumAttrMD(self, EnumAttrMD):
        self.EnumAttrMD = EnumAttrMD
    def add_EnumAttrMD(self, value):
        self.EnumAttrMD.append(value)
    def insert_EnumAttrMD_at(self, index, value):
        self.EnumAttrMD.insert(index, value)
    def replace_EnumAttrMD_at(self, index, value):
        self.EnumAttrMD[index] = value
    def _hasContent(self):
        if (
            self.EnumAttrMD
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='EnumMDType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EnumMDType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EnumMDType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EnumMDType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EnumMDType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EnumMDType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='EnumMDType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for EnumAttrMD_ in self.EnumAttrMD:
            namespaceprefix_ = self.EnumAttrMD_nsprefix_ + ':' if (UseCapturedNS_ and self.EnumAttrMD_nsprefix_) else ''
            EnumAttrMD_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EnumAttrMD', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='EnumMDType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('EnumAttrMD=[\n')
        level += 1
        for EnumAttrMD_ in self.EnumAttrMD:
            showIndent(outfile, level)
            outfile.write('model_.EnumAttrMDType(\n')
            EnumAttrMD_.exportLiteral(outfile, level, name_='EnumAttrMDType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'EnumAttrMD':
            obj_ = EnumAttrMDType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EnumAttrMD.append(obj_)
            obj_.original_tagname_ = 'EnumAttrMD'
# end class EnumMDType


class EnumAttrMDType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, DTyp=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.DTyp = _cast(None, DTyp)
        self.DTyp_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EnumAttrMDType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EnumAttrMDType.subclass:
            return EnumAttrMDType.subclass(*args_, **kwargs_)
        else:
            return EnumAttrMDType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def get_DTyp(self):
        return self.DTyp
    def set_DTyp(self, DTyp):
        self.DTyp = DTyp
    def validate_DTypType(self, value):
        # Validate type DTypType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Unk', 'Dbl', 'Lng', 'Int', 'Dte', 'DTm', 'Str', 'VLS', 'Byt', 'Bln', 'Any']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on DTypType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='EnumAttrMDType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EnumAttrMDType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EnumAttrMDType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EnumAttrMDType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EnumAttrMDType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EnumAttrMDType'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
        if self.DTyp is not None and 'DTyp' not in already_processed:
            already_processed.add('DTyp')
            outfile.write(' DTyp=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.DTyp), input_name='DTyp')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='EnumAttrMDType', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='EnumAttrMDType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
        if self.DTyp is not None and 'DTyp' not in already_processed:
            already_processed.add('DTyp')
            showIndent(outfile, level)
            outfile.write('DTyp="%s",\n' % (self.DTyp,))
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
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
        value = find_attr_value_('DTyp', node)
        if value is not None and 'DTyp' not in already_processed:
            already_processed.add('DTyp')
            self.DTyp = value
            self.validate_DTypType(self.DTyp)    # validate type DTypType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class EnumAttrMDType


class PythonType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, depends=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.depends = depends
        self.depends_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PythonType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PythonType.subclass:
            return PythonType.subclass(*args_, **kwargs_)
        else:
            return PythonType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_depends(self):
        return self.depends
    def set_depends(self, depends):
        self.depends = depends
    def _hasContent(self):
        if (
            self.depends is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='PythonType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PythonType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PythonType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PythonType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PythonType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PythonType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='PythonType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.depends is not None:
            namespaceprefix_ = self.depends_nsprefix_ + ':' if (UseCapturedNS_ and self.depends_nsprefix_) else ''
            self.depends.export(outfile, level, namespaceprefix_, namespacedef_='', name_='depends', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='PythonType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.depends is not None:
            showIndent(outfile, level)
            outfile.write('depends=model_.dependsType(\n')
            self.depends.exportLiteral(outfile, level, name_='depends')
            showIndent(outfile, level)
            outfile.write('),\n')
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
        if nodeName_ == 'depends':
            obj_ = dependsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.depends = obj_
            obj_.original_tagname_ = 'depends'
# end class PythonType


class dependsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, depend=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if depend is None:
            self.depend = []
        else:
            self.depend = depend
        self.depend_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dependsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dependsType.subclass:
            return dependsType.subclass(*args_, **kwargs_)
        else:
            return dependsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_depend(self):
        return self.depend
    def set_depend(self, depend):
        self.depend = depend
    def add_depend(self, value):
        self.depend.append(value)
    def insert_depend_at(self, index, value):
        self.depend.insert(index, value)
    def replace_depend_at(self, index, value):
        self.depend[index] = value
    def _hasContent(self):
        if (
            self.depend
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='dependsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dependsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dependsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dependsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dependsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dependsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='dependsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for depend_ in self.depend:
            namespaceprefix_ = self.depend_nsprefix_ + ':' if (UseCapturedNS_ and self.depend_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdepend>%s</%sdepend>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(depend_), input_name='depend')), namespaceprefix_ , eol_))
    def exportLiteral(self, outfile, level, name_='dependsType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('depend=[\n')
        level += 1
        for depend_ in self.depend:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(depend_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'depend':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'depend')
            value_ = self.gds_validate_string(value_, node, 'depend')
            self.depend.append(value_)
            self.depend_nsprefix_ = child_.prefix
# end class dependsType


class SQLType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Vertica=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Vertica = Vertica
        self.Vertica_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SQLType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SQLType.subclass:
            return SQLType.subclass(*args_, **kwargs_)
        else:
            return SQLType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Vertica(self):
        return self.Vertica
    def set_Vertica(self, Vertica):
        self.Vertica = Vertica
    def _hasContent(self):
        if (
            self.Vertica is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='SQLType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SQLType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SQLType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SQLType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SQLType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SQLType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='SQLType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Vertica is not None:
            namespaceprefix_ = self.Vertica_nsprefix_ + ':' if (UseCapturedNS_ and self.Vertica_nsprefix_) else ''
            self.Vertica.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Vertica', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='SQLType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.Vertica is not None:
            showIndent(outfile, level)
            outfile.write('Vertica=model_.VerticaType(\n')
            self.Vertica.exportLiteral(outfile, level, name_='Vertica')
            showIndent(outfile, level)
            outfile.write('),\n')
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
        if nodeName_ == 'Vertica':
            obj_ = VerticaType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Vertica = obj_
            obj_.original_tagname_ = 'Vertica'
# end class SQLType


class VerticaType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Schema=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Schema = _cast(None, Schema)
        self.Schema_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VerticaType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VerticaType.subclass:
            return VerticaType.subclass(*args_, **kwargs_)
        else:
            return VerticaType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Schema(self):
        return self.Schema
    def set_Schema(self, Schema):
        self.Schema = Schema
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='VerticaType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VerticaType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VerticaType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VerticaType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VerticaType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VerticaType'):
        if self.Schema is not None and 'Schema' not in already_processed:
            already_processed.add('Schema')
            outfile.write(' Schema=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Schema), input_name='Schema')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='VerticaType', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='VerticaType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Schema is not None and 'Schema' not in already_processed:
            already_processed.add('Schema')
            showIndent(outfile, level)
            outfile.write('Schema="%s",\n' % (self.Schema,))
    def _exportLiteralChildren(self, outfile, level, name_):
        pass
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
        value = find_attr_value_('Schema', node)
        if value is not None and 'Schema' not in already_processed:
            already_processed.add('Schema')
            self.Schema = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class VerticaType


class UDFType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, UDxInfo=None, Parameters=None, Columns=None, Enums=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        if UDxInfo is None:
            self.UDxInfo = []
        else:
            self.UDxInfo = UDxInfo
        self.UDxInfo_nsprefix_ = None
        if Parameters is None:
            self.Parameters = []
        else:
            self.Parameters = Parameters
        self.Parameters_nsprefix_ = None
        if Columns is None:
            self.Columns = []
        else:
            self.Columns = Columns
        self.Columns_nsprefix_ = None
        if Enums is None:
            self.Enums = []
        else:
            self.Enums = Enums
        self.Enums_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, UDFType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if UDFType.subclass:
            return UDFType.subclass(*args_, **kwargs_)
        else:
            return UDFType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_UDxInfo(self):
        return self.UDxInfo
    def set_UDxInfo(self, UDxInfo):
        self.UDxInfo = UDxInfo
    def add_UDxInfo(self, value):
        self.UDxInfo.append(value)
    def insert_UDxInfo_at(self, index, value):
        self.UDxInfo.insert(index, value)
    def replace_UDxInfo_at(self, index, value):
        self.UDxInfo[index] = value
    def get_Parameters(self):
        return self.Parameters
    def set_Parameters(self, Parameters):
        self.Parameters = Parameters
    def add_Parameters(self, value):
        self.Parameters.append(value)
    def insert_Parameters_at(self, index, value):
        self.Parameters.insert(index, value)
    def replace_Parameters_at(self, index, value):
        self.Parameters[index] = value
    def get_Columns(self):
        return self.Columns
    def set_Columns(self, Columns):
        self.Columns = Columns
    def add_Columns(self, value):
        self.Columns.append(value)
    def insert_Columns_at(self, index, value):
        self.Columns.insert(index, value)
    def replace_Columns_at(self, index, value):
        self.Columns[index] = value
    def get_Enums(self):
        return self.Enums
    def set_Enums(self, Enums):
        self.Enums = Enums
    def add_Enums(self, value):
        self.Enums.append(value)
    def insert_Enums_at(self, index, value):
        self.Enums.insert(index, value)
    def replace_Enums_at(self, index, value):
        self.Enums[index] = value
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def _hasContent(self):
        if (
            self.UDxInfo or
            self.Parameters or
            self.Columns or
            self.Enums
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='UDFType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('UDFType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'UDFType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='UDFType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='UDFType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='UDFType'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='UDFType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for UDxInfo_ in self.UDxInfo:
            namespaceprefix_ = self.UDxInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.UDxInfo_nsprefix_) else ''
            UDxInfo_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UDxInfo', pretty_print=pretty_print)
        for Parameters_ in self.Parameters:
            namespaceprefix_ = self.Parameters_nsprefix_ + ':' if (UseCapturedNS_ and self.Parameters_nsprefix_) else ''
            Parameters_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Parameters', pretty_print=pretty_print)
        for Columns_ in self.Columns:
            namespaceprefix_ = self.Columns_nsprefix_ + ':' if (UseCapturedNS_ and self.Columns_nsprefix_) else ''
            Columns_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Columns', pretty_print=pretty_print)
        for Enums_ in self.Enums:
            namespaceprefix_ = self.Enums_nsprefix_ + ':' if (UseCapturedNS_ and self.Enums_nsprefix_) else ''
            Enums_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Enums', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='UDFType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('UDxInfo=[\n')
        level += 1
        for UDxInfo_ in self.UDxInfo:
            showIndent(outfile, level)
            outfile.write('model_.UDxInfo(\n')
            UDxInfo_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('Parameters=[\n')
        level += 1
        for Parameters_ in self.Parameters:
            showIndent(outfile, level)
            outfile.write('model_.Parameters(\n')
            Parameters_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('Columns=[\n')
        level += 1
        for Columns_ in self.Columns:
            showIndent(outfile, level)
            outfile.write('model_.Columns(\n')
            Columns_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('Enums=[\n')
        level += 1
        for Enums_ in self.Enums:
            showIndent(outfile, level)
            outfile.write('model_.Enums(\n')
            Enums_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'UDxInfo':
            obj_ = UDxInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UDxInfo.append(obj_)
            obj_.original_tagname_ = 'UDxInfo'
        elif nodeName_ == 'Parameters':
            obj_ = Parameters.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Parameters.append(obj_)
            obj_.original_tagname_ = 'Parameters'
        elif nodeName_ == 'Columns':
            obj_ = Columns.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Columns.append(obj_)
            obj_.original_tagname_ = 'Columns'
        elif nodeName_ == 'Enums':
            obj_ = Enums.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Enums.append(obj_)
            obj_.original_tagname_ = 'Enums'
# end class UDFType


class UDTFType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, UDxInfo=None, Parameters=None, Columns=None, Enums=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        if UDxInfo is None:
            self.UDxInfo = []
        else:
            self.UDxInfo = UDxInfo
        self.UDxInfo_nsprefix_ = None
        if Parameters is None:
            self.Parameters = []
        else:
            self.Parameters = Parameters
        self.Parameters_nsprefix_ = None
        if Columns is None:
            self.Columns = []
        else:
            self.Columns = Columns
        self.Columns_nsprefix_ = None
        if Enums is None:
            self.Enums = []
        else:
            self.Enums = Enums
        self.Enums_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, UDTFType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if UDTFType.subclass:
            return UDTFType.subclass(*args_, **kwargs_)
        else:
            return UDTFType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_UDxInfo(self):
        return self.UDxInfo
    def set_UDxInfo(self, UDxInfo):
        self.UDxInfo = UDxInfo
    def add_UDxInfo(self, value):
        self.UDxInfo.append(value)
    def insert_UDxInfo_at(self, index, value):
        self.UDxInfo.insert(index, value)
    def replace_UDxInfo_at(self, index, value):
        self.UDxInfo[index] = value
    def get_Parameters(self):
        return self.Parameters
    def set_Parameters(self, Parameters):
        self.Parameters = Parameters
    def add_Parameters(self, value):
        self.Parameters.append(value)
    def insert_Parameters_at(self, index, value):
        self.Parameters.insert(index, value)
    def replace_Parameters_at(self, index, value):
        self.Parameters[index] = value
    def get_Columns(self):
        return self.Columns
    def set_Columns(self, Columns):
        self.Columns = Columns
    def add_Columns(self, value):
        self.Columns.append(value)
    def insert_Columns_at(self, index, value):
        self.Columns.insert(index, value)
    def replace_Columns_at(self, index, value):
        self.Columns[index] = value
    def get_Enums(self):
        return self.Enums
    def set_Enums(self, Enums):
        self.Enums = Enums
    def add_Enums(self, value):
        self.Enums.append(value)
    def insert_Enums_at(self, index, value):
        self.Enums.insert(index, value)
    def replace_Enums_at(self, index, value):
        self.Enums[index] = value
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def _hasContent(self):
        if (
            self.UDxInfo or
            self.Parameters or
            self.Columns or
            self.Enums
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='UDTFType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('UDTFType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'UDTFType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='UDTFType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='UDTFType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='UDTFType'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='UDTFType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for UDxInfo_ in self.UDxInfo:
            namespaceprefix_ = self.UDxInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.UDxInfo_nsprefix_) else ''
            UDxInfo_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UDxInfo', pretty_print=pretty_print)
        for Parameters_ in self.Parameters:
            namespaceprefix_ = self.Parameters_nsprefix_ + ':' if (UseCapturedNS_ and self.Parameters_nsprefix_) else ''
            Parameters_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Parameters', pretty_print=pretty_print)
        for Columns_ in self.Columns:
            namespaceprefix_ = self.Columns_nsprefix_ + ':' if (UseCapturedNS_ and self.Columns_nsprefix_) else ''
            Columns_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Columns', pretty_print=pretty_print)
        for Enums_ in self.Enums:
            namespaceprefix_ = self.Enums_nsprefix_ + ':' if (UseCapturedNS_ and self.Enums_nsprefix_) else ''
            Enums_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Enums', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='UDTFType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            showIndent(outfile, level)
            outfile.write('Name="%s",\n' % (self.Name,))
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('UDxInfo=[\n')
        level += 1
        for UDxInfo_ in self.UDxInfo:
            showIndent(outfile, level)
            outfile.write('model_.UDxInfo(\n')
            UDxInfo_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('Parameters=[\n')
        level += 1
        for Parameters_ in self.Parameters:
            showIndent(outfile, level)
            outfile.write('model_.Parameters(\n')
            Parameters_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('Columns=[\n')
        level += 1
        for Columns_ in self.Columns:
            showIndent(outfile, level)
            outfile.write('model_.Columns(\n')
            Columns_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('Enums=[\n')
        level += 1
        for Enums_ in self.Enums:
            showIndent(outfile, level)
            outfile.write('model_.Enums(\n')
            Enums_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'UDxInfo':
            obj_ = UDxInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UDxInfo.append(obj_)
            obj_.original_tagname_ = 'UDxInfo'
        elif nodeName_ == 'Parameters':
            obj_ = Parameters.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Parameters.append(obj_)
            obj_.original_tagname_ = 'Parameters'
        elif nodeName_ == 'Columns':
            obj_ = Columns.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Columns.append(obj_)
            obj_.original_tagname_ = 'Columns'
        elif nodeName_ == 'Enums':
            obj_ = Enums.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Enums.append(obj_)
            obj_.original_tagname_ = 'Enums'
# end class UDTFType


class VersionType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Major=None, Minor=None, Patch=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Major = Major
        self.Major_nsprefix_ = None
        self.Minor = Minor
        self.Minor_nsprefix_ = None
        self.Patch = Patch
        self.Patch_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VersionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VersionType.subclass:
            return VersionType.subclass(*args_, **kwargs_)
        else:
            return VersionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Major(self):
        return self.Major
    def set_Major(self, Major):
        self.Major = Major
    def get_Minor(self):
        return self.Minor
    def set_Minor(self, Minor):
        self.Minor = Minor
    def get_Patch(self):
        return self.Patch
    def set_Patch(self, Patch):
        self.Patch = Patch
    def _hasContent(self):
        if (
            self.Major is not None or
            self.Minor is not None or
            self.Patch is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='VersionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VersionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VersionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VersionType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VersionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VersionType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='VersionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Major is not None:
            namespaceprefix_ = self.Major_nsprefix_ + ':' if (UseCapturedNS_ and self.Major_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMajor>%s</%sMajor>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Major), input_name='Major')), namespaceprefix_ , eol_))
        if self.Minor is not None:
            namespaceprefix_ = self.Minor_nsprefix_ + ':' if (UseCapturedNS_ and self.Minor_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMinor>%s</%sMinor>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Minor), input_name='Minor')), namespaceprefix_ , eol_))
        if self.Patch is not None:
            namespaceprefix_ = self.Patch_nsprefix_ + ':' if (UseCapturedNS_ and self.Patch_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPatch>%s</%sPatch>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Patch), input_name='Patch')), namespaceprefix_ , eol_))
    def exportLiteral(self, outfile, level, name_='VersionType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.Major is not None:
            showIndent(outfile, level)
            outfile.write('Major=%s,\n' % self.gds_encode(quote_python(self.Major)))
        if self.Minor is not None:
            showIndent(outfile, level)
            outfile.write('Minor=%s,\n' % self.gds_encode(quote_python(self.Minor)))
        if self.Patch is not None:
            showIndent(outfile, level)
            outfile.write('Patch=%s,\n' % self.gds_encode(quote_python(self.Patch)))
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
        if nodeName_ == 'Major':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Major')
            value_ = self.gds_validate_string(value_, node, 'Major')
            self.Major = value_
            self.Major_nsprefix_ = child_.prefix
        elif nodeName_ == 'Minor':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Minor')
            value_ = self.gds_validate_string(value_, node, 'Minor')
            self.Minor = value_
            self.Minor_nsprefix_ = child_.prefix
        elif nodeName_ == 'Patch':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Patch')
            value_ = self.gds_validate_string(value_, node, 'Patch')
            self.Patch = value_
            self.Patch_nsprefix_ = child_.prefix
# end class VersionType


class TextType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, par=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if par is None:
            self.par = []
        else:
            self.par = par
        self.par_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TextType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TextType.subclass:
            return TextType.subclass(*args_, **kwargs_)
        else:
            return TextType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_par(self):
        return self.par
    def set_par(self, par):
        self.par = par
    def add_par(self, value):
        self.par.append(value)
    def insert_par_at(self, index, value):
        self.par.insert(index, value)
    def replace_par_at(self, index, value):
        self.par[index] = value
    def _hasContent(self):
        if (
            self.par
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='TextType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TextType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TextType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TextType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TextType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TextType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='TextType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for par_ in self.par:
            namespaceprefix_ = self.par_nsprefix_ + ':' if (UseCapturedNS_ and self.par_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spar>%s</%spar>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(par_), input_name='par')), namespaceprefix_ , eol_))
    def exportLiteral(self, outfile, level, name_='TextType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('par=[\n')
        level += 1
        for par_ in self.par:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(par_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
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
        if nodeName_ == 'par':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'par')
            value_ = self.gds_validate_string(value_, node, 'par')
            self.par.append(value_)
            self.par_nsprefix_ = child_.prefix
# end class TextType


class CoefficientList(DblList):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = DblList
    def __init__(self, Response=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("CoefficientList"), self).__init__(valueOf_,  **kwargs_)
        self.Response = _cast(None, Response)
        self.Response_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CoefficientList)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CoefficientList.subclass:
            return CoefficientList.subclass(*args_, **kwargs_)
        else:
            return CoefficientList(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Response(self):
        return self.Response
    def set_Response(self, Response):
        self.Response = Response
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            super(CoefficientList, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CoefficientList', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CoefficientList')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CoefficientList':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CoefficientList')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CoefficientList', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CoefficientList'):
        super(CoefficientList, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CoefficientList')
        if self.Response is not None and 'Response' not in already_processed:
            already_processed.add('Response')
            outfile.write(' Response=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Response), input_name='Response')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CoefficientList', fromsubclass_=False, pretty_print=True):
        super(CoefficientList, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        pass
    def exportLiteral(self, outfile, level, name_='CoefficientList'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Response is not None and 'Response' not in already_processed:
            already_processed.add('Response')
            showIndent(outfile, level)
            outfile.write('Response="%s",\n' % (self.Response,))
        super(CoefficientList, self)._exportLiteralAttributes(outfile, level, already_processed, name_)
    def _exportLiteralChildren(self, outfile, level, name_):
        super(CoefficientList, self)._exportLiteralChildren(outfile, level, name_)
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Response', node)
        if value is not None and 'Response' not in already_processed:
            already_processed.add('Response')
            self.Response = value
        super(CoefficientList, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class CoefficientList


class CleanLimitList(DblList):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = DblList
    def __init__(self, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("CleanLimitList"), self).__init__(valueOf_,  **kwargs_)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CleanLimitList)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CleanLimitList.subclass:
            return CleanLimitList.subclass(*args_, **kwargs_)
        else:
            return CleanLimitList(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            super(CleanLimitList, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CleanLimitList', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CleanLimitList')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CleanLimitList':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CleanLimitList')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CleanLimitList', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CleanLimitList'):
        super(CleanLimitList, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CleanLimitList')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='CleanLimitList', fromsubclass_=False, pretty_print=True):
        super(CleanLimitList, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        pass
    def exportLiteral(self, outfile, level, name_='CleanLimitList'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(CleanLimitList, self)._exportLiteralAttributes(outfile, level, already_processed, name_)
    def _exportLiteralChildren(self, outfile, level, name_):
        super(CleanLimitList, self)._exportLiteralChildren(outfile, level, name_)
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(CleanLimitList, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class CleanLimitList


GDSClassesMapping = {
    'CriticalValueList': DblList,
    'DropIndex': Int,
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
        rootTag = 'Annotation'
        rootClass = Annotation
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
        rootTag = 'Annotation'
        rootClass = Annotation
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
        rootTag = 'Annotation'
        rootClass = Annotation
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
        rootTag = 'Annotation'
        rootClass = Annotation
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from gWDSModel_literal import *\n\n')
        sys.stdout.write('import gWDSModel_literal as model_\n\n')
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
NamespaceToDefMappings_ = {'https://github.com/wdatasci/WDS-ModelSpec': [('Nbr',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST'),
                                               ('Int',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST'),
                                               ('Lng',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST'),
                                               ('Dbl',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST'),
                                               ('DblList',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST'),
                                               ('Str',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST'),
                                               ('StrList',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST'),
                                               ('VLS',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST'),
                                               ('VLSList',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST'),
                                               ('Dte',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST'),
                                               ('DteList',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST'),
                                               ('DTm',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST'),
                                               ('DTmList',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST'),
                                               ('Any',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST'),
                                               ('AnyList',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST'),
                                               ('DblListOrStr',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST'),
                                               ('DblOrStr',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST'),
                                               ('DTypType',
                                                './WDS-XML/XSD/WDSModel.xsd',
                                                'ST')]}

__all__ = [
    "Annotation",
    "AppInfoType",
    "CleanLimit",
    "CleanLimitList",
    "CleanLimits",
    "Coefficient",
    "CoefficientList",
    "CoefficientSet",
    "CoefficientSets",
    "Coefficients",
    "Column",
    "ColumnDbl",
    "ColumnStr",
    "Columns",
    "ComponentModel",
    "ComponentModels",
    "Constants",
    "CriticalValue",
    "CriticalValues",
    "CriticalWord",
    "CriticalWordList",
    "CriticalWordSet",
    "CriticalWords",
    "DblList",
    "Dictionary",
    "Documentation",
    "DropIndices",
    "ElemMD",
    "Enum",
    "EnumAttrMDType",
    "EnumMDType",
    "EnumValue",
    "EnumValues",
    "Enums",
    "FieldExtMD",
    "FieldMD",
    "Int",
    "LeftLimit",
    "MatrixColMD",
    "MatrixDbl",
    "MatrixRowMD",
    "MatrixStr",
    "Model",
    "ModelDirectives",
    "Models",
    "Parameter",
    "Parameters",
    "Project",
    "Projects",
    "PythonType",
    "Response",
    "Responses",
    "RightLimit",
    "RowDbl",
    "RowStr",
    "SQLType",
    "Signature",
    "Signatures",
    "Source",
    "Sources",
    "TextType",
    "Transformations",
    "UDFType",
    "UDTFType",
    "UDxInfo",
    "UDxs",
    "Variable",
    "Variables",
    "VersionType",
    "VerticaType",
    "dependsType",
    "v",
    "w"
]
