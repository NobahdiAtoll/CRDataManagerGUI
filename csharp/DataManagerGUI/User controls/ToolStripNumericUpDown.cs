using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms.Design;
using System.Windows.Forms;
using System.ComponentModel;

namespace DataManagerGUI
{
    [ToolStripItemDesignerAvailability(ToolStripItemDesignerAvailability.ToolStrip)]
    public class ToolStripNumberControl : ToolStripControlHost
    {
        public ToolStripNumberControl()
            : base(new NumericUpDown())
        {

        }
                

        protected override void OnSubscribeControlEvents(Control control)
        {
            base.OnSubscribeControlEvents(control);
            ((NumericUpDown)control).ValueChanged += new EventHandler(OnValueChanged);
        }

        protected override void OnUnsubscribeControlEvents(Control control)
        {
            base.OnUnsubscribeControlEvents(control);
            ((NumericUpDown)control).ValueChanged -= new EventHandler(OnValueChanged);
        }

        public event EventHandler ValueChanged;

        public Control NumericUpDownControl
        {
            get { return Control as NumericUpDown; }
        }

        public void OnValueChanged(object sender, EventArgs e)
        {
            if (ValueChanged != null)
            {
                ValueChanged(this, e);
            }
        }

        [Category("Data")]
        public decimal Maximum
        {
            get
            {
                return ((NumericUpDown)Control).Maximum;
            }
            set
            {
                ((NumericUpDown)Control).Maximum = value;
            }
        }
        [Category("Data")]
        public decimal Minimum
        {
            get
            {
                return ((NumericUpDown)Control).Minimum;
            }
            set
            {
                ((NumericUpDown)Control).Minimum = value;
            }
        }
        [Category("Data")]
        public decimal Value
        {
            get
            {
                return ((NumericUpDown)Control).Value;
            }
            set
            {
                if (Visible)
                {
                    ((NumericUpDown)Control).Value = value;
                }
            }
        }

    }
}
