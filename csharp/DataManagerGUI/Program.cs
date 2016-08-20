using System;
using System.Collections.Generic;
using System.Windows.Forms;
using System.Threading;
using System.Globalization;

namespace DataManagerGUI
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            DebugAppend("Checking for Running Instance");
            bool ok;
            Mutex m = new System.Threading.Mutex(true, "crdmcgui", out ok);

            if (!ok)
            {
                DebugAppend("Instance Found Execution will be aborted");
                MessageBox.Show("Another instance is already running.");
                return;
            }

            DebugAppend("Enabling Visual Styles...");
            Application.EnableVisualStyles();
            DebugAppend("Setting Compatible Text Rendering to false...");
            Application.SetCompatibleTextRenderingDefault(false);
            DebugAppend("Starting GUI...");
            Application.Run(new gui());
            DebugAppend("Ensuring only a single instance is allowed...");
            GC.KeepAlive(m);
        }
        public static void DebugAppend(string strDebugInfo)
        {
            string outFile = Application.StartupPath + System.IO.Path.DirectorySeparatorChar + "guidebug.log";
            using (System.IO.FileStream tmp = new System.IO.FileStream(outFile, System.IO.FileMode.Append))
            {
                System.IO.StreamWriter sw = new System.IO.StreamWriter(tmp);
                sw.WriteLine(string.Format("{0} ##{1}", DateTime.Now.ToString("yyyy.MM.dd hh:mm:ss"), strDebugInfo));
                sw.Close();
            }
        }

        public static void SendToClipboard(object item)
        {
            Type tmpType = item.GetType();

            if (tmpType == typeof(dmRuleset))
                Clipboard.SetData(typeof(dmRuleset).FullName, ((dmRuleset)item).ToXML("ruleset").ToString());
            else if (item.GetType() == typeof(dmGroup))
                Clipboard.SetData(typeof(dmGroup).FullName, ((dmGroup)item).ToXML("group").ToString());
            else if (item.GetType() == typeof(dmRule))
                Clipboard.SetData(typeof(dmRule).FullName, ((dmRule)item).ToXML("rule").ToString());
            else if (item.GetType() == typeof(dmAction))
                Clipboard.SetData(typeof(dmAction).FullName, ((dmAction)item).ToXML("action").ToString());
            else if (item.GetType() == typeof(dmRuleTemplate))
                Clipboard.SetData(item.GetType().FullName, ((dmRuleTemplate)item).ToXML("ruletemplate").ToString());
            else if (item.GetType() == typeof(dmActionTemplate))
                Clipboard.SetData(item.GetType().FullName, ((dmActionTemplate)item).ToXML("actiontemplate").ToString());
        }
    }    
}
