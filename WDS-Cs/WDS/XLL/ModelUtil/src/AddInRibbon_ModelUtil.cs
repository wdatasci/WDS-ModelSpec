using System;
using System.Runtime.InteropServices;
using ExcelDna.Integration;
using ExcelDna.Integration.CustomUI;
using MOIE=Microsoft.Office.Interop.Excel;
using VBIDE = Microsoft.Vbe.Interop;
using System.Drawing.Imaging;
using System.Reflection;
using System.Windows.Forms;
using System.IO;
using Microsoft.Vbe.Interop;

using static WDS.Util;

namespace WDS
{
    [ComVisible(true)]
    public class RibbonController : ExcelRibbon
    {

        public override string GetCustomUI(string uiName)
        {
            return "hey";
        }


        [ExcelCommand(Description ="About"
            ,ExplicitRegistration =true
            )]
        public static void ShowAboutForm()
        {
            AddIn_About wf = new AddIn_About();
            wf.ShowDialog();
            return;
        }



        [ExcelCommand(Description ="Add WDSCore VBA Module"
            ,ExplicitRegistration = true
            )]
        public static void AddWDSCoreVBAModule()
        {
            MOIE.Application tapp = (ExcelDnaUtil.Application as MOIE.Application);
            MOIE.Workbook twb = tapp.ActiveWorkbook;
            VBIDE.VBProject tVBProject = twb.VBProject;

            bool found = false;
            foreach (VBIDE.VBComponent aVBComponent in tVBProject.VBComponents)
            {
                if (aVBComponent.Name == "WDSCore") found = true;
            }
            if (!found)
            {
                string pWDSCore = "Error, ";
                string pWDSHOME = sWDSHOME();
                if (pWDSHOME == "ERROR")
                {
                    MessageBox.Show("Either Environment Variable WDSHOME needs to be set or WDS\\lib on PATH");
                    return;
                }
                pWDSCore = pWDSHOME + "\\lib";
                try
                {
                    DirectoryInfo aDirectoryInfo = new DirectoryInfo(pWDSCore);
                    FileInfo[] lFileInfo = aDirectoryInfo.GetFiles("VBA\\WDSCore.bas");
                    pWDSCore = lFileInfo[0].FullName;
                }
                catch (Exception)
                {
                    MessageBox.Show("Cannot find WDSCore.bas in WDSHOME\\lib\\VBA or WDS\\lib\\VBA");
                }
                tVBProject.VBComponents.Import(pWDSCore);
            }
        }


        [ExcelCommand(Description ="Remove WDSCore VBA Module"
            ,ExplicitRegistration = true
            )]
        public static void RemoveWDSCoreVBAModule()
        {
            MOIE.Application tapp = (ExcelDnaUtil.Application as MOIE.Application);
            MOIE.Workbook twb = tapp.ActiveWorkbook;
            VBIDE.VBProject tVBProject = twb.VBProject;

            foreach (VBIDE.VBComponent aVBComponent in tVBProject.VBComponents)
            {
                //MessageBox.Show(aVBComponent.Name);
                if (aVBComponent.Name == "WDSCore")
                {
                    tVBProject.VBComponents.Remove(aVBComponent);
                    break;
                }
            }
        }


        //small helper
        private static void lMultiColumnCellRange(MOIE.Range r, object v, int width, bool bIsBold = false)
        {
            r.Value2 = v;
            MOIE.Range r2 = r.Parent.Range[r, r.Offset[0, width]];
            r2.Merge(true);
            if (bIsBold) r2.Font.Bold = true;
        }

