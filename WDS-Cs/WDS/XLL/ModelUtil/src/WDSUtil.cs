//Brought over from WDS-JniPMML-XLL, Util.cs

using System;
using System.IO;
using System.Text.RegularExpressions;
using System.Xml;
using System.Windows.Forms;
using ExcelDna.Integration;
using ExcelDna.Utilities;
using MOIE = Microsoft.Office.Interop.Excel;
using VBIDE = Microsoft.Vbe.Interop;


using WDS.Wrangler;
using WDS.ModelSpec;

namespace WDS {

    public static partial class Util {
        public static string sWDSHOME()
        {
            //MOIE.Application tapp = (ExcelDnaUtil.Application as MOIE.Application);
            //MOIE.Workbook twb = tapp.ActiveWorkbook;
            //VBIDE.VBProject tVBProject = twb.VBProject;

            string rv = "ERROR";
            try
            {
                rv = System.Environment.GetEnvironmentVariable("WDSHOME");
                if (rv == "") return "ERROR";
            }
            catch (Exception)
            {
                string p = System.Environment.GetEnvironmentVariable("PATH");
                rv = PathElementOf(p, "WDS\\lib");
            }
            return rv;
        }


        [ExcelFunction(
                Name = "FetchFileAsString"
                , Category = "WDS"
                , Description = "Pulls the contents of a file and returns as one string."
                , ExplicitRegistration = true
                )]
        public static String FetchFileAsString
        (
            [ExcelArgument(Name = "FileName")] String arg
            )
        {
            String rv = "Error:";
            try {
                if ( arg == null || arg.isEmpty() ) {
                    rv = "Error: Empty File Name";
                    return rv;
                }
                rv = System.IO.File.ReadAllText(arg);
            }
            catch ( Exception e ) {
                throw new WDSException("Error in FetchFileAsString", e);
            }
            return rv;
        }

        [ExcelFunction(
                Name = "bIn"
                , Category = "WDS"
                , Description = "Returns true if first argument value is any of the optional arguments"
                , ExplicitRegistration = true
                , IsThreadSafe = true
                , IsVolatile =false
                )]
        public static Boolean bIn(object arg0, params object[] args) {
            if ( arg0 == null ) return false;
            if (args == null) return false;
            bool bFoundDifferentType = false;
            Type arg0Type = arg0.GetType();
            foreach (object o in args)
            {
                if (o != null)
                {
                    if (o.GetType() == arg0Type)
                    {
                        if (arg0.Equals(o)) return true;
                    }
                    else
                    {
                        if (o is object[] && bIn(arg0, o)) return true;
                        if (o is object[,] && bIn(arg0, o.ToVector<object>())) return true;
                        bFoundDifferentType = true;
                    }
                }
            }
            if (!bFoundDifferentType)
                return false;
            String s = arg0.ToString();
            foreach (object o in args)
            {
                if (o != null)
                {
                    if (s.Equals(o.ToString())) return true;
                }
            }
            return false;
        }

        //overloading for nullity checks

        public static Boolean MatchingNullity(String A, String B) {
            if ( A == null && B == null ) return true;
            if ( A != null && B != null ) return true;
            return false;
        }

        public static Boolean MatchingNullityAndValueEquals(String A, String B) {
            if ( !MatchingNullity(A, B) ) return false;
            if ( A == null ) return true;
            if ( !A.equals(B) ) return false;
            return true;
        }

        public static Boolean MatchingNullity(Object A, Object B) {
            if ( A == null && B == null ) return true;
            if ( A != null && B != null ) return true;
            return false;
        }

