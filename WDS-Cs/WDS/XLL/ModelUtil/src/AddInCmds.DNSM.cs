using System;
using System.Collections.Generic;
using System.IO;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using System.Xml;

using ExcelDna.Integration;

using MOIE=Microsoft.Office.Interop.Excel;

using WDS;
using WDS.ModelSpec;
using static WDS.Util;
using FieldName = WDS.ModelSpec.FieldName;
using Microsoft.Office.Interop.Excel;
using System.Globalization;

namespace WDS.DNMS
{

    public partial class Cmds
    {

        private static String pAssemblyLocation = null;
        private static String pWDSHome = null;
        private static String pWDSXSD = null;


        private static void pUsualSuspects()
        {
            AppDomain cDomain = AppDomain.CurrentDomain;
            pAssemblyLocation = cDomain.BaseDirectory;
            pWDSHome = sWDSHOME();
            pWDSXSD="";
            //pWDSJniPMML
            foreach (String tmpLocation in new List<string> { pWDSHome + "\\lib\\XSD", pAssemblyLocation, pAssemblyLocation + "\\Resources" })
            {
                try
                {
                    DirectoryInfo aDirectoryInfo = new DirectoryInfo(tmpLocation);
                    FileInfo[] lFileInfo = aDirectoryInfo.GetFiles("WDS*.xsd");
                    if (lFileInfo != null && lFileInfo.Length > 0)
                    {
                        pWDSXSD = tmpLocation;
                        break;
                    }
                } catch (Exception) { }
            }
            if (pWDSXSD == "")
            {
                pWDSXSD = null;
                throw new WDSException("Cannot find location for WDS*.xsd");
            }

        }


        private static void MapElement(MOIE.Worksheet tws, MOIE.XmlMap m, MOIE.XmlNamespace ns, string rpath, XmlNode n, ref MOIE.Range r)
        {
            if (n.ChildNodes.Count == 1 && n.ChildNodes[0].Name == "xs:complexType")
            {
                if (n.SelectNodes("./@*[name()='maxOccurs']").Count == 0)
                {
                    string nname = n.Attributes.GetNamedItem("name").Value;
                    string npath = rpath + "/" + nname;
                    if (!bIn(nname, "ParameterList", "Segments", "Units", "Stocks", "Flows", "Orders", "States", "Stages", "Bridges", "StateLabels"))
                    {
                        r = r.Offset[1, 0];
                        r.Value2 = "Node Name";
                        r.Offset[0, 1].Value2 = nname;
                    }
                    foreach (XmlNode a in n.ChildNodes[0].SelectNodes("./*[name()='xs:attribute']"))
                    {
                        r = r.Offset[1, 0];
                        string aname = a.Attributes.GetNamedItem("name").Value;
                        string apath = npath + "/@" + aname;
                        r.Value2 = aname;
                        r.Offset[0, 1].XPath.SetValue(m, apath, ns);
                    }
                    foreach (XmlNode e in n.ChildNodes[0].SelectNodes("./*[name()='xs:sequence']/*[name()='xs:element']"))
                    {
                        string ename = e.Attributes.GetNamedItem("name").Value;
                        if (!bIn(ename, "ParameterList"))
                        {

                            //form specific adjustments
                            switch (ename)
                            {
                                case "Units":
                                    r = r.Offset[-r.Row + 1, 5];
                                    break;
                                case "Unit":
                                case "Stock":
                                case "Flow":
                                    r = r.Offset[-7, 4];
                                    break;
                                case "Stocks":
                                case "Flows":
                                    r = r.Offset[4, -4];
                                    break;
                                case "Orders":
                                    r = r.Offset[-r.Row + 1 + 15, -r.Column + 1];
                                    break;
                            }

                            r = r.Offset[1, 0];
                            r.Value2 = ename;
                        }
                        if (e.ChildNodes.Count == 0)
                        {
                            string epath = npath + "/" + ename;
                            r.Offset[0, 1].XPath.SetValue(m, epath, ns);
                        }
                        else if (e.ChildNodes.Count == 1 && n.ChildNodes[0].Name == "xs:complexType")
                        {
                            MapElement(tws, m, ns, npath, e, ref r);
                        }
                    }
                }
                else
                {
                    string nname = n.Attributes.GetNamedItem("name").Value;
                    int ncols = n.ChildNodes[0].SelectNodes("./*[name()='xs:attribute']").Count + n.ChildNodes[0].SelectNodes("./*[name()='xs:sequence']/*[name()='xs:element']").Count;
                    r = r.Offset[1, 0];
                    MOIE.ListObjects sLO = tws.ListObjects;
                    MOIE.ListObject aLO = sLO.AddEx(MOIE.XlListObjectSourceType.xlSrcRange, tws.Range[r, r.Offset[1, ncols - 1]], null, MOIE.XlYesNoGuess.xlYes);
                    string aLOName = rpath + "/" + nname;
                    aLO.Name = aLOName.replaceAll("/([^_]+)(List|s)/\\1$", "/$1$2").replaceAll("^/(WDSDNSM|DNSM|WDS)","").replaceAll("/", "_");
                    switch (nname)
                    {
                        case "Unit":
                            r = r.Offset[2, 0];
                            break;
                        case "Stock":
                            r = r.Offset[15, 0];
                            break;
                        default:
                            r = r.Offset[5, 0];
                            break;
                    }
                    int j = 0;
                    foreach (XmlNode a in n.ChildNodes[0].SelectNodes("./*[name()='xs:attribute']"))
                    {
                        j++;
                        string aname = a.Attributes.GetNamedItem("name").Value;
                        aLO.ListColumns[j].Name = aname;
                        aLO.ListColumns[j].DataBodyRange.XPath.SetValue(m, rpath + "/" + nname + "/@" + aname, ns);
                    }
                    foreach (XmlNode e in n.ChildNodes[0].SelectNodes("./*[name()='xs:sequence']/*[name()='xs:element']"))
                    {
                        j++;
                        string ename = e.Attributes.GetNamedItem("name").Value;
                        aLO.ListColumns[j].Name = ename;
                        aLO.ListColumns[j].DataBodyRange.XPath.SetValue(m, rpath + "/" + nname + "/" + ename, ns);
                    }

                    //form specific redirects
                    if (nname == "State")  //start Stages in column 10
                    {
                        r = r.Offset[-r.Row + 1, 10];
                    }
                }
            }

        }


