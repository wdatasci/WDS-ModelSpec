using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.IO;
using System.ComponentModel;
using System.Text.RegularExpressions;
using ExcelDna.Integration;

using Microsoft.ClearScript.V8;
using Microsoft.ClearScript.JavaScript;
using Microsoft.ClearScript;
using Microsoft.ClearScript.Windows;

using static WDS.Util;
using WDS.Wrangler;

namespace WDS
{
    public partial class AddIn : IExcelAddIn
    {
        
        [ExcelFunction(Name = "WDS.MSClearScript.ClearScriptTest"
        , Category = "WDS.MSClearScript"
        , Description = "Well, what did you think?"
        , IsThreadSafe = true
        , IsVolatile = false
        )]
        public static object ClearScriptTest(
            [ExcelArgument(Name = "ModuleString", Description = "Something")] string dummyModuleString
            , [ExcelArgument(Name = "X", Description = "Something")] Double x
            , [ExcelArgument(Name = "ExportName", Description = "Something")] string dummyExportName
            )
        {
            try
            {
                return lScriptEngine.Invoke("foo", x);
            }
            catch (Exception e)
            {
                return e.Message;
            }
        }


        [ExcelFunction(Name = "WDS.MSClearScript.QuoteIt"
            , Category = "WDS.MSClearScript"
            , Description = "Escapes internal quotes."
            , IsThreadSafe = true
            , IsVolatile = false
            )]
        public static String QuoteIt(String arg, String arg2)
        {
            if (arg2 == "") return arg;
            String s = Regex.Replace(arg, "([^\\])" + arg2, "${1}\\" + arg2);
            s = Regex.Replace(s, "([^\\])" + arg2, "${1}\\" + arg2);
            if (s.StartsWith(arg2)) s = "\\" + s;
            return s;
        }

        [ExcelFunction(Name = "WDS.MSClearScript.RunCode"
        , Category = "WDS.MSClearScript"
        , Description = "Executes MS ClearScript V8 code in the global namespace."
        , IsThreadSafe = true
        , IsVolatile = false
        , IsMacroType = false
        , HelpTopic = "Executes MS ClearScript V8 code in the global namespace."
        )]
        public static object RunCode(
              [ExcelArgument(Name = "code", Description = "a string containing the file location for the V8 function body")] String code
            , [ExcelArgument(Name = "ExtraDependencies", Description = "a range, not used, but just to string dependencies in Excel")] object[] ExtraDependencies
            )
        {
            try
            {
                lScriptEngine.ExecuteCommand(code);
                return code;
            }
            catch (Exception e)
            {
                return e.Message + ", Details:" + e.ToString();
            }
        }


        [ExcelFunction(Name = "WDS.MSClearScript.RunCodeFromFile"
        , Category = "WDS.MSClearScript"
        , Description = "Executes MS ClearScript V8 code from a file in the global namespace."
        , IsThreadSafe = true
        , IsVolatile = false
        , IsMacroType = false
        , HelpTopic = "Executes MS ClearScript V8 code from a file in the global namespace."
        )]
        public static object RunCodeFromFile(
              [ExcelArgument(Name = "filename", Description = "a string containing the file location for the V8 function body")] String filename
            , [ExcelArgument(Name = "ExtraDependencies", Description = "a range, not used, but just to string dependencies in Excel")] object[] ExtraDependencies
            )
        {
            string s = "";
            try
            {
                s = System.IO.File.ReadAllText(filename);
                int l = s.Length;
                //System.IO.File.WriteAllText(filename + ".tmp.out", s);
                lScriptEngine.ExecuteDocument(s);
                return filename;
            }
            catch (Exception e)
            {
                return e.Message + ", Details:" + e.ToString();
            }
        }