        /**
         * CleanAsNMToken returns a clean and valid NMToken (name token) string for a given input, following XML 1.1, through \uFFFF.
         */
        [ExcelFunction(
                Name = "CleanAsNMToken"
                , Category = "WDS"
                , Description = "Returns a clean and valid \\i\\c* NMToken (name token) string for a given input, following XML 1.1, through \\uFFFF. Note use CleanAsNMTokenXSD where the first character is not treated differently."
                , IsVolatile = false
                , ExplicitRegistration = true
                )]
        public static String CleanAsNMToken(
            [ExcelArgument(Name = "aInputString",
                Description ="A general string")] String arg
            )
        {
            //from https://www.w3.org/TR/2006/REC-xml11-20060816/
            //NameStartChar::= ":" | [A - Z] | "_" | [a - z] | [#xC0-#xD6] | [#xD8-#xF6] | [#xF8-#x2FF] | [#x370-#x37D] | [#x37F-#x1FFF] | [#x200C-#x200D] | [#x2070-#x218F] | [#x2C00-#x2FEF] | [#x3001-#xD7FF] | [#xF900-#xFDCF] | [#xFDF0-#xFFFD] | [#x10000-#xEFFFF]
            //NameStartChar::= ":" | [A - Z] | "_" | [a - z] | [ latin without math                   ] | [ greek, cyrillic            ] | [#x200C-#x200D] | [#x2070-#x218F] | [#x2C00-#x2FEF] | [#x3001-#xD7FF] | [#xF900-#xFDCF] | [#xFDF0-#xFFFD] | [#x10000-#xEFFFF]
            //NameChar::= NameStartChar | "-" | "." | [0 - 9] | #xB7       | [#x0300-#x036F] | [#x203F-#x2040]
            //NameChar::= NameStartChar | "-" | "." | [0 - 9] | middle dot | [#x0300-#x036F] | [#x203F-#x2040]
            //Name::= NameStartChar(NameChar) *
            //Names::= Name(#x20 Name)*
            //Nmtoken::= (NameChar) +
            //Nmtokens::= Nmtoken(#x20 Nmtoken)*

            String rv = arg.replaceAll("^[^:A-Z_a-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD]+", "");
            rv = rv.replaceAll("[^:A-Z_a-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD-.0-9\u00B7\u0300-\u036F\u203F-\u2040]+", "");
            return rv;
        }

        /**
         * CleanAsNMTokenXSD returns a clean and valid NMToken (name token) string for a given input, following XML 1.1, through \uFFFF.
         */
        [ExcelFunction(
                Name = "CleanAsNMTokenXSD"
                , Category = "WDS"
                , Description = "Returns a clean and valid \\c* NMToken (name token) string for a given input, through \\uFFFF. Note use CleanAsNMTokenXSD where the first character is not treated differently."
                , IsVolatile = false
                , ExplicitRegistration = true
                )]
        public static String CleanAsNMTokenXSD(
            [ExcelArgument(Name = "aInputString",
                Description ="A general string")] String arg
            )
        {
            String rv=arg.replaceAll("[^:A-Z_a-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD-.0-9\u00B7\u0300-\u036F\u203F-\u2040]+", "");
            return rv;
        }

        [ExcelFunction(
                Name = "CleanStringWithRegex"
                , Category = "WDS"
                , Description = "Performs a C# eval of Regex.Replace(InputString,RegexToFind,RegexToReplaceWith)"
                , IsVolatile = false
                , ExplicitRegistration = true
                )]
        public static String CleanStringWithRegex(
            [ExcelArgument(Name = "InputString", Description ="A general string")] String arg0
            , [ExcelArgument(Name = "RegexToFind", Description ="A Regex Expression")] String arg1
            , [ExcelArgument(Name = "RegexToReplaceWith", Description ="Replacement String")] String arg2
            )
            {
            String rv = arg0.replaceAll(arg1, arg2);
            return rv;
        }

        [ExcelFunction(
                Name = "CleanAsToken"
                , Category = "WDS"
                , Description = "Returns a TOKEN of the input string where white-space is normalized.  Additionally, ascii non-printables are removed."
                , IsVolatile = false
                , ExplicitRegistration = true
                )]
        public static String CleanAsToken(
            [ExcelArgument(Name = "aInputString",
                Description ="A general string")] String arg
            )
            {
            String rv = Regex.Replace(arg, "[\u0000-\u001F]", " ");
            rv = Regex.Replace(rv, "^\\s+", "");
            rv = Regex.Replace(rv, "\\s+$", "");
            rv = Regex.Replace(rv,"\\s+"," ");
            return rv;
        }

        [ExcelFunction(
                Name = "CleanQuotes"
                , Category = "WDS"
                , Description = "Removes double or single quotes."
                , IsVolatile = false
                , ExplicitRegistration = true
                )]
        public static String CleanQuotes(String arg)
            {
            String rv = Regex.Replace(arg,"[\\\"\\\']", " ");
            return rv;
        }

