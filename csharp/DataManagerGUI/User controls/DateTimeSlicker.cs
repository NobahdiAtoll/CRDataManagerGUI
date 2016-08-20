using System;
using System.ComponentModel;
using System.Diagnostics;
using System.Security.Permissions;
using System.Windows.Forms;


namespace DataManagerGUI
{
    // Author:     Nils Jonsson
    // Originated: 10/03/2003
    /// <summary>
    /// Represents an enhanced Windows date-time picker control.
    /// </summary>
    [DefaultEvent("ValueChanged")]
    [DefaultProperty("Value")]
    [ToolboxItemFilter("System.Windows.Forms")]
    public class DateTimeSlicker : DateTimePicker
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DateTimePicker" />
        /// class.
        /// </summary>
        public DateTimeSlicker()
            : base()
        {
            this.ParentChanged += new EventHandler(this.this_ParentChanged);

            // Show the check box because it is most of the raison d’être for
            // this class.
            this.ShowCheckBox = true;

            this.customFormat = base.CustomFormat;
            this.format = base.Format;
        }


        /// <summary>
        /// Occurs when the value of the <see cref="Checked" /> property
        /// changes.
        /// </summary>
        [Category("Property Changed")]
        [Description("Occurs when the Checked property value is changed.")]
        public event EventHandler CheckedChanged
        {
            add { this.checkedChanged += value; }

            remove { this.checkedChanged -= value; }
        }

        /// <summary>
        /// Occurs when the value of the <see cref="CustomFormat" /> property
        /// changes.
        /// </summary>
        [Category("Property Changed")]
        [Description("Occurs when the CustomFormat property value is changed.")]
        public event EventHandler CustomFormatChanged
        {
            add { this.customFormatChanged += value; }

            remove { this.customFormatChanged -= value; }
        }

        /// <summary>
        /// Gets or sets a value indicating whether the <see cref="Value" />
        /// property has been set with a valid date-time value and the displayed
        /// value is able to be updated.
        /// </summary>
        /// <value><c>true</c> if the <see cref="Value" /> property has been set
        /// with a valid <see cref="DateTime" /> value and the displayed value
        /// is able to be updated; otherwise, <c>false</c>. The default is
        /// <c>true</c>.</value>
        [Bindable(true)]
        [Category("Behavior")]
        [DefaultValue(true)]
        [Description("Determines if the check box is checked, indicating that "
         + "the user has selected a value.")]
        public new bool Checked
        {
            get { return base.Checked; }

            set
            {
                if (value == this.Checked)
                    return;

                this.SetCheckBoxState(value);
                this.OnCheckedChanged();
                this.KlugeFocusBug();
            }
        }

        /// <summary>
        /// Gets or sets the custom date-time format string.
        /// </summary>
        /// <value>A string that represents the custom date-time format. The
        /// default is a null reference (<c>Nothing</c> in Visual
        /// Basic).</value>
        [Category("Behavior")]
        [DefaultValue(null)]
        [Description("The custom format string used to format the date and/or "
         + "time displayed.")]
        [RefreshProperties(RefreshProperties.Repaint)]
        public new string CustomFormat
        {
            get { return this.customFormat; }

            set
            {
                if (value == this.CustomFormat)
                    return;

                if (this.Checked)
                    base.CustomFormat = value;
                this.customFormat = value;
                this.OnCustomFormatChanged();
            }
        }

        /// <summary>
        /// Gets or sets the format of the date and time displayed in the
        /// control.
        /// </summary>
        /// <value>One of the <see cref="DateTimePickerFormat" /> values. The
        /// default is <see cref="DateTimePickerFormat.Long" />.</value>
        /// <exception cref="InvalidEnumArgumentException">The value assigned is
        /// not one of the <see cref="DateTimePickerFormat" />
        /// values.</exception>
        [Category("Appearance")]
        [DefaultValue(DateTimePickerFormat.Long)]
        [Description("Determines whether the date and/or time is displayed "
         + "using standard or custom formatting.")]
        [RefreshProperties(RefreshProperties.Repaint)]
        public new DateTimePickerFormat Format
        {
            get { return this.format; }

            set
            {
                if (value == this.Format)
                    return;

                if (this.Checked)
                {
                    // Calls OnFormatChanged().
                    base.Format = value;
                }
                this.format = value;
                if (!(this.Checked))
                    this.OnFormatChanged();
            }
        }

        /// <summary>
        /// Gets or sets the text associated with this control.
        /// </summary>
        /// <value>A <see cref="String" /> object that represents the text
        /// associated with this control.</value>
        /// <exception cref="ArgumentNullException">Argument is a null reference
        /// (<c>Nothing</c> in Visual Basic).</exception>
        [Browsable(false)]
        [DesignerSerializationVisibility(
         DesignerSerializationVisibility.Hidden)]
        [EditorBrowsable(EditorBrowsableState.Advanced)]
        public override string Text
        {
            get
            {
                if (this.Checked)
                    return base.Text;
                else
                    return string.Empty;
            }

            set
            {
                if (value == null)
                {
                    throw new ArgumentNullException(null,
                     "Argument cannot be null.");
                }

                if (value == this.Text)
                    return;

                if (value == string.Empty)
                {
                    this.OnTextChanged();
                    this.Checked = false;
                }
                else
                {
                    // Calls OnTextChanged().
                    base.Text = value;
                }
            }
        }

