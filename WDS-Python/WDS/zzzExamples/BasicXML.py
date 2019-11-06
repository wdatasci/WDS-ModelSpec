''' 1: basic XML
    '''


#basic python imports
import os,sys
import pudb
import argparse
import traceback


import time
import os.path as osp
import xml.etree.ElementTree as xmlet
#using lxml because of xslt support
import lxml.etree as lxmlet

import xml.dom.minidom as minidom
import xml


#CodeDoc - CJW - Here, we are embedding all functions in the body of the if-statement.
#see HelloWorld and MonkeyPatch examples for argparse and class notes

#RefDoc - CJW - using the following references:
#https://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree/

#RefDoc - CJW - getting rid of namespace prefixes in:
#https://stackoverflow.com/questions/13412496/python-elementtree-module-how-to-ignore-the-namespace-of-xml-files-to-locate-ma
#from xml.parsers import expat
#_HoldExpatParserCreate_Orig=expat.ParserCreate
#_ParserCreate=lambda enc, sep: _HoldExpatParserCreate_Orig(enc, None)

#using an XSL to remove them
#https://stackoverflow.com/questions/5268182/how-to-remove-namespaces-from-xml-using-xslt#5875074


if __name__=="__main__":
    def main_argparser():
        _parser=argparse.ArgumentParser()
        #positional
        _parser.add_argument("xml_to_load"
                            , help="first argument, xml to load")
        #positional
        _parser.add_argument("xsd_to_validate_with"
                            , help="second argument, xsd_to_validate_with to load")
        #optional switches
        _parser.add_argument("--pudb"
                            , help="turn on the pudb debugger before main"
                            , action="store_true"
                            )
        return _parser


    def main(args=None):
        if not args:
            raise('nothing passed into main')

        x1=lxmlet.ElementTree(file=args.xml_to_load)

        print()
        print(dir(x1))
        print(x1.getroot())
        r1=x1.getroot()
        print(dir(r1))
        #note: key python class attributes of tag and attributes might not show up in dir, see help(lxmlet)
        #help(lxmlet)
        print(r1.tag,r1.attrib)


        print()
        print('stripping the xmlns prefix with the parser:')
        print(' this turned out to be harder than expected, but using lxml with xslt support as an example')
        xslt_xml=lxmlet.XML(b'''<?xml version="1.0" encoding="UTF-8"?>
                    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
                    <xsl:output method="xml" indent="yes" encoding="UTF-8"/>
                    <xsl:template match="/">
                        <xsl:copy>
                                <xsl:apply-templates/>
                        </xsl:copy>
                    </xsl:template>
                    <xsl:template match="@*">
                        <xsl:attribute name="{local-name()}">
                            <xsl:value-of select="current()"/>
                        </xsl:attribute>
                    </xsl:template>
                    <xsl:template match="*">
                        <xsl:element name="{local-name()}">
                            <xsl:apply-templates select="@* | * | text()"/>
                        </xsl:element>
                    </xsl:template>
                    <xsl:template match="text()">
                        <xsl:copy>
                            <xsl:value-of select="current()"/>
                        </xsl:copy>
                     </xsl:template>
                  </xsl:stylesheet>
                ''')
        xslt=lxmlet.XSLT(xslt_xml)
        x2=xslt(x1)
        print(dir(x2))
        r2=x2.getroot()
        print(dir(r2))
        print(r2.tag,r2.attrib)


        
        print('%s\n' % lxmlet.tostring(x1,pretty_print=True,xml_declaration=True).decode('utf-8'))
        print('%s\n' % lxmlet.tostring(x2,pretty_print=True,xml_declaration=True).decode('utf-8'))
        #sys.exit()


        xsdf=lxmlet.parse(args.xsd_to_validate_with)
        xsd=lxmlet.XMLSchema(xsdf)

        if xsd.validate(x1):
            print('x1 can be validated with xsd')
        else:
            print('x1 cannot be validated with xsd')


        if xsd.validate(x2):
            print('x2 can be validated with xsd')
        else:
            print('x2 cannot be validated with xsd')




        print()
        print('fin')

    #end def main
        

    l_argparser = main_argparser()
    try:
        args=l_argparser.parse_args()
        if args.pudb:
            pudb.set_trace()
        main(args=args)
    except Exception as e:
        print("Hey")
        print(e)
        print(traceback.format_tb(e.__traceback__))


