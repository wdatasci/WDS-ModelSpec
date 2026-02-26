using System;
using System.Collections.Generic;

using ExcelDna.Registration;
using ExcelDna.Integration;
using ExcelDna.Integration.CustomUI;

using static WDS.Util;

namespace WDS
{
    public partial class XLL : IExcelAddIn
    {


        [ExcelFunction(
                Name = "CleanAsNMToken_ViaJni"
                , Category = "WDS.JniPMML"
                , Description = "Returns a NMToken of the input string with invalid characters removed"
                , IsVolatile = false
                , ExplicitRegistration = true
                )]
        public static String CleanAsNMToken_ViaJni(
            [ExcelArgument(Name = "InputString",
                Description ="A general string")] String aInputString
            )
        {
#if COMPILE_WITH_JNI
            if ( ExcelDnaUtil.IsInFunctionWizard() ) return "In Function Wizard, holding calls to Java";
            if ( aInputString == null || aInputString.Length == 0 ) return "";

            String aClassName = "com/WDataSci/WDS/Util";
            IntPtr aClassID = Java.FindClassID(aClassName);
            String aMethodName = "CleanAsNMToken";
            String aSignatureString = "(Ljava/lang/String;)Ljava/lang/String;";

            List<object> cmargs = new List<object>{ aInputString };
            String rv="Err";

            unsafe {
                IntPtr aMethodID = Java.FindStaticMethodID(aClassID, aMethodName, aSignatureString);
                rv = Java.CallMethod<string>(aMethodID, true, aSignatureString, cmargs);
            }
            cmargs = null;

            return rv;
#else
            return "XLL not compiled with JniPMML";
#endif
        }



        [ExcelFunction(
                Name = "CleanStringWithRegex_ViaJni"
                , Category = "WDS.JniPMML"
                , Description = "Returns a NMToken of the input string with invalid characters removed"
                , IsVolatile = false
                , ExplicitRegistration = true
                )]
        public static String CleanStringWithRegex_ViaJni(
            [ExcelArgument(Name = "InputString")] String aInputString,
            [ExcelArgument(Name = "RegexToFind")] String aRegexString,
            [ExcelArgument(Name = "RegexToReplaceWith")] String aReplaceWithString,
            [ExcelArgument(Name = "JVM_class")] object _aClassName,
            [ExcelArgument(Name = "JVM_method")] object _aMethodName,
            [ExcelArgument(Name = "JVM_signature")] object _aSignatureString
            )
        {
#if COMPILE_WITH_JNI
            if ( ExcelDnaUtil.IsInFunctionWizard() ) return "In Function Wizard, holding calls to Java";
            if ( aInputString == null || aInputString.Length == 0 ) return "";

            String aClassName=__OptionalStringValue(_aClassName, "com/WDataSci/WDS/Util");
            if ( aClassName == null || aClassName.Length == 0 ) return "";
            String aMethodName = __OptionalStringValue(_aMethodName,"CleanAsString");
            if ( aMethodName == null || aMethodName.Length == 0 ) return "";
            String aSignatureString = __OptionalStringValue(_aSignatureString,"(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;");
            if ( aSignatureString == null || aSignatureString.Length == 0 ) return "";

            List<object> cmargs = new List<object>{ aInputString, aRegexString, aReplaceWithString };

            IntPtr aClassID = Java.FindClassID(aClassName);
            IntPtr aMethodID = Java.FindStaticMethodID(aClassID, aMethodName, aSignatureString);
            String rv = Java.CallMethod<string>(aMethodID, true, aSignatureString, cmargs);

            cmargs = null;
            return rv;
#else
            return "XLL not compiled with JniPMML";
#endif
        }



        [ExcelFunction(
                Name = "FetchFileAsString_ViaJni"
                , Category = "WDS.JniPMML"
                , Description = "Pulls the contents of a file and returns as one string."
                , ExplicitRegistration = true
                )]
        public static String FetchFileAsString_ViaJni(
            [ExcelArgument(Name = "FileName")] String arg1
            )
        {
#if COMPILE_WITH_JNI
            if ( ExcelDnaUtil.IsInFunctionWizard() ) return "In Function Wizard, holding calls to Java";

            List<object> cmargs = new List<object>{ arg1 };

            String aClassName = "com/WDataSci/WDS/Util";
            String aMethodName = "FetchFileAsString";
            String aSignatureString = "(Ljava/lang/String;)Ljava/lang/String;";

            IntPtr aClassID = Java.FindClassID(aClassName);
            IntPtr aMethodID = Java.FindStaticMethodID(aClassID, aMethodName, aSignatureString);
            String rv = Java.CallMethod<string>(aMethodID, true, aSignatureString, cmargs);

            cmargs = null;
            return rv;
#else
            return "XLL not compiled with JniPMML";
#endif

        }

    }
}