        [ExcelCommand(Description = "Build New DNSM Workbook"
            , ExplicitRegistration = true
            )]
        public static void BuildNewDNSMWorkbook()
        {

            MOIE.Application tapp = (ExcelDnaUtil.Application as MOIE.Application);
            MOIE.Workbook twb = tapp.Workbooks.Add();
            AddVBAModule(twb, "WDSCore", "WDSUtilODBC", "WDSUtilPivotTable", "WDSUtilGenericTOC");

            //Scripting Runtime (for a VBA dictionary)
            twb.VBProject.References.AddFromFile("C:\\Windows\\System32\\scrrun.dll");
            //Microsoft XML, v6.0
            twb.VBProject.References.AddFromFile("C:\\Windows\\System32\\msxml6.dll");
            //Microsoft ActiveX Data Objects 6.1
            twb.VBProject.References.AddFromFile("C:\\Program Files\\Common Files\\System\\ado\\msado15.dll");
            //VBScript_RegExp_66
            twb.VBProject.References.AddFromFile("C:\\Windows\\System32\\vbscript.dll\\3");



            MOIE.Worksheet tws = twb.Sheets[1];
            tws.Name = "README";
            tws.Range["A1"].Value2 = "Created via New DNSM Workbook command.";
            MOIE.Worksheet SpecLeft = twb.Worksheets.Add();
            SpecLeft.Move(After: tws);
            SpecLeft.Name = "Spec>>";
            MOIE.Worksheet SpecRight = twb.Worksheets.Add();
            SpecRight.Move(After: SpecLeft);
            SpecRight.Name = "<<Spec";

            MOIE.Worksheet SD = twb.Worksheets.Add();
            SD.Move(Before: SpecRight);
            SD.Name = "DNSMDriver";

            MOIE.Worksheet SS = twb.Worksheets.Add();
            SS.Name = "StatesAndStages";
            SS.Move(Before: SpecRight);

            MOIE.Worksheet SF = twb.Worksheets.Add();
            SF.Name = "StocksAndFlows";
            SF.Move(Before: SpecRight);

            MOIE.Worksheet Samp = twb.Worksheets.Add();
            Samp.Name = "StateSpaceSampler";
            Samp.Move(Before: SpecRight);

            if (pWDSXSD == null) pUsualSuspects();
            if (pWDSXSD == null)
            {
                MessageBox.Show("Cannot find WDS*.xsd, check environment variable WDSHOME");
                return;
            }

            int row = 1;

            //Driver Info
            MOIE.XmlMap SDMap = twb.XmlMaps.Add(pWDSXSD + "\\WDSDNSMDriver.xsd");
            MOIE.XmlNamespace SDns = SDMap.Schemas[1].Namespace;
            XmlDocument SDxml = new XmlDocument();
            SDxml.LoadXml(SDMap.Schemas[1].XML);
            //Top Element past schema
            XmlNode SDxmlroot = SDxml.DocumentElement.SelectSingleNode("/node()/*");
            MOIE.Range r = SD.Cells[row, 1];
            r.Value2 = "Driver Information";
            SD.Range[r, r.Offset[0, 3]].Merge(true);
            SD.Range[r, r.Offset[0, 3]].Font.Bold=true;
            MapElement(SD,SDMap,SDns, "", SDxmlroot, ref r);
            SD.Cells.EntireColumn.AutoFit();
            
            //States and Stages
            MOIE.XmlMap SSMap = twb.XmlMaps.Add(pWDSXSD + "\\WDSStatesAndStages.xsd");
            MOIE.XmlNamespace SSns = SSMap.Schemas[1].Namespace;
            XmlDocument SSxml = new XmlDocument();
            SSxml.LoadXml(SSMap.Schemas[1].XML);
            //Top Element past schema
            XmlNode SSxmlroot = SSxml.DocumentElement.SelectSingleNode("/node()/*");
            r = SS.Cells[row, 1];
            r.Value2 = "States and Stages Specification";
            SS.Range[r, r.Offset[0, 3]].Merge(true);
            SS.Range[r, r.Offset[0, 3]].Font.Bold=true;
            MapElement(SS,SSMap,SSns, "", SSxmlroot, ref r);
            SS.Cells.EntireColumn.AutoFit();

            //Stocks and Flows
            MOIE.XmlMap SFMap = twb.XmlMaps.Add(pWDSXSD + "\\WDSStocksAndFlows.xsd");
            MOIE.XmlNamespace SFns = SFMap.Schemas[1].Namespace;
            XmlDocument SFxml = new XmlDocument();
            SFxml.LoadXml(SFMap.Schemas[1].XML);
            //Top Element past schema
            XmlNode SFxmlroot = SFxml.DocumentElement.SelectSingleNode("/node()/*");
            r = SF.Cells[row, 1];
            r.Value2 = "Stocks an Flows Specification";
            SF.Range[r, r.Offset[0, 3]].Merge(true);
            SF.Range[r, r.Offset[0, 3]].Font.Bold=true;
            MapElement(SF,SFMap,SFns, "", SFxmlroot, ref r);
            SF.Cells.EntireColumn.AutoFit();

            //State Space Sampler
            MOIE.XmlMap SampMap = twb.XmlMaps.Add(pWDSXSD + "\\WDSDNSMSampler.xsd");
            MOIE.XmlNamespace Sampns = SampMap.Schemas[1].Namespace;
            XmlDocument Sampxml = new XmlDocument();
            Sampxml.LoadXml(SampMap.Schemas[1].XML);
            //Top Element past schema
            XmlNode Sampxmlroot = Sampxml.DocumentElement.SelectSingleNode("/node()/*");
            r = Samp.Cells[row, 1];
            r.Value2 = "Stocks an Flows Specification";
            Samp.Range[r, r.Offset[0, 3]].Merge(true);
            Samp.Range[r, r.Offset[0, 3]].Font.Bold=true;
            MapElement(Samp,SampMap,Sampns, "", Sampxmlroot, ref r);
            Samp.Cells.EntireColumn.AutoFit();

               
            tapp.Run("xsql_SetUpODBCNamedRanges");
            MOIE.Worksheet nws = twb.ActiveSheet;
            nws.Move(Before: SpecRight);
            nws.Range["A1"].Value2 = "Parameters for connection to database";
            nws.Cells.Columns.AutoFit();
            foreach (string pvtspec in new ArrayList<string> { "MainPVTSpec", "TotalsPVTSpec", "RefPVTSpec", "RefPVTSpecWithAgePaged" })
            {
                tapp.Run("pvt_LoadPivotTableODBCSpecProtoType");
                nws = twb.ActiveSheet;
                nws.Name = pvtspec;
                nws.Move(Before: SpecRight);
            }


            tapp.Run("zzaCreateTOC");
            return;

        }

