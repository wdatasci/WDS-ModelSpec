using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.IO;
using System.Text.RegularExpressions;
using ExcelDna.Integration;


namespace WDS_ExcelAddIn_Common
{
    public partial class AddIn : IExcelAddIn
    {

        private static void lDimensions(ref int ndim, ref int nelem, ref int nrows, ref int ncols, object arg1)
        {
            try {
                if ( arg1 is object[] ) {
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
                    catch (SystemException )
                    {
                        ndim = 0;
                        nelem = 0;
                        nrows = 0;
                        ncols = 0;
                    }
                    return;
                }
                if ( arg1 is ExcelMissing ) {
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
            catch ( SystemException  ) {
                ndim = 0;
                nelem = 0;
                nrows = 0;
                ncols = 0;
            }
        }


        [ExcelFunction(Name = "ClearScriptTest"
        , Category = "WDS.Core"
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


        [ExcelFunction(Name ="WDS.MSClearScript.QuoteIt"
            , Category ="WDS.MSClearScript"
            , Description ="Escapes internal quotes."
            , IsThreadSafe =true
            , IsVolatile =false
            )]
        public static String QuoteIt(String arg, String arg2)
        {
            if (arg2 == "") return arg;
            String s=Regex.Replace(arg, "([^\\])" + arg2, "${1}\\" + arg2);
            s=Regex.Replace(s, "([^\\])" + arg2, "${1}\\" + arg2);
            if (s.StartsWith(arg2)) s = "\\" + s;
            return s;
        }

        [ExcelFunction(Name = "WDS.MSClearScript.ConstantConstructorFromFile"
        , Category = "WDS.MSClearScript"
        , Description = "Executes a MS ClearScript V8 code to define a constant value that can be used elsewhere.  There are no arguments but the body of the construction is a body of a function which assigns a \"result\" variable to be assigned to the constant."
        , IsThreadSafe = true
        , IsVolatile = false
        , HelpTopic = "Hey HelpTopic"
        )]
        public static object ConstantConstructorFromFile(
            [ExcelArgument(Name = "constantname", Description = "constant name")] string constantname
            , [ExcelArgument(Name = "functionbody", Description = "a string containing the file location for the V8 function body")] String functionbody
            , [ExcelArgument(Name ="ExtraDependencies", Description ="a range, not used, but just to string dependencies in Excel")] object[] ExtraDependencies
            )
        {
            string s = "";
            try
            {
                s = "var " + constantname + " = new Function (`\r" + System.IO.File.ReadAllText(functionbody) + "\r`+'return result;')()";
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
        , Description = "Executes a MS ClearScript V8 code to define a constant value that can be used elsewhere.  There are no arguments but the body of the construction is a body of a function which assigns a \"result\" variable to be assigned to the constant."
        , IsThreadSafe = true
        , IsVolatile = false
        //, ExplicitRegistration = true
        //, HelpTopic = "Hey HelpTopic"
        , IsMacroType = false
        )]
        public static object ConstantConstructor(
            [ExcelArgument(Name = "constantname", Description = "constant name")] string constantname
            , [ExcelArgument(Name = "functionbody", Description = "a string containing the V8 function body")] String functionbody
            , [ExcelArgument(Name ="ExtraDependencies", Description ="a range, not used, but just to string dependencies in Excel")] object[] ExtraDependencies
            )
        {
            string s = "";
            try
            {

                s = "var " + constantname + " = new Function ('" + functionbody + "'+'\n return result;')()";

                lScriptEngine.Execute(s);
                return constantname;

            }
            catch (Exception e)
            {
                return e.Message;
            }
        }


        [ExcelFunction(Name = "WDS.MSClearScript.FunctionConstructorFromFile"
        , Category = "WDS.MSClearScript"
        , Description = "Executes a MS ClearScript V8 function constructor"
        , IsThreadSafe = true
        , IsVolatile = false
        //, ExplicitRegistration = true
        , HelpTopic = "The addin initializes a V8 (javascript engine used in node.js).  This function executes a function definition in the global namespace that can be called from a subsequent Evaluator."
        //, IsClusterSafe = true
        , IsHidden = false
        , IsMacroType = false
        //, SuppressOverwriteError = false
        )]
        public static object FunctionConstructorFromFile(
            [ExcelArgument(Name = "functionname", Description = "function name")] string functionname
            , [ExcelArgument(Name = "functionparams", Description = "an array of param names used in the function body")] object[] functionparams
            , [ExcelArgument(Name = "functionbody", Description = "a string containing the V8 function body")] string functionbody
            , [ExcelArgument(Name = "functionbodymaps", Description = "an optional two column array of regex changes (from, to)")] object functionbodymaps
            , [ExcelArgument(Name ="ExtraDependencies", Description ="a range, not used, but just to string dependencies in Excel")] object[] ExtraDependencies
            )
        {
            try
            {

                string s = "";
                string sb = "";

                if (functionparams.Length > 0)
                {
                    for (int i=0;i<functionparams.Length;i++)
                    {
                        s += "\"" + functionparams[i] + "\",";
                    }
                }

                sb = System.IO.File.ReadAllText(functionbody);
                int ndim=0, nelem=0, nrows=0, ncols=0;
                lDimensions(ref ndim, ref nelem, ref nrows, ref ncols, functionbodymaps);
                if (nrows>0)
                {
                    if (ncols != 2) throw new Exception("functionbodymap must have 2 columns");
                    for (int i = 0; i <nrows; i++)
                        sb = Regex.Replace(sb, ((object[,]) functionbodymaps)[i, 0].ToString(), ((object[,]) functionbodymaps)[i, 1].ToString());
                }

                s = "var " + functionname + " = new Function (" + s + "`\r" + sb + "\r`+'return result;')";
                lScriptEngine.Execute(s);
                try
                {
                    lScriptEngine.Execute("\"function\" == typeof " + functionname );
                    return functionname;
                } catch (Exception e)
                {
                    return e.Message;
                }

            }
            catch (Exception e)
            {
                return e.Message;
            }
        }


        [ExcelFunction(Name = "WDS.MSClearScript.FunctionConstructor"
        , Category = "WDS.MSClearScript"
        , Description = "Executes a MS ClearScript V8 function constructor"
        , IsThreadSafe = true
        , IsVolatile = false
        //, ExplicitRegistration = true
        //, HelpTopic = "Hey HelpTopic"
        //, IsClusterSafe = true
        //, IsHidden = false
        //, IsMacroType = false
        //, SuppressOverwriteError = false
        )]
        public static object FunctionConstructor(
            [ExcelArgument(Name = "functionname", Description = "function name")] string functionname
            , [ExcelArgument(Name = "functionparams", Description = "an array of param names used in the function body")] object[] functionparams
            , [ExcelArgument(Name = "functionbody", Description = "a string containing the V8 function body")] string functionbody
            , [ExcelArgument(Name ="ExtraDependencies", Description ="a range, not used, but just to string dependencies in Excel")] object[] ExtraDependencies
            )
        {
            try
            {

                string s = "";

                if (functionparams.Length > 0)
                {
                    for (int i=0;i<functionparams.Length;i++)
                    {
                        s += "\"" + functionparams[i] + "\",";
                    }
                }

                s="var " + functionname + " = new Function (" + s + "\"" + functionbody + "\")";
                lScriptEngine.Execute(s);
                try
                {
                    lScriptEngine.Execute("\"function\" == typeof " + functionname );
                    return functionname;
                } catch (Exception e)
                {
                    return e.Message;
                }

            }
            catch (Exception e)
            {
                return e.Message;
            }
        }



        [ExcelFunction(Name = "WDS.MSClearScript.FunctionEvaluator"
        , Category = "WDS.MSClearScript"
        , Description = "Executes a MS ClearScript V8 function (previously defined with FunctionEvaluator) on a set of parameters"
        , IsThreadSafe = true
        , IsVolatile = false
        //, ExplicitRegistration = true
        //, HelpTopic = "Hey HelpTopic"
        //, IsClusterSafe = true
        //, IsHidden = false
        //, IsMacroType = false
        //, SuppressOverwriteError = false
        )]
        public static object FunctionEvaluator(
            [ExcelArgument(Name = "functionname", Description = "function name")] string functionname
            , [ExcelArgument(Name = "functionparams", Description = "an array of param names used in the function body")] object[] functionparams
            , [ExcelArgument(Name = "functionparamsValues", Description = "an array of param values corresponding to the names")] object[] functionparamsValues
            , [ExcelArgument(Name ="ExtraDependencies", Description ="a range, not used, but just to string dependencies in Excel")] object[] ExtraDependencies
            )
        {
            try
            {

                string s = "";
                string vs = "";
                if (functionparams.Length != functionparamsValues.Length) throw new Exception("functionparams and functionparamValues must have the same length");

                if (functionparams.Length > 0)
                {
                    for (int i=0;i<functionparams.Length;i++)
                    {
                        if (i > 0)
                        {
                            s += ",";
                            vs += ",";
                        }
                        s += "\"" + functionparams[i] + "\",";
                        vs += "\"" + functionparams[i] + "\"";
                        if (functionparams[i].GetType()==typeof(string))
                            vs += "\"" + functionparams[i] + "\"";
                        else
                            vs +=  functionparams[i].ToString();
                    }
                }

                return lScriptEngine.Invoke(functionname, functionparamsValues);

            }
            catch (Exception e)
            {
                return e.Message;
            }
        }








    }
}