        /// <summary>
        /// Gets or sets the date-time value assigned to the control.
        /// </summary>
        /// <value>The <see cref="DateTime" /> value assigned to the
        /// control.</value>
        /// <exception cref="ArgumentNullException">Argument is a null reference
        /// (<c>Nothing</c> in Visual Basic).</exception>
        /// <exception cref="ArgumentException">Argument is neither a
        /// <see cref="DateTime" /> nor a <see cref="DBNull" />
        /// value.</exception>
        [Bindable(true)]
        [Category("Behavior")]
        [Description("The date and/or time value (also can be DBNull).")]
        [RefreshProperties(RefreshProperties.All)]
        public new object Value
        {
            get
            {
                if (this.Checked)
                    return base.Value;
                else
                    return DBNull.Value;
            }

            set
            {
                if (value == null || (value is DateTime && (DateTime)value < this.MinDate))
                {
                    value = DBNull.Value;
                }

                if (value == this.Value)
                    return;

                if (value == DBNull.Value)
                {
                    this.Checked = false;
                    this.OnValueChanged();
                }
                else if (value is DateTime)
                {
                    // Calls OnValueChanged().
                    base.Value = (DateTime)value;
                    this.Checked = true;
                }
                else
                {
                    throw new ArgumentException(
                     "Argument must be a DateTime or DBNull.Value.");
                }
            }
        }


        // Estimates the right edge of the area in which a mouse click will
        // toggle the check box. This varies with the font used to display the
        // text of the DateTimePicker.
        private int GetCheckBoxExtent()
        {
            // Use the Height property because the check box is square.
            return
             (int)this.CreateGraphics().MeasureString("X", this.Font).Height;
        }

        // DateTimePicker paints a focus cue on the check box when the control
        // is created, and any time the Checked property changes. This means
        // that a focus cue can appear while the control does not actually have
        // focus. This method works around that behavior.
        [UIPermission(SecurityAction.Demand)]
        private void KlugeFocusBug()
        {
            // The kluge is not necessary if this DateTimeSlicker has the focus.
            if (this.Focused)
                return;

            Control parent = this.Parent;
            while ((parent != null) && !(parent is ContainerControl))
                parent = parent.Parent;

            ContainerControl parentContainer = parent as ContainerControl;
            if (parentContainer == null)
                return;

            Control activeControl = parentContainer.ActiveControl;
            // Set focus on this DateTimeSlicker.
            this.Focus();
            // Set focus back on the previously active control.
            if (activeControl != null)
                activeControl.Focus();
        }

        /// <summary>
        /// Raises the <see cref="CheckedChanged" /> event.
        /// </summary>
        /// <param name="e">An <see cref="EventArgs" /> that contains the event
        /// data.</param>
        /// <exception cref="ArgumentNullException"><paramref name="e" /> is a
        /// null reference (<c>Nothing</c> in Visual Basic).</exception>
        protected virtual void OnCheckedChanged(EventArgs e)
        {
            if (e == null)
            {
                throw new ArgumentNullException("e",
                 "Argument e cannot be null.");
            }

            if (this.checkedChanged != null)
                this.checkedChanged(this, e);
        }

        private void OnCheckedChanged()
        {
            this.OnCheckedChanged(EventArgs.Empty);
        }

        /// <summary>
        /// Raises the <see cref="CustomFormatChanged" /> event.
        /// </summary>
        /// <param name="e">An <see cref="EventArgs" /> that contains the event
        /// data.</param>
        /// <exception cref="ArgumentNullException"><paramref name="e" /> is a
        /// null reference (<c>Nothing</c> in Visual Basic).</exception>
        protected virtual void OnCustomFormatChanged(EventArgs e)
        {
            if (e == null)
            {
                throw new ArgumentNullException("e",
                 "Argument e cannot be null.");
            }

            if (this.customFormatChanged != null)
                this.customFormatChanged(this, e);
        }

        private void OnCustomFormatChanged()
        {
            this.OnCustomFormatChanged(EventArgs.Empty);
        }

        /// <summary>
        /// Raises the <see cref="DateTimePicker.FormatChanged" /> event.
        /// </summary>
        /// <param name="e">An <see cref="EventArgs" /> that contains the event
        /// data.</param>
        /// <exception cref="ArgumentNullException"><paramref name="e" /> is a
        /// null reference (<c>Nothing</c> in Visual Basic).</exception>
        protected override void OnFormatChanged(EventArgs e)
        {
            // Suppress the event if Format changed in order to hide the text.
            if (!(this.showingOrHidingText))
                base.OnFormatChanged(e);
        }