        [ExcelCommand(Description = "DNSM, Configure States and Stages"
            , ExplicitRegistration = true
            )]
        public static void DNSMConfigSS()
        {

            MOIE.Application tapp = (ExcelDnaUtil.Application as MOIE.Application);
            MOIE.Workbook twb = tapp.ActiveWorkbook;
            MOIE.Worksheet tws = twb.Sheets["StatesAndStages"];
            tws.Activate();
            XmlMap SSmap = twb.XmlMaps["WDSStatesAndStages_Map"];
            tws.XmlDataQuery("/WDSStatesAndStages/@Name").Value2 = "StatesAndStages";
            tws.XmlDataQuery("/WDSStatesAndStages/@Handle").Value2 = "StatesAndStagesSpec";

            MOIE.Range rParam = tws.XmlDataQuery("/WDSStatesAndStages/Parameters/Parameter/@Name");

            MOIE.Range rStates = tws.XmlDataQuery("/WDSStatesAndStages/States/@Handle");
            rStates.Value2 = "StateSpec";
            rParam.Value2 = "StatesHandle";
            rParam.Offset[0, 1].Value2 = "string";
            rParam.Offset[0, 2].NumberFormat = NumberStyles.None  ;
            rParam.Offset[0, 2].Formula = "=" + rStates.Address;

            MOIE.Range rStages = tws.XmlDataQuery("/WDSStatesAndStages/Stages/@Handle");
            rParam = rParam.Offset[1, 0];
            rStages.Value2 = "StageSpec";
            rParam.Value2 = "StagesHandle";
            rParam.Offset[0, 1].Value2 = "string";
            rParam.Offset[0, 2].NumberFormat = NumberStyles.None  ;
            rParam.Offset[0, 2].Formula = "=" + rStages.Address;

            MOIE.Range rBridges = tws.XmlDataQuery("/WDSStatesAndStages/Bridges/@Handle");
            rParam = rParam.Offset[1, 0];
            rBridges.Value2 = "BridgeSpec";
            rParam.Value2 = "BridgesHandle";
            rParam.Offset[0, 1].Value2 = "string";
            rParam.Offset[0, 2].NumberFormat = NumberStyles.None  ;
            rParam.Offset[0, 2].Formula = "=" + rBridges.Address;

            tws.XmlDataQuery("/WDSStatesAndStages/States/@Handle").Value2 = "StateSpec";
            tws.XmlDataQuery("/WDSStatesAndStages/States/Number").Formula = "=COUNT(StatesAndStages_States[Position])";
            tws.XmlDataQuery("/WDSStatesAndStages/States/NumberOfBaseDimensions").Value2 = 2;
            tws.XmlDataQuery("/WDSStatesAndStages/States/NumberOfAgePages").Value2 = 24;
            foreach (string s in new ArrayList<string> { "Axis1LimitDefault", "Axis2LimitDefault", "Axis3LimitDefault", "Axis4LimitDefault" })
            {
                tws.XmlDataQuery("/WDSStatesAndStages/States/"+s).Value2 = 0;
            }
            rParam = tws.XmlDataQuery("/WDSStatesAndStages/States/Parameters/Parameter/@Name");
            rParam.Value2 = "GeneralPrefix";
            rParam.Offset[0,1].Value2 = "string";
            rParam.Offset[0,2].Value2 = "aaa";
            rParam = rParam.Offset[1, 0];
            rParam.Value2 = "StateVariable";
            rParam.Offset[0,1].Value2 = "string";
            rParam.Offset[0,2].Value2 = "atState";
            rParam = rParam.Offset[1, 0];
            rParam.Value2 = "StateVariable_Lag1";
            rParam.Offset[0,1].Value2 = "string";
            rParam.Offset[0,2].Value2 = "atState_Lag1";
            MOIE.Range r = tws.XmlDataQuery("/WDSStatesAndStages/States/State/@Position");
            r.Formula = "=N(" + r.Offset[-1, 0].AddressLocal[false,false,XlReferenceStyle.xlA1] + ")+1";
            r.Offset[0, 1].Value2 = "aaaNULL";
            r.Offset[0, 2].Value2 = "NULL";
            r.Offset[0, 3].Value2 = "Initial";
            r.Offset[0, 4].Value2 = "Yes";
            r.Offset[0, 5].Value2 = "StrictlyTransient";
            r.Offset[0, 6].Value2 = 0;

            r = r.Offset[1, 0];
            r.Offset[0, 1].Value2 = "abaZ";
            r.Offset[0, 2].Value2 = "Z";
            //r.Offset[0, 3].Value2 = "";
            r.Offset[0, 4].Value2 = "No";
            r.Offset[0, 5].Value2 = "Transient";
            r.Offset[0, 6].Value2 = 0;

            r = r.Offset[1, 0];
            r.Offset[0, 1].Value2 = "acaI";
            r.Offset[0, 2].Value2 = "I";
            //r.Offset[0, 3].Value2 = "";
            r.Offset[0, 4].Value2 = "No";
            r.Offset[0, 5].Value2 = "Transient";
            r.Offset[0, 6].Value2 = 0;

            r = r.Offset[1, 0];
            r.Offset[0, 1].Value2 = "adaD0";
            r.Offset[0, 2].Value2 = "D0";
            //r.Offset[0, 3].Value2 = "";
            r.Offset[0, 4].Value2 = "No";
            r.Offset[0, 5].Value2 = "Transient";
            r.Offset[0, 6].Value2 = 0;

            r = r.Offset[1, 0];
            r.Offset[0, 1].Value2 = "adaD1";
            r.Offset[0, 2].Value2 = "D1";
            //r.Offset[0, 3].Value2 = "";
            r.Offset[0, 4].Value2 = "No";
            r.Offset[0, 5].Value2 = "Transient";
            r.Offset[0, 6].Value2 = 1;

            r = r.Offset[1, 0];
            r.Offset[0, 1].Value2 = "ataDC";
            r.Offset[0, 2].Value2 = "DC";
            //r.Offset[0, 3].Value2 = "";
            r.Offset[0, 4].Value2 = "No";
            r.Offset[0, 5].Value2 = "StrictlyTransient";
            r.Offset[0, 6].Value2 = 1000;

            r = r.Offset[1, 0];
            r.Offset[0, 1].Value2 = "ataP";
            r.Offset[0, 2].Value2 = "P";
            //r.Offset[0, 3].Value2 = "";
            r.Offset[0, 4].Value2 = "No";
            r.Offset[0, 5].Value2 = "StrictlyTransient";
            r.Offset[0, 6].Value2 = 1000;

            r = r.Offset[1, 0];
            r.Offset[0, 1].Value2 = "axaDC";
            r.Offset[0, 2].Value2 = "DC";
            //r.Offset[0, 3].Value2 = "";
            r.Offset[0, 4].Value2 = "No";
            r.Offset[0, 5].Value2 = "Absorbing";
            r.Offset[0, 6].Value2 = 1000;

            r = r.Offset[1, 0];
            r.Offset[0, 1].Value2 = "axaP";
            r.Offset[0, 2].Value2 = "P";
            //r.Offset[0, 3].Value2 = "";
            r.Offset[0, 4].Value2 = "No";
            r.Offset[0, 5].Value2 = "Absorbing";
            r.Offset[0, 6].Value2 = 1000;



            tws.XmlDataQuery("/WDSStatesAndStages/Stages/@Handle").Value2 = "StageSpec";
            tws.XmlDataQuery("/WDSStatesAndStages/Stages/Number").Formula = "=COUNT(StatesAndStages_Stages[Position])";
            rParam = tws.XmlDataQuery("/WDSStatesAndStages/Stages/Parameters/Parameter/@Name");
            rParam.Value2 = "GeneralPrefix";
            rParam.Offset[0,1].Value2 = "string";
            rParam.Offset[0,2].Value2 = "Sg";
            
            r = tws.XmlDataQuery("/WDSStatesAndStages/Stages/Stage/@Position");
            r.Formula = "=N(" + r.Offset[-1, 0].AddressLocal[false,false,XlReferenceStyle.xlA1] + ")+1";
            r.Offset[0, 1].Value2 = "Sg1";
            r.Offset[0, 2].Value2 = "1";
            r.Offset[0, 3].Value2 = "Initial";

            tws.XmlDataQuery("/WDSStatesAndStages/Bridges/@Handle").Value2 = "BridgeSpec";
            tws.XmlDataQuery("/WDSStatesAndStages/Bridges/Number").Formula = "=COUNT(StatesAndStages_Bridges[Position])";
            rParam = tws.XmlDataQuery("/WDSStatesAndStages/Bridges/Parameters/Parameter/@Name");
            rParam.Value2 = "DefaultType";
            rParam.Offset[0,1].Value2 = "string";
            rParam.Offset[0,2].Value2 = "PickUp";

            tws.Cells.Columns.AutoFit();

        }

