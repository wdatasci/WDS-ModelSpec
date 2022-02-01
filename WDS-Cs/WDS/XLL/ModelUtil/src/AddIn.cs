using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ExcelDna.Integration;
using ExcelDna.Registration;
using ExcelDna.IntelliSense;
using Microsoft.ClearScript;
using Microsoft.ClearScript.Windows;
using Microsoft.ClearScript.V8;
using Microsoft.ClearScript.JavaScript;


namespace WDS_ExcelAddIn_Common
{

    public partial class AddIn : IExcelAddIn
    {

        private static V8ScriptEngine lScriptEngine;
        
        public void AutoOpen()
        {
            //lScriptEngine = new V8ScriptEngine(V8ScriptEngineFlags.EnableDebugging); 
            lScriptEngine = new V8ScriptEngine(V8ScriptEngineFlags.EnableDateTimeConversion); 
            RegisterFunctions();
            ExcelIntegration.RegisterUnhandledExceptionHandler( ex => "!!! EXCEPTION: " + ex.ToString());
     
        }

        public void AutoClose()
        {
             lScriptEngine.Dispose();
        }

        public void RegisterFunctions()
        {
            ExcelRegistration.GetExcelFunctions()
                            .ProcessParamsRegistrations()
                            .Select(UpdateHelpTopic)
                            .RegisterFunctions();
        }

        public ExcelFunctionRegistration UpdateHelpTopic(ExcelFunctionRegistration funcReg)
        {
            funcReg.FunctionAttribute.HelpTopic = "http://WypasekDataScience.com";
            return funcReg;
        }
    }




}