        [ExcelFunction(
                Name = "CleanDeadWhiteSpaceInXML"
                , Category = "WDS"
                , Description = "Removes inter-element space and non-printables in XML"
                , IsVolatile = false
                , ExplicitRegistration = true
                )]
        public static String CleanDeadWhiteSpaceInXML(
            [ExcelArgument(Name = "aInputString",
                Description ="A general string")] String arg
            )
            {
            String rv = Regex.Replace(arg, ">[\u0000-\u001F]+<", "><");
            rv = Regex.Replace(rv, "^\\s+", "");
            rv = Regex.Replace(rv, "\\s+$", "");
            return rv;
        }

        public static String PathAndName(String aPath, String aFileName) {
            String rv = null;
            if ( aPath != null && !aPath.isEmpty() ) {
                rv = System.IO.Path.Combine(aPath, aFileName);
            }
            else
                rv = aFileName;
            return rv;
        }

        public static bool lIsAtomic(ref Object arg)
        {
            if (arg is double) return true;
            if (arg is Double) return true;
            if (arg is string) return true;
            if (arg is String) return true;
            if (arg is int) return true;
            if (arg is Int16) return true;
            if (arg is UInt16) return true;
            if (arg is Int32) return true;
            if (arg is UInt32) return true;
            if (arg is Int64) return true;
            if (arg is UInt64) return true;
            return false;
        }

        public static void lDimensions(ref int ndim, ref int nelem, ref int nrows, ref int ncols, object arg1)
        {
            try
            {
                if (arg1 is object[])
                {
                    ndim = 1;
                    nelem = (arg1 as object[]).Length;
                    nrows = nelem;
                    ncols = 1;
                    return;
                }
                if (arg1 is object[,])
                {
                    try
                    {
                        object[,] arg12 = (object[,])arg1;
                        ndim = arg12.Rank;
                        if (ndim == 1)
                        {
                            nelem = arg12.GetLength(0);
                            nrows = nelem;
                            ncols = 1;
                        }
                        else if (ndim == 2)
                        {
                            nrows = arg12.GetLength(0);
                            ncols = arg12.GetLength(1);
                            nelem = nrows * ncols;
                        }
                    }
                    catch (SystemException)
                    {
                        ndim = 0;
                        nelem = 0;
                        nrows = 0;
                        ncols = 0;
                    }
                    return;
                }
                if (arg1 is ExcelMissing)
                {
                    ndim = 0;
                    nelem = 0;
                    nrows = 0;
                    ncols = 0;
                    return;
                }
                ndim = -1;
                nelem = 1;
                nrows = 1;
                ncols = 1;
                return;
            }
            catch (SystemException)
            {
                ndim = 0;
                nelem = 0;
                nrows = 0;
                ncols = 0;
            }
        }
        public static String PathElementOf(String path, String loc)
        {
            try
            {

                int iloc = path.IndexOf(loc);
                int i = path.IndexOf(";", iloc + 1);
                if (i < 0) i = path.Length;
                int j = path.LastIndexOf(";", iloc);
                String elem = path.Substring(j + 1, i - j);
                if (elem.EndsWith(";")) elem = elem.Substring(0, elem.Length - 1);
                if (elem.EndsWith("\\")) elem = elem.Substring(0, elem.Length - 1);
                if (elem.EndsWith("\\bin")) elem = elem.Substring(0, elem.Length - 4);
                if (elem.EndsWith("\\lib")) elem = elem.Substring(0, elem.Length - 4);
                return elem;
            } catch (Exception e)
            {
                return "Error, " + e.Message;
            }

        }

        public static String __OptionalStringValue(object arg, String defv)
        {
            if ( arg == null ) return defv;
            if ( arg is ExcelDna.Integration.ExcelMissing ) return defv;
            if ( arg is ExcelDna.Integration.ExcelEmpty ) return defv;
            if ( arg is ExcelDna.Integration.ExcelError ) return defv;
            String rv = arg.ToString();
            return rv;
        }


        public static int __OptionalIntValue(object arg, int defv)
        {
            if ( arg == null ) return defv;
            if ( arg is ExcelDna.Integration.ExcelMissing ) return defv;
            if ( arg is ExcelDna.Integration.ExcelEmpty ) return defv;
            if ( arg is ExcelDna.Integration.ExcelError ) return defv;
            int rv = defv;
            try {
                rv = Convert.ToInt32(arg);
            }
            catch ( Exception ) {
                rv=defv;
            }
            return rv;
        }

    }
}
