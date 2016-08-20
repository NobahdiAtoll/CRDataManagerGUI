using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace DataManagerGUI
{
    public partial class RegExVarReplace : UserControl
    {
        [Bindable(true)]
        [Category("PropertyChanged")]
        public event EventHandler RegularExpressionChanged;

        public string Results
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
        public RegExVarReplace()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            RegExEditor tmp = new RegExEditor(true);

            tmp.Result = textBox1.Text;

            if (tmp.ShowDialog() == DialogResult.OK)
            {
                textBox1.Text = tmp.Result;
                if (RegularExpressionChanged != null)
                    RegularExpressionChanged(this, new EventArgs());
            }
        }
    }
}