        [ExcelCommand(Description = "DNSM, Configure Stocks and Flows"
            , ExplicitRegistration = true
            )]
        public static void DNSMConfigSF()
        {

            MOIE.Application tapp = (ExcelDnaUtil.Application as MOIE.Application);
            MOIE.Workbook twb = tapp.ActiveWorkbook;
            MOIE.Worksheet tws = twb.Sheets["StocksAndFlows"];
            tws.Activate();
            XmlMap SSmap = twb.XmlMaps["WDSStocksAndFlows_Map"];
            tws.XmlDataQuery("/WDSStocksAndFlows/@Name").Value2 = "StocksAndFlows";
            tws.XmlDataQuery("/WDSStocksAndFlows/@Handle").Value2 = "StocksAndFlowsSpec";

            MOIE.Range rParam = tws.XmlDataQuery("/WDSStocksAndFlows/Parameters/Parameter/@Name");

            MOIE.Range rUnits = tws.XmlDataQuery("/WDSStocksAndFlows/Units/@Handle");
            rUnits.Value2 = "UnitSpec";
            rParam.Value2 = "UnitsHandle";
            rParam.Offset[0, 1].Value2 = "string";
            rParam.Offset[0, 2].NumberFormat = NumberStyles.None  ;
            rParam.Offset[0, 2].Formula = "=" + rUnits.Address;

            MOIE.Range rStocks = tws.XmlDataQuery("/WDSStocksAndFlows/Stocks/@Handle");
            rParam = rParam.Offset[1, 0];
            rStocks.Value2 = "StockSpec";
            rParam.Value2 = "StocksHandle";
            rParam.Offset[0, 1].Value2 = "string";
            rParam.Offset[0, 2].NumberFormat = NumberStyles.None  ;
            rParam.Offset[0, 2].Formula = "=" + rStocks.Address;

            MOIE.Range rFlows = tws.XmlDataQuery("/WDSStocksAndFlows/Flows/@Handle");
            rParam = rParam.Offset[1, 0];
            rFlows.Value2 = "FlowSpec";
            rParam.Value2 = "FlowsHandle";
            rParam.Offset[0, 1].Value2 = "string";
            rParam.Offset[0, 2].NumberFormat = NumberStyles.None  ;
            rParam.Offset[0, 2].Formula = "=" + rFlows.Address;

            MOIE.Range rOrders = tws.XmlDataQuery("/WDSStocksAndFlows/Orders/@Handle");
            rParam = rParam.Offset[1, 0];
            rOrders.Value2 = "OrderSpec";
            rParam.Value2 = "OrdersHandle";
            rParam.Offset[0, 1].Value2 = "string";
            rParam.Offset[0, 2].NumberFormat = NumberStyles.None  ;
            rParam.Offset[0, 2].Formula = "=" + rOrders.Address;

            //Units
            rParam = tws.XmlDataQuery("/WDSStocksAndFlows/Units/Parameters/Parameter/@Name");
            rParam.Value2 = "GeneralPrefix";
            rParam.Offset[0, 1].Value2 = "string";
            rParam.Offset[0, 2].Value2 = "U";

            MOIE.Range r = tws.XmlDataQuery("/WDSStocksAndFlows/Units/Unit/@Position");
            r.Formula = "=N(" + r.Offset[-1, 0].AddressLocal[false,false,XlReferenceStyle.xlA1] + ")+1";
            int i = 0;
            foreach (object o in new ArrayList<object> { "Units", "Units", "Units", "N", "MC", 1, 0, 0.4 })
            {
                i++;
                r.Offset[0, i].Value2 = o;
            }

            //Stocks
            rParam = tws.XmlDataQuery("/WDSStocksAndFlows/Stocks/Parameters/Parameter/@Name");
            rParam.Value2 = "GeneralPrefix";
            rParam.Offset[0, 1].Value2 = "string";
            rParam.Offset[0, 2].Value2 = "B";

            r = tws.XmlDataQuery("/WDSStocksAndFlows/Stocks/Stock/@Position");
            r.Formula = "=N(" + r.Offset[-1, 0].AddressLocal[false,false,XlReferenceStyle.xlA1] + ")+1";
            foreach (ArrayList<object> oo in new ArrayList<ArrayList<object>> {
                new ArrayList<object> { "BAR","AR","Accounts Receivable","stARBalance","Agg",null,"NC",1, "MacroOutput", 0,0,"NumberOfBases"
                                ,"Base1Type","BFCs","Base1IndexOrCode",1
                                ,"Base2Type","BFees","Base2IndexOrCode",1
                                ,"Base3Type","BCash","Base3IndexOrCode",1
                                ,"Base4Type","BPurch","Base4IndexOrCode",1
                                ,"Base5Type",null,"Base5ndexOrCode",1
                                ,"Base6Type",null,"Base6IndexOrCode",1
                                ,}
                ,new ArrayList<object> { "BPB","PB","Principal Balance","stPrincipalBalance","Agg",null,"NC",1, null,0,0,null,null,"BCash",null,null,null,"BPurch"}
                ,new ArrayList<object> { "BCL","CL","Credit Limit","stCreditLimit","SLR",null,"BUR",1, null,0,0,null,null,"BCash",null,null,null,"BPurch"}
                ,new ArrayList<object> { "BPurch","Purch","Purchases Balance","stPurch","SumOfBases",null,"NC",0, null,0,0,null,null,"BCash",null,null,null,"BPurch"}
                ,new ArrayList<object> { "BCash","Cash","Cash Advances","stCash","SumOfBases",null,"NC",0, null,0,0,null,null,"BCash",null,null,null,"BPurch"}
                ,new ArrayList<object> { "BFees","Fees","Fees","stFees","SumOfBases",null,"NC",0, null,0,0,null,null,"BCash",null,null,null,"BPurch"}
                ,new ArrayList<object> { "BFCs","FCs","Finance Charges","stFCs","SumOfBases",null,"NC",0, null,0,0,null,null,"BCash",null,null,null,"BPurch"}
            })
            {
                i = 0;
                foreach (object o in oo)
                {
                    i++;
                    switch (o)
                    {
                        case null:
                            break;
                        case "MacroOutput":
                            r.Offset[0, i].Formula = "=N(" + r.Offset[-1, i].AddressLocal[false,false,XlReferenceStyle.xlA1] + ")+1";
                            break;
                        case "NumberOfBases":
                            r.Offset[0, i].Formula = "=COUNTA([@Base1Variable],[@Base2Variable],[@Base3Variable],[@Base4Variable],[@Base5Variable],[@Base6Variable])";
                            break;
                        case "Base1Type":
                        case "Base2Type":
                        case "Base3Type":
                        case "Base4Type":
                        case "Base5Type":
                        case "Base6Type":
                            {
                                string tmps = o.ToString().replaceAll("Type", "");
                                r.Offset[0, i].Formula = "=IF(ISBLANK([@" + tmps + "Variable]),0,IF(OR(LEFT([@" + tmps + "Variable],1)=\"B\",LEFT([@" + tmps + "Variable],1)=\"T\"),1,2))";
                            }
                            break;
                        case "Base1IndexOrCode":
                        case "Base2IndexOrCode":
                        case "Base3IndexOrCode":
                        case "Base4IndexOrCode":
                        case "Base5IndexOrCode":
                        case "Base6IndexOrCode":
                            {
                                string tmps = o.ToString().replaceAll("IndexOrCode", "");
                                r.Offset[0, i].Formula = "=IF([@" +tmps + "Type]=0,0,IF([@" + tmps + "Type]=1,MATCH([@" + tmps + "Variable],StocksAndFlows_Stocks[Mneumonic],0),MATCH([@" + tmps + "Variable],StocksAndFlows_Flows[Mneumonic],0)))";
                            }
                            break;
                        default:
                            r.Offset[0, i].Value2 = o;
                            break;
                    }
                }
                r = r.Offset[1, 0];
            }

            //Flows
            rParam = tws.XmlDataQuery("/WDSStocksAndFlows/Flows/Parameters/Parameter/@Name");
            rParam.Value2 = "GeneralPrefix";
            rParam.Offset[0, 1].Value2 = "string";
            rParam.Offset[0, 2].Value2 = "F";

            r = tws.XmlDataQuery("/WDSStocksAndFlows/Flows/Flow/@Position");
            r.Formula = "=N(" + r.Offset[-1, 0].AddressLocal[false,false,XlReferenceStyle.xlA1] + ")+1";
            foreach (ArrayList<object> oo in new ArrayList<ArrayList<object>> {
                new ArrayList<object> { "FPurch","Purch","Purchases","Pre","A","UnitBasisUnitRollBounded","ftPurchases",1,1,3,"NumberOfBases"
                                ,"Base1Type",null,"Base1IndexOrCode",1
                                ,"Base2Type",null,"Base2IndexOrCode",1
                                ,"Base3Type",null,"Base3IndexOrCode",1
                                ,"Base4Type",null,"Base4IndexOrCode",1
                                ,"Base5Type",null,"Base5ndexOrCode",1
                                ,"Base6Type",null,"Base6IndexOrCode",1
                                ,}
                ,new ArrayList<object> { "FCash","Cash","Cash Advances", "Pre","A","UnitBasisUnitRollBounded","ftCash",1,1,0.4, }
            })
            {
                i = 0;
                foreach (object o in oo)
                {
                    i++;
                    switch (o)
                    {
                        case null:
                            break;
                        case "MacroOutput":
                            r.Offset[0, i].Formula = "=N(" + r.Offset[-1, i].AddressLocal[false,false,XlReferenceStyle.xlA1] + ")+1";
                            break;
                        case "NumberOfBases":
                            r.Offset[0, i].Formula = "=COUNTA([@Base1Variable],[@Base2Variable],[@Base3Variable],[@Base4Variable],[@Base5Variable],[@Base6Variable])";
                            break;
                        case "Base1Type":
                        case "Base2Type":
                        case "Base3Type":
                        case "Base4Type":
                        case "Base5Type":
                        case "Base6Type":
                            {
                                string tmps = o.ToString().replaceAll("Type", "");
                                r.Offset[0, i].Formula = "=IF(ISBLANK([@" + tmps + "Variable]),0,IF(OR(LEFT([@" + tmps + "Variable],1)=\"B\",LEFT([@" + tmps + "Variable],1)=\"T\"),1,2))";
                            }
                            break;
                        case "Base1IndexOrCode":
                        case "Base2IndexOrCode":
                        case "Base3IndexOrCode":
                        case "Base4IndexOrCode":
                        case "Base5IndexOrCode":
                        case "Base6IndexOrCode":
                            {
                                string tmps = o.ToString().replaceAll("IndexOrCode", "");
                                r.Offset[0, i].Formula = "=IF([@" +tmps + "Type]=0,0,IF([@" + tmps + "Type]=1,MATCH([@" + tmps + "Variable],StocksAndFlows_Stocks[Mneumonic],0),MATCH([@" + tmps + "Variable],StocksAndFlows_Flows[Mneumonic],0)))";
                            }
                            break;
                        default:
                            r.Offset[0, i].Value2 = o;
                            break;
                    }
                }
                r = r.Offset[1, 0];
            }

            //Orders
            r = tws.XmlDataQuery("/WDSStocksAndFlows/Orders/@Handle");
            r.Offset[-1, 1].Value2 = "Check:";
            r.Offset[-1, 2].Formula = "=IF(" + r.Offset[0, 2].Address + "=" + r.Offset[1, 2].Address + ",\"OK\",\"NOT FULLY SPEC'd\")";
            r.Offset[0, 1].Value2 = "#Units/Stocks/Flows:";
            r.Offset[0, 2].Formula = "=COUNTA(StocksAndFlows_Units[Position])+COUNTA(StocksAndFlows_Stocks[Position])+COUNTA(StocksAndFlows_Flows[Position])";
            r.Offset[1, 1].Value2 = "#Orders:";
            r.Offset[1, 2].Formula = "=COUNTA(StocksAndFlows_Orders[Position])";
            
            r = tws.XmlDataQuery("/WDSStocksAndFlows/Orders/Order/@Position");
            r.Formula = "=N(" + r.Offset[-1, 0].AddressLocal[false,false,XlReferenceStyle.xlA1] + ")+1";
            r.Offset[0, 1].Value2 = "Units";
            r.Offset[0, 2].Formula = "=IF(NOT(ISNA(MATCH([@Mneumonic],StocksAndFlows_Units[Mneumonic],0))),0,IF(NOT(ISNA(MATCH([@Mneumonic],StocksAndFlows_Stocks[Mneumonic],0))),1,2))";
            r.Offset[0, 3].Formula = "=IF([@USF]=0,MATCH([@Mneumonic],StocksAndFlows_Units[Mneumonic],0),IF([@USF]=1,MATCH([@Mneumonic],StocksAndFlows_Stocks[Mneumonic],0),MATCH([@Mneumonic],StocksAndFlows_Flows[Mneumonic],0)))";

            tws.Cells.Columns.AutoFit();

        }