        [ExcelCommand(Description ="VBA Module Check"
            ,ExplicitRegistration = true
            )]
        public static void VBACheck()
        {
            MOIE.Application tapp = (ExcelDnaUtil.Application as MOIE.Application);
            MOIE.Workbook twb = tapp.ActiveWorkbook;
            MOIE.Worksheet nws;
            object respContinue = true;
            try
            {
                nws = twb.Worksheets["VBAModuleCheck"];
                object resp = tapp.InputBox("VBAModuleCheck already exists, clear all?", "Exists", "Continue");
                if (resp is bool && (bool)resp == false) return;
                if (resp.ToString() != "Continue") return;
            }
            catch (Exception)
            {
                nws = twb.Worksheets.Add();
                nws.Name = "VBAModuleCheck";
            }

            nws.Cells.Clear();

            MOIE.Range r;

            //Excel Interop Cells is 1-based
            int i = 1;
            int j = 1;

            r = (MOIE.Range)nws.Cells[i, j];
            lMultiColumnCellRange(r, "VBA Modules, Import/Export", 4, true);
            r = r.Offset[1, 0];
            lMultiColumnCellRange(r, "WDSHOME", 4);
            r = r.Offset[1, 0];
            string pWDSHOME = sWDSHOME();
            lMultiColumnCellRange(r, pWDSHOME, 4);
            r = r.Offset[1, 0];
            lMultiColumnCellRange(r, "VBA External Location", 4);

            r = r.Offset[1, 0];
            string pWDSHOMELIBVBA = pWDSHOME + "\\lib\\VBA";
            try
            {
                DirectoryInfo aDirectoryInfo = new DirectoryInfo(pWDSHOMELIBVBA);
                lMultiColumnCellRange(r, pWDSHOMELIBVBA, 4);
            } catch (Exception)
            {
                MessageBox.Show("Problem with WDSHOME\\lib\\VBA, place correct target and hit VBA Module Check Refresh");
                return;
            }
            VBACheckRefresh();
        }

        [ExcelCommand(Description ="Remove VBA Module Check Sheet" 
            ,ExplicitRegistration = true
            )]
        public static void VBACheckRemove()
        {
            MOIE.Application tapp = (ExcelDnaUtil.Application as MOIE.Application);
            MOIE.Workbook twb = tapp.ActiveWorkbook;
            MOIE.Worksheet nws;
            object respContinue = true;
            try
            {
                nws = twb.Worksheets["VBAModuleCheck"];
                nws.Delete();
            }
            catch (Exception)
            {
                return;
            }
        }

        [ExcelCommand(Description = "VBA Module Check Refresh"
            , ExplicitRegistration = true
            )]
        public static void VBACheckRefresh()
        {
            MOIE.Application tapp = (ExcelDnaUtil.Application as MOIE.Application);
            MOIE.Workbook twb = tapp.ActiveWorkbook;
            MOIE.Worksheet nws;
            try
            {
                nws = twb.Worksheets["VBAModuleCheck"];
            }
            catch (Exception)
            {
                MessageBox.Show("Run VBA Module Check first");
                return;
            }

            MOIE.Range r;

            //Excel Interop Cells is 1-based
            int i = 1;
            int j = 1;

            while (nws.Cells[i, j].Value2 != "VBA External Location" && i < 12)
            {
                i += 1;
                if (i > 10)
                {
                    MessageBox.Show("Format of VBAModuleCheck is messed up, remove and rerun");
                    return;
                }
            }

            i += 1;
            r = nws.Cells[i, j];
            string pWDSHOMELIBVBA = r.Value;
            i += 1;
            r = (MOIE.Range)nws.Cells[i, j];
            r.Value2 = "Modules In WorkBook";
            r.Offset[0, 1].Value2 = "Modules Available";
            //r.Offset[1, 1].Value2 = "X"; // just in case empty, last cell will register correctly
            //nws.Range[r.Offset[1, 0], nws.Cells.SpecialCells(MOIE.XlCellType.xlCellTypeLastCell)].Clear();
            _VBAImportExport_Guts(twb, nws, r.Row, pWDSHOMELIBVBA);

        }

        private static void _VBAImportExport_Guts(MOIE.Workbook twb, MOIE.Worksheet tws, int row, string pWDSHOMELIBVBA)
        {
            int i = row;
            tws.Cells[row + 1, 1].Value2 = "X"; // just in case empty, last cell will register correctly
            tws.Range[tws.Cells[row + 1, 1], tws.Cells.SpecialCells(MOIE.XlCellType.xlCellTypeLastCell)].Clear();
            foreach (VBComponent aVBComponent in twb.VBProject.VBComponents)
            {
                if (aVBComponent.Type == vbext_ComponentType.vbext_ct_StdModule 
                    || aVBComponent.Type == vbext_ComponentType.vbext_ct_ClassModule )
                {
                    i += 1;
                    tws.Cells[i, 1].Value2 = aVBComponent.Name;
                }
            }
            i = row;
            DirectoryInfo aDirectoryInfo = new DirectoryInfo(pWDSHOMELIBVBA);
            foreach (FileInfo lFileInfo in aDirectoryInfo.GetFiles("*.bas*"))
            {
                i += 1;
                tws.Cells[i, 2].Value2 = lFileInfo.Name;

            }
            return;
        }