        [ExcelFunction(Name = "WDS.MSClearScript.ConstantConstructorFromFile"
        , Category = "WDS.MSClearScript"
        , Description = "Executes MS ClearScript V8 code to define a constant value that can be used elsewhere.  "
        , IsThreadSafe = true
        , IsVolatile = false
        , IsMacroType = false
        , HelpTopic = "Executes MS ClearScript V8 code to define a constant value that can be used elsewhere.  " +
            "The constant object is defined in the external file. The contents of which are executed in the interior of a function call to construct the object."
        )]
        public static object ConstantConstructorFromFile(
            [ExcelArgument(Name = "constantname", Description = "constant name")] string constantname
            , [ExcelArgument(Name = "filename", Description = "a string containing the file location for the V8 function body")] String constantbody
            , [ExcelArgument(Name = "objectname_in_file", Description = "the name of the object to be returned in the file code, defaults to \"result\"")] String internalname
            , [ExcelArgument(Name = "ExtraDependencies", Description = "a range, not used, but just to string dependencies in Excel")] object[] ExtraDependencies
            )
        {
            string s = "";
            string linternalname = "result";
            if (internalname != null) linternalname = internalname.Trim();
            try
            {
                s = "var " + constantname + " = new Function (`\r" + System.IO.File.ReadAllText(constantbody) + "\r`+'return " + linternalname + "')()";
                int l = s.Length;
                //System.IO.File.WriteAllText(functionbody + ".tmp.out", s);
                lScriptEngine.Evaluate(s);
                return constantname;
            }
            catch (Exception e)
            {
                return e.Message + ", Details:" + e.ToString();
            }
        }


        [ExcelFunction(Name = "WDS.MSClearScript.ConstantConstructor"
        , Category = "WDS.MSClearScript"
        , Description = "Executes MS ClearScript V8 code to define a constant value that can be used elsewhere.  "
        , IsThreadSafe = true
        , IsVolatile = false
        , IsMacroType = false
        , HelpTopic = "Executes MS ClearScript V8 code to define a constant value that can be used elsewhere.  " +
            "The contents of constantdefinition are executed in the interior of a function call to construct the object."
        )]
        public static object ConstantConstructor(
            [ExcelArgument(Name = "constantname", Description = "constant name")] string constantname
            , [ExcelArgument(Name = "constantdefinition", Description = "a string containing V8 definition of the constant value")] String constantbody
            , [ExcelArgument(Name = "objectname", Description = "the name of the object to be returned in the file code, defaults to \"result\"")] String internalname
            , [ExcelArgument(Name = "ExtraDependencies", Description = "a range, not used, but just to string dependencies in Excel")] object[] ExtraDependencies
            )
        {
            string s = "";
            try
            {

                string linternalname = "result";
                if (internalname != null) linternalname = internalname.Trim();

                s = "var " + constantname + " = new Function ('" + constantbody + "'+'\n return " + linternalname + ";')()";

                lScriptEngine.Execute(s);
                return constantname;

            }
            catch (Exception e)
            {
                return e.Message;
            }
        }


        [ExcelFunction(Name = "WDS.MSClearScript.FunctionConstructorFromFileWithBodyOnly"
        , Category = "WDS.MSClearScript"
        , Description = "Executes MS ClearScript V8 function constructor from an external file which has just the \"body\" of the function "
        , IsThreadSafe = true
        , IsVolatile = false
        //, ExplicitRegistration = true
        , HelpTopic = "Executes MS ClearScript V8 code to define a constant value that can be used elsewhere.  " +
            "The body of a function is defined in the external file. " +
            "The contents of which are wrapped with a \"new Function\" call and constructed in the global namespace. " +
            "The new function can be call from a subsequent Evaluator call."
        //, IsClusterSafe = true
        , IsHidden = false
        , IsMacroType = false
        //, SuppressOverwriteError = false
        )]
        public static object FunctionConstructorFromFileWithBodyOnly(
            [ExcelArgument(Name = "functionname", Description = "function name")] string functionname
            , [ExcelArgument(Name = "functionparams", Description = "an array of param names used in the function body")] object[] functionparams
            , [ExcelArgument(Name = "functionbody", Description = "the external path and filename of the V8 function body")] string functionbody
            , [ExcelArgument(Name = "functionbodymaps", Description = "an optional two column array of regex changes (from, to)")] object functionbodymaps
            , [ExcelArgument(Name = "objectname", Description = "the name of the object to be returned from the function body code, defaults to \"result\"")] String internalname
            , [ExcelArgument(Name = "ExtraDependencies", Description = "a range, not used, but just to string dependencies in Excel")] object[] ExtraDependencies
            )
        {
            try
            {

                string s = "";
                string sb = "";

                string linternalname = "result";
                if (internalname != null) linternalname = internalname.Trim();

                if (functionparams.Length > 0)
                {
                    for (int i = 0; i < functionparams.Length; i++)
                    {
                        s += "\"" + functionparams[i] + "\",";
                    }
                }

                sb = System.IO.File.ReadAllText(functionbody);
                int ndim = 0, nelem = 0, nrows = 0, ncols = 0;
                lDimensions(ref ndim, ref nelem, ref nrows, ref ncols, functionbodymaps);
                if (nrows > 0)
                {
                    if (ncols != 2) throw new Exception("functionbodymap must have 2 columns");
                    for (int i = 0; i < nrows; i++)
                        sb = Regex.Replace(sb, ((object[,])functionbodymaps)[i, 0].ToString(), ((object[,])functionbodymaps)[i, 1].ToString());
                }

                s = "var " + functionname + " = new Function (" + s + "`\r" + sb + "\r`+'return " + linternalname + ";')";
                lScriptEngine.Execute(s);
                try
                {
                    lScriptEngine.Execute("\"function\" == typeof " + functionname);
                    return functionname;
                }
                catch (Exception e)
                {
                    return e.Message;
                }

            }
            catch (Exception e)
            {
                return e.Message;
            }
        }


        [ExcelFunction(Name = "WDS.MSClearScript.FunctionConstructorFromBodyOnly"
        , Category = "WDS.MSClearScript"
        , Description = "Executes MS ClearScript V8 function constructor"
        , IsThreadSafe = true
        , IsVolatile = false
        , HelpTopic = "The addin initializes a V8 (javascript engine used in node.js).  This function executes a function definition in the global namespace that can be called from a subsequent Evaluator."
        //, ExplicitRegistration = true
        //, HelpTopic = "Hey HelpTopic"
        //, IsClusterSafe = true
        //, IsHidden = false
        //, IsMacroType = false
        //, SuppressOverwriteError = false
        )]
        public static object FunctionConstructorFromBodyOnly(
            [ExcelArgument(Name = "functionname", Description = "function name")] string functionname
            , [ExcelArgument(Name = "functionparams", Description = "an array of param names used in the function body")] object[] functionparams
            , [ExcelArgument(Name = "functionbody", Description = "a string containing the V8 function body")] string functionbody
            , [ExcelArgument(Name = "objectname", Description = "the name of the object to be returned from the function body code, defaults to \"result\"")] String internalname
            , [ExcelArgument(Name = "ExtraDependencies", Description = "a range, not used, but just to string dependencies in Excel")] object[] ExtraDependencies
            )
        {
            try
            {

                string s = "";

                string linternalname = "result";
                if (internalname != null) linternalname = internalname.Trim();

                if (functionparams.Length > 0)
                {
                    for (int i = 0; i < functionparams.Length; i++)
                    {
                        s += "\"" + functionparams[i] + "\",";
                    }
                }

                s = "var " + functionname + " = new Function (" + s + "`\r" + functionbody + "\r`+'return " + linternalname + ";')";
                lScriptEngine.Execute(s);
                try
                {
                    lScriptEngine.Execute("\"function\" == typeof " + functionname);
                    return functionname;
                }
                catch (Exception e)
                {
                    return e.Message;
                }

            }
            catch (Exception e)
            {
                return e.Message;
            }
        }



        [ExcelFunction(Name = "WDS.MSClearScript.SimpleFunctionEvaluator"
        , Category = "WDS.MSClearScript"
        , Description = "NOTE: Use with an atomic valued function.  Executes MS ClearScript V8 function (previously defined with FunctionConstructor) on a set of parameters."
        , IsThreadSafe = true
        , IsVolatile = false
        //, ExplicitRegistration = true
        //, SuppressOverwriteError = false
        //, IsClusterSafe = true
        , IsHidden = false
        , IsMacroType = false
        , HelpTopic = "Using a functionname already defined in the global namespace, functionname(functionparamsValues) is called in the global namespace and result returned."
        )]
        public static object SimpleFunctionEvaluator(
            [ExcelArgument(Name = "functionname", Description = "function name")] string functionname
            , [ExcelArgument(Name = "functionparams", Description = "an array of param names used in the function body")] object[] functionparams
            , [ExcelArgument(Name = "functionparamsValues", Description = "an array of param values corresponding to the names")] object[] functionparamsValues
            , [ExcelArgument(Name = "ExtraDependencies", Description = "a range, not used, but just to string dependencies in Excel")] object[] ExtraDependencies
            )
        {
            try
            {

                string s = "";
                string vs = "";
                if (functionparams.Length != functionparamsValues.Length) throw new Exception("functionparams and functionparamValues must have the same length");

                if (functionparams.Length > 0)
                {
                    for (int i = 0; i < functionparams.Length; i++)
                    {
                        if (i > 0)
                        {
                            s += ",";
                            vs += ",";
                        }
                        s += "\"" + functionparams[i] + "\",";
                        vs += "\"" + functionparams[i] + "\"";
                        if (functionparams[i].GetType() == typeof(string))
                            vs += "\"" + functionparams[i] + "\"";
                        else
                            vs += functionparams[i].ToString();
                    }
                }

                return lScriptEngine.Invoke(functionname, functionparamsValues);

            }
            catch (Exception e)
            {
                return e.Message + " in SimpleFunctionEvaluator, if return object is complex, try FunctionEvaluatior";
            }
        }






