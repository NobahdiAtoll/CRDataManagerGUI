using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using DataManagerGUI;

namespace DataManagerGUI
{

    public enum DebugLevel : int
    {
        StartupOnly = 0,
        Minimal = 1,
        Verbose = 2,
    }

    public class dmUserInfo
    {
        public List<dmTemplate> RuleTemplates { get; set; }
        public List<dmTemplate> ActionTemplates { get; set; }
        Dictionary<string, string> KeyStorage { get; set; }
        DebugLevel DebugLevel { get; set; }

        public bool SessionAutoComplete
        {
            get
            {
                if (KeyStorage.ContainsKey("SessionAutoComplete"))
                    return Boolean.Parse(KeyStorage["SessionAutoComplete"]);
                else
                    return false;
            }
            set
            {
                if (KeyStorage.ContainsKey("SessionAutoComplete"))
                    KeyStorage["SessionAutoComplete"] = value.ToString();
                else
                    KeyStorage.Add("SessionAutoComplete", value.ToString());
            }
        }

        public bool ShowStartupDialog
        {
            get
            {
                if (!KeyStorage.ContainsKey("ShowStartupDialog"))
                    KeyStorage.Add("ShowStartupDialog", true.ToString());
                return Boolean.Parse(KeyStorage["ShowStartupDialog"]);
            }
            set
            {
                if (!KeyStorage.ContainsKey("ShowStartupDialog"))
                    KeyStorage.Add("ShowStartupDialog", value.ToString());
                KeyStorage["ShowStartupDialog"] = value.ToString();
            }
        }

        public string DateTimeFormat
        {
            get
            {
                if (!KeyStorage.ContainsKey("DateTimeFormat"))
                    KeyStorage.Add("DateTimeFormat", "yyyy/MM/dd hh:mm:ss");
                return KeyStorage["DateTimeFormat"];
            }
            set
            {
                if (!KeyStorage.ContainsKey("DateTimeFormat"))
                    KeyStorage.Add("DateTimeFormat", value.ToString());
                KeyStorage["DateTimeFormat"] = value;
            }
        }

        public bool BreakAfterFirstError
        {
            get
            {
                if (!KeyStorage.ContainsKey("BreakAfterFirstError"))
                    KeyStorage.Add("BreakAfterFirstError", true.ToString());
                return Boolean.Parse(KeyStorage["BreakAfterFirstError"]);
            }
            set
            {
                if (!KeyStorage.ContainsKey("BreakAfterFirstError"))
                    KeyStorage.Add("BreakAfterFirstError", value.ToString());
                KeyStorage["BreakAfterFirstError"] = value.ToString();
            }
        }

        public bool DebugMode
        {
            get
            {
                bool bReturn = false;
                if (KeyStorage.ContainsKey("Debug"))
                    Boolean.TryParse(KeyStorage["Debug"], out bReturn);
                return bReturn;
            }
        }

        public bool LogBookOnlyWhenValuesChanged
        {
            get
            {
                if (KeyStorage.ContainsKey("LogBookOnlyWhenValuesChanged"))
                    return bool.Parse(KeyStorage["LogBookOnlyWhenValuesChanged"]);
                else
                    return false;
            }
            set
            {
                if (KeyStorage.ContainsKey("LogBookOnlyWhenValuesChanged"))
                    KeyStorage["LogBookOnlyWhenValuesChanged"] = value.ToString();
                else
                    KeyStorage.Add("LogBookOnlyWhenValuesChanged", value.ToString());
            }
        }
        Dictionary<string, List<string>> AutoCompleteStrings { get; set; }

        public dmUserInfo()
        {
            KeyStorage = new Dictionary<string, string>();
            RuleTemplates = new List<dmTemplate>();
            ActionTemplates = new List<dmTemplate>();
            ConfirmOverwrite = true;
            DateTimeFormat = "yyyy/MM/dd hh:mm:dd";
            BreakAfterFirstError = false;
            AutoCompleteStrings = new Dictionary<string, List<string>>();
            DebugLevel = DebugLevel.StartupOnly;
        }

