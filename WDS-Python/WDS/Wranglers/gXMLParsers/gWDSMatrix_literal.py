#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Mon Jun 20 11:53:17 2022 by generateDS.py version 2.40.13.
# Python 3.9.5 (default, Nov 23 2021, 15:27:38)  [GCC 9.3.0]
#
# Command line options:
#   ('--mixed-case-enums', '')
#   ('-f', '')
#   ('--export', 'write literal')
#   ('-o', './WDS-Python/WDS/Wranglers/gXMLParsers/gWDSMatrix_literal.py')
#
# Command line arguments:
#   ./WDS-XML/XSD/WDSMatrix.xsd
#
# Command line:
#   ./WDS-Python/scripts/generateDS_unsnaked --mixed-case-enums -f --export="write literal" -o "./WDS-Python/WDS/Wranglers/gXMLParsers/gWDSMatrix_literal.py" ./WDS-XML/XSD/WDSMatrix.xsd
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


class WDSMatrix(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, NumberOfStates=None, NumberOfAdditionalAxes=None, ProvidesNonZeroCoords=None, AdditionalAxesUpperLimits=None, AdditionalAxesLowerLimits=None, StateLabels=None, NonZeroElements=None, MData=None, Betas=None, FunctionalInputs=None, RedundantFunctionalInputs=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.NumberOfStates = NumberOfStates
        self.NumberOfStates_nsprefix_ = None
        self.NumberOfAdditionalAxes = NumberOfAdditionalAxes
        self.NumberOfAdditionalAxes_nsprefix_ = None
        self.ProvidesNonZeroCoords = ProvidesNonZeroCoords
        self.ProvidesNonZeroCoords_nsprefix_ = None
        self.AdditionalAxesUpperLimits = AdditionalAxesUpperLimits
        self.AdditionalAxesUpperLimits_nsprefix_ = None
        self.AdditionalAxesLowerLimits = AdditionalAxesLowerLimits
        self.AdditionalAxesLowerLimits_nsprefix_ = None
        self.StateLabels = StateLabels
        self.StateLabels_nsprefix_ = None
        self.NonZeroElements = NonZeroElements
        self.NonZeroElements_nsprefix_ = None
        if MData is None:
            self.MData = []
        else:
            self.MData = MData
        self.MData_nsprefix_ = None
        self.Betas = Betas
        self.Betas_nsprefix_ = None
        self.FunctionalInputs = FunctionalInputs
        self.FunctionalInputs_nsprefix_ = None
        self.RedundantFunctionalInputs = RedundantFunctionalInputs
        self.RedundantFunctionalInputs_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, WDSMatrix)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if WDSMatrix.subclass:
            return WDSMatrix.subclass(*args_, **kwargs_)
        else:
            return WDSMatrix(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_NumberOfStates(self):
        return self.NumberOfStates
    def set_NumberOfStates(self, NumberOfStates):
        self.NumberOfStates = NumberOfStates
    def get_NumberOfAdditionalAxes(self):
        return self.NumberOfAdditionalAxes
    def set_NumberOfAdditionalAxes(self, NumberOfAdditionalAxes):
        self.NumberOfAdditionalAxes = NumberOfAdditionalAxes
    def get_ProvidesNonZeroCoords(self):
        return self.ProvidesNonZeroCoords
    def set_ProvidesNonZeroCoords(self, ProvidesNonZeroCoords):
        self.ProvidesNonZeroCoords = ProvidesNonZeroCoords
    def get_AdditionalAxesUpperLimits(self):
        return self.AdditionalAxesUpperLimits
    def set_AdditionalAxesUpperLimits(self, AdditionalAxesUpperLimits):
        self.AdditionalAxesUpperLimits = AdditionalAxesUpperLimits
    def get_AdditionalAxesLowerLimits(self):
        return self.AdditionalAxesLowerLimits
    def set_AdditionalAxesLowerLimits(self, AdditionalAxesLowerLimits):
        self.AdditionalAxesLowerLimits = AdditionalAxesLowerLimits
    def get_StateLabels(self):
        return self.StateLabels
    def set_StateLabels(self, StateLabels):
        self.StateLabels = StateLabels
    def get_NonZeroElements(self):
        return self.NonZeroElements
    def set_NonZeroElements(self, NonZeroElements):
        self.NonZeroElements = NonZeroElements
    def get_MData(self):
        return self.MData
    def set_MData(self, MData):
        self.MData = MData
    def add_MData(self, value):
        self.MData.append(value)
    def insert_MData_at(self, index, value):
        self.MData.insert(index, value)
    def replace_MData_at(self, index, value):
        self.MData[index] = value
    def get_Betas(self):
        return self.Betas
    def set_Betas(self, Betas):
        self.Betas = Betas
    def get_FunctionalInputs(self):
        return self.FunctionalInputs
    def set_FunctionalInputs(self, FunctionalInputs):
        self.FunctionalInputs = FunctionalInputs
    def get_RedundantFunctionalInputs(self):
        return self.RedundantFunctionalInputs
    def set_RedundantFunctionalInputs(self, RedundantFunctionalInputs):
        self.RedundantFunctionalInputs = RedundantFunctionalInputs
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def _hasContent(self):
        if (
            self.NumberOfStates is not None or
            self.NumberOfAdditionalAxes is not None or
            self.ProvidesNonZeroCoords is not None or
            self.AdditionalAxesUpperLimits is not None or
            self.AdditionalAxesLowerLimits is not None or
            self.StateLabels is not None or
            self.NonZeroElements is not None or
            self.MData or
            self.Betas is not None or
            self.FunctionalInputs is not None or
            self.RedundantFunctionalInputs is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='WDSMatrix', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('WDSMatrix')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'WDSMatrix':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='WDSMatrix')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='WDSMatrix', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='WDSMatrix'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='WDSMatrix', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.NumberOfStates is not None:
            namespaceprefix_ = self.NumberOfStates_nsprefix_ + ':' if (UseCapturedNS_ and self.NumberOfStates_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumberOfStates>%s</%sNumberOfStates>%s' % (namespaceprefix_ , self.gds_format_integer(self.NumberOfStates, input_name='NumberOfStates'), namespaceprefix_ , eol_))
        if self.NumberOfAdditionalAxes is not None:
            namespaceprefix_ = self.NumberOfAdditionalAxes_nsprefix_ + ':' if (UseCapturedNS_ and self.NumberOfAdditionalAxes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumberOfAdditionalAxes>%s</%sNumberOfAdditionalAxes>%s' % (namespaceprefix_ , self.gds_format_integer(self.NumberOfAdditionalAxes, input_name='NumberOfAdditionalAxes'), namespaceprefix_ , eol_))
        if self.ProvidesNonZeroCoords is not None:
            namespaceprefix_ = self.ProvidesNonZeroCoords_nsprefix_ + ':' if (UseCapturedNS_ and self.ProvidesNonZeroCoords_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sProvidesNonZeroCoords>%s</%sProvidesNonZeroCoords>%s' % (namespaceprefix_ , self.gds_format_integer(self.ProvidesNonZeroCoords, input_name='ProvidesNonZeroCoords'), namespaceprefix_ , eol_))
        if self.AdditionalAxesUpperLimits is not None:
            namespaceprefix_ = self.AdditionalAxesUpperLimits_nsprefix_ + ':' if (UseCapturedNS_ and self.AdditionalAxesUpperLimits_nsprefix_) else ''
            self.AdditionalAxesUpperLimits.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AdditionalAxesUpperLimits', pretty_print=pretty_print)
        if self.AdditionalAxesLowerLimits is not None:
            namespaceprefix_ = self.AdditionalAxesLowerLimits_nsprefix_ + ':' if (UseCapturedNS_ and self.AdditionalAxesLowerLimits_nsprefix_) else ''
            self.AdditionalAxesLowerLimits.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AdditionalAxesLowerLimits', pretty_print=pretty_print)
        if self.StateLabels is not None:
            namespaceprefix_ = self.StateLabels_nsprefix_ + ':' if (UseCapturedNS_ and self.StateLabels_nsprefix_) else ''
            self.StateLabels.export(outfile, level, namespaceprefix_, namespacedef_='', name_='StateLabels', pretty_print=pretty_print)
        if self.NonZeroElements is not None:
            namespaceprefix_ = self.NonZeroElements_nsprefix_ + ':' if (UseCapturedNS_ and self.NonZeroElements_nsprefix_) else ''
            self.NonZeroElements.export(outfile, level, namespaceprefix_, namespacedef_='', name_='NonZeroElements', pretty_print=pretty_print)
        for MData_ in self.MData:
            namespaceprefix_ = self.MData_nsprefix_ + ':' if (UseCapturedNS_ and self.MData_nsprefix_) else ''
            MData_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MData', pretty_print=pretty_print)
        if self.Betas is not None:
            namespaceprefix_ = self.Betas_nsprefix_ + ':' if (UseCapturedNS_ and self.Betas_nsprefix_) else ''
            self.Betas.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Betas', pretty_print=pretty_print)
        if self.FunctionalInputs is not None:
            namespaceprefix_ = self.FunctionalInputs_nsprefix_ + ':' if (UseCapturedNS_ and self.FunctionalInputs_nsprefix_) else ''
            self.FunctionalInputs.export(outfile, level, namespaceprefix_, namespacedef_='', name_='FunctionalInputs', pretty_print=pretty_print)
        if self.RedundantFunctionalInputs is not None:
            namespaceprefix_ = self.RedundantFunctionalInputs_nsprefix_ + ':' if (UseCapturedNS_ and self.RedundantFunctionalInputs_nsprefix_) else ''
            self.RedundantFunctionalInputs.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RedundantFunctionalInputs', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='WDSMatrix'):
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
        if self.NumberOfStates is not None:
            showIndent(outfile, level)
            outfile.write('NumberOfStates=%d,\n' % self.NumberOfStates)
        if self.NumberOfAdditionalAxes is not None:
            showIndent(outfile, level)
            outfile.write('NumberOfAdditionalAxes=%d,\n' % self.NumberOfAdditionalAxes)
        if self.ProvidesNonZeroCoords is not None:
            showIndent(outfile, level)
            outfile.write('ProvidesNonZeroCoords=%d,\n' % self.ProvidesNonZeroCoords)
        if self.AdditionalAxesUpperLimits is not None:
            showIndent(outfile, level)
            outfile.write('AdditionalAxesUpperLimits=model_.AdditionalAxesUpperLimitsType(\n')
            self.AdditionalAxesUpperLimits.exportLiteral(outfile, level, name_='AdditionalAxesUpperLimits')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.AdditionalAxesLowerLimits is not None:
            showIndent(outfile, level)
            outfile.write('AdditionalAxesLowerLimits=model_.AdditionalAxesLowerLimitsType(\n')
            self.AdditionalAxesLowerLimits.exportLiteral(outfile, level, name_='AdditionalAxesLowerLimits')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.StateLabels is not None:
            showIndent(outfile, level)
            outfile.write('StateLabels=model_.StateLabelsType(\n')
            self.StateLabels.exportLiteral(outfile, level, name_='StateLabels')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.NonZeroElements is not None:
            showIndent(outfile, level)
            outfile.write('NonZeroElements=model_.NonZeroElementsType(\n')
            self.NonZeroElements.exportLiteral(outfile, level, name_='NonZeroElements')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('MData=[\n')
        level += 1
        for MData_ in self.MData:
            showIndent(outfile, level)
            outfile.write('model_.MDataType(\n')
            MData_.exportLiteral(outfile, level, name_='MDataType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Betas is not None:
            showIndent(outfile, level)
            outfile.write('Betas=model_.BetasType(\n')
            self.Betas.exportLiteral(outfile, level, name_='Betas')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.FunctionalInputs is not None:
            showIndent(outfile, level)
            outfile.write('FunctionalInputs=model_.FunctionalInputsType(\n')
            self.FunctionalInputs.exportLiteral(outfile, level, name_='FunctionalInputs')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.RedundantFunctionalInputs is not None:
            showIndent(outfile, level)
            outfile.write('RedundantFunctionalInputs=model_.RedundantFunctionalInputsType(\n')
            self.RedundantFunctionalInputs.exportLiteral(outfile, level, name_='RedundantFunctionalInputs')
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
        if nodeName_ == 'NumberOfStates' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NumberOfStates')
            ival_ = self.gds_validate_integer(ival_, node, 'NumberOfStates')
            self.NumberOfStates = ival_
            self.NumberOfStates_nsprefix_ = child_.prefix
        elif nodeName_ == 'NumberOfAdditionalAxes' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NumberOfAdditionalAxes')
            ival_ = self.gds_validate_integer(ival_, node, 'NumberOfAdditionalAxes')
            self.NumberOfAdditionalAxes = ival_
            self.NumberOfAdditionalAxes_nsprefix_ = child_.prefix
        elif nodeName_ == 'ProvidesNonZeroCoords' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'ProvidesNonZeroCoords')
            ival_ = self.gds_validate_integer(ival_, node, 'ProvidesNonZeroCoords')
            self.ProvidesNonZeroCoords = ival_
            self.ProvidesNonZeroCoords_nsprefix_ = child_.prefix
        elif nodeName_ == 'AdditionalAxesUpperLimits':
            obj_ = AdditionalAxesUpperLimitsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AdditionalAxesUpperLimits = obj_
            obj_.original_tagname_ = 'AdditionalAxesUpperLimits'
        elif nodeName_ == 'AdditionalAxesLowerLimits':
            obj_ = AdditionalAxesLowerLimitsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AdditionalAxesLowerLimits = obj_
            obj_.original_tagname_ = 'AdditionalAxesLowerLimits'
        elif nodeName_ == 'StateLabels':
            obj_ = StateLabelsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.StateLabels = obj_
            obj_.original_tagname_ = 'StateLabels'
        elif nodeName_ == 'NonZeroElements':
            obj_ = NonZeroElementsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.NonZeroElements = obj_
            obj_.original_tagname_ = 'NonZeroElements'
        elif nodeName_ == 'MData':
            obj_ = MDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MData.append(obj_)
            obj_.original_tagname_ = 'MData'
        elif nodeName_ == 'Betas':
            obj_ = BetasType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Betas = obj_
            obj_.original_tagname_ = 'Betas'
        elif nodeName_ == 'FunctionalInputs':
            obj_ = FunctionalInputsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.FunctionalInputs = obj_
            obj_.original_tagname_ = 'FunctionalInputs'
        elif nodeName_ == 'RedundantFunctionalInputs':
            obj_ = RedundantFunctionalInputsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RedundantFunctionalInputs = obj_
            obj_.original_tagname_ = 'RedundantFunctionalInputs'
# end class WDSMatrix


class AdditionalAxesUpperLimitsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Axis1=None, Axis2=None, Axis3=None, Axis4=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Axis1 = Axis1
        self.Axis1_nsprefix_ = None
        self.Axis2 = Axis2
        self.Axis2_nsprefix_ = None
        self.Axis3 = Axis3
        self.Axis3_nsprefix_ = None
        self.Axis4 = Axis4
        self.Axis4_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AdditionalAxesUpperLimitsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AdditionalAxesUpperLimitsType.subclass:
            return AdditionalAxesUpperLimitsType.subclass(*args_, **kwargs_)
        else:
            return AdditionalAxesUpperLimitsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Axis1(self):
        return self.Axis1
    def set_Axis1(self, Axis1):
        self.Axis1 = Axis1
    def get_Axis2(self):
        return self.Axis2
    def set_Axis2(self, Axis2):
        self.Axis2 = Axis2
    def get_Axis3(self):
        return self.Axis3
    def set_Axis3(self, Axis3):
        self.Axis3 = Axis3
    def get_Axis4(self):
        return self.Axis4
    def set_Axis4(self, Axis4):
        self.Axis4 = Axis4
    def _hasContent(self):
        if (
            self.Axis1 is not None or
            self.Axis2 is not None or
            self.Axis3 is not None or
            self.Axis4 is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='AdditionalAxesUpperLimitsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AdditionalAxesUpperLimitsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AdditionalAxesUpperLimitsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AdditionalAxesUpperLimitsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AdditionalAxesUpperLimitsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AdditionalAxesUpperLimitsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='AdditionalAxesUpperLimitsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Axis1 is not None:
            namespaceprefix_ = self.Axis1_nsprefix_ + ':' if (UseCapturedNS_ and self.Axis1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAxis1>%s</%sAxis1>%s' % (namespaceprefix_ , self.gds_format_integer(self.Axis1, input_name='Axis1'), namespaceprefix_ , eol_))
        if self.Axis2 is not None:
            namespaceprefix_ = self.Axis2_nsprefix_ + ':' if (UseCapturedNS_ and self.Axis2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAxis2>%s</%sAxis2>%s' % (namespaceprefix_ , self.gds_format_integer(self.Axis2, input_name='Axis2'), namespaceprefix_ , eol_))
        if self.Axis3 is not None:
            namespaceprefix_ = self.Axis3_nsprefix_ + ':' if (UseCapturedNS_ and self.Axis3_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAxis3>%s</%sAxis3>%s' % (namespaceprefix_ , self.gds_format_integer(self.Axis3, input_name='Axis3'), namespaceprefix_ , eol_))
        if self.Axis4 is not None:
            namespaceprefix_ = self.Axis4_nsprefix_ + ':' if (UseCapturedNS_ and self.Axis4_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAxis4>%s</%sAxis4>%s' % (namespaceprefix_ , self.gds_format_integer(self.Axis4, input_name='Axis4'), namespaceprefix_ , eol_))
    def exportLiteral(self, outfile, level, name_='AdditionalAxesUpperLimitsType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.Axis1 is not None:
            showIndent(outfile, level)
            outfile.write('Axis1=%d,\n' % self.Axis1)
        if self.Axis2 is not None:
            showIndent(outfile, level)
            outfile.write('Axis2=%d,\n' % self.Axis2)
        if self.Axis3 is not None:
            showIndent(outfile, level)
            outfile.write('Axis3=%d,\n' % self.Axis3)
        if self.Axis4 is not None:
            showIndent(outfile, level)
            outfile.write('Axis4=%d,\n' % self.Axis4)
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
        if nodeName_ == 'Axis1' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Axis1')
            ival_ = self.gds_validate_integer(ival_, node, 'Axis1')
            self.Axis1 = ival_
            self.Axis1_nsprefix_ = child_.prefix
        elif nodeName_ == 'Axis2' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Axis2')
            ival_ = self.gds_validate_integer(ival_, node, 'Axis2')
            self.Axis2 = ival_
            self.Axis2_nsprefix_ = child_.prefix
        elif nodeName_ == 'Axis3' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Axis3')
            ival_ = self.gds_validate_integer(ival_, node, 'Axis3')
            self.Axis3 = ival_
            self.Axis3_nsprefix_ = child_.prefix
        elif nodeName_ == 'Axis4' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Axis4')
            ival_ = self.gds_validate_integer(ival_, node, 'Axis4')
            self.Axis4 = ival_
            self.Axis4_nsprefix_ = child_.prefix
# end class AdditionalAxesUpperLimitsType


class AdditionalAxesLowerLimitsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Axis1=None, Axis2=None, Axis3=None, Axis4=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Axis1 = Axis1
        self.Axis1_nsprefix_ = None
        self.Axis2 = Axis2
        self.Axis2_nsprefix_ = None
        self.Axis3 = Axis3
        self.Axis3_nsprefix_ = None
        self.Axis4 = Axis4
        self.Axis4_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AdditionalAxesLowerLimitsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AdditionalAxesLowerLimitsType.subclass:
            return AdditionalAxesLowerLimitsType.subclass(*args_, **kwargs_)
        else:
            return AdditionalAxesLowerLimitsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Axis1(self):
        return self.Axis1
    def set_Axis1(self, Axis1):
        self.Axis1 = Axis1
    def get_Axis2(self):
        return self.Axis2
    def set_Axis2(self, Axis2):
        self.Axis2 = Axis2
    def get_Axis3(self):
        return self.Axis3
    def set_Axis3(self, Axis3):
        self.Axis3 = Axis3
    def get_Axis4(self):
        return self.Axis4
    def set_Axis4(self, Axis4):
        self.Axis4 = Axis4
    def _hasContent(self):
        if (
            self.Axis1 is not None or
            self.Axis2 is not None or
            self.Axis3 is not None or
            self.Axis4 is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='AdditionalAxesLowerLimitsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AdditionalAxesLowerLimitsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AdditionalAxesLowerLimitsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AdditionalAxesLowerLimitsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AdditionalAxesLowerLimitsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AdditionalAxesLowerLimitsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='AdditionalAxesLowerLimitsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Axis1 is not None:
            namespaceprefix_ = self.Axis1_nsprefix_ + ':' if (UseCapturedNS_ and self.Axis1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAxis1>%s</%sAxis1>%s' % (namespaceprefix_ , self.gds_format_integer(self.Axis1, input_name='Axis1'), namespaceprefix_ , eol_))
        if self.Axis2 is not None:
            namespaceprefix_ = self.Axis2_nsprefix_ + ':' if (UseCapturedNS_ and self.Axis2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAxis2>%s</%sAxis2>%s' % (namespaceprefix_ , self.gds_format_integer(self.Axis2, input_name='Axis2'), namespaceprefix_ , eol_))
        if self.Axis3 is not None:
            namespaceprefix_ = self.Axis3_nsprefix_ + ':' if (UseCapturedNS_ and self.Axis3_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAxis3>%s</%sAxis3>%s' % (namespaceprefix_ , self.gds_format_integer(self.Axis3, input_name='Axis3'), namespaceprefix_ , eol_))
        if self.Axis4 is not None:
            namespaceprefix_ = self.Axis4_nsprefix_ + ':' if (UseCapturedNS_ and self.Axis4_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAxis4>%s</%sAxis4>%s' % (namespaceprefix_ , self.gds_format_integer(self.Axis4, input_name='Axis4'), namespaceprefix_ , eol_))
    def exportLiteral(self, outfile, level, name_='AdditionalAxesLowerLimitsType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.Axis1 is not None:
            showIndent(outfile, level)
            outfile.write('Axis1=%d,\n' % self.Axis1)
        if self.Axis2 is not None:
            showIndent(outfile, level)
            outfile.write('Axis2=%d,\n' % self.Axis2)
        if self.Axis3 is not None:
            showIndent(outfile, level)
            outfile.write('Axis3=%d,\n' % self.Axis3)
        if self.Axis4 is not None:
            showIndent(outfile, level)
            outfile.write('Axis4=%d,\n' % self.Axis4)
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
        if nodeName_ == 'Axis1' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Axis1')
            ival_ = self.gds_validate_integer(ival_, node, 'Axis1')
            self.Axis1 = ival_
            self.Axis1_nsprefix_ = child_.prefix
        elif nodeName_ == 'Axis2' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Axis2')
            ival_ = self.gds_validate_integer(ival_, node, 'Axis2')
            self.Axis2 = ival_
            self.Axis2_nsprefix_ = child_.prefix
        elif nodeName_ == 'Axis3' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Axis3')
            ival_ = self.gds_validate_integer(ival_, node, 'Axis3')
            self.Axis3 = ival_
            self.Axis3_nsprefix_ = child_.prefix
        elif nodeName_ == 'Axis4' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Axis4')
            ival_ = self.gds_validate_integer(ival_, node, 'Axis4')
            self.Axis4 = ival_
            self.Axis4_nsprefix_ = child_.prefix
# end class AdditionalAxesLowerLimitsType


class StateLabelsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, StateLabel=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if StateLabel is None:
            self.StateLabel = []
        else:
            self.StateLabel = StateLabel
        self.StateLabel_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, StateLabelsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if StateLabelsType.subclass:
            return StateLabelsType.subclass(*args_, **kwargs_)
        else:
            return StateLabelsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_StateLabel(self):
        return self.StateLabel
    def set_StateLabel(self, StateLabel):
        self.StateLabel = StateLabel
    def add_StateLabel(self, value):
        self.StateLabel.append(value)
    def insert_StateLabel_at(self, index, value):
        self.StateLabel.insert(index, value)
    def replace_StateLabel_at(self, index, value):
        self.StateLabel[index] = value
    def _hasContent(self):
        if (
            self.StateLabel
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='StateLabelsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('StateLabelsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'StateLabelsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='StateLabelsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='StateLabelsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='StateLabelsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='StateLabelsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for StateLabel_ in self.StateLabel:
            namespaceprefix_ = self.StateLabel_nsprefix_ + ':' if (UseCapturedNS_ and self.StateLabel_nsprefix_) else ''
            StateLabel_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='StateLabel', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='StateLabelsType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('StateLabel=[\n')
        level += 1
        for StateLabel_ in self.StateLabel:
            showIndent(outfile, level)
            outfile.write('model_.StateLabelType(\n')
            StateLabel_.exportLiteral(outfile, level, name_='StateLabelType')
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
        if nodeName_ == 'StateLabel':
            obj_ = StateLabelType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.StateLabel.append(obj_)
            obj_.original_tagname_ = 'StateLabel'
# end class StateLabelsType


class StateLabelType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Position = _cast(int, Position)
        self.Position_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, StateLabelType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if StateLabelType.subclass:
            return StateLabelType.subclass(*args_, **kwargs_)
        else:
            return StateLabelType(*args_, **kwargs_)
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
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='StateLabelType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('StateLabelType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'StateLabelType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='StateLabelType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='StateLabelType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='StateLabelType'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position="%s"' % self.gds_format_integer(self.Position, input_name='Position'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='StateLabelType', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='StateLabelType'):
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
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class StateLabelType


class NonZeroElementsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Number=None, NonZeroCoordinates=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Number = Number
        self.Number_nsprefix_ = None
        self.NonZeroCoordinates = NonZeroCoordinates
        self.NonZeroCoordinates_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NonZeroElementsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NonZeroElementsType.subclass:
            return NonZeroElementsType.subclass(*args_, **kwargs_)
        else:
            return NonZeroElementsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Number(self):
        return self.Number
    def set_Number(self, Number):
        self.Number = Number
    def get_NonZeroCoordinates(self):
        return self.NonZeroCoordinates
    def set_NonZeroCoordinates(self, NonZeroCoordinates):
        self.NonZeroCoordinates = NonZeroCoordinates
    def _hasContent(self):
        if (
            self.Number is not None or
            self.NonZeroCoordinates is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='NonZeroElementsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NonZeroElementsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NonZeroElementsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NonZeroElementsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NonZeroElementsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NonZeroElementsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='NonZeroElementsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Number is not None:
            namespaceprefix_ = self.Number_nsprefix_ + ':' if (UseCapturedNS_ and self.Number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumber>%s</%sNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.Number, input_name='Number'), namespaceprefix_ , eol_))
        if self.NonZeroCoordinates is not None:
            namespaceprefix_ = self.NonZeroCoordinates_nsprefix_ + ':' if (UseCapturedNS_ and self.NonZeroCoordinates_nsprefix_) else ''
            self.NonZeroCoordinates.export(outfile, level, namespaceprefix_, namespacedef_='', name_='NonZeroCoordinates', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='NonZeroElementsType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.Number is not None:
            showIndent(outfile, level)
            outfile.write('Number=%d,\n' % self.Number)
        if self.NonZeroCoordinates is not None:
            showIndent(outfile, level)
            outfile.write('NonZeroCoordinates=model_.NonZeroCoordinatesType(\n')
            self.NonZeroCoordinates.exportLiteral(outfile, level, name_='NonZeroCoordinates')
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
        if nodeName_ == 'Number' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Number')
            ival_ = self.gds_validate_integer(ival_, node, 'Number')
            self.Number = ival_
            self.Number_nsprefix_ = child_.prefix
        elif nodeName_ == 'NonZeroCoordinates':
            obj_ = NonZeroCoordinatesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.NonZeroCoordinates = obj_
            obj_.original_tagname_ = 'NonZeroCoordinates'
# end class NonZeroElementsType


class NonZeroCoordinatesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, NonZeroCoordinate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if NonZeroCoordinate is None:
            self.NonZeroCoordinate = []
        else:
            self.NonZeroCoordinate = NonZeroCoordinate
        self.NonZeroCoordinate_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NonZeroCoordinatesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NonZeroCoordinatesType.subclass:
            return NonZeroCoordinatesType.subclass(*args_, **kwargs_)
        else:
            return NonZeroCoordinatesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_NonZeroCoordinate(self):
        return self.NonZeroCoordinate
    def set_NonZeroCoordinate(self, NonZeroCoordinate):
        self.NonZeroCoordinate = NonZeroCoordinate
    def add_NonZeroCoordinate(self, value):
        self.NonZeroCoordinate.append(value)
    def insert_NonZeroCoordinate_at(self, index, value):
        self.NonZeroCoordinate.insert(index, value)
    def replace_NonZeroCoordinate_at(self, index, value):
        self.NonZeroCoordinate[index] = value
    def _hasContent(self):
        if (
            self.NonZeroCoordinate
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='NonZeroCoordinatesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NonZeroCoordinatesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NonZeroCoordinatesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NonZeroCoordinatesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NonZeroCoordinatesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NonZeroCoordinatesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='NonZeroCoordinatesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for NonZeroCoordinate_ in self.NonZeroCoordinate:
            namespaceprefix_ = self.NonZeroCoordinate_nsprefix_ + ':' if (UseCapturedNS_ and self.NonZeroCoordinate_nsprefix_) else ''
            NonZeroCoordinate_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='NonZeroCoordinate', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='NonZeroCoordinatesType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('NonZeroCoordinate=[\n')
        level += 1
        for NonZeroCoordinate_ in self.NonZeroCoordinate:
            showIndent(outfile, level)
            outfile.write('model_.NonZeroCoordinateType(\n')
            NonZeroCoordinate_.exportLiteral(outfile, level, name_='NonZeroCoordinateType')
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
        if nodeName_ == 'NonZeroCoordinate':
            obj_ = NonZeroCoordinateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.NonZeroCoordinate.append(obj_)
            obj_.original_tagname_ = 'NonZeroCoordinate'
# end class NonZeroCoordinatesType


class NonZeroCoordinateType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, I=None, J=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Position = _cast(int, Position)
        self.Position_nsprefix_ = None
        self.I = I
        self.I_nsprefix_ = None
        self.J = J
        self.J_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NonZeroCoordinateType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NonZeroCoordinateType.subclass:
            return NonZeroCoordinateType.subclass(*args_, **kwargs_)
        else:
            return NonZeroCoordinateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_I(self):
        return self.I
    def set_I(self, I):
        self.I = I
    def get_J(self):
        return self.J
    def set_J(self, J):
        self.J = J
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def _hasContent(self):
        if (
            self.I is not None or
            self.J is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='NonZeroCoordinateType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NonZeroCoordinateType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NonZeroCoordinateType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NonZeroCoordinateType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NonZeroCoordinateType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NonZeroCoordinateType'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position="%s"' % self.gds_format_integer(self.Position, input_name='Position'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='NonZeroCoordinateType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.I is not None:
            namespaceprefix_ = self.I_nsprefix_ + ':' if (UseCapturedNS_ and self.I_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sI>%s</%sI>%s' % (namespaceprefix_ , self.gds_format_integer(self.I, input_name='I'), namespaceprefix_ , eol_))
        if self.J is not None:
            namespaceprefix_ = self.J_nsprefix_ + ':' if (UseCapturedNS_ and self.J_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sJ>%s</%sJ>%s' % (namespaceprefix_ , self.gds_format_integer(self.J, input_name='J'), namespaceprefix_ , eol_))
    def exportLiteral(self, outfile, level, name_='NonZeroCoordinateType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            showIndent(outfile, level)
            outfile.write('Position=%d,\n' % (self.Position,))
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.I is not None:
            showIndent(outfile, level)
            outfile.write('I=%d,\n' % self.I)
        if self.J is not None:
            showIndent(outfile, level)
            outfile.write('J=%d,\n' % self.J)
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
        if nodeName_ == 'I' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'I')
            ival_ = self.gds_validate_integer(ival_, node, 'I')
            self.I = ival_
            self.I_nsprefix_ = child_.prefix
        elif nodeName_ == 'J' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'J')
            ival_ = self.gds_validate_integer(ival_, node, 'J')
            self.J = ival_
            self.J_nsprefix_ = child_.prefix
# end class NonZeroCoordinateType


class MDataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Row=None, Axis1=None, Axis2=None, Axis3=None, Axis4=None, Col1=None, Col2=None, Col3=None, Col4=None, Col5=None, Col6=None, Col7=None, Col8=None, Col9=None, Col10=None, Col11=None, Col12=None, Col13=None, Col14=None, Col15=None, Col16=None, Col17=None, Col18=None, Col19=None, Col20=None, Col21=None, Col22=None, Col23=None, Col24=None, Col25=None, Col26=None, Col27=None, Col28=None, Col29=None, Col30=None, Col31=None, Col32=None, Col33=None, Col34=None, Col35=None, Col36=None, Col37=None, Col38=None, Col39=None, Col40=None, Col41=None, Col42=None, Col43=None, Col44=None, Col45=None, Col46=None, Col47=None, Col48=None, Col49=None, Col50=None, Col51=None, Col52=None, Col53=None, Col54=None, Col55=None, Col56=None, Col57=None, Col58=None, Col59=None, Col60=None, Col61=None, Col62=None, Col63=None, Col64=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Row = _cast(int, Row)
        self.Row_nsprefix_ = None
        self.Axis1 = _cast(int, Axis1)
        self.Axis1_nsprefix_ = None
        self.Axis2 = _cast(int, Axis2)
        self.Axis2_nsprefix_ = None
        self.Axis3 = _cast(int, Axis3)
        self.Axis3_nsprefix_ = None
        self.Axis4 = _cast(int, Axis4)
        self.Axis4_nsprefix_ = None
        self.Col1 = Col1
        self.Col1_nsprefix_ = None
        self.Col2 = Col2
        self.Col2_nsprefix_ = None
        self.Col3 = Col3
        self.Col3_nsprefix_ = None
        self.Col4 = Col4
        self.Col4_nsprefix_ = None
        self.Col5 = Col5
        self.Col5_nsprefix_ = None
        self.Col6 = Col6
        self.Col6_nsprefix_ = None
        self.Col7 = Col7
        self.Col7_nsprefix_ = None
        self.Col8 = Col8
        self.Col8_nsprefix_ = None
        self.Col9 = Col9
        self.Col9_nsprefix_ = None
        self.Col10 = Col10
        self.Col10_nsprefix_ = None
        self.Col11 = Col11
        self.Col11_nsprefix_ = None
        self.Col12 = Col12
        self.Col12_nsprefix_ = None
        self.Col13 = Col13
        self.Col13_nsprefix_ = None
        self.Col14 = Col14
        self.Col14_nsprefix_ = None
        self.Col15 = Col15
        self.Col15_nsprefix_ = None
        self.Col16 = Col16
        self.Col16_nsprefix_ = None
        self.Col17 = Col17
        self.Col17_nsprefix_ = None
        self.Col18 = Col18
        self.Col18_nsprefix_ = None
        self.Col19 = Col19
        self.Col19_nsprefix_ = None
        self.Col20 = Col20
        self.Col20_nsprefix_ = None
        self.Col21 = Col21
        self.Col21_nsprefix_ = None
        self.Col22 = Col22
        self.Col22_nsprefix_ = None
        self.Col23 = Col23
        self.Col23_nsprefix_ = None
        self.Col24 = Col24
        self.Col24_nsprefix_ = None
        self.Col25 = Col25
        self.Col25_nsprefix_ = None
        self.Col26 = Col26
        self.Col26_nsprefix_ = None
        self.Col27 = Col27
        self.Col27_nsprefix_ = None
        self.Col28 = Col28
        self.Col28_nsprefix_ = None
        self.Col29 = Col29
        self.Col29_nsprefix_ = None
        self.Col30 = Col30
        self.Col30_nsprefix_ = None
        self.Col31 = Col31
        self.Col31_nsprefix_ = None
        self.Col32 = Col32
        self.Col32_nsprefix_ = None
        self.Col33 = Col33
        self.Col33_nsprefix_ = None
        self.Col34 = Col34
        self.Col34_nsprefix_ = None
        self.Col35 = Col35
        self.Col35_nsprefix_ = None
        self.Col36 = Col36
        self.Col36_nsprefix_ = None
        self.Col37 = Col37
        self.Col37_nsprefix_ = None
        self.Col38 = Col38
        self.Col38_nsprefix_ = None
        self.Col39 = Col39
        self.Col39_nsprefix_ = None
        self.Col40 = Col40
        self.Col40_nsprefix_ = None
        self.Col41 = Col41
        self.Col41_nsprefix_ = None
        self.Col42 = Col42
        self.Col42_nsprefix_ = None
        self.Col43 = Col43
        self.Col43_nsprefix_ = None
        self.Col44 = Col44
        self.Col44_nsprefix_ = None
        self.Col45 = Col45
        self.Col45_nsprefix_ = None
        self.Col46 = Col46
        self.Col46_nsprefix_ = None
        self.Col47 = Col47
        self.Col47_nsprefix_ = None
        self.Col48 = Col48
        self.Col48_nsprefix_ = None
        self.Col49 = Col49
        self.Col49_nsprefix_ = None
        self.Col50 = Col50
        self.Col50_nsprefix_ = None
        self.Col51 = Col51
        self.Col51_nsprefix_ = None
        self.Col52 = Col52
        self.Col52_nsprefix_ = None
        self.Col53 = Col53
        self.Col53_nsprefix_ = None
        self.Col54 = Col54
        self.Col54_nsprefix_ = None
        self.Col55 = Col55
        self.Col55_nsprefix_ = None
        self.Col56 = Col56
        self.Col56_nsprefix_ = None
        self.Col57 = Col57
        self.Col57_nsprefix_ = None
        self.Col58 = Col58
        self.Col58_nsprefix_ = None
        self.Col59 = Col59
        self.Col59_nsprefix_ = None
        self.Col60 = Col60
        self.Col60_nsprefix_ = None
        self.Col61 = Col61
        self.Col61_nsprefix_ = None
        self.Col62 = Col62
        self.Col62_nsprefix_ = None
        self.Col63 = Col63
        self.Col63_nsprefix_ = None
        self.Col64 = Col64
        self.Col64_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MDataType.subclass:
            return MDataType.subclass(*args_, **kwargs_)
        else:
            return MDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Col1(self):
        return self.Col1
    def set_Col1(self, Col1):
        self.Col1 = Col1
    def get_Col2(self):
        return self.Col2
    def set_Col2(self, Col2):
        self.Col2 = Col2
    def get_Col3(self):
        return self.Col3
    def set_Col3(self, Col3):
        self.Col3 = Col3
    def get_Col4(self):
        return self.Col4
    def set_Col4(self, Col4):
        self.Col4 = Col4
    def get_Col5(self):
        return self.Col5
    def set_Col5(self, Col5):
        self.Col5 = Col5
    def get_Col6(self):
        return self.Col6
    def set_Col6(self, Col6):
        self.Col6 = Col6
    def get_Col7(self):
        return self.Col7
    def set_Col7(self, Col7):
        self.Col7 = Col7
    def get_Col8(self):
        return self.Col8
    def set_Col8(self, Col8):
        self.Col8 = Col8
    def get_Col9(self):
        return self.Col9
    def set_Col9(self, Col9):
        self.Col9 = Col9
    def get_Col10(self):
        return self.Col10
    def set_Col10(self, Col10):
        self.Col10 = Col10
    def get_Col11(self):
        return self.Col11
    def set_Col11(self, Col11):
        self.Col11 = Col11
    def get_Col12(self):
        return self.Col12
    def set_Col12(self, Col12):
        self.Col12 = Col12
    def get_Col13(self):
        return self.Col13
    def set_Col13(self, Col13):
        self.Col13 = Col13
    def get_Col14(self):
        return self.Col14
    def set_Col14(self, Col14):
        self.Col14 = Col14
    def get_Col15(self):
        return self.Col15
    def set_Col15(self, Col15):
        self.Col15 = Col15
    def get_Col16(self):
        return self.Col16
    def set_Col16(self, Col16):
        self.Col16 = Col16
    def get_Col17(self):
        return self.Col17
    def set_Col17(self, Col17):
        self.Col17 = Col17
    def get_Col18(self):
        return self.Col18
    def set_Col18(self, Col18):
        self.Col18 = Col18
    def get_Col19(self):
        return self.Col19
    def set_Col19(self, Col19):
        self.Col19 = Col19
    def get_Col20(self):
        return self.Col20
    def set_Col20(self, Col20):
        self.Col20 = Col20
    def get_Col21(self):
        return self.Col21
    def set_Col21(self, Col21):
        self.Col21 = Col21
    def get_Col22(self):
        return self.Col22
    def set_Col22(self, Col22):
        self.Col22 = Col22
    def get_Col23(self):
        return self.Col23
    def set_Col23(self, Col23):
        self.Col23 = Col23
    def get_Col24(self):
        return self.Col24
    def set_Col24(self, Col24):
        self.Col24 = Col24
    def get_Col25(self):
        return self.Col25
    def set_Col25(self, Col25):
        self.Col25 = Col25
    def get_Col26(self):
        return self.Col26
    def set_Col26(self, Col26):
        self.Col26 = Col26
    def get_Col27(self):
        return self.Col27
    def set_Col27(self, Col27):
        self.Col27 = Col27
    def get_Col28(self):
        return self.Col28
    def set_Col28(self, Col28):
        self.Col28 = Col28
    def get_Col29(self):
        return self.Col29
    def set_Col29(self, Col29):
        self.Col29 = Col29
    def get_Col30(self):
        return self.Col30
    def set_Col30(self, Col30):
        self.Col30 = Col30
    def get_Col31(self):
        return self.Col31
    def set_Col31(self, Col31):
        self.Col31 = Col31
    def get_Col32(self):
        return self.Col32
    def set_Col32(self, Col32):
        self.Col32 = Col32
    def get_Col33(self):
        return self.Col33
    def set_Col33(self, Col33):
        self.Col33 = Col33
    def get_Col34(self):
        return self.Col34
    def set_Col34(self, Col34):
        self.Col34 = Col34
    def get_Col35(self):
        return self.Col35
    def set_Col35(self, Col35):
        self.Col35 = Col35
    def get_Col36(self):
        return self.Col36
    def set_Col36(self, Col36):
        self.Col36 = Col36
    def get_Col37(self):
        return self.Col37
    def set_Col37(self, Col37):
        self.Col37 = Col37
    def get_Col38(self):
        return self.Col38
    def set_Col38(self, Col38):
        self.Col38 = Col38
    def get_Col39(self):
        return self.Col39
    def set_Col39(self, Col39):
        self.Col39 = Col39
    def get_Col40(self):
        return self.Col40
    def set_Col40(self, Col40):
        self.Col40 = Col40
    def get_Col41(self):
        return self.Col41
    def set_Col41(self, Col41):
        self.Col41 = Col41
    def get_Col42(self):
        return self.Col42
    def set_Col42(self, Col42):
        self.Col42 = Col42
    def get_Col43(self):
        return self.Col43
    def set_Col43(self, Col43):
        self.Col43 = Col43
    def get_Col44(self):
        return self.Col44
    def set_Col44(self, Col44):
        self.Col44 = Col44
    def get_Col45(self):
        return self.Col45
    def set_Col45(self, Col45):
        self.Col45 = Col45
    def get_Col46(self):
        return self.Col46
    def set_Col46(self, Col46):
        self.Col46 = Col46
    def get_Col47(self):
        return self.Col47
    def set_Col47(self, Col47):
        self.Col47 = Col47
    def get_Col48(self):
        return self.Col48
    def set_Col48(self, Col48):
        self.Col48 = Col48
    def get_Col49(self):
        return self.Col49
    def set_Col49(self, Col49):
        self.Col49 = Col49
    def get_Col50(self):
        return self.Col50
    def set_Col50(self, Col50):
        self.Col50 = Col50
    def get_Col51(self):
        return self.Col51
    def set_Col51(self, Col51):
        self.Col51 = Col51
    def get_Col52(self):
        return self.Col52
    def set_Col52(self, Col52):
        self.Col52 = Col52
    def get_Col53(self):
        return self.Col53
    def set_Col53(self, Col53):
        self.Col53 = Col53
    def get_Col54(self):
        return self.Col54
    def set_Col54(self, Col54):
        self.Col54 = Col54
    def get_Col55(self):
        return self.Col55
    def set_Col55(self, Col55):
        self.Col55 = Col55
    def get_Col56(self):
        return self.Col56
    def set_Col56(self, Col56):
        self.Col56 = Col56
    def get_Col57(self):
        return self.Col57
    def set_Col57(self, Col57):
        self.Col57 = Col57
    def get_Col58(self):
        return self.Col58
    def set_Col58(self, Col58):
        self.Col58 = Col58
    def get_Col59(self):
        return self.Col59
    def set_Col59(self, Col59):
        self.Col59 = Col59
    def get_Col60(self):
        return self.Col60
    def set_Col60(self, Col60):
        self.Col60 = Col60
    def get_Col61(self):
        return self.Col61
    def set_Col61(self, Col61):
        self.Col61 = Col61
    def get_Col62(self):
        return self.Col62
    def set_Col62(self, Col62):
        self.Col62 = Col62
    def get_Col63(self):
        return self.Col63
    def set_Col63(self, Col63):
        self.Col63 = Col63
    def get_Col64(self):
        return self.Col64
    def set_Col64(self, Col64):
        self.Col64 = Col64
    def get_Row(self):
        return self.Row
    def set_Row(self, Row):
        self.Row = Row
    def get_Axis1(self):
        return self.Axis1
    def set_Axis1(self, Axis1):
        self.Axis1 = Axis1
    def get_Axis2(self):
        return self.Axis2
    def set_Axis2(self, Axis2):
        self.Axis2 = Axis2
    def get_Axis3(self):
        return self.Axis3
    def set_Axis3(self, Axis3):
        self.Axis3 = Axis3
    def get_Axis4(self):
        return self.Axis4
    def set_Axis4(self, Axis4):
        self.Axis4 = Axis4
    def _hasContent(self):
        if (
            self.Col1 is not None or
            self.Col2 is not None or
            self.Col3 is not None or
            self.Col4 is not None or
            self.Col5 is not None or
            self.Col6 is not None or
            self.Col7 is not None or
            self.Col8 is not None or
            self.Col9 is not None or
            self.Col10 is not None or
            self.Col11 is not None or
            self.Col12 is not None or
            self.Col13 is not None or
            self.Col14 is not None or
            self.Col15 is not None or
            self.Col16 is not None or
            self.Col17 is not None or
            self.Col18 is not None or
            self.Col19 is not None or
            self.Col20 is not None or
            self.Col21 is not None or
            self.Col22 is not None or
            self.Col23 is not None or
            self.Col24 is not None or
            self.Col25 is not None or
            self.Col26 is not None or
            self.Col27 is not None or
            self.Col28 is not None or
            self.Col29 is not None or
            self.Col30 is not None or
            self.Col31 is not None or
            self.Col32 is not None or
            self.Col33 is not None or
            self.Col34 is not None or
            self.Col35 is not None or
            self.Col36 is not None or
            self.Col37 is not None or
            self.Col38 is not None or
            self.Col39 is not None or
            self.Col40 is not None or
            self.Col41 is not None or
            self.Col42 is not None or
            self.Col43 is not None or
            self.Col44 is not None or
            self.Col45 is not None or
            self.Col46 is not None or
            self.Col47 is not None or
            self.Col48 is not None or
            self.Col49 is not None or
            self.Col50 is not None or
            self.Col51 is not None or
            self.Col52 is not None or
            self.Col53 is not None or
            self.Col54 is not None or
            self.Col55 is not None or
            self.Col56 is not None or
            self.Col57 is not None or
            self.Col58 is not None or
            self.Col59 is not None or
            self.Col60 is not None or
            self.Col61 is not None or
            self.Col62 is not None or
            self.Col63 is not None or
            self.Col64 is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='MDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MDataType'):
        if self.Row is not None and 'Row' not in already_processed:
            already_processed.add('Row')
            outfile.write(' Row="%s"' % self.gds_format_integer(self.Row, input_name='Row'))
        if self.Axis1 is not None and 'Axis1' not in already_processed:
            already_processed.add('Axis1')
            outfile.write(' Axis1="%s"' % self.gds_format_integer(self.Axis1, input_name='Axis1'))
        if self.Axis2 is not None and 'Axis2' not in already_processed:
            already_processed.add('Axis2')
            outfile.write(' Axis2="%s"' % self.gds_format_integer(self.Axis2, input_name='Axis2'))
        if self.Axis3 is not None and 'Axis3' not in already_processed:
            already_processed.add('Axis3')
            outfile.write(' Axis3="%s"' % self.gds_format_integer(self.Axis3, input_name='Axis3'))
        if self.Axis4 is not None and 'Axis4' not in already_processed:
            already_processed.add('Axis4')
            outfile.write(' Axis4="%s"' % self.gds_format_integer(self.Axis4, input_name='Axis4'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='MDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Col1 is not None:
            namespaceprefix_ = self.Col1_nsprefix_ + ':' if (UseCapturedNS_ and self.Col1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol1>%s</%sCol1>%s' % (namespaceprefix_ , self.gds_format_double(self.Col1, input_name='Col1'), namespaceprefix_ , eol_))
        if self.Col2 is not None:
            namespaceprefix_ = self.Col2_nsprefix_ + ':' if (UseCapturedNS_ and self.Col2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol2>%s</%sCol2>%s' % (namespaceprefix_ , self.gds_format_double(self.Col2, input_name='Col2'), namespaceprefix_ , eol_))
        if self.Col3 is not None:
            namespaceprefix_ = self.Col3_nsprefix_ + ':' if (UseCapturedNS_ and self.Col3_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol3>%s</%sCol3>%s' % (namespaceprefix_ , self.gds_format_double(self.Col3, input_name='Col3'), namespaceprefix_ , eol_))
        if self.Col4 is not None:
            namespaceprefix_ = self.Col4_nsprefix_ + ':' if (UseCapturedNS_ and self.Col4_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol4>%s</%sCol4>%s' % (namespaceprefix_ , self.gds_format_double(self.Col4, input_name='Col4'), namespaceprefix_ , eol_))
        if self.Col5 is not None:
            namespaceprefix_ = self.Col5_nsprefix_ + ':' if (UseCapturedNS_ and self.Col5_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol5>%s</%sCol5>%s' % (namespaceprefix_ , self.gds_format_double(self.Col5, input_name='Col5'), namespaceprefix_ , eol_))
        if self.Col6 is not None:
            namespaceprefix_ = self.Col6_nsprefix_ + ':' if (UseCapturedNS_ and self.Col6_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol6>%s</%sCol6>%s' % (namespaceprefix_ , self.gds_format_double(self.Col6, input_name='Col6'), namespaceprefix_ , eol_))
        if self.Col7 is not None:
            namespaceprefix_ = self.Col7_nsprefix_ + ':' if (UseCapturedNS_ and self.Col7_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol7>%s</%sCol7>%s' % (namespaceprefix_ , self.gds_format_double(self.Col7, input_name='Col7'), namespaceprefix_ , eol_))
        if self.Col8 is not None:
            namespaceprefix_ = self.Col8_nsprefix_ + ':' if (UseCapturedNS_ and self.Col8_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol8>%s</%sCol8>%s' % (namespaceprefix_ , self.gds_format_double(self.Col8, input_name='Col8'), namespaceprefix_ , eol_))
        if self.Col9 is not None:
            namespaceprefix_ = self.Col9_nsprefix_ + ':' if (UseCapturedNS_ and self.Col9_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol9>%s</%sCol9>%s' % (namespaceprefix_ , self.gds_format_double(self.Col9, input_name='Col9'), namespaceprefix_ , eol_))
        if self.Col10 is not None:
            namespaceprefix_ = self.Col10_nsprefix_ + ':' if (UseCapturedNS_ and self.Col10_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol10>%s</%sCol10>%s' % (namespaceprefix_ , self.gds_format_double(self.Col10, input_name='Col10'), namespaceprefix_ , eol_))
        if self.Col11 is not None:
            namespaceprefix_ = self.Col11_nsprefix_ + ':' if (UseCapturedNS_ and self.Col11_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol11>%s</%sCol11>%s' % (namespaceprefix_ , self.gds_format_double(self.Col11, input_name='Col11'), namespaceprefix_ , eol_))
        if self.Col12 is not None:
            namespaceprefix_ = self.Col12_nsprefix_ + ':' if (UseCapturedNS_ and self.Col12_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol12>%s</%sCol12>%s' % (namespaceprefix_ , self.gds_format_double(self.Col12, input_name='Col12'), namespaceprefix_ , eol_))
        if self.Col13 is not None:
            namespaceprefix_ = self.Col13_nsprefix_ + ':' if (UseCapturedNS_ and self.Col13_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol13>%s</%sCol13>%s' % (namespaceprefix_ , self.gds_format_double(self.Col13, input_name='Col13'), namespaceprefix_ , eol_))
        if self.Col14 is not None:
            namespaceprefix_ = self.Col14_nsprefix_ + ':' if (UseCapturedNS_ and self.Col14_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol14>%s</%sCol14>%s' % (namespaceprefix_ , self.gds_format_double(self.Col14, input_name='Col14'), namespaceprefix_ , eol_))
        if self.Col15 is not None:
            namespaceprefix_ = self.Col15_nsprefix_ + ':' if (UseCapturedNS_ and self.Col15_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol15>%s</%sCol15>%s' % (namespaceprefix_ , self.gds_format_double(self.Col15, input_name='Col15'), namespaceprefix_ , eol_))
        if self.Col16 is not None:
            namespaceprefix_ = self.Col16_nsprefix_ + ':' if (UseCapturedNS_ and self.Col16_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol16>%s</%sCol16>%s' % (namespaceprefix_ , self.gds_format_double(self.Col16, input_name='Col16'), namespaceprefix_ , eol_))
        if self.Col17 is not None:
            namespaceprefix_ = self.Col17_nsprefix_ + ':' if (UseCapturedNS_ and self.Col17_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol17>%s</%sCol17>%s' % (namespaceprefix_ , self.gds_format_double(self.Col17, input_name='Col17'), namespaceprefix_ , eol_))
        if self.Col18 is not None:
            namespaceprefix_ = self.Col18_nsprefix_ + ':' if (UseCapturedNS_ and self.Col18_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol18>%s</%sCol18>%s' % (namespaceprefix_ , self.gds_format_double(self.Col18, input_name='Col18'), namespaceprefix_ , eol_))
        if self.Col19 is not None:
            namespaceprefix_ = self.Col19_nsprefix_ + ':' if (UseCapturedNS_ and self.Col19_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol19>%s</%sCol19>%s' % (namespaceprefix_ , self.gds_format_double(self.Col19, input_name='Col19'), namespaceprefix_ , eol_))
        if self.Col20 is not None:
            namespaceprefix_ = self.Col20_nsprefix_ + ':' if (UseCapturedNS_ and self.Col20_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol20>%s</%sCol20>%s' % (namespaceprefix_ , self.gds_format_double(self.Col20, input_name='Col20'), namespaceprefix_ , eol_))
        if self.Col21 is not None:
            namespaceprefix_ = self.Col21_nsprefix_ + ':' if (UseCapturedNS_ and self.Col21_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol21>%s</%sCol21>%s' % (namespaceprefix_ , self.gds_format_double(self.Col21, input_name='Col21'), namespaceprefix_ , eol_))
        if self.Col22 is not None:
            namespaceprefix_ = self.Col22_nsprefix_ + ':' if (UseCapturedNS_ and self.Col22_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol22>%s</%sCol22>%s' % (namespaceprefix_ , self.gds_format_double(self.Col22, input_name='Col22'), namespaceprefix_ , eol_))
        if self.Col23 is not None:
            namespaceprefix_ = self.Col23_nsprefix_ + ':' if (UseCapturedNS_ and self.Col23_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol23>%s</%sCol23>%s' % (namespaceprefix_ , self.gds_format_double(self.Col23, input_name='Col23'), namespaceprefix_ , eol_))
        if self.Col24 is not None:
            namespaceprefix_ = self.Col24_nsprefix_ + ':' if (UseCapturedNS_ and self.Col24_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol24>%s</%sCol24>%s' % (namespaceprefix_ , self.gds_format_double(self.Col24, input_name='Col24'), namespaceprefix_ , eol_))
        if self.Col25 is not None:
            namespaceprefix_ = self.Col25_nsprefix_ + ':' if (UseCapturedNS_ and self.Col25_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol25>%s</%sCol25>%s' % (namespaceprefix_ , self.gds_format_double(self.Col25, input_name='Col25'), namespaceprefix_ , eol_))
        if self.Col26 is not None:
            namespaceprefix_ = self.Col26_nsprefix_ + ':' if (UseCapturedNS_ and self.Col26_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol26>%s</%sCol26>%s' % (namespaceprefix_ , self.gds_format_double(self.Col26, input_name='Col26'), namespaceprefix_ , eol_))
        if self.Col27 is not None:
            namespaceprefix_ = self.Col27_nsprefix_ + ':' if (UseCapturedNS_ and self.Col27_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol27>%s</%sCol27>%s' % (namespaceprefix_ , self.gds_format_double(self.Col27, input_name='Col27'), namespaceprefix_ , eol_))
        if self.Col28 is not None:
            namespaceprefix_ = self.Col28_nsprefix_ + ':' if (UseCapturedNS_ and self.Col28_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol28>%s</%sCol28>%s' % (namespaceprefix_ , self.gds_format_double(self.Col28, input_name='Col28'), namespaceprefix_ , eol_))
        if self.Col29 is not None:
            namespaceprefix_ = self.Col29_nsprefix_ + ':' if (UseCapturedNS_ and self.Col29_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol29>%s</%sCol29>%s' % (namespaceprefix_ , self.gds_format_double(self.Col29, input_name='Col29'), namespaceprefix_ , eol_))
        if self.Col30 is not None:
            namespaceprefix_ = self.Col30_nsprefix_ + ':' if (UseCapturedNS_ and self.Col30_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol30>%s</%sCol30>%s' % (namespaceprefix_ , self.gds_format_double(self.Col30, input_name='Col30'), namespaceprefix_ , eol_))
        if self.Col31 is not None:
            namespaceprefix_ = self.Col31_nsprefix_ + ':' if (UseCapturedNS_ and self.Col31_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol31>%s</%sCol31>%s' % (namespaceprefix_ , self.gds_format_double(self.Col31, input_name='Col31'), namespaceprefix_ , eol_))
        if self.Col32 is not None:
            namespaceprefix_ = self.Col32_nsprefix_ + ':' if (UseCapturedNS_ and self.Col32_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol32>%s</%sCol32>%s' % (namespaceprefix_ , self.gds_format_double(self.Col32, input_name='Col32'), namespaceprefix_ , eol_))
        if self.Col33 is not None:
            namespaceprefix_ = self.Col33_nsprefix_ + ':' if (UseCapturedNS_ and self.Col33_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol33>%s</%sCol33>%s' % (namespaceprefix_ , self.gds_format_double(self.Col33, input_name='Col33'), namespaceprefix_ , eol_))
        if self.Col34 is not None:
            namespaceprefix_ = self.Col34_nsprefix_ + ':' if (UseCapturedNS_ and self.Col34_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol34>%s</%sCol34>%s' % (namespaceprefix_ , self.gds_format_double(self.Col34, input_name='Col34'), namespaceprefix_ , eol_))
        if self.Col35 is not None:
            namespaceprefix_ = self.Col35_nsprefix_ + ':' if (UseCapturedNS_ and self.Col35_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol35>%s</%sCol35>%s' % (namespaceprefix_ , self.gds_format_double(self.Col35, input_name='Col35'), namespaceprefix_ , eol_))
        if self.Col36 is not None:
            namespaceprefix_ = self.Col36_nsprefix_ + ':' if (UseCapturedNS_ and self.Col36_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol36>%s</%sCol36>%s' % (namespaceprefix_ , self.gds_format_double(self.Col36, input_name='Col36'), namespaceprefix_ , eol_))
        if self.Col37 is not None:
            namespaceprefix_ = self.Col37_nsprefix_ + ':' if (UseCapturedNS_ and self.Col37_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol37>%s</%sCol37>%s' % (namespaceprefix_ , self.gds_format_double(self.Col37, input_name='Col37'), namespaceprefix_ , eol_))
        if self.Col38 is not None:
            namespaceprefix_ = self.Col38_nsprefix_ + ':' if (UseCapturedNS_ and self.Col38_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol38>%s</%sCol38>%s' % (namespaceprefix_ , self.gds_format_double(self.Col38, input_name='Col38'), namespaceprefix_ , eol_))
        if self.Col39 is not None:
            namespaceprefix_ = self.Col39_nsprefix_ + ':' if (UseCapturedNS_ and self.Col39_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol39>%s</%sCol39>%s' % (namespaceprefix_ , self.gds_format_double(self.Col39, input_name='Col39'), namespaceprefix_ , eol_))
        if self.Col40 is not None:
            namespaceprefix_ = self.Col40_nsprefix_ + ':' if (UseCapturedNS_ and self.Col40_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol40>%s</%sCol40>%s' % (namespaceprefix_ , self.gds_format_double(self.Col40, input_name='Col40'), namespaceprefix_ , eol_))
        if self.Col41 is not None:
            namespaceprefix_ = self.Col41_nsprefix_ + ':' if (UseCapturedNS_ and self.Col41_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol41>%s</%sCol41>%s' % (namespaceprefix_ , self.gds_format_double(self.Col41, input_name='Col41'), namespaceprefix_ , eol_))
        if self.Col42 is not None:
            namespaceprefix_ = self.Col42_nsprefix_ + ':' if (UseCapturedNS_ and self.Col42_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol42>%s</%sCol42>%s' % (namespaceprefix_ , self.gds_format_double(self.Col42, input_name='Col42'), namespaceprefix_ , eol_))
        if self.Col43 is not None:
            namespaceprefix_ = self.Col43_nsprefix_ + ':' if (UseCapturedNS_ and self.Col43_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol43>%s</%sCol43>%s' % (namespaceprefix_ , self.gds_format_double(self.Col43, input_name='Col43'), namespaceprefix_ , eol_))
        if self.Col44 is not None:
            namespaceprefix_ = self.Col44_nsprefix_ + ':' if (UseCapturedNS_ and self.Col44_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol44>%s</%sCol44>%s' % (namespaceprefix_ , self.gds_format_double(self.Col44, input_name='Col44'), namespaceprefix_ , eol_))
        if self.Col45 is not None:
            namespaceprefix_ = self.Col45_nsprefix_ + ':' if (UseCapturedNS_ and self.Col45_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol45>%s</%sCol45>%s' % (namespaceprefix_ , self.gds_format_double(self.Col45, input_name='Col45'), namespaceprefix_ , eol_))
        if self.Col46 is not None:
            namespaceprefix_ = self.Col46_nsprefix_ + ':' if (UseCapturedNS_ and self.Col46_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol46>%s</%sCol46>%s' % (namespaceprefix_ , self.gds_format_double(self.Col46, input_name='Col46'), namespaceprefix_ , eol_))
        if self.Col47 is not None:
            namespaceprefix_ = self.Col47_nsprefix_ + ':' if (UseCapturedNS_ and self.Col47_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol47>%s</%sCol47>%s' % (namespaceprefix_ , self.gds_format_double(self.Col47, input_name='Col47'), namespaceprefix_ , eol_))
        if self.Col48 is not None:
            namespaceprefix_ = self.Col48_nsprefix_ + ':' if (UseCapturedNS_ and self.Col48_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol48>%s</%sCol48>%s' % (namespaceprefix_ , self.gds_format_double(self.Col48, input_name='Col48'), namespaceprefix_ , eol_))
        if self.Col49 is not None:
            namespaceprefix_ = self.Col49_nsprefix_ + ':' if (UseCapturedNS_ and self.Col49_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol49>%s</%sCol49>%s' % (namespaceprefix_ , self.gds_format_double(self.Col49, input_name='Col49'), namespaceprefix_ , eol_))
        if self.Col50 is not None:
            namespaceprefix_ = self.Col50_nsprefix_ + ':' if (UseCapturedNS_ and self.Col50_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol50>%s</%sCol50>%s' % (namespaceprefix_ , self.gds_format_double(self.Col50, input_name='Col50'), namespaceprefix_ , eol_))
        if self.Col51 is not None:
            namespaceprefix_ = self.Col51_nsprefix_ + ':' if (UseCapturedNS_ and self.Col51_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol51>%s</%sCol51>%s' % (namespaceprefix_ , self.gds_format_double(self.Col51, input_name='Col51'), namespaceprefix_ , eol_))
        if self.Col52 is not None:
            namespaceprefix_ = self.Col52_nsprefix_ + ':' if (UseCapturedNS_ and self.Col52_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol52>%s</%sCol52>%s' % (namespaceprefix_ , self.gds_format_double(self.Col52, input_name='Col52'), namespaceprefix_ , eol_))
        if self.Col53 is not None:
            namespaceprefix_ = self.Col53_nsprefix_ + ':' if (UseCapturedNS_ and self.Col53_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol53>%s</%sCol53>%s' % (namespaceprefix_ , self.gds_format_double(self.Col53, input_name='Col53'), namespaceprefix_ , eol_))
        if self.Col54 is not None:
            namespaceprefix_ = self.Col54_nsprefix_ + ':' if (UseCapturedNS_ and self.Col54_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol54>%s</%sCol54>%s' % (namespaceprefix_ , self.gds_format_double(self.Col54, input_name='Col54'), namespaceprefix_ , eol_))
        if self.Col55 is not None:
            namespaceprefix_ = self.Col55_nsprefix_ + ':' if (UseCapturedNS_ and self.Col55_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol55>%s</%sCol55>%s' % (namespaceprefix_ , self.gds_format_double(self.Col55, input_name='Col55'), namespaceprefix_ , eol_))
        if self.Col56 is not None:
            namespaceprefix_ = self.Col56_nsprefix_ + ':' if (UseCapturedNS_ and self.Col56_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol56>%s</%sCol56>%s' % (namespaceprefix_ , self.gds_format_double(self.Col56, input_name='Col56'), namespaceprefix_ , eol_))
        if self.Col57 is not None:
            namespaceprefix_ = self.Col57_nsprefix_ + ':' if (UseCapturedNS_ and self.Col57_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol57>%s</%sCol57>%s' % (namespaceprefix_ , self.gds_format_double(self.Col57, input_name='Col57'), namespaceprefix_ , eol_))
        if self.Col58 is not None:
            namespaceprefix_ = self.Col58_nsprefix_ + ':' if (UseCapturedNS_ and self.Col58_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol58>%s</%sCol58>%s' % (namespaceprefix_ , self.gds_format_double(self.Col58, input_name='Col58'), namespaceprefix_ , eol_))
        if self.Col59 is not None:
            namespaceprefix_ = self.Col59_nsprefix_ + ':' if (UseCapturedNS_ and self.Col59_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol59>%s</%sCol59>%s' % (namespaceprefix_ , self.gds_format_double(self.Col59, input_name='Col59'), namespaceprefix_ , eol_))
        if self.Col60 is not None:
            namespaceprefix_ = self.Col60_nsprefix_ + ':' if (UseCapturedNS_ and self.Col60_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol60>%s</%sCol60>%s' % (namespaceprefix_ , self.gds_format_double(self.Col60, input_name='Col60'), namespaceprefix_ , eol_))
        if self.Col61 is not None:
            namespaceprefix_ = self.Col61_nsprefix_ + ':' if (UseCapturedNS_ and self.Col61_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol61>%s</%sCol61>%s' % (namespaceprefix_ , self.gds_format_double(self.Col61, input_name='Col61'), namespaceprefix_ , eol_))
        if self.Col62 is not None:
            namespaceprefix_ = self.Col62_nsprefix_ + ':' if (UseCapturedNS_ and self.Col62_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol62>%s</%sCol62>%s' % (namespaceprefix_ , self.gds_format_double(self.Col62, input_name='Col62'), namespaceprefix_ , eol_))
        if self.Col63 is not None:
            namespaceprefix_ = self.Col63_nsprefix_ + ':' if (UseCapturedNS_ and self.Col63_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol63>%s</%sCol63>%s' % (namespaceprefix_ , self.gds_format_double(self.Col63, input_name='Col63'), namespaceprefix_ , eol_))
        if self.Col64 is not None:
            namespaceprefix_ = self.Col64_nsprefix_ + ':' if (UseCapturedNS_ and self.Col64_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCol64>%s</%sCol64>%s' % (namespaceprefix_ , self.gds_format_double(self.Col64, input_name='Col64'), namespaceprefix_ , eol_))
    def exportLiteral(self, outfile, level, name_='MDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Row is not None and 'Row' not in already_processed:
            already_processed.add('Row')
            showIndent(outfile, level)
            outfile.write('Row=%d,\n' % (self.Row,))
        if self.Axis1 is not None and 'Axis1' not in already_processed:
            already_processed.add('Axis1')
            showIndent(outfile, level)
            outfile.write('Axis1=%d,\n' % (self.Axis1,))
        if self.Axis2 is not None and 'Axis2' not in already_processed:
            already_processed.add('Axis2')
            showIndent(outfile, level)
            outfile.write('Axis2=%d,\n' % (self.Axis2,))
        if self.Axis3 is not None and 'Axis3' not in already_processed:
            already_processed.add('Axis3')
            showIndent(outfile, level)
            outfile.write('Axis3=%d,\n' % (self.Axis3,))
        if self.Axis4 is not None and 'Axis4' not in already_processed:
            already_processed.add('Axis4')
            showIndent(outfile, level)
            outfile.write('Axis4=%d,\n' % (self.Axis4,))
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.Col1 is not None:
            showIndent(outfile, level)
            outfile.write(Col1=self.gds_format_double(self.Col1))
        if self.Col2 is not None:
            showIndent(outfile, level)
            outfile.write(Col2=self.gds_format_double(self.Col2))
        if self.Col3 is not None:
            showIndent(outfile, level)
            outfile.write(Col3=self.gds_format_double(self.Col3))
        if self.Col4 is not None:
            showIndent(outfile, level)
            outfile.write(Col4=self.gds_format_double(self.Col4))
        if self.Col5 is not None:
            showIndent(outfile, level)
            outfile.write(Col5=self.gds_format_double(self.Col5))
        if self.Col6 is not None:
            showIndent(outfile, level)
            outfile.write(Col6=self.gds_format_double(self.Col6))
        if self.Col7 is not None:
            showIndent(outfile, level)
            outfile.write(Col7=self.gds_format_double(self.Col7))
        if self.Col8 is not None:
            showIndent(outfile, level)
            outfile.write(Col8=self.gds_format_double(self.Col8))
        if self.Col9 is not None:
            showIndent(outfile, level)
            outfile.write(Col9=self.gds_format_double(self.Col9))
        if self.Col10 is not None:
            showIndent(outfile, level)
            outfile.write(Col10=self.gds_format_double(self.Col10))
        if self.Col11 is not None:
            showIndent(outfile, level)
            outfile.write(Col11=self.gds_format_double(self.Col11))
        if self.Col12 is not None:
            showIndent(outfile, level)
            outfile.write(Col12=self.gds_format_double(self.Col12))
        if self.Col13 is not None:
            showIndent(outfile, level)
            outfile.write(Col13=self.gds_format_double(self.Col13))
        if self.Col14 is not None:
            showIndent(outfile, level)
            outfile.write(Col14=self.gds_format_double(self.Col14))
        if self.Col15 is not None:
            showIndent(outfile, level)
            outfile.write(Col15=self.gds_format_double(self.Col15))
        if self.Col16 is not None:
            showIndent(outfile, level)
            outfile.write(Col16=self.gds_format_double(self.Col16))
        if self.Col17 is not None:
            showIndent(outfile, level)
            outfile.write(Col17=self.gds_format_double(self.Col17))
        if self.Col18 is not None:
            showIndent(outfile, level)
            outfile.write(Col18=self.gds_format_double(self.Col18))
        if self.Col19 is not None:
            showIndent(outfile, level)
            outfile.write(Col19=self.gds_format_double(self.Col19))
        if self.Col20 is not None:
            showIndent(outfile, level)
            outfile.write(Col20=self.gds_format_double(self.Col20))
        if self.Col21 is not None:
            showIndent(outfile, level)
            outfile.write(Col21=self.gds_format_double(self.Col21))
        if self.Col22 is not None:
            showIndent(outfile, level)
            outfile.write(Col22=self.gds_format_double(self.Col22))
        if self.Col23 is not None:
            showIndent(outfile, level)
            outfile.write(Col23=self.gds_format_double(self.Col23))
        if self.Col24 is not None:
            showIndent(outfile, level)
            outfile.write(Col24=self.gds_format_double(self.Col24))
        if self.Col25 is not None:
            showIndent(outfile, level)
            outfile.write(Col25=self.gds_format_double(self.Col25))
        if self.Col26 is not None:
            showIndent(outfile, level)
            outfile.write(Col26=self.gds_format_double(self.Col26))
        if self.Col27 is not None:
            showIndent(outfile, level)
            outfile.write(Col27=self.gds_format_double(self.Col27))
        if self.Col28 is not None:
            showIndent(outfile, level)
            outfile.write(Col28=self.gds_format_double(self.Col28))
        if self.Col29 is not None:
            showIndent(outfile, level)
            outfile.write(Col29=self.gds_format_double(self.Col29))
        if self.Col30 is not None:
            showIndent(outfile, level)
            outfile.write(Col30=self.gds_format_double(self.Col30))
        if self.Col31 is not None:
            showIndent(outfile, level)
            outfile.write(Col31=self.gds_format_double(self.Col31))
        if self.Col32 is not None:
            showIndent(outfile, level)
            outfile.write(Col32=self.gds_format_double(self.Col32))
        if self.Col33 is not None:
            showIndent(outfile, level)
            outfile.write(Col33=self.gds_format_double(self.Col33))
        if self.Col34 is not None:
            showIndent(outfile, level)
            outfile.write(Col34=self.gds_format_double(self.Col34))
        if self.Col35 is not None:
            showIndent(outfile, level)
            outfile.write(Col35=self.gds_format_double(self.Col35))
        if self.Col36 is not None:
            showIndent(outfile, level)
            outfile.write(Col36=self.gds_format_double(self.Col36))
        if self.Col37 is not None:
            showIndent(outfile, level)
            outfile.write(Col37=self.gds_format_double(self.Col37))
        if self.Col38 is not None:
            showIndent(outfile, level)
            outfile.write(Col38=self.gds_format_double(self.Col38))
        if self.Col39 is not None:
            showIndent(outfile, level)
            outfile.write(Col39=self.gds_format_double(self.Col39))
        if self.Col40 is not None:
            showIndent(outfile, level)
            outfile.write(Col40=self.gds_format_double(self.Col40))
        if self.Col41 is not None:
            showIndent(outfile, level)
            outfile.write(Col41=self.gds_format_double(self.Col41))
        if self.Col42 is not None:
            showIndent(outfile, level)
            outfile.write(Col42=self.gds_format_double(self.Col42))
        if self.Col43 is not None:
            showIndent(outfile, level)
            outfile.write(Col43=self.gds_format_double(self.Col43))
        if self.Col44 is not None:
            showIndent(outfile, level)
            outfile.write(Col44=self.gds_format_double(self.Col44))
        if self.Col45 is not None:
            showIndent(outfile, level)
            outfile.write(Col45=self.gds_format_double(self.Col45))
        if self.Col46 is not None:
            showIndent(outfile, level)
            outfile.write(Col46=self.gds_format_double(self.Col46))
        if self.Col47 is not None:
            showIndent(outfile, level)
            outfile.write(Col47=self.gds_format_double(self.Col47))
        if self.Col48 is not None:
            showIndent(outfile, level)
            outfile.write(Col48=self.gds_format_double(self.Col48))
        if self.Col49 is not None:
            showIndent(outfile, level)
            outfile.write(Col49=self.gds_format_double(self.Col49))
        if self.Col50 is not None:
            showIndent(outfile, level)
            outfile.write(Col50=self.gds_format_double(self.Col50))
        if self.Col51 is not None:
            showIndent(outfile, level)
            outfile.write(Col51=self.gds_format_double(self.Col51))
        if self.Col52 is not None:
            showIndent(outfile, level)
            outfile.write(Col52=self.gds_format_double(self.Col52))
        if self.Col53 is not None:
            showIndent(outfile, level)
            outfile.write(Col53=self.gds_format_double(self.Col53))
        if self.Col54 is not None:
            showIndent(outfile, level)
            outfile.write(Col54=self.gds_format_double(self.Col54))
        if self.Col55 is not None:
            showIndent(outfile, level)
            outfile.write(Col55=self.gds_format_double(self.Col55))
        if self.Col56 is not None:
            showIndent(outfile, level)
            outfile.write(Col56=self.gds_format_double(self.Col56))
        if self.Col57 is not None:
            showIndent(outfile, level)
            outfile.write(Col57=self.gds_format_double(self.Col57))
        if self.Col58 is not None:
            showIndent(outfile, level)
            outfile.write(Col58=self.gds_format_double(self.Col58))
        if self.Col59 is not None:
            showIndent(outfile, level)
            outfile.write(Col59=self.gds_format_double(self.Col59))
        if self.Col60 is not None:
            showIndent(outfile, level)
            outfile.write(Col60=self.gds_format_double(self.Col60))
        if self.Col61 is not None:
            showIndent(outfile, level)
            outfile.write(Col61=self.gds_format_double(self.Col61))
        if self.Col62 is not None:
            showIndent(outfile, level)
            outfile.write(Col62=self.gds_format_double(self.Col62))
        if self.Col63 is not None:
            showIndent(outfile, level)
            outfile.write(Col63=self.gds_format_double(self.Col63))
        if self.Col64 is not None:
            showIndent(outfile, level)
            outfile.write(Col64=self.gds_format_double(self.Col64))
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
        value = find_attr_value_('Row', node)
        if value is not None and 'Row' not in already_processed:
            already_processed.add('Row')
            self.Row = self.gds_parse_integer(value, node, 'Row')
        value = find_attr_value_('Axis1', node)
        if value is not None and 'Axis1' not in already_processed:
            already_processed.add('Axis1')
            self.Axis1 = self.gds_parse_integer(value, node, 'Axis1')
        value = find_attr_value_('Axis2', node)
        if value is not None and 'Axis2' not in already_processed:
            already_processed.add('Axis2')
            self.Axis2 = self.gds_parse_integer(value, node, 'Axis2')
        value = find_attr_value_('Axis3', node)
        if value is not None and 'Axis3' not in already_processed:
            already_processed.add('Axis3')
            self.Axis3 = self.gds_parse_integer(value, node, 'Axis3')
        value = find_attr_value_('Axis4', node)
        if value is not None and 'Axis4' not in already_processed:
            already_processed.add('Axis4')
            self.Axis4 = self.gds_parse_integer(value, node, 'Axis4')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Col1' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col1')
            fval_ = self.gds_validate_double(fval_, node, 'Col1')
            self.Col1 = fval_
            self.Col1_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col2' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col2')
            fval_ = self.gds_validate_double(fval_, node, 'Col2')
            self.Col2 = fval_
            self.Col2_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col3' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col3')
            fval_ = self.gds_validate_double(fval_, node, 'Col3')
            self.Col3 = fval_
            self.Col3_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col4' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col4')
            fval_ = self.gds_validate_double(fval_, node, 'Col4')
            self.Col4 = fval_
            self.Col4_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col5' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col5')
            fval_ = self.gds_validate_double(fval_, node, 'Col5')
            self.Col5 = fval_
            self.Col5_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col6' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col6')
            fval_ = self.gds_validate_double(fval_, node, 'Col6')
            self.Col6 = fval_
            self.Col6_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col7' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col7')
            fval_ = self.gds_validate_double(fval_, node, 'Col7')
            self.Col7 = fval_
            self.Col7_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col8' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col8')
            fval_ = self.gds_validate_double(fval_, node, 'Col8')
            self.Col8 = fval_
            self.Col8_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col9' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col9')
            fval_ = self.gds_validate_double(fval_, node, 'Col9')
            self.Col9 = fval_
            self.Col9_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col10' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col10')
            fval_ = self.gds_validate_double(fval_, node, 'Col10')
            self.Col10 = fval_
            self.Col10_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col11' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col11')
            fval_ = self.gds_validate_double(fval_, node, 'Col11')
            self.Col11 = fval_
            self.Col11_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col12' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col12')
            fval_ = self.gds_validate_double(fval_, node, 'Col12')
            self.Col12 = fval_
            self.Col12_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col13' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col13')
            fval_ = self.gds_validate_double(fval_, node, 'Col13')
            self.Col13 = fval_
            self.Col13_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col14' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col14')
            fval_ = self.gds_validate_double(fval_, node, 'Col14')
            self.Col14 = fval_
            self.Col14_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col15' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col15')
            fval_ = self.gds_validate_double(fval_, node, 'Col15')
            self.Col15 = fval_
            self.Col15_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col16' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col16')
            fval_ = self.gds_validate_double(fval_, node, 'Col16')
            self.Col16 = fval_
            self.Col16_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col17' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col17')
            fval_ = self.gds_validate_double(fval_, node, 'Col17')
            self.Col17 = fval_
            self.Col17_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col18' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col18')
            fval_ = self.gds_validate_double(fval_, node, 'Col18')
            self.Col18 = fval_
            self.Col18_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col19' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col19')
            fval_ = self.gds_validate_double(fval_, node, 'Col19')
            self.Col19 = fval_
            self.Col19_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col20' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col20')
            fval_ = self.gds_validate_double(fval_, node, 'Col20')
            self.Col20 = fval_
            self.Col20_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col21' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col21')
            fval_ = self.gds_validate_double(fval_, node, 'Col21')
            self.Col21 = fval_
            self.Col21_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col22' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col22')
            fval_ = self.gds_validate_double(fval_, node, 'Col22')
            self.Col22 = fval_
            self.Col22_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col23' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col23')
            fval_ = self.gds_validate_double(fval_, node, 'Col23')
            self.Col23 = fval_
            self.Col23_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col24' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col24')
            fval_ = self.gds_validate_double(fval_, node, 'Col24')
            self.Col24 = fval_
            self.Col24_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col25' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col25')
            fval_ = self.gds_validate_double(fval_, node, 'Col25')
            self.Col25 = fval_
            self.Col25_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col26' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col26')
            fval_ = self.gds_validate_double(fval_, node, 'Col26')
            self.Col26 = fval_
            self.Col26_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col27' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col27')
            fval_ = self.gds_validate_double(fval_, node, 'Col27')
            self.Col27 = fval_
            self.Col27_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col28' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col28')
            fval_ = self.gds_validate_double(fval_, node, 'Col28')
            self.Col28 = fval_
            self.Col28_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col29' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col29')
            fval_ = self.gds_validate_double(fval_, node, 'Col29')
            self.Col29 = fval_
            self.Col29_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col30' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col30')
            fval_ = self.gds_validate_double(fval_, node, 'Col30')
            self.Col30 = fval_
            self.Col30_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col31' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col31')
            fval_ = self.gds_validate_double(fval_, node, 'Col31')
            self.Col31 = fval_
            self.Col31_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col32' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col32')
            fval_ = self.gds_validate_double(fval_, node, 'Col32')
            self.Col32 = fval_
            self.Col32_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col33' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col33')
            fval_ = self.gds_validate_double(fval_, node, 'Col33')
            self.Col33 = fval_
            self.Col33_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col34' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col34')
            fval_ = self.gds_validate_double(fval_, node, 'Col34')
            self.Col34 = fval_
            self.Col34_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col35' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col35')
            fval_ = self.gds_validate_double(fval_, node, 'Col35')
            self.Col35 = fval_
            self.Col35_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col36' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col36')
            fval_ = self.gds_validate_double(fval_, node, 'Col36')
            self.Col36 = fval_
            self.Col36_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col37' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col37')
            fval_ = self.gds_validate_double(fval_, node, 'Col37')
            self.Col37 = fval_
            self.Col37_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col38' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col38')
            fval_ = self.gds_validate_double(fval_, node, 'Col38')
            self.Col38 = fval_
            self.Col38_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col39' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col39')
            fval_ = self.gds_validate_double(fval_, node, 'Col39')
            self.Col39 = fval_
            self.Col39_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col40' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col40')
            fval_ = self.gds_validate_double(fval_, node, 'Col40')
            self.Col40 = fval_
            self.Col40_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col41' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col41')
            fval_ = self.gds_validate_double(fval_, node, 'Col41')
            self.Col41 = fval_
            self.Col41_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col42' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col42')
            fval_ = self.gds_validate_double(fval_, node, 'Col42')
            self.Col42 = fval_
            self.Col42_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col43' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col43')
            fval_ = self.gds_validate_double(fval_, node, 'Col43')
            self.Col43 = fval_
            self.Col43_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col44' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col44')
            fval_ = self.gds_validate_double(fval_, node, 'Col44')
            self.Col44 = fval_
            self.Col44_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col45' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col45')
            fval_ = self.gds_validate_double(fval_, node, 'Col45')
            self.Col45 = fval_
            self.Col45_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col46' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col46')
            fval_ = self.gds_validate_double(fval_, node, 'Col46')
            self.Col46 = fval_
            self.Col46_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col47' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col47')
            fval_ = self.gds_validate_double(fval_, node, 'Col47')
            self.Col47 = fval_
            self.Col47_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col48' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col48')
            fval_ = self.gds_validate_double(fval_, node, 'Col48')
            self.Col48 = fval_
            self.Col48_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col49' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col49')
            fval_ = self.gds_validate_double(fval_, node, 'Col49')
            self.Col49 = fval_
            self.Col49_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col50' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col50')
            fval_ = self.gds_validate_double(fval_, node, 'Col50')
            self.Col50 = fval_
            self.Col50_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col51' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col51')
            fval_ = self.gds_validate_double(fval_, node, 'Col51')
            self.Col51 = fval_
            self.Col51_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col52' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col52')
            fval_ = self.gds_validate_double(fval_, node, 'Col52')
            self.Col52 = fval_
            self.Col52_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col53' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col53')
            fval_ = self.gds_validate_double(fval_, node, 'Col53')
            self.Col53 = fval_
            self.Col53_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col54' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col54')
            fval_ = self.gds_validate_double(fval_, node, 'Col54')
            self.Col54 = fval_
            self.Col54_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col55' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col55')
            fval_ = self.gds_validate_double(fval_, node, 'Col55')
            self.Col55 = fval_
            self.Col55_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col56' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col56')
            fval_ = self.gds_validate_double(fval_, node, 'Col56')
            self.Col56 = fval_
            self.Col56_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col57' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col57')
            fval_ = self.gds_validate_double(fval_, node, 'Col57')
            self.Col57 = fval_
            self.Col57_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col58' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col58')
            fval_ = self.gds_validate_double(fval_, node, 'Col58')
            self.Col58 = fval_
            self.Col58_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col59' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col59')
            fval_ = self.gds_validate_double(fval_, node, 'Col59')
            self.Col59 = fval_
            self.Col59_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col60' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col60')
            fval_ = self.gds_validate_double(fval_, node, 'Col60')
            self.Col60 = fval_
            self.Col60_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col61' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col61')
            fval_ = self.gds_validate_double(fval_, node, 'Col61')
            self.Col61 = fval_
            self.Col61_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col62' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col62')
            fval_ = self.gds_validate_double(fval_, node, 'Col62')
            self.Col62 = fval_
            self.Col62_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col63' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col63')
            fval_ = self.gds_validate_double(fval_, node, 'Col63')
            self.Col63 = fval_
            self.Col63_nsprefix_ = child_.prefix
        elif nodeName_ == 'Col64' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Col64')
            fval_ = self.gds_validate_double(fval_, node, 'Col64')
            self.Col64 = fval_
            self.Col64_nsprefix_ = child_.prefix
# end class MDataType


class BetasType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Number=None, Beta=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Number = Number
        self.Number_nsprefix_ = None
        if Beta is None:
            self.Beta = []
        else:
            self.Beta = Beta
        self.Beta_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BetasType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BetasType.subclass:
            return BetasType.subclass(*args_, **kwargs_)
        else:
            return BetasType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Number(self):
        return self.Number
    def set_Number(self, Number):
        self.Number = Number
    def get_Beta(self):
        return self.Beta
    def set_Beta(self, Beta):
        self.Beta = Beta
    def add_Beta(self, value):
        self.Beta.append(value)
    def insert_Beta_at(self, index, value):
        self.Beta.insert(index, value)
    def replace_Beta_at(self, index, value):
        self.Beta[index] = value
    def _hasContent(self):
        if (
            self.Number is not None or
            self.Beta
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='BetasType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BetasType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BetasType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='BetasType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='BetasType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='BetasType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='BetasType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Number is not None:
            namespaceprefix_ = self.Number_nsprefix_ + ':' if (UseCapturedNS_ and self.Number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumber>%s</%sNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.Number, input_name='Number'), namespaceprefix_ , eol_))
        for Beta_ in self.Beta:
            namespaceprefix_ = self.Beta_nsprefix_ + ':' if (UseCapturedNS_ and self.Beta_nsprefix_) else ''
            Beta_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Beta', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='BetasType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.Number is not None:
            showIndent(outfile, level)
            outfile.write('Number=%d,\n' % self.Number)
        showIndent(outfile, level)
        outfile.write('Beta=[\n')
        level += 1
        for Beta_ in self.Beta:
            showIndent(outfile, level)
            outfile.write('model_.BetaType(\n')
            Beta_.exportLiteral(outfile, level, name_='BetaType')
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
        if nodeName_ == 'Number' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Number')
            ival_ = self.gds_validate_integer(ival_, node, 'Number')
            self.Number = ival_
            self.Number_nsprefix_ = child_.prefix
        elif nodeName_ == 'Beta':
            obj_ = BetaType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Beta.append(obj_)
            obj_.original_tagname_ = 'Beta'
# end class BetasType


class BetaType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, Label=None, I=None, J=None, Value=None, FlowRef=None, OpZeroOrOne=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Position = _cast(int, Position)
        self.Position_nsprefix_ = None
        self.Label = Label
        self.Label_nsprefix_ = None
        self.I = I
        self.I_nsprefix_ = None
        self.J = J
        self.J_nsprefix_ = None
        self.Value = Value
        self.Value_nsprefix_ = None
        self.FlowRef = FlowRef
        self.FlowRef_nsprefix_ = None
        self.OpZeroOrOne = OpZeroOrOne
        self.OpZeroOrOne_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BetaType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BetaType.subclass:
            return BetaType.subclass(*args_, **kwargs_)
        else:
            return BetaType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Label(self):
        return self.Label
    def set_Label(self, Label):
        self.Label = Label
    def get_I(self):
        return self.I
    def set_I(self, I):
        self.I = I
    def get_J(self):
        return self.J
    def set_J(self, J):
        self.J = J
    def get_Value(self):
        return self.Value
    def set_Value(self, Value):
        self.Value = Value
    def get_FlowRef(self):
        return self.FlowRef
    def set_FlowRef(self, FlowRef):
        self.FlowRef = FlowRef
    def get_OpZeroOrOne(self):
        return self.OpZeroOrOne
    def set_OpZeroOrOne(self, OpZeroOrOne):
        self.OpZeroOrOne = OpZeroOrOne
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def _hasContent(self):
        if (
            self.Label is not None or
            self.I is not None or
            self.J is not None or
            self.Value is not None or
            self.FlowRef is not None or
            self.OpZeroOrOne is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='BetaType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BetaType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BetaType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='BetaType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='BetaType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='BetaType'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position="%s"' % self.gds_format_integer(self.Position, input_name='Position'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='BetaType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Label is not None:
            namespaceprefix_ = self.Label_nsprefix_ + ':' if (UseCapturedNS_ and self.Label_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sLabel>%s</%sLabel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Label), input_name='Label')), namespaceprefix_ , eol_))
        if self.I is not None:
            namespaceprefix_ = self.I_nsprefix_ + ':' if (UseCapturedNS_ and self.I_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sI>%s</%sI>%s' % (namespaceprefix_ , self.gds_format_integer(self.I, input_name='I'), namespaceprefix_ , eol_))
        if self.J is not None:
            namespaceprefix_ = self.J_nsprefix_ + ':' if (UseCapturedNS_ and self.J_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sJ>%s</%sJ>%s' % (namespaceprefix_ , self.gds_format_integer(self.J, input_name='J'), namespaceprefix_ , eol_))
        if self.Value is not None:
            namespaceprefix_ = self.Value_nsprefix_ + ':' if (UseCapturedNS_ and self.Value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValue>%s</%sValue>%s' % (namespaceprefix_ , self.gds_format_double(self.Value, input_name='Value'), namespaceprefix_ , eol_))
        if self.FlowRef is not None:
            namespaceprefix_ = self.FlowRef_nsprefix_ + ':' if (UseCapturedNS_ and self.FlowRef_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sFlowRef>%s</%sFlowRef>%s' % (namespaceprefix_ , self.gds_format_integer(self.FlowRef, input_name='FlowRef'), namespaceprefix_ , eol_))
        if self.OpZeroOrOne is not None:
            namespaceprefix_ = self.OpZeroOrOne_nsprefix_ + ':' if (UseCapturedNS_ and self.OpZeroOrOne_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOpZeroOrOne>%s</%sOpZeroOrOne>%s' % (namespaceprefix_ , self.gds_format_integer(self.OpZeroOrOne, input_name='OpZeroOrOne'), namespaceprefix_ , eol_))
    def exportLiteral(self, outfile, level, name_='BetaType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            showIndent(outfile, level)
            outfile.write('Position=%d,\n' % (self.Position,))
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.Label is not None:
            showIndent(outfile, level)
            outfile.write('Label=%s,\n' % self.gds_encode(quote_python(self.Label)))
        if self.I is not None:
            showIndent(outfile, level)
            outfile.write('I=%d,\n' % self.I)
        if self.J is not None:
            showIndent(outfile, level)
            outfile.write('J=%d,\n' % self.J)
        if self.Value is not None:
            showIndent(outfile, level)
            outfile.write(Value=self.gds_format_double(self.Value))
        if self.FlowRef is not None:
            showIndent(outfile, level)
            outfile.write('FlowRef=%d,\n' % self.FlowRef)
        if self.OpZeroOrOne is not None:
            showIndent(outfile, level)
            outfile.write('OpZeroOrOne=%d,\n' % self.OpZeroOrOne)
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
        if nodeName_ == 'Label':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Label')
            value_ = self.gds_validate_string(value_, node, 'Label')
            self.Label = value_
            self.Label_nsprefix_ = child_.prefix
        elif nodeName_ == 'I' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'I')
            ival_ = self.gds_validate_integer(ival_, node, 'I')
            self.I = ival_
            self.I_nsprefix_ = child_.prefix
        elif nodeName_ == 'J' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'J')
            ival_ = self.gds_validate_integer(ival_, node, 'J')
            self.J = ival_
            self.J_nsprefix_ = child_.prefix
        elif nodeName_ == 'Value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Value')
            fval_ = self.gds_validate_double(fval_, node, 'Value')
            self.Value = fval_
            self.Value_nsprefix_ = child_.prefix
        elif nodeName_ == 'FlowRef' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'FlowRef')
            ival_ = self.gds_validate_integer(ival_, node, 'FlowRef')
            self.FlowRef = ival_
            self.FlowRef_nsprefix_ = child_.prefix
        elif nodeName_ == 'OpZeroOrOne' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'OpZeroOrOne')
            ival_ = self.gds_validate_integer(ival_, node, 'OpZeroOrOne')
            self.OpZeroOrOne = ival_
            self.OpZeroOrOne_nsprefix_ = child_.prefix
# end class BetaType


class FunctionalInputsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Number=None, FunctionInput=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Number = Number
        self.Number_nsprefix_ = None
        if FunctionInput is None:
            self.FunctionInput = []
        else:
            self.FunctionInput = FunctionInput
        self.FunctionInput_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, FunctionalInputsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if FunctionalInputsType.subclass:
            return FunctionalInputsType.subclass(*args_, **kwargs_)
        else:
            return FunctionalInputsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Number(self):
        return self.Number
    def set_Number(self, Number):
        self.Number = Number
    def get_FunctionInput(self):
        return self.FunctionInput
    def set_FunctionInput(self, FunctionInput):
        self.FunctionInput = FunctionInput
    def add_FunctionInput(self, value):
        self.FunctionInput.append(value)
    def insert_FunctionInput_at(self, index, value):
        self.FunctionInput.insert(index, value)
    def replace_FunctionInput_at(self, index, value):
        self.FunctionInput[index] = value
    def _hasContent(self):
        if (
            self.Number is not None or
            self.FunctionInput
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='FunctionalInputsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('FunctionalInputsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'FunctionalInputsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='FunctionalInputsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='FunctionalInputsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='FunctionalInputsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='FunctionalInputsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Number is not None:
            namespaceprefix_ = self.Number_nsprefix_ + ':' if (UseCapturedNS_ and self.Number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumber>%s</%sNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.Number, input_name='Number'), namespaceprefix_ , eol_))
        for FunctionInput_ in self.FunctionInput:
            namespaceprefix_ = self.FunctionInput_nsprefix_ + ':' if (UseCapturedNS_ and self.FunctionInput_nsprefix_) else ''
            FunctionInput_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='FunctionInput', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='FunctionalInputsType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.Number is not None:
            showIndent(outfile, level)
            outfile.write('Number=%d,\n' % self.Number)
        showIndent(outfile, level)
        outfile.write('FunctionInput=[\n')
        level += 1
        for FunctionInput_ in self.FunctionInput:
            showIndent(outfile, level)
            outfile.write('model_.FunctionInputType(\n')
            FunctionInput_.exportLiteral(outfile, level, name_='FunctionInputType')
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
        if nodeName_ == 'Number' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Number')
            ival_ = self.gds_validate_integer(ival_, node, 'Number')
            self.Number = ival_
            self.Number_nsprefix_ = child_.prefix
        elif nodeName_ == 'FunctionInput':
            obj_ = FunctionInputType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.FunctionInput.append(obj_)
            obj_.original_tagname_ = 'FunctionInput'
# end class FunctionalInputsType


class FunctionInputType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, Label=None, I=None, J=None, Value=None, FlowRef=None, OpZeroOrOne=None, BaseSetInd=None, Script=None, InputReference=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Position = _cast(int, Position)
        self.Position_nsprefix_ = None
        self.Label = Label
        self.Label_nsprefix_ = None
        self.I = I
        self.I_nsprefix_ = None
        self.J = J
        self.J_nsprefix_ = None
        self.Value = Value
        self.Value_nsprefix_ = None
        self.FlowRef = FlowRef
        self.FlowRef_nsprefix_ = None
        self.OpZeroOrOne = OpZeroOrOne
        self.OpZeroOrOne_nsprefix_ = None
        self.BaseSetInd = BaseSetInd
        self.BaseSetInd_nsprefix_ = None
        self.Script = Script
        self.Script_nsprefix_ = None
        self.InputReference = InputReference
        self.InputReference_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, FunctionInputType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if FunctionInputType.subclass:
            return FunctionInputType.subclass(*args_, **kwargs_)
        else:
            return FunctionInputType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Label(self):
        return self.Label
    def set_Label(self, Label):
        self.Label = Label
    def get_I(self):
        return self.I
    def set_I(self, I):
        self.I = I
    def get_J(self):
        return self.J
    def set_J(self, J):
        self.J = J
    def get_Value(self):
        return self.Value
    def set_Value(self, Value):
        self.Value = Value
    def get_FlowRef(self):
        return self.FlowRef
    def set_FlowRef(self, FlowRef):
        self.FlowRef = FlowRef
    def get_OpZeroOrOne(self):
        return self.OpZeroOrOne
    def set_OpZeroOrOne(self, OpZeroOrOne):
        self.OpZeroOrOne = OpZeroOrOne
    def get_BaseSetInd(self):
        return self.BaseSetInd
    def set_BaseSetInd(self, BaseSetInd):
        self.BaseSetInd = BaseSetInd
    def get_Script(self):
        return self.Script
    def set_Script(self, Script):
        self.Script = Script
    def get_InputReference(self):
        return self.InputReference
    def set_InputReference(self, InputReference):
        self.InputReference = InputReference
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def _hasContent(self):
        if (
            self.Label is not None or
            self.I is not None or
            self.J is not None or
            self.Value is not None or
            self.FlowRef is not None or
            self.OpZeroOrOne is not None or
            self.BaseSetInd is not None or
            self.Script is not None or
            self.InputReference is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='FunctionInputType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('FunctionInputType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'FunctionInputType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='FunctionInputType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='FunctionInputType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='FunctionInputType'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position="%s"' % self.gds_format_integer(self.Position, input_name='Position'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='FunctionInputType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Label is not None:
            namespaceprefix_ = self.Label_nsprefix_ + ':' if (UseCapturedNS_ and self.Label_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sLabel>%s</%sLabel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Label), input_name='Label')), namespaceprefix_ , eol_))
        if self.I is not None:
            namespaceprefix_ = self.I_nsprefix_ + ':' if (UseCapturedNS_ and self.I_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sI>%s</%sI>%s' % (namespaceprefix_ , self.gds_format_integer(self.I, input_name='I'), namespaceprefix_ , eol_))
        if self.J is not None:
            namespaceprefix_ = self.J_nsprefix_ + ':' if (UseCapturedNS_ and self.J_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sJ>%s</%sJ>%s' % (namespaceprefix_ , self.gds_format_integer(self.J, input_name='J'), namespaceprefix_ , eol_))
        if self.Value is not None:
            namespaceprefix_ = self.Value_nsprefix_ + ':' if (UseCapturedNS_ and self.Value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValue>%s</%sValue>%s' % (namespaceprefix_ , self.gds_format_double(self.Value, input_name='Value'), namespaceprefix_ , eol_))
        if self.FlowRef is not None:
            namespaceprefix_ = self.FlowRef_nsprefix_ + ':' if (UseCapturedNS_ and self.FlowRef_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sFlowRef>%s</%sFlowRef>%s' % (namespaceprefix_ , self.gds_format_integer(self.FlowRef, input_name='FlowRef'), namespaceprefix_ , eol_))
        if self.OpZeroOrOne is not None:
            namespaceprefix_ = self.OpZeroOrOne_nsprefix_ + ':' if (UseCapturedNS_ and self.OpZeroOrOne_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOpZeroOrOne>%s</%sOpZeroOrOne>%s' % (namespaceprefix_ , self.gds_format_integer(self.OpZeroOrOne, input_name='OpZeroOrOne'), namespaceprefix_ , eol_))
        if self.BaseSetInd is not None:
            namespaceprefix_ = self.BaseSetInd_nsprefix_ + ':' if (UseCapturedNS_ and self.BaseSetInd_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBaseSetInd>%s</%sBaseSetInd>%s' % (namespaceprefix_ , self.gds_format_integer(self.BaseSetInd, input_name='BaseSetInd'), namespaceprefix_ , eol_))
        if self.Script is not None:
            namespaceprefix_ = self.Script_nsprefix_ + ':' if (UseCapturedNS_ and self.Script_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sScript>%s</%sScript>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Script), input_name='Script')), namespaceprefix_ , eol_))
        if self.InputReference is not None:
            namespaceprefix_ = self.InputReference_nsprefix_ + ':' if (UseCapturedNS_ and self.InputReference_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInputReference>%s</%sInputReference>%s' % (namespaceprefix_ , self.gds_format_integer(self.InputReference, input_name='InputReference'), namespaceprefix_ , eol_))
    def exportLiteral(self, outfile, level, name_='FunctionInputType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            showIndent(outfile, level)
            outfile.write('Position=%d,\n' % (self.Position,))
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.Label is not None:
            showIndent(outfile, level)
            outfile.write('Label=%s,\n' % self.gds_encode(quote_python(self.Label)))
        if self.I is not None:
            showIndent(outfile, level)
            outfile.write('I=%d,\n' % self.I)
        if self.J is not None:
            showIndent(outfile, level)
            outfile.write('J=%d,\n' % self.J)
        if self.Value is not None:
            showIndent(outfile, level)
            outfile.write(Value=self.gds_format_double(self.Value))
        if self.FlowRef is not None:
            showIndent(outfile, level)
            outfile.write('FlowRef=%d,\n' % self.FlowRef)
        if self.OpZeroOrOne is not None:
            showIndent(outfile, level)
            outfile.write('OpZeroOrOne=%d,\n' % self.OpZeroOrOne)
        if self.BaseSetInd is not None:
            showIndent(outfile, level)
            outfile.write('BaseSetInd=%d,\n' % self.BaseSetInd)
        if self.Script is not None:
            showIndent(outfile, level)
            outfile.write('Script=%s,\n' % self.gds_encode(quote_python(self.Script)))
        if self.InputReference is not None:
            showIndent(outfile, level)
            outfile.write('InputReference=%d,\n' % self.InputReference)
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
        if nodeName_ == 'Label':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Label')
            value_ = self.gds_validate_string(value_, node, 'Label')
            self.Label = value_
            self.Label_nsprefix_ = child_.prefix
        elif nodeName_ == 'I' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'I')
            ival_ = self.gds_validate_integer(ival_, node, 'I')
            self.I = ival_
            self.I_nsprefix_ = child_.prefix
        elif nodeName_ == 'J' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'J')
            ival_ = self.gds_validate_integer(ival_, node, 'J')
            self.J = ival_
            self.J_nsprefix_ = child_.prefix
        elif nodeName_ == 'Value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Value')
            fval_ = self.gds_validate_double(fval_, node, 'Value')
            self.Value = fval_
            self.Value_nsprefix_ = child_.prefix
        elif nodeName_ == 'FlowRef' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'FlowRef')
            ival_ = self.gds_validate_integer(ival_, node, 'FlowRef')
            self.FlowRef = ival_
            self.FlowRef_nsprefix_ = child_.prefix
        elif nodeName_ == 'OpZeroOrOne' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'OpZeroOrOne')
            ival_ = self.gds_validate_integer(ival_, node, 'OpZeroOrOne')
            self.OpZeroOrOne = ival_
            self.OpZeroOrOne_nsprefix_ = child_.prefix
        elif nodeName_ == 'BaseSetInd' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'BaseSetInd')
            ival_ = self.gds_validate_integer(ival_, node, 'BaseSetInd')
            self.BaseSetInd = ival_
            self.BaseSetInd_nsprefix_ = child_.prefix
        elif nodeName_ == 'Script':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Script')
            value_ = self.gds_validate_string(value_, node, 'Script')
            self.Script = value_
            self.Script_nsprefix_ = child_.prefix
        elif nodeName_ == 'InputReference' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'InputReference')
            ival_ = self.gds_validate_integer(ival_, node, 'InputReference')
            self.InputReference = ival_
            self.InputReference_nsprefix_ = child_.prefix
# end class FunctionInputType


class RedundantFunctionalInputsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Number=None, FunctionInput=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Number = Number
        self.Number_nsprefix_ = None
        if FunctionInput is None:
            self.FunctionInput = []
        else:
            self.FunctionInput = FunctionInput
        self.FunctionInput_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RedundantFunctionalInputsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RedundantFunctionalInputsType.subclass:
            return RedundantFunctionalInputsType.subclass(*args_, **kwargs_)
        else:
            return RedundantFunctionalInputsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Number(self):
        return self.Number
    def set_Number(self, Number):
        self.Number = Number
    def get_FunctionInput(self):
        return self.FunctionInput
    def set_FunctionInput(self, FunctionInput):
        self.FunctionInput = FunctionInput
    def add_FunctionInput(self, value):
        self.FunctionInput.append(value)
    def insert_FunctionInput_at(self, index, value):
        self.FunctionInput.insert(index, value)
    def replace_FunctionInput_at(self, index, value):
        self.FunctionInput[index] = value
    def _hasContent(self):
        if (
            self.Number is not None or
            self.FunctionInput
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='RedundantFunctionalInputsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RedundantFunctionalInputsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RedundantFunctionalInputsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RedundantFunctionalInputsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RedundantFunctionalInputsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RedundantFunctionalInputsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='RedundantFunctionalInputsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Number is not None:
            namespaceprefix_ = self.Number_nsprefix_ + ':' if (UseCapturedNS_ and self.Number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumber>%s</%sNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.Number, input_name='Number'), namespaceprefix_ , eol_))
        for FunctionInput_ in self.FunctionInput:
            namespaceprefix_ = self.FunctionInput_nsprefix_ + ':' if (UseCapturedNS_ and self.FunctionInput_nsprefix_) else ''
            FunctionInput_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='FunctionInput', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='RedundantFunctionalInputsType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.Number is not None:
            showIndent(outfile, level)
            outfile.write('Number=%d,\n' % self.Number)
        showIndent(outfile, level)
        outfile.write('FunctionInput=[\n')
        level += 1
        for FunctionInput_ in self.FunctionInput:
            showIndent(outfile, level)
            outfile.write('model_.FunctionInputType1(\n')
            FunctionInput_.exportLiteral(outfile, level, name_='FunctionInputType1')
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
        if nodeName_ == 'Number' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Number')
            ival_ = self.gds_validate_integer(ival_, node, 'Number')
            self.Number = ival_
            self.Number_nsprefix_ = child_.prefix
        elif nodeName_ == 'FunctionInput':
            obj_ = FunctionInputType1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.FunctionInput.append(obj_)
            obj_.original_tagname_ = 'FunctionInput'
# end class RedundantFunctionalInputsType


class FunctionInputType1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Position=None, Label=None, I=None, J=None, Value=None, FlowRef=None, OpZeroOrOne=None, BaseSetInd=None, Script=None, InputReference=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Position = _cast(int, Position)
        self.Position_nsprefix_ = None
        self.Label = Label
        self.Label_nsprefix_ = None
        self.I = I
        self.I_nsprefix_ = None
        self.J = J
        self.J_nsprefix_ = None
        self.Value = Value
        self.Value_nsprefix_ = None
        self.FlowRef = FlowRef
        self.FlowRef_nsprefix_ = None
        self.OpZeroOrOne = OpZeroOrOne
        self.OpZeroOrOne_nsprefix_ = None
        self.BaseSetInd = BaseSetInd
        self.BaseSetInd_nsprefix_ = None
        self.Script = Script
        self.Script_nsprefix_ = None
        self.InputReference = InputReference
        self.InputReference_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, FunctionInputType1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if FunctionInputType1.subclass:
            return FunctionInputType1.subclass(*args_, **kwargs_)
        else:
            return FunctionInputType1(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Label(self):
        return self.Label
    def set_Label(self, Label):
        self.Label = Label
    def get_I(self):
        return self.I
    def set_I(self, I):
        self.I = I
    def get_J(self):
        return self.J
    def set_J(self, J):
        self.J = J
    def get_Value(self):
        return self.Value
    def set_Value(self, Value):
        self.Value = Value
    def get_FlowRef(self):
        return self.FlowRef
    def set_FlowRef(self, FlowRef):
        self.FlowRef = FlowRef
    def get_OpZeroOrOne(self):
        return self.OpZeroOrOne
    def set_OpZeroOrOne(self, OpZeroOrOne):
        self.OpZeroOrOne = OpZeroOrOne
    def get_BaseSetInd(self):
        return self.BaseSetInd
    def set_BaseSetInd(self, BaseSetInd):
        self.BaseSetInd = BaseSetInd
    def get_Script(self):
        return self.Script
    def set_Script(self, Script):
        self.Script = Script
    def get_InputReference(self):
        return self.InputReference
    def set_InputReference(self, InputReference):
        self.InputReference = InputReference
    def get_Position(self):
        return self.Position
    def set_Position(self, Position):
        self.Position = Position
    def _hasContent(self):
        if (
            self.Label is not None or
            self.I is not None or
            self.J is not None or
            self.Value is not None or
            self.FlowRef is not None or
            self.OpZeroOrOne is not None or
            self.BaseSetInd is not None or
            self.Script is not None or
            self.InputReference is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='FunctionInputType1', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('FunctionInputType1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'FunctionInputType1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='FunctionInputType1')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='FunctionInputType1', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='FunctionInputType1'):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            outfile.write(' Position="%s"' % self.gds_format_integer(self.Position, input_name='Position'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:wds="https://github.com/wdatasci/WDS-ModelSpec"', name_='FunctionInputType1', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Label is not None:
            namespaceprefix_ = self.Label_nsprefix_ + ':' if (UseCapturedNS_ and self.Label_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sLabel>%s</%sLabel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Label), input_name='Label')), namespaceprefix_ , eol_))
        if self.I is not None:
            namespaceprefix_ = self.I_nsprefix_ + ':' if (UseCapturedNS_ and self.I_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sI>%s</%sI>%s' % (namespaceprefix_ , self.gds_format_integer(self.I, input_name='I'), namespaceprefix_ , eol_))
        if self.J is not None:
            namespaceprefix_ = self.J_nsprefix_ + ':' if (UseCapturedNS_ and self.J_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sJ>%s</%sJ>%s' % (namespaceprefix_ , self.gds_format_integer(self.J, input_name='J'), namespaceprefix_ , eol_))
        if self.Value is not None:
            namespaceprefix_ = self.Value_nsprefix_ + ':' if (UseCapturedNS_ and self.Value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValue>%s</%sValue>%s' % (namespaceprefix_ , self.gds_format_double(self.Value, input_name='Value'), namespaceprefix_ , eol_))
        if self.FlowRef is not None:
            namespaceprefix_ = self.FlowRef_nsprefix_ + ':' if (UseCapturedNS_ and self.FlowRef_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sFlowRef>%s</%sFlowRef>%s' % (namespaceprefix_ , self.gds_format_integer(self.FlowRef, input_name='FlowRef'), namespaceprefix_ , eol_))
        if self.OpZeroOrOne is not None:
            namespaceprefix_ = self.OpZeroOrOne_nsprefix_ + ':' if (UseCapturedNS_ and self.OpZeroOrOne_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOpZeroOrOne>%s</%sOpZeroOrOne>%s' % (namespaceprefix_ , self.gds_format_integer(self.OpZeroOrOne, input_name='OpZeroOrOne'), namespaceprefix_ , eol_))
        if self.BaseSetInd is not None:
            namespaceprefix_ = self.BaseSetInd_nsprefix_ + ':' if (UseCapturedNS_ and self.BaseSetInd_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBaseSetInd>%s</%sBaseSetInd>%s' % (namespaceprefix_ , self.gds_format_integer(self.BaseSetInd, input_name='BaseSetInd'), namespaceprefix_ , eol_))
        if self.Script is not None:
            namespaceprefix_ = self.Script_nsprefix_ + ':' if (UseCapturedNS_ and self.Script_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sScript>%s</%sScript>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Script), input_name='Script')), namespaceprefix_ , eol_))
        if self.InputReference is not None:
            namespaceprefix_ = self.InputReference_nsprefix_ + ':' if (UseCapturedNS_ and self.InputReference_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInputReference>%s</%sInputReference>%s' % (namespaceprefix_ , self.gds_format_integer(self.InputReference, input_name='InputReference'), namespaceprefix_ , eol_))
    def exportLiteral(self, outfile, level, name_='FunctionInputType1'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Position is not None and 'Position' not in already_processed:
            already_processed.add('Position')
            showIndent(outfile, level)
            outfile.write('Position=%d,\n' % (self.Position,))
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.Label is not None:
            showIndent(outfile, level)
            outfile.write('Label=%s,\n' % self.gds_encode(quote_python(self.Label)))
        if self.I is not None:
            showIndent(outfile, level)
            outfile.write('I=%d,\n' % self.I)
        if self.J is not None:
            showIndent(outfile, level)
            outfile.write('J=%d,\n' % self.J)
        if self.Value is not None:
            showIndent(outfile, level)
            outfile.write(Value=self.gds_format_double(self.Value))
        if self.FlowRef is not None:
            showIndent(outfile, level)
            outfile.write('FlowRef=%d,\n' % self.FlowRef)
        if self.OpZeroOrOne is not None:
            showIndent(outfile, level)
            outfile.write('OpZeroOrOne=%d,\n' % self.OpZeroOrOne)
        if self.BaseSetInd is not None:
            showIndent(outfile, level)
            outfile.write('BaseSetInd=%d,\n' % self.BaseSetInd)
        if self.Script is not None:
            showIndent(outfile, level)
            outfile.write('Script=%s,\n' % self.gds_encode(quote_python(self.Script)))
        if self.InputReference is not None:
            showIndent(outfile, level)
            outfile.write('InputReference=%d,\n' % self.InputReference)
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
        if nodeName_ == 'Label':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Label')
            value_ = self.gds_validate_string(value_, node, 'Label')
            self.Label = value_
            self.Label_nsprefix_ = child_.prefix
        elif nodeName_ == 'I' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'I')
            ival_ = self.gds_validate_integer(ival_, node, 'I')
            self.I = ival_
            self.I_nsprefix_ = child_.prefix
        elif nodeName_ == 'J' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'J')
            ival_ = self.gds_validate_integer(ival_, node, 'J')
            self.J = ival_
            self.J_nsprefix_ = child_.prefix
        elif nodeName_ == 'Value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'Value')
            fval_ = self.gds_validate_double(fval_, node, 'Value')
            self.Value = fval_
            self.Value_nsprefix_ = child_.prefix
        elif nodeName_ == 'FlowRef' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'FlowRef')
            ival_ = self.gds_validate_integer(ival_, node, 'FlowRef')
            self.FlowRef = ival_
            self.FlowRef_nsprefix_ = child_.prefix
        elif nodeName_ == 'OpZeroOrOne' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'OpZeroOrOne')
            ival_ = self.gds_validate_integer(ival_, node, 'OpZeroOrOne')
            self.OpZeroOrOne = ival_
            self.OpZeroOrOne_nsprefix_ = child_.prefix
        elif nodeName_ == 'BaseSetInd' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'BaseSetInd')
            ival_ = self.gds_validate_integer(ival_, node, 'BaseSetInd')
            self.BaseSetInd = ival_
            self.BaseSetInd_nsprefix_ = child_.prefix
        elif nodeName_ == 'Script':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Script')
            value_ = self.gds_validate_string(value_, node, 'Script')
            self.Script = value_
            self.Script_nsprefix_ = child_.prefix
        elif nodeName_ == 'InputReference' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'InputReference')
            ival_ = self.gds_validate_integer(ival_, node, 'InputReference')
            self.InputReference = ival_
            self.InputReference_nsprefix_ = child_.prefix
# end class FunctionInputType1


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
        rootTag = 'WDSMatrix'
        rootClass = WDSMatrix
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
        rootTag = 'WDSMatrix'
        rootClass = WDSMatrix
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
        rootTag = 'WDSMatrix'
        rootClass = WDSMatrix
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
        rootTag = 'WDSMatrix'
        rootClass = WDSMatrix
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from gWDSMatrix_literal import *\n\n')
        sys.stdout.write('import gWDSMatrix_literal as model_\n\n')
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
    "AdditionalAxesLowerLimitsType",
    "AdditionalAxesUpperLimitsType",
    "BetaType",
    "BetasType",
    "FunctionInputType",
    "FunctionInputType1",
    "FunctionalInputsType",
    "MDataType",
    "NonZeroCoordinateType",
    "NonZeroCoordinatesType",
    "NonZeroElementsType",
    "RedundantFunctionalInputsType",
    "StateLabelType",
    "StateLabelsType",
    "WDSMatrix"
]