        [ExcelFunction(Name = "WDS.MSClearScript.FunctionEvaluator"
        , Category = "WDS.MSClearScript"
        , Description = "Executes MS ClearScript V8 function (previously defined with FunctionConstructor) on a set of parameters, can be used with non-atomic valued function"
        , IsThreadSafe = true
        , IsVolatile = false
        //, ExplicitRegistration = true
        //, SuppressOverwriteError = false
        //, IsClusterSafe = true
        , IsHidden = false
        , IsMacroType = false
        , HelpTopic = "Using a functionname already defined in the global namespace, functionname(functionparamsValues) is called in the global namespace and result returned."
        )]
        public static Object FunctionEvaluator(
            [ExcelArgument(Name = "functionname", Description = "function name")] string functionname
            , [ExcelArgument(Name = "functionparams", Description = "an array of param names used in the function body")] object[] functionparams
            , [ExcelArgument(Name = "functionparamsValues", Description = "an array of param values corresponding to the names")] object[] functionparamsValues
            , [ExcelArgument(Name = "ExtraDependencies", Description = "a range, not used, but just to string dependencies in Excel")] object[] ExtraDependencies
            )
        {
            try
            {

                string s = "";
                string vs = "";
                if (functionparams.Length != functionparamsValues.Length) throw new Exception("functionparams and functionparamValues must have the same length");

                if (functionparams.Length > 0)
                {
                    for (int i = 0; i < functionparams.Length; i++)
                    {
                        if (i > 0)
                        {
                            s += ",";
                            vs += ",";
                        }
                        s += "\"" + functionparams[i] + "\",";
                        vs += "\"" + functionparams[i] + "\"";
                        if (functionparams[i].GetType() == typeof(string))
                            vs += "\"" + functionparams[i] + "\"";
                        else
                            vs += functionparams[i].ToString();
                    }
                }

                Object returned_value= lScriptEngine.Invoke(functionname, functionparamsValues);
                if (lIsAtomic(ref returned_value)) return returned_value;

                int cnt = 0, ndim = 0, nelem = 0, nrows = 0, ncols = 0;
                foreach (PropertyDescriptor prop in TypeDescriptor.GetProperties(returned_value))
                {
                    if (prop.Name == "Count")
                    {
                        cnt = (int)prop.GetValue(returned_value);
                        break;
                    }
                }
                if (cnt == 0) {
                    lDimensions(ref ndim, ref nelem, ref nrows, ref ncols, returned_value);
                    cnt = nelem;
                }
                if (returned_value.GetType().Name == "V8Array")
                {
                    cnt = returned_value.ToEnumerable().Count();
                }
                if (cnt == 0) return new object();

                dynamic dreturned_value = (dynamic)returned_value;

                if (lIsAtomic(ref dreturned_value[0]))
                {
                    Object[] rv = new object[cnt];
                    for (int i = 0; i < cnt; i++) rv[i] = dreturned_value[i];
                    return rv;
                }
                else
                {
                    int ccnt = 0;
                    int[] rccnt = new int[cnt];
                    for (int i = 0; i < cnt; i++)
                    {
                        rccnt[i] = 0;
                        foreach (PropertyDescriptor prop in TypeDescriptor.GetProperties(dreturned_value[i]))
                        {
                            if (prop.Name == "Count")
                            {
                                rccnt[i] = (int)prop.GetValue(dreturned_value[i]);
                                break;
                            }
                        }
                        if (rccnt[i]==0)
                        {
                            rccnt[i] = dreturned_value[i].length;
                        }
                        if (rccnt[i] > ccnt) ccnt = rccnt[i];
                    }
                    Object[,] rv = new object[cnt, ccnt];
                    for (int i = 0; i < cnt; i++)
                        for (int j = 0; j < rccnt[i]; j++)
                            rv[i, j] = dreturned_value[i][j];
                    return rv;
                }

            }
            catch (Exception e)
            {
                return e.Message + " in FunctionEvaluator";
            }
        }



    }
}