        public bool ConfirmOverwrite 
        { 
            get
            {
                if (KeyStorage.ContainsKey("ConfirmOverwrite"))
                    return bool.Parse(KeyStorage["ConfirmOverwrite"]);
                else
                    return true;
            }
            set
            {
                if (!KeyStorage.ContainsKey("ConfirmOverwrite"))
                    KeyStorage.Add("ConfirmOverwrite", ConfirmOverwrite.ToString());
                else
                    KeyStorage["ConfirmOverwrite"] = value.ToString();
            }
        }

        public dmUserInfo(string strFilePath)
            : this()
        {
            ReadFile(strFilePath);
        }

        public dmUserInfo(string strFilePath, string strBackupFilePath)
            : this()
        {
            if (!System.IO.File.Exists(strFilePath))
            {
                Program.DebugAppend("User file does not exist, searching for backup...");
                if (!System.IO.File.Exists(strBackupFilePath))
                {
                    Program.DebugAppend("Backup User file does not exist, creating default...");
                    ReadFile(strFilePath);
                    WriteFile(strFilePath);
                }
                else
                {
                    Program.DebugAppend("Backup found copying to folder...");
                    ReadFile(strBackupFilePath);
                    WriteFile(strBackupFilePath);
                }
            }
            else
            {
                Program.DebugAppend("User file found, loading user settings...");
                ReadFile(strFilePath);
            }
        }


        public void ReadFile(string strFilePath)
        {
            Dictionary<string, string> tmpKeys = ConfigHandler.ReadAllKeys(strFilePath);
            foreach (KeyValuePair<string, string> item in tmpKeys)
            {
                if (item.Key.StartsWith("RuleTemplate_")) 
                    RuleTemplates.Add(new dmRuleTemplate(item.Key.Replace("RuleTemplate_", ""), item.Value));
                else if (item.Key.StartsWith("ActionTemplate_")) 
                    ActionTemplates.Add(new dmActionTemplate(item.Key.Replace("ActionTemplate_", ""), item.Value));
                else if (item.Key.StartsWith("AutoComplete_"))
                    AutoCompleteStrings.Add(item.Key.Replace("AutoComplete_", ""), new List<string>(item.Value.Split(new char[] { ',' }, StringSplitOptions.RemoveEmptyEntries)));
                else 
                    AddToKeyStorage(item.Key, item.Value);
            }
        }

        private void AddToKeyStorage(string strKey, string strValue)
        {
            if (!KeyStorage.ContainsKey(strKey))
                KeyStorage.Add(strKey, strValue);
            else
                KeyStorage[strKey] = strValue;
        }

        public void WriteFile(string strFilePath)
        {
            Dictionary<string, string> tmpKeys = new Dictionary<string, string>();

            foreach (KeyValuePair<string, string> item in KeyStorage)
                tmpKeys.Add(item.Key, item.Value);
            for (int i = 0; i < RuleTemplates.Count; i++)
                tmpKeys.Add("RuleTemplate_" + RuleTemplates[i].Name, RuleTemplates[i].ToString());
            for (int i = 0; i < ActionTemplates.Count; i++)
                tmpKeys.Add("ActionTemplate_" + ActionTemplates[i].Name, ActionTemplates[i].ToString());
            if (!System.IO.Directory.Exists(System.IO.Path.GetDirectoryName(strFilePath)))
                System.IO.Directory.CreateDirectory(System.IO.Path.GetDirectoryName(strFilePath));

            foreach (KeyValuePair<string, List<string>> item in AutoCompleteStrings)
                tmpKeys.Add("AutoComplete_" + item.Key, item.Value.ToArray().Join(','));
            ConfigHandler.WriteAllKeys(tmpKeys, strFilePath);
        }

        public string[] GetAutoComplete(string p)
        {
            if (!AutoCompleteStrings.ContainsKey(p))
                AutoCompleteStrings.Add(p, new List<string>());
            AutoCompleteStrings[p].Sort();
            return AutoCompleteStrings[p].ToArray();
        }

        public void AddAutoComplete(string p, string p_2)
        {
            if (!AutoCompleteStrings.ContainsKey(p))
                AutoCompleteStrings.Add(p, new List<string>());
            if (!AutoCompleteStrings[p].Contains(p_2))
                AutoCompleteStrings[p].Add(p_2);
        }
    }
}