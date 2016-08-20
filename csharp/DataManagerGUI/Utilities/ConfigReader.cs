using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace DataManagerGUI
{
    public static class ConfigHandler
    {
        public static Dictionary<string, string> ReadAllKeys(string strConfigFile)
        {
            Dictionary<string, string> tmpKeys = new Dictionary<string, string>();
            if (System.IO.File.Exists(strConfigFile))
            {
                string[] tmpStrings = System.IO.File.ReadAllLines(strConfigFile);
                int i = 0;
                while (i < tmpStrings.Length)
                {
                    string[] KeyValue = tmpStrings[i].Split(new string[] { ";", "#", " = " }, StringSplitOptions.RemoveEmptyEntries);
                    if (KeyValue.Length == 2)
                    {
                        tmpKeys.Add(KeyValue[0], KeyValue[1]);
                    }
                    i++;
                }
            }
            return tmpKeys;
        }

        internal static void WriteAllKeys(Dictionary<string, string> KeyStorage, string strFilePath)
        {
            //prepare
            string[] tmp = new string[KeyStorage.Count];
            int i = 0;
            foreach (KeyValuePair<string, string> item in KeyStorage)
            {
                tmp[i] = item.Key + " = " + item.Value;
                i++;
            }

            System.IO.File.WriteAllLines(strFilePath, tmp);
        }
    }
}