        [ExcelCommand(Description = "VBA Import Selected"
            , ExplicitRegistration = true
            )]
        public static void VBAImportSelected()
        {
            MOIE.Application tapp = (ExcelDnaUtil.Application as MOIE.Application);
            MOIE.Workbook twb = tapp.ActiveWorkbook;
            MOIE.Worksheet nws;
            try
            {
                nws = twb.Worksheets["VBAModuleCheck"];
            }
            catch (Exception)
            {
                MessageBox.Show("Run VBA Module Check first");
                return;
            }

            MOIE.Range r;

            //Excel Interop Cells is 1-based
            int i = 1;
            int j = 1;

            while (nws.Cells[i, j].Value2 != "VBA External Location" && i < 12)
            {
                i += 1;
                if (i > 10)
                {
                    MessageBox.Show("Format of VBAModuleCheck is messed up, remove and rerun");
                    return;
                }
            }


            i += 1;
            r = nws.Cells[i, j];
            string pWDSHOMELIBVBA = r.Value;
            r = r.Offset[1, 0];
            DirectoryInfo aDirectoryInfo;
            try
            {
                aDirectoryInfo = new DirectoryInfo(pWDSHOMELIBVBA);
            }
            catch (Exception)
            {
                MessageBox.Show("Check VBA External Location value");
                return;
            }
            
            i += 1;
            i += 1;
            foreach (MOIE.Range r2 in tapp.Selection)
            {
                if (r2.Parent == nws && r2.Column==2 && r2.Row>=i)
                {
                    String p = r2.Cells[1,1].Value;
                    try
                    {
                        FileInfo[] aFileInfo = aDirectoryInfo.GetFiles(p);
                        twb.VBProject.VBComponents.Import(aFileInfo[0].FullName);
                    } catch (Exception e)
                    {
                        MessageBox.Show("Problem Importing " + pWDSHOMELIBVBA + "\\" + p + ", " + e.ToString());
                    }
                }
            }

            _VBAImportExport_Guts(twb, nws, r.Row, pWDSHOMELIBVBA);

        }

        [ExcelCommand(Description = "VBA Export Selected"
            , ExplicitRegistration = true
            )]
        public static void VBAExportSelected()
        {
            MOIE.Application tapp = (ExcelDnaUtil.Application as MOIE.Application);
            MOIE.Workbook twb = tapp.ActiveWorkbook;
            MOIE.Worksheet nws;
            try
            {
                nws = twb.Worksheets["VBAModuleCheck"];
            }
            catch (Exception)
            {
                MessageBox.Show("Run VBA Module Check first");
                return;
            }

            MOIE.Range r;

            //Excel Interop Cells is 1-based
            int i = 1;
            int j = 1;

            while (nws.Cells[i, j].Value2 != "VBA External Location" && i < 12)
            {
                i += 1;
                if (i > 10)
                {
                    MessageBox.Show("Format of VBAModuleCheck is messed up, remove and rerun");
                    return;
                }
            }


            i += 1;
            r = nws.Cells[i, j];
            string pWDSHOMELIBVBA = r.Value;
            DirectoryInfo aDirectoryInfo;
            try
            {
                aDirectoryInfo = new DirectoryInfo(pWDSHOMELIBVBA);
            }
            catch (Exception)
            {
                MessageBox.Show("Check VBA External Location value");
                return;
            }
            
            r = r.Offset[1, 0];
            i += 1;
            i += 1;
            foreach (MOIE.Range r2 in tapp.Selection)
            {
                if (r2.Parent == nws && r2.Column==1 && r2.Row>=i)
                {
                    String p = r2.Cells[1, 1].Value;
                    foreach (VBComponent aVBComponent in twb.VBProject.VBComponents)
                    {
                        if (aVBComponent.Name == p)
                        {
                            int t = 0;
                            FileInfo[] aFileInfo = aDirectoryInfo.GetFiles(p + ".bas");
                            while (aFileInfo.Length > 0)
                            {
                                t += 1;
                                aFileInfo = aDirectoryInfo.GetFiles(p + ".bas." + t.toString());
                            }
                            if (t == 0)
                            {
                                aVBComponent.Export(pWDSHOMELIBVBA + "\\" + p + ".bas");
                            } else
                            {
                                object resp = tapp.InputBox("File " + pWDSHOMELIBVBA + "\\" + p + ".bas exists. Save as ?", "Exists", pWDSHOMELIBVBA + "\\" + p + ".bas." + t.toString());
                                if (resp is bool && (bool)resp == false) continue;
                                aVBComponent.Export(resp.ToString());
                            }
                            break;
                        }
                    }
                }
            }

            _VBAImportExport_Guts(twb, nws, r.Row, pWDSHOMELIBVBA);

        }