        public static String XSDUserInput()
        {

            //Typing for possible GC purposes
            MOIE.Application tapp = null;
            //MOIE.Range trng = null;
            //MOIE.Range trng2 = null;
            //MOIE.XmlMap aXmlMap = null;
            MOIE.ListObject aListObject = null;
            MOIE.Workbook twb = null;
            MOIE.Worksheet tws = null;
            //JniPMMLItem aJniPMMLItem=null;
            //XmlDocument aXmlDocument=null;
            //XmlNodeList aXmlNodeList=null;

            String rv = "";


            //int h=-1;
            //Boolean bIsModelCached=true;
            tapp = (ExcelDnaUtil.Application as MOIE.Application);
            Boolean screenupdating_prior=tapp.ScreenUpdating;
            MOIE.XlCalculation calculation_prior=tapp.Calculation;

            try {


                //int i, j, iP1, jP1, ii, iiP1;

                twb = tapp.ActiveWorkbook;
                tws = twb.ActiveSheet;

                String sFile="?";
                MessageBoxButtons msgboxbuttons = MessageBoxButtons.YesNoCancel;
                DialogResult msgboxresponse;
                //bIsModelCached = false;
                msgboxresponse = MessageBox.Show("Would you like to point to an XSD file (Yes/no)?", "Confirm", msgboxbuttons);
                if ( msgboxresponse == System.Windows.Forms.DialogResult.Cancel )
                    throw new WDSException("Cancel");
                if ( msgboxresponse == System.Windows.Forms.DialogResult.Yes )
                    using ( OpenFileDialog aOpenFileDialog = new OpenFileDialog() ) {
                        aOpenFileDialog.InitialDirectory = tapp.ActiveWorkbook.Path;
                        aOpenFileDialog.Filter = "XSD File (*.xsd)|*.xsd|All Files (*.*)|*.*";
                        aOpenFileDialog.FilterIndex = 1;
                        aOpenFileDialog.RestoreDirectory = true;
                        aOpenFileDialog.AddExtension = true;
                        aOpenFileDialog.DefaultExt = ".xsd";
                        aOpenFileDialog.CheckFileExists = true;
                        aOpenFileDialog.CheckPathExists = true;
                        aOpenFileDialog.Title = "XML Schema (XSD) File....";
                        if ( aOpenFileDialog.ShowDialog() == DialogResult.OK )
                            sFile = aOpenFileDialog.FileName;
                        else
                            throw new WDSException("Cancel");
                        rv=FetchFileAsString(sFile);
                    }
                else {
                    msgboxresponse = MessageBox.Show("Point to an XSD string in a cells (Yes) or leave unspecified (No)?", "Confirm", msgboxbuttons);
                    if ( msgboxresponse == System.Windows.Forms.DialogResult.Cancel )
                        throw new WDSException("Cancel");
                    if ( msgboxresponse == System.Windows.Forms.DialogResult.Yes ) {
                        try {
                            MOIE.Range trng3 = tapp.InputBox("Use an XSD as one string contained in a cell, enter cell address (navigable)", "XSD Input", "Entire XSD File as a String", 100, 100, "", 0, 8) as MOIE.Range;
                            sFile = trng3.Text;
                            trng3 = null;
                            if ( !sFile.StartsWith("<?xml") ) {
                                if ( sFile.IndexOf("!") < 0 )
                                    sFile = "'[" + tapp.ActiveWorkbook.Name + "]" + aListObject.DataBodyRange.Worksheet.Name + "'!" + sFile;
                                ExcelReference rf = XlCall.Excel(XlCall.xlfEvaluate, sFile) as ExcelReference;
                                trng3 = tapp.Evaluate(XlCall.Excel(XlCall.xlfReftext, rf, true)) as MOIE.Range;
                                sFile = trng3.Text;
                                rf = null;
                                trng3 = null;
                                rv = sFile;
                            } else {
                                throw new WDSException("Error, value not a valid XSD string");
                            }
                        }
                        catch {
                            throw new WDSException("Cancel");
                        }
                    }
                }

            }
            catch ( WDSException e ) {
                if ( tapp.ScreenUpdating != screenupdating_prior ) tapp.ScreenUpdating = screenupdating_prior;
                if ( !e.getMessage().Equals("Cancel") ) {
                    MessageBox.Show(e.getMessage() + "\n" + e.StackTrace.ToString());
                }
            }
            catch ( Exception e ) {
                if ( tapp.ScreenUpdating != screenupdating_prior ) tapp.ScreenUpdating = screenupdating_prior;
                MessageBox.Show("Error!\n" + e.Message + "\n" + e.StackTrace.ToString());
            }
            finally {

                if ( tapp.ScreenUpdating != screenupdating_prior ) tapp.ScreenUpdating = screenupdating_prior;
                if ( tapp.Calculation != calculation_prior ) tapp.Calculation = calculation_prior;

                aListObject = null;
                //aXmlMap = null;
                tapp = null;
                //trng = null;
                //trng2 = null;
                twb = null;
                tws = null;

                GC.Collect();
                GC.WaitForPendingFinalizers();
                GC.Collect();
                GC.WaitForPendingFinalizers();

            }
            return rv;
        }


        [ExcelCommand(Description = "Import CSV to XMLMapped List", ExplicitRegistration =true)]
        public static void xxxImportCSVToXMLMappedList()
        {
            String sFileName = "test.csv";
            ExcelReference selection;
            MOIE.Application tapp;
            MOIE.Range trng;
            MOIE.Range trng2;
            MOIE.Workbook twb;
            MOIE.Sheets twbSheets;
            MOIE.Worksheet tws;
            MOIE.Range tblr;
            MOIE.ListObject tbl;
            MOIE.XmlMap aXmlMap;
            tapp = (ExcelDnaUtil.Application as MOIE.Application);
            Boolean screenupdating_prior=tapp.ScreenUpdating;
            MOIE.XlCalculation calculation_prior=tapp.Calculation;
            RecordSetMD aRecordSetMD;
            RecordSet aRecordSet;

            //using isContinuing instead of throwing on last steps
            Boolean isContinuing=true;

            try {

                //tapp.ScreenUpdating = false;
                tapp.Calculation = MOIE.XlCalculation.xlCalculationManual;

                int i, iP1;

                using ( OpenFileDialog aOpenFileDialog = new OpenFileDialog() ) {

                    aOpenFileDialog.InitialDirectory = tapp.ActiveWorkbook.Path;
                    aOpenFileDialog.Filter = "CSV Files (*.csv)|*.csv|All Files (*.*)|*.*";
                    aOpenFileDialog.FilterIndex = 1;
                    aOpenFileDialog.RestoreDirectory = true;
                    aOpenFileDialog.CheckPathExists = true;
                    aOpenFileDialog.CheckFileExists = true;
                    aOpenFileDialog.FileName = sFileName;
                    aOpenFileDialog.AddExtension = true;
                    aOpenFileDialog.DefaultExt = ".csv";
                    aOpenFileDialog.Title = "Import compound data from CSV (*.csv) File....";

                    if ( aOpenFileDialog.ShowDialog() == DialogResult.OK )
                        sFileName = aOpenFileDialog.FileName;
                    else
                        isContinuing = false;
                }

                if ( !isContinuing )
                    throw new WDSException("Cancel");

                String aXSDString = XSDUserInput();
                if ( aXSDString.Equals("Cancel") || aXSDString.StartsWith("Err") )
                    throw new WDSException(aXSDString);
                Boolean isXSDProvided = aXSDString.StartsWith("<");


                RecordSetMDEnums.eSchemaType aSchemaType = RecordSetMDEnums.eSchemaType.XSD;
                if ( !isXSDProvided ) aSchemaType = RecordSetMDEnums.eSchemaType.NamingConvention;

                aRecordSetMD = new RecordSetMD(RecordSetMDEnums.eMode.Input)
                .cAs(RecordSetMDEnums.eType.CSV, aSchemaType, false, aXSDString)
                .cAsDlmFile(sFileName)
                ;

                MessageBoxButtons msgboxbuttons = MessageBoxButtons.YesNoCancel;
                DialogResult msgboxresponse;

                msgboxresponse = MessageBox.Show("Does file have a header row (Yes) or (No)?", "Confirm", msgboxbuttons);
                if ( msgboxresponse == System.Windows.Forms.DialogResult.Cancel )
                    throw new WDSException("Cancel");
                if ( msgboxresponse == System.Windows.Forms.DialogResult.Yes )
                    aRecordSetMD.cWithHeaderRow();

                aRecordSetMD.mReadMapFor(null, null, true);

                aRecordSet = new RecordSet()
                .cAsInput()
                .mReadRecordSet(aRecordSetMD)
                ;

                msgboxresponse = MessageBox.Show("Write to a new sheet (Yes) or point to cell for the upper left corder (No)?", "Confirm", msgboxbuttons);
                if ( msgboxresponse == System.Windows.Forms.DialogResult.Cancel )
                    throw new WDSException("Cancel");
                if ( msgboxresponse == System.Windows.Forms.DialogResult.No ) {
                    try {
                        selection = (ExcelReference) XlCall.Excel(XlCall.xlfSelection);
                        trng = tapp.Evaluate(XlCall.Excel(XlCall.xlfReftext, selection, true)) as MOIE.Range;
                        trng2 = tapp.InputBox("Enter cell address (navigable)", "Output Location", trng.Address.ToString(), 100, 100, "", 0, 8) as MOIE.Range;
                        trng = null;
                        tws = trng2.Parent;
                        twb = tws.Parent;
                    }
                    catch {
                        throw new WDSException("Cancel");
                    }
                }
                else {
                    twb = tapp.ActiveWorkbook;
                    twbSheets = twb.Sheets;
                    tws = twbSheets.Add();
                    twbSheets = null;
                    trng2 = tws.Cells[1, 1];
                    try {
                        tws.Name = sFileName;
                    }
                    catch ( Exception ) {
                        String s = tapp.InputBox("Cannot name sheet to " + sFileName, "New Sheet Name", "Leave-As-Is", 100, 100, "");
                        if ( !s.Equals("Leave-As-Is") ) {
                            try {
                                tws.Name = s;
                            }
                            catch ( Exception ) {

                            }
                        }
                    }
                }

                //tapp.ScreenUpdating = false;

                int nRows = aRecordSet.Records.Count;
                int nColumns = aRecordSetMD.nColumns();

                for ( uint jj = 0 ; jj < nColumns ; jj++ ) {
                    trng2.Offset[0,jj].Value2 = aRecordSetMD.Column[jj].Name;
                    for ( i = 0, iP1=1 ; i < nRows ; i++, iP1++ )
                        trng2.Offset[iP1, jj].Value2 = aRecordSet.Records_Orig[i][jj];
                }

                tblr = tws.Range[trng2, trng2.Offset[nRows, nColumns - 1]];
                tbl = (MOIE.ListObject) tws.ListObjects.AddEx(MOIE.XlListObjectSourceType.xlSrcRange, tblr, null, MOIE.XlYesNoGuess.xlYes);

                if ( aRecordSetMD.SchemaType.bIn(RecordSetMDEnums.eSchemaType.XSD) ) {

                    aXmlMap = twb.XmlMaps.Add(aRecordSetMD.SchemaMatter.InputSchemaString);

                    for ( int j = 0, jP1 = 1 ; j < nColumns ; j++, jP1++ ) {
                        tbl.ListColumns[jP1].XPath.SetValue(aXmlMap
                            , "/" + aRecordSetMD.SchemaMatter.RecordSetElementName
                            + "/" + aRecordSetMD.SchemaMatter.RecordElementName
                            + "/" + aRecordSetMD.Column[j].Name);
                    }

                }

                if ( tapp.ScreenUpdating != screenupdating_prior ) tapp.ScreenUpdating = screenupdating_prior;

            }
            catch ( WDSException e ) {
                if ( tapp.ScreenUpdating != screenupdating_prior ) tapp.ScreenUpdating = screenupdating_prior;
                MessageBox.Show(e.getMessage());
            }
            catch ( Exception e ) {
                if ( tapp.ScreenUpdating != screenupdating_prior ) tapp.ScreenUpdating = screenupdating_prior;
                MessageBox.Show(e.Message);
            }
            finally {
                if ( tapp.ScreenUpdating != screenupdating_prior ) tapp.ScreenUpdating = screenupdating_prior;
                if ( tapp.Calculation != calculation_prior ) tapp.Calculation = calculation_prior;
                //Queuing up for GC
                aXmlMap = null;
                aRecordSet = null;
                aRecordSetMD = null;
                tapp = null;
                twb = null;
                twbSheets = null;
                tws = null;
                tblr = null;
                tbl = null;
                trng = null;
                trng2 = null;
                selection = null;
                GC.Collect();
                GC.WaitForPendingFinalizers();
                GC.Collect();
                GC.WaitForPendingFinalizers();
            }
            return;
        }

    }

}
