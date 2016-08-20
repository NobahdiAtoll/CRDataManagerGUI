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
    public partial class Language_Add : Form
    {
        public List<string> Result;

        public Language_Add()
        {
            InitializeComponent();
        }

        public Language_Add(string strCaption, string[] strList, string[] strAdded)
            :this()
        {
            this.Text = strCaption;
            listBox1.Items.AddRange(strList);
            for (int i = 0; i < listBox1.Items.Count; i++)
            {
                if (strAdded.Contains(listBox1.Items[i]))
                {
                    listBox2.Items.Add(listBox1.Items[i]);
                    listBox1.Items.RemoveAt(i);
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            List<object> itemsToRemove = new List<object>();
            foreach (object item in listBox2.SelectedItems)
            {
                listBox1.Items.Add(item);
                itemsToRemove.Add(item);
            }

            foreach (string item in itemsToRemove)
            {
                listBox2.Items.Remove(item);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {

            List<object> itemsToRemove = new List<object>();
            foreach (object item in listBox1.SelectedItems)
            {
                listBox2.Items.Add(item);
                itemsToRemove.Add(item);
            }

            foreach (string item in itemsToRemove)
            {
                listBox1.Items.Remove(item);
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            Close();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.DialogResult = System.Windows.Forms.DialogResult.OK;
            this.Result = new List<string>();
            foreach (object item in listBox2.Items)
            {
                Result.Add(item.ToString());
            }
            Close();
        }
    }
}
