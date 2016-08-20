using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Windows.Forms;

namespace DataManagerGUI
{
    public partial class RegExEditor : Form
    {
        public string Result
        {
            get
            {
                return textBox1.Text;
            }
            set
            {
                textBox1.Text = value;
            }
        }
        public RegExEditor()
        {
            InitializeComponent();
            List<string> EditableStringKeys = new List<string>();
            foreach (string item in Global.AllowedKeys)
            {
                if (Global.StringKeys.Contains(item) || Global.ListKeys.Contains(item))
                    EditableStringKeys.Add(item);
            }

            listBox1.Items.AddRange(EditableStringKeys.ToArray());
        }

        public RegExEditor(bool VariableReplace)
            :this()
        {
            
        }

        private void textBox1_SelectionChanged(object sender, EventArgs e)
        {
            panel1.Enabled = textBox1.SelectedText.Length > 0;
        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            this.DialogResult = System.Windows.Forms.DialogResult.OK;
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            this.DialogResult = System.Windows.Forms.DialogResult.Cancel;
        }

        private void btnValidate_Click(object sender, EventArgs e)
        {
            try
            {
                Regex tmp = new Regex(textBox1.Text);
                btnOK.Enabled = true;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error Found in regular expression", MessageBoxButtons.OK, MessageBoxIcon.Error);
                btnOK.Enabled = false;
            }
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            listBox1.Enabled = radioButton1.Checked;
            textBox2.Enabled = radioButton2.Checked;
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            btnValidate.Enabled = textBox1.Text.Length > 0;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string Capture = textBox1.SelectedText;
            string Field = textBox2.Text;
            if (radioButton1.Checked)
            {
                Field = listBox1.SelectedItem.ToString();
            }
            string CaptureInfo = string.Format("(?<{0}>{1})", Field, Capture);

            //get start position of selection
            int StartPosition = textBox1.SelectionStart;
            int SelectLegnth = textBox1.SelectionLength;

            //delete the selection
            textBox1.Select(0, 0);

            textBox1.Text = textBox1.Text.Remove(StartPosition, SelectLegnth).Insert(StartPosition, CaptureInfo);

        }
    }
}
