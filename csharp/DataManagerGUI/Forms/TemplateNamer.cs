using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace DataManagerGUI
{
    public partial class TemplateNamer : Form
    {
        internal TemplateNamer()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            btnOK.Enabled = IsValid(textBox1.Text);
        }

        private bool IsValid(string strName)
        {
            bool bReturn = true;
            for (int i = 0; i < strName.Length; i++)
            {
                if (Char.IsWhiteSpace(strName[i]) || strName[i] == '=')
                {
                    bReturn = false;
                    break;
                }
            }
            return bReturn;
        }

        public string Results { get; set; }

        private void btnOK_Click(object sender, EventArgs e)
        {
            Results = textBox1.Text;
            this.DialogResult = System.Windows.Forms.DialogResult.OK;
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            this.DialogResult = System.Windows.Forms.DialogResult.Cancel;
        }
    }
}
