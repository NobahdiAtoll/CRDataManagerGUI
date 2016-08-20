using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace DataManagerGUI
{
    public static class Extensions
    {
        public static string Join(this string[] strArray, char Seperator)
        {
            string strReturn = "";

            for (int i = 0; i < strArray.Length; i++)
            {
                strReturn += strArray[i];

                if (i != strArray.Length - 1)
                {
                    strReturn += Seperator;
                }
            }

            return strReturn;
        }
        public static string Join(this string[] strArray, string Seperator)
        {
            string strReturn = "";

            for (int i = 0; i < strArray.Length; i++)
            {
                strReturn += strArray[i];

                if (i != strArray.Length - 1)
                {
                    strReturn += Seperator;
                }
            }

            return strReturn;
        }
        public static bool IsDecendantOf(this System.Windows.Forms.TreeNode ndToCheckFor, System.Windows.Forms.TreeNode ndToCheck)
        {
            bool bReturn = false;

            string ndCheckPath = ndToCheck.FullPath;
            string ndCheckForPath = ndToCheckFor.FullPath;

            bReturn = ndCheckForPath.StartsWith(ndCheckPath);
            
            return bReturn;
        }
    }
   
}