        [ExcelCommand(Description = "VBA Remove Selected"
            , ExplicitRegistration = true
            )]
        public static void VBARemoveSelected()
        {
            MOIE.Application tapp = (ExcelDnaUtil.Application as MOIE.Application);
            MOIE.Workbook twb = tapp.ActiveWorkbook;
            MOIE.Worksheet nws;
            try
            {
                nws = twb.Worksheets["VBAModuleCheck"];
            }
            catch (Exception)
            {
                MessageBox.Show("Run VBA Module Check first");
                return;
            }

            MOIE.Range r;

            //Excel Interop Cells is 1-based
            int i = 1;
            int j = 1;

            while (nws.Cells[i, j].Value2 != "VBA External Location" && i < 12)
            {
                i += 1;
                if (i > 10)
                {
                    MessageBox.Show("Format of VBAModuleCheck is messed up, remove and rerun");
                    return;
                }
            }


            i += 1;
            r = nws.Cells[i, j];
            string pWDSHOMELIBVBA = r.Value;
            i += 1;
            r = r.Offset[1, 0];
            DirectoryInfo aDirectoryInfo;
            try
            {
                aDirectoryInfo = new DirectoryInfo(pWDSHOMELIBVBA);
            }
            catch (Exception)
            {
                MessageBox.Show("Check VBA External Location value");
                return;
            }
            
            i += 1;
            i += 1;
            foreach (MOIE.Range r2 in tapp.Selection)
            {
                if (r2.Parent == nws && r2.Column==1 && r2.Row>=i)
                {
                    String p = r2.Cells[1, 1].Value;
                    foreach (VBComponent aVBComponent in twb.VBProject.VBComponents)
                    {
                        if (aVBComponent.Name == p)
                        {
                            twb.VBProject.VBComponents.Remove(aVBComponent);
                            break;
                        }
                    }
                }
            }

            _VBAImportExport_Guts(twb, nws, r.Row, pWDSHOMELIBVBA);

        }

        [ExcelCommand(Description ="Build New DNSM Workbook"
            ,ExplicitRegistration =true
            )]
        public static void BuildNewDNSMWorkbook()
        {
            //MOIE.Application tapp = (ExcelDnaUtil.Application as MOIE.Application);
            //tapp.Run("WDSVBAModuleReviewRefresh");
            AddIn_About wf = new AddIn_About();
            wf.ShowDialog();
            return;
        }


        [ExcelCommand(Description ="TBD"
            ,ExplicitRegistration =true
            )]
        public static void TBD()
        {
            //MOIE.Application tapp = (ExcelDnaUtil.Application as MOIE.Application);
            //tapp.Run("WDSVBAModuleReviewRefresh");
            AddIn_About wf = new AddIn_About();
            wf.ShowDialog();
            return;
        }

        [ExcelCommand(Description ="Add VBA Module: WDSJniPMML"
            ,ExplicitRegistration =true
            )]
        public static void VBAComponentAdd_WDSJniPMML()
        {
            MOIE.Application tapp = (ExcelDnaUtil.Application as MOIE.Application);
            tapp.Run("WDSVBAComponentAdd_WDSJniPMML");
            tapp.Run("WDSJniPMML_CallMacroOptions");
            return;
        }

        [ExcelCommand(Description ="Remove VBA Module: WDSJniPMML"
            ,ExplicitRegistration =true
            )]
        public static void VBAComponentRemove_WDSJniPMML()
        {
            MOIE.Application tapp = (ExcelDnaUtil.Application as MOIE.Application);
            tapp.Run("WDSVBAComponentRemove_WDSJniPMML");
            return;
        }


    }

}