        private void OnFormatChanged()
        {
            this.OnFormatChanged(EventArgs.Empty);
        }

        /// <summary>
        /// Raises the <see cref="Control.KeyDown" /> event.
        /// </summary>
        /// <param name="e">A <see cref="KeyEventArgs" /> that contains the event
        /// data.</param>
        /// <exception cref="ArgumentNullException"><paramref name="e" /> is a
        /// null reference (<c>Nothing</c> in Visual Basic).</exception>
        protected override void OnKeyDown(KeyEventArgs e)
        {
            if (((e.KeyCode == Keys.F4) && !(e.Alt))
             || (e.KeyCode == Keys.Down) && e.Alt)
            {
                // Check the check box because the user dropped down the
                // calendar via keyboard input.
                this.Checked = true;
            }

            base.OnKeyDown(e);
        }

        private void OnTextChanged()
        {
            this.OnTextChanged(EventArgs.Empty);
        }

        private void OnValueChanged()
        {
            this.OnValueChanged(EventArgs.Empty);
        }

        private void SetCheckBoxState(bool value)
        {
            base.Checked = value;
            if (this.Checked)
            {
                this.showingOrHidingText = true;
                base.CustomFormat = this.customFormat;
                base.Format = this.format;
                this.showingOrHidingText = false;
            }
            else
            {
                // Tweak CustomFormat and Format in order to make the text
                // portion appear empty.
                this.showingOrHidingText = true;
                base.CustomFormat = " ";
                base.Format = DateTimePickerFormat.Custom;
                this.showingOrHidingText = false;
            }
        }

        private void Parent_Paint(object sender, PaintEventArgs e)
        {
            Debug.Assert(sender == this.Parent,
             string.Format("Unexpected sender {0}.", sender));

            // Run once for this Parent.
            if (this.Parent != null)
                this.Parent.Paint -= new PaintEventHandler(this.Parent_Paint);

            this.KlugeFocusBug();
        }

        private void this_ParentChanged(object sender, EventArgs e)
        {
            Debug.Assert(sender == this,
             string.Format("Unexpected sender {0}.", sender));

            if (this.Parent != null)
                this.Parent.Paint += new PaintEventHandler(this.Parent_Paint);
        }

        /// <summary>
        /// This member overrides <see cref="Control.WndProc" />.
        /// </summary>
        /// <param name="m">The Windows <see cref="Message" /> to
        /// process.</param>
        /// <exception cref="ArgumentNullException"><paramref name="m" /> is a
        /// null reference (<c>Nothing</c> in Visual Basic).</exception>
        [SecurityPermission(SecurityAction.Demand)]
        protected override void WndProc(ref Message m)
        {
            switch (m.Msg)
            {
                case 0x102: // WM_CHAR
                    int charAsInt32 = m.WParam.ToInt32();
                    char charAsChar = (char)charAsInt32;
                    if (charAsInt32 == (int)Keys.Space)
                    {
                        // Toggle the check box because the user pressed the
                        // space bar.
                        this.OnKeyPress(new KeyPressEventArgs(charAsChar));
                        this.Checked = !(this.Checked);
                    }
                    else
                    {
                        // Forward the message to DateTimePicker because a key
                        // other than the space bar was pressed.
                        base.WndProc(ref m);
                    }
                    break;
                case 0x201: // WM_LBUTTONDOWN
                    // The X value of the mouse position is stored in the
                    // low-order bits of LParam, and the Y value in the
                    // high-order bits.
                    int x = (m.LParam.ToInt32() << 16) >> 16;
                    int y = m.LParam.ToInt32() >> 16;
                    if (x <= this.GetCheckBoxExtent())
                    {
                        // Toggle the check box because the user clicked (near)
                        // the check box.
                        this.OnMouseDown(
                         new MouseEventArgs(MouseButtons.Left, 1, x, y, 0));
                        this.Checked = !(this.Checked);
                        // Grab focus because we are eating the message.
                        this.Focus();
                    }
                    else
                    {
                        bool checkedChange = !(this.Checked);
                        if (checkedChange)
                        {
                            // Check the check box because the user clicked
                            // somewhere within the control while it was not
                            // checked.
                            this.SetCheckBoxState(true);
                        }
                        // Forward the message to DateTimePicker so that mouse
                        // events will be fired, focus will be taken, etc.
                        base.WndProc(ref m);
                        if (checkedChange)
                            this.OnCheckedChanged();
                    }
                    break;
                default:
                    // Forward the message to DateTimePicker because it pertains
                    // to neither the left mouse button nor a pressed key.
                    base.WndProc(ref m);
                    break;
            }
        }


        private bool showingOrHidingText;

        private EventHandler checkedChanged;
        private EventHandler customFormatChanged;

        private string customFormat;
        private DateTimePickerFormat format;
    }
}

//                                 ~ S. D. G. ~
