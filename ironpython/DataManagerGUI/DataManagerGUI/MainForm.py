import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("DataManagerGUI.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._tabControl1 = System.Windows.Forms.TabControl()
		self._tabEdit = System.Windows.Forms.TabPage()
		self._splitContainer1 = System.Windows.Forms.SplitContainer()
		self._toolStripContainer1 = System.Windows.Forms.ToolStripContainer()
		self._toolStrip1 = System.Windows.Forms.ToolStrip()
		self._tsmiFile = System.Windows.Forms.ToolStripDropDownButton()
		self._tsmiAbout = System.Windows.Forms.ToolStripMenuItem()
		self._tsmiSettings = System.Windows.Forms.ToolStripMenuItem()
		self._tssSeparator1 = System.Windows.Forms.ToolStripSeparator()
		self._tsmiProfileImport = System.Windows.Forms.ToolStripMenuItem()
		self._tsmiMerge = System.Windows.Forms.ToolStripMenuItem()
		self._tsmiRevert = System.Windows.Forms.ToolStripMenuItem()
		self._tsmiLoadDefault = System.Windows.Forms.ToolStripMenuItem()
		self._tsmiLoad = System.Windows.Forms.ToolStripMenuItem()
		self._tsmiNew = System.Windows.Forms.ToolStripMenuItem()
		self._tsmiSaveAsDefault = System.Windows.Forms.ToolStripMenuItem()
		self._tsmiSaveAs = System.Windows.Forms.ToolStripMenuItem()
		self._tsmiSave = System.Windows.Forms.ToolStripMenuItem()
		self._tsbSave = System.Windows.Forms.ToolStripButton()
		self._tvCollectionTree = System.Windows.Forms.TreeView()
		self._pnlRulesets = System.Windows.Forms.Panel()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._btnRulesetRulesMoveDown = System.Windows.Forms.Button()
		self._btnRulesetRulesMoveUp = System.Windows.Forms.Button()
		self._btnActionMoveDown = System.Windows.Forms.Button()
		self._btnActionMoveUp = System.Windows.Forms.Button()
		self._btnRulesetReparse = System.Windows.Forms.Button()
		self._pictureBox2 = System.Windows.Forms.PictureBox()
		self._lblRulesetOriginalText = System.Windows.Forms.Label()
		self._txtRulesetReparse = System.Windows.Forms.TextBox()
		self._btnRulesetRuleRemove = System.Windows.Forms.Button()
		self._btnRulesetRuleUpdate = System.Windows.Forms.Button()
		self._btnRulesetRuleClear = System.Windows.Forms.Button()
		self._commentLabel1 = System.Windows.Forms.Label()
		self._txtRulesetComment = System.Windows.Forms.TextBox()
		self._btnRulesetRuleAdd = System.Windows.Forms.Button()
		self._nameLabel1 = System.Windows.Forms.Label()
		self._txtRulesetName = System.Windows.Forms.TextBox()
		self._dgvRulesetRules = System.Windows.Forms.DataGridView()
		self._dataGridViewTextBoxColumn3 = System.Windows.Forms.DataGridViewTextBoxColumn()
		self._dgvtcRulesetRuleValue = System.Windows.Forms.DataGridViewTextBoxColumn()
		self._dgvRulesetActions = System.Windows.Forms.DataGridView()
		self._dataGridViewTextBoxColumn2 = System.Windows.Forms.DataGridViewTextBoxColumn()
		self._dgvtcRulesetActionValue = System.Windows.Forms.DataGridViewTextBoxColumn()
		self._btnRulesetActionAdd = System.Windows.Forms.Button()
		self._label5 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._btnRulesetActionClear = System.Windows.Forms.Button()
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._label3 = System.Windows.Forms.Label()
		self._btnRulesetActionUpdate = System.Windows.Forms.Button()
		self._btnRulesetActionRemove = System.Windows.Forms.Button()
		self._pnlGroups = System.Windows.Forms.Panel()
		self._tabGroupTabs = System.Windows.Forms.TabControl()
		self._tabPage3 = System.Windows.Forms.TabPage()
		self._label19 = System.Windows.Forms.Label()
		self._btnGroupRulesetRemove = System.Windows.Forms.Button()
		self._btnGroupGroupRemove = System.Windows.Forms.Button()
		self._btnGroupRulesetMoveDown = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._dgvGroupRulesets = System.Windows.Forms.DataGridView()
		self._btnGroupRulesetMoveUp = System.Windows.Forms.Button()
		self._dgvGroupGroups = System.Windows.Forms.DataGridView()
		self._btnGroupGroupMoveDown = System.Windows.Forms.Button()
		self._btnGroupRulesetAdd = System.Windows.Forms.Button()
		self._dataGridView5 = System.Windows.Forms.DataGridView()
		self._btnGroupGroupMoveUp = System.Windows.Forms.Button()
		self._btnGroupGroupAdd = System.Windows.Forms.Button()
		self._label8 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._label13 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._tabGrpRuleset = System.Windows.Forms.TabPage()
		self._btnGroupFiltersMoveDown = System.Windows.Forms.Button()
		self._btnGroupFiltersMoveUp = System.Windows.Forms.Button()
		self._comboBox2 = System.Windows.Forms.ComboBox()
		self._btnGroupDefaultMoveDown = System.Windows.Forms.Button()
		self._btnGroupDefaultMoveUp = System.Windows.Forms.Button()
		self._pictureBox3 = System.Windows.Forms.PictureBox()
		self._btnGroupFilterRemove = System.Windows.Forms.Button()
		self._btnGroupFilterUpdate = System.Windows.Forms.Button()
		self._btnGroupFilterClear = System.Windows.Forms.Button()
		self._btnGroupFilterAdd = System.Windows.Forms.Button()
		self._dgvGroupFilters = System.Windows.Forms.DataGridView()
		self._Field = System.Windows.Forms.DataGridViewTextBoxColumn()
		self._dgvGroupDefaults = System.Windows.Forms.DataGridView()
		self._dataGridViewTextBoxColumn1 = System.Windows.Forms.DataGridViewTextBoxColumn()
		self._btnGroupDefaultAdd = System.Windows.Forms.Button()
		self._label21 = System.Windows.Forms.Label()
		self._label22 = System.Windows.Forms.Label()
		self._btnGroupDefaultClear = System.Windows.Forms.Button()
		self._pictureBox4 = System.Windows.Forms.PictureBox()
		self._label23 = System.Windows.Forms.Label()
		self._btnGroupDefaultUpdate = System.Windows.Forms.Button()
		self._btnGroupDefaultRemove = System.Windows.Forms.Button()
		self._lblGroupOverview = System.Windows.Forms.Label()
		self._commentLabel = System.Windows.Forms.Label()
		self._txtGroupComment = System.Windows.Forms.TextBox()
		self._nameLabel = System.Windows.Forms.Label()
		self._txtGroupName = System.Windows.Forms.TextBox()
		self._pnlGeneral = System.Windows.Forms.Panel()
		self._btnCollectionRulesetMoveDown = System.Windows.Forms.Button()
		self._btnCollectionRulesetMoveUp = System.Windows.Forms.Button()
		self._btnCollectionGroupMoveDown = System.Windows.Forms.Button()
		self._btnCollectionGroupMoveUp = System.Windows.Forms.Button()
		self._label20 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label18 = System.Windows.Forms.Label()
		self._txtCollectionNotes = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._txtCollectionAuthor = System.Windows.Forms.TextBox()
		self._label17 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self._btnCollectionRulesetAdd = System.Windows.Forms.Button()
		self._btnCollectionGroupAdd = System.Windows.Forms.Button()
		self._dgvCollectionRulesets = System.Windows.Forms.DataGridView()
		self._btnCollectionRulesetsRemove = System.Windows.Forms.Button()
		self._dgvCollectionGroups = System.Windows.Forms.DataGridView()
		self._btnCollectionGroupRemove = System.Windows.Forms.Button()
		self._tabTemplateManager = System.Windows.Forms.TabPage()
		self._txtTemplateAdd = System.Windows.Forms.TextBox()
		self._btnTemplatesRuleActionAdd = System.Windows.Forms.Button()
		self._btnTemplatesClear = System.Windows.Forms.Button()
		self._btnTemplateRename = System.Windows.Forms.Button()
		self._btnTemplateAdd = System.Windows.Forms.Button()
		self._btnTemplatesRemoveTemplate = System.Windows.Forms.Button()
		self._btnTemplatesRuleActionClear = System.Windows.Forms.Button()
		self._btnTemplatesRuleActionUpdate = System.Windows.Forms.Button()
		self._btnTemplatesRuleActionRemove = System.Windows.Forms.Button()
		self._dataGridView1 = System.Windows.Forms.DataGridView()
		self._cmbTemplates = System.Windows.Forms.ComboBox()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._tabSearch = System.Windows.Forms.TabPage()
		self._toolStripContainer2 = System.Windows.Forms.ToolStripContainer()
		self._dataGridView3 = System.Windows.Forms.DataGridView()
		self._label6 = System.Windows.Forms.Label()
		self._tsSearch = System.Windows.Forms.ToolStrip()
		self._toolStripLabel1 = System.Windows.Forms.ToolStripLabel()
		self._tscbSearchType = System.Windows.Forms.ToolStripComboBox()
		self._toolStripSeparator4 = System.Windows.Forms.ToolStripSeparator()
		self._tsLabelSearchField = System.Windows.Forms.ToolStripLabel()
		self._tscbSearchField = System.Windows.Forms.ToolStripComboBox()
		self._tsLabelSearchModifier = System.Windows.Forms.ToolStripLabel()
		self._tscbSearchModifier = System.Windows.Forms.ToolStripComboBox()
		self._tslblSearchValue = System.Windows.Forms.ToolStripLabel()
		self._tstbValue = System.Windows.Forms.ToolStripTextBox()
		self._tsbRunSearch = System.Windows.Forms.ToolStripButton()
		self._toolStripSeparator5 = System.Windows.Forms.ToolStripSeparator()
		self._statusStrip1 = System.Windows.Forms.StatusStrip()
		self._tabControl1.SuspendLayout()
		self._tabEdit.SuspendLayout()
		self._splitContainer1.BeginInit()
		self._splitContainer1.Panel1.SuspendLayout()
		self._splitContainer1.Panel2.SuspendLayout()
		self._splitContainer1.SuspendLayout()
		self._toolStripContainer1.BottomToolStripPanel.SuspendLayout()
		self._toolStripContainer1.ContentPanel.SuspendLayout()
		self._toolStripContainer1.SuspendLayout()
		self._toolStrip1.SuspendLayout()
		self._pnlRulesets.SuspendLayout()
		self._pictureBox2.BeginInit()
		self._dgvRulesetRules.BeginInit()
		self._dgvRulesetActions.BeginInit()
		self._pictureBox1.BeginInit()
		self._pnlGroups.SuspendLayout()
		self._tabGroupTabs.SuspendLayout()
		self._tabPage3.SuspendLayout()
		self._dgvGroupRulesets.BeginInit()
		self._dgvGroupGroups.BeginInit()
		self._dataGridView5.BeginInit()
		self._tabGrpRuleset.SuspendLayout()
		self._pictureBox3.BeginInit()
		self._dgvGroupFilters.BeginInit()
		self._dgvGroupDefaults.BeginInit()
		self._pictureBox4.BeginInit()
		self._pnlGeneral.SuspendLayout()
		self._dgvCollectionRulesets.BeginInit()
		self._dgvCollectionGroups.BeginInit()
		self._tabTemplateManager.SuspendLayout()
		self._dataGridView1.BeginInit()
		self._tabSearch.SuspendLayout()
		self._toolStripContainer2.ContentPanel.SuspendLayout()
		self._toolStripContainer2.TopToolStripPanel.SuspendLayout()
		self._toolStripContainer2.SuspendLayout()
		self._dataGridView3.BeginInit()
		self._tsSearch.SuspendLayout()
		self.SuspendLayout()
		# 
		# tabControl1
		# 
		self._tabControl1.Controls.Add(self._tabEdit)
		self._tabControl1.Controls.Add(self._tabTemplateManager)
		self._tabControl1.Controls.Add(self._tabSearch)
		self._tabControl1.Location = System.Drawing.Point(0, 0)
		self._tabControl1.Name = "tabControl1"
		self._tabControl1.SelectedIndex = 0
		self._tabControl1.Size = System.Drawing.Size(922, 665)
		self._tabControl1.TabIndex = 1
		# 
		# tabEdit
		# 
		self._tabEdit.Controls.Add(self._splitContainer1)
		self._tabEdit.Location = System.Drawing.Point(4, 22)
		self._tabEdit.Name = "tabEdit"
		self._tabEdit.Padding = System.Windows.Forms.Padding(3)
		self._tabEdit.Size = System.Drawing.Size(914, 639)
		self._tabEdit.TabIndex = 0
		self._tabEdit.Text = "Edit"
		self._tabEdit.UseVisualStyleBackColor = True
		# 
		# splitContainer1
		# 
		self._splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill
		self._splitContainer1.FixedPanel = System.Windows.Forms.FixedPanel.Panel1
		self._splitContainer1.Location = System.Drawing.Point(3, 3)
		self._splitContainer1.Name = "splitContainer1"
		# 
		# splitContainer1.Panel1
		# 
		self._splitContainer1.Panel1.Controls.Add(self._toolStripContainer1)
		# 
		# splitContainer1.Panel2
		# 
		self._splitContainer1.Panel2.Controls.Add(self._pnlRulesets)
		self._splitContainer1.Panel2.Controls.Add(self._pnlGroups)
		self._splitContainer1.Panel2.Controls.Add(self._pnlGeneral)
		self._splitContainer1.Panel2MinSize = 676
		self._splitContainer1.Size = System.Drawing.Size(908, 633)
		self._splitContainer1.SplitterDistance = 216
		self._splitContainer1.TabIndex = 1
		# 
		# toolStripContainer1
		# 
		# 
		# toolStripContainer1.BottomToolStripPanel
		# 
		self._toolStripContainer1.BottomToolStripPanel.Controls.Add(self._toolStrip1)
		# 
		# toolStripContainer1.ContentPanel
		# 
		self._toolStripContainer1.ContentPanel.Controls.Add(self._tvCollectionTree)
		self._toolStripContainer1.ContentPanel.Size = System.Drawing.Size(216, 608)
		self._toolStripContainer1.Dock = System.Windows.Forms.DockStyle.Fill
		self._toolStripContainer1.LeftToolStripPanelVisible = False
		self._toolStripContainer1.Location = System.Drawing.Point(0, 0)
		self._toolStripContainer1.Name = "toolStripContainer1"
		self._toolStripContainer1.RightToolStripPanelVisible = False
		self._toolStripContainer1.Size = System.Drawing.Size(216, 633)
		self._toolStripContainer1.TabIndex = 2
		self._toolStripContainer1.Text = "toolStripContainer1"
		self._toolStripContainer1.TopToolStripPanelVisible = False
		# 
		# toolStrip1
		# 
		self._toolStrip1.CanOverflow = False
		self._toolStrip1.Dock = System.Windows.Forms.DockStyle.None
		self._toolStrip1.GripStyle = System.Windows.Forms.ToolStripGripStyle.Hidden
		self._toolStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._tsmiFile,
			self._tsbSave]))
		self._toolStrip1.Location = System.Drawing.Point(0, 0)
		self._toolStrip1.Name = "toolStrip1"
		self._toolStrip1.Size = System.Drawing.Size(216, 25)
		self._toolStrip1.Stretch = True
		self._toolStrip1.TabIndex = 0
		# 
		# tsmiFile
		# 
		self._tsmiFile.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._tsmiAbout,
			self._tsmiSettings,
			self._tssSeparator1,
			self._tsmiProfileImport,
			self._tsmiMerge,
			self._tsmiRevert,
			self._tsmiLoadDefault,
			self._tsmiLoad,
			self._tsmiNew,
			self._tsmiSaveAsDefault,
			self._tsmiSaveAs,
			self._tsmiSave]))
		self._tsmiFile.Image = resources.GetObject("tsmiFile.Image")
		self._tsmiFile.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._tsmiFile.ImageTransparentColor = System.Drawing.Color.Magenta
		self._tsmiFile.Name = "tsmiFile"
		self._tsmiFile.Size = System.Drawing.Size(54, 22)
		self._tsmiFile.Text = "File"
		self._tsmiFile.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# tsmiAbout
		# 
		self._tsmiAbout.Name = "tsmiAbout"
		self._tsmiAbout.Size = System.Drawing.Size(253, 22)
		self._tsmiAbout.Text = "About"
		# 
		# tsmiSettings
		# 
		self._tsmiSettings.Name = "tsmiSettings"
		self._tsmiSettings.Size = System.Drawing.Size(253, 22)
		self._tsmiSettings.Text = "Settings"
		# 
		# tssSeparator1
		# 
		self._tssSeparator1.Name = "tssSeparator1"
		self._tssSeparator1.Size = System.Drawing.Size(250, 6)
		# 
		# tsmiProfileImport
		# 
		self._tsmiProfileImport.Name = "tsmiProfileImport"
		self._tsmiProfileImport.ShortcutKeyDisplayString = "Ctrl+I"
		self._tsmiProfileImport.Size = System.Drawing.Size(253, 22)
		self._tsmiProfileImport.Text = "Import..."
		self._tsmiProfileImport.ToolTipText = resources.GetString("tsmiProfileImport.ToolTipText")
		# 
		# tsmiMerge
		# 
		self._tsmiMerge.Image = resources.GetObject("tsmiMerge.Image")
		self._tsmiMerge.Name = "tsmiMerge"
		self._tsmiMerge.ShortcutKeyDisplayString = "Ctrl+M"
		self._tsmiMerge.Size = System.Drawing.Size(253, 22)
		self._tsmiMerge.Text = "Merge..."
		self._tsmiMerge.ToolTipText = "Merge Current Profile With Another Profile File"
		# 
		# tsmiRevert
		# 
		self._tsmiRevert.Image = resources.GetObject("tsmiRevert.Image")
		self._tsmiRevert.Name = "tsmiRevert"
		self._tsmiRevert.ShortcutKeyDisplayString = "Ctrl+R"
		self._tsmiRevert.Size = System.Drawing.Size(253, 22)
		self._tsmiRevert.Text = "Revert"
		self._tsmiRevert.ToolTipText = "Reload the currently loaded file from last save."
		# 
		# tsmiLoadDefault
		# 
		self._tsmiLoadDefault.Image = resources.GetObject("tsmiLoadDefault.Image")
		self._tsmiLoadDefault.Name = "tsmiLoadDefault"
		self._tsmiLoadDefault.ShortcutKeyDisplayString = "Crtl+Shift+O"
		self._tsmiLoadDefault.Size = System.Drawing.Size(253, 22)
		self._tsmiLoadDefault.Text = "Load Default Profile"
		# 
		# tsmiLoad
		# 
		self._tsmiLoad.Image = resources.GetObject("tsmiLoad.Image")
		self._tsmiLoad.Name = "tsmiLoad"
		self._tsmiLoad.ShortcutKeyDisplayString = "Ctrl+O"
		self._tsmiLoad.Size = System.Drawing.Size(253, 22)
		self._tsmiLoad.Text = "Load..."
		self._tsmiLoad.ToolTipText = "Open A new Profile File"
		# 
		# tsmiNew
		# 
		self._tsmiNew.Image = resources.GetObject("tsmiNew.Image")
		self._tsmiNew.Name = "tsmiNew"
		self._tsmiNew.ShortcutKeyDisplayString = "Ctrl+N"
		self._tsmiNew.Size = System.Drawing.Size(253, 22)
		self._tsmiNew.Text = "New"
		# 
		# tsmiSaveAsDefault
		# 
		self._tsmiSaveAsDefault.Name = "tsmiSaveAsDefault"
		self._tsmiSaveAsDefault.ShortcutKeyDisplayString = "Ctrl+D"
		self._tsmiSaveAsDefault.Size = System.Drawing.Size(253, 22)
		self._tsmiSaveAsDefault.Text = "Save As Default"
		self._tsmiSaveAsDefault.ToolTipText = "Save this file as the default dataman profile."
		# 
		# tsmiSaveAs
		# 
		self._tsmiSaveAs.Image = resources.GetObject("tsmiSaveAs.Image")
		self._tsmiSaveAs.Name = "tsmiSaveAs"
		self._tsmiSaveAs.ShortcutKeyDisplayString = "Ctrl +Shift+S"
		self._tsmiSaveAs.Size = System.Drawing.Size(253, 22)
		self._tsmiSaveAs.Text = "Save As..."
		self._tsmiSaveAs.ToolTipText = "Save File with different name."
		# 
		# tsmiSave
		# 
		self._tsmiSave.Image = resources.GetObject("tsmiSave.Image")
		self._tsmiSave.Name = "tsmiSave"
		self._tsmiSave.ShortcutKeyDisplayString = "Ctrl+S"
		self._tsmiSave.Size = System.Drawing.Size(253, 22)
		self._tsmiSave.Text = "Save"
		self._tsmiSave.ToolTipText = "Save the currenly loaded profile file."
		# 
		# tsbSave
		# 
		self._tsbSave.Image = resources.GetObject("tsbSave.Image")
		self._tsbSave.ImageTransparentColor = System.Drawing.Color.Magenta
		self._tsbSave.Name = "tsbSave"
		self._tsbSave.Size = System.Drawing.Size(51, 22)
		self._tsbSave.Text = "Save"
		# 
		# tvCollectionTree
		# 
		self._tvCollectionTree.AllowDrop = True
		self._tvCollectionTree.Dock = System.Windows.Forms.DockStyle.Fill
		self._tvCollectionTree.HideSelection = False
		self._tvCollectionTree.HotTracking = True
		self._tvCollectionTree.Location = System.Drawing.Point(0, 0)
		self._tvCollectionTree.Name = "tvCollectionTree"
		self._tvCollectionTree.Size = System.Drawing.Size(216, 608)
		self._tvCollectionTree.TabIndex = 0
		# 
		# pnlRulesets
		# 
		self._pnlRulesets.Controls.Add(self._comboBox1)
		self._pnlRulesets.Controls.Add(self._btnRulesetRulesMoveDown)
		self._pnlRulesets.Controls.Add(self._btnRulesetRulesMoveUp)
		self._pnlRulesets.Controls.Add(self._btnActionMoveDown)
		self._pnlRulesets.Controls.Add(self._btnActionMoveUp)
		self._pnlRulesets.Controls.Add(self._btnRulesetReparse)
		self._pnlRulesets.Controls.Add(self._pictureBox2)
		self._pnlRulesets.Controls.Add(self._lblRulesetOriginalText)
		self._pnlRulesets.Controls.Add(self._txtRulesetReparse)
		self._pnlRulesets.Controls.Add(self._btnRulesetRuleRemove)
		self._pnlRulesets.Controls.Add(self._btnRulesetRuleUpdate)
		self._pnlRulesets.Controls.Add(self._btnRulesetRuleClear)
		self._pnlRulesets.Controls.Add(self._commentLabel1)
		self._pnlRulesets.Controls.Add(self._txtRulesetComment)
		self._pnlRulesets.Controls.Add(self._btnRulesetRuleAdd)
		self._pnlRulesets.Controls.Add(self._nameLabel1)
		self._pnlRulesets.Controls.Add(self._txtRulesetName)
		self._pnlRulesets.Controls.Add(self._dgvRulesetRules)
		self._pnlRulesets.Controls.Add(self._dgvRulesetActions)
		self._pnlRulesets.Controls.Add(self._btnRulesetActionAdd)
		self._pnlRulesets.Controls.Add(self._label5)
		self._pnlRulesets.Controls.Add(self._label2)
		self._pnlRulesets.Controls.Add(self._btnRulesetActionClear)
		self._pnlRulesets.Controls.Add(self._pictureBox1)
		self._pnlRulesets.Controls.Add(self._label3)
		self._pnlRulesets.Controls.Add(self._btnRulesetActionUpdate)
		self._pnlRulesets.Controls.Add(self._btnRulesetActionRemove)
		self._pnlRulesets.Dock = System.Windows.Forms.DockStyle.Fill
		self._pnlRulesets.Location = System.Drawing.Point(0, 0)
		self._pnlRulesets.Name = "pnlRulesets"
		self._pnlRulesets.Size = System.Drawing.Size(688, 633)
		self._pnlRulesets.TabIndex = 4
		# 
		# comboBox1
		# 
		self._comboBox1.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._comboBox1.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["AND",
			"OR"]))
		self._comboBox1.Location = System.Drawing.Point(526, 64)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(130, 21)
		self._comboBox1.TabIndex = 23
		# 
		# btnRulesetRulesMoveDown
		# 
		self._btnRulesetRulesMoveDown.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnRulesetRulesMoveDown.Enabled = False
		self._btnRulesetRulesMoveDown.ImageIndex = 13
		self._btnRulesetRulesMoveDown.Location = System.Drawing.Point(658, 246)
		self._btnRulesetRulesMoveDown.Name = "btnRulesetRulesMoveDown"
		self._btnRulesetRulesMoveDown.Size = System.Drawing.Size(25, 25)
		self._btnRulesetRulesMoveDown.TabIndex = 17
		self._btnRulesetRulesMoveDown.UseVisualStyleBackColor = True
		# 
		# btnRulesetRulesMoveUp
		# 
		self._btnRulesetRulesMoveUp.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnRulesetRulesMoveUp.Enabled = False
		self._btnRulesetRulesMoveUp.ImageIndex = 12
		self._btnRulesetRulesMoveUp.Location = System.Drawing.Point(658, 220)
		self._btnRulesetRulesMoveUp.Name = "btnRulesetRulesMoveUp"
		self._btnRulesetRulesMoveUp.Size = System.Drawing.Size(25, 25)
		self._btnRulesetRulesMoveUp.TabIndex = 16
		self._btnRulesetRulesMoveUp.UseVisualStyleBackColor = True
		# 
		# btnActionMoveDown
		# 
		self._btnActionMoveDown.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnActionMoveDown.Enabled = False
		self._btnActionMoveDown.ImageIndex = 13
		self._btnActionMoveDown.Location = System.Drawing.Point(658, 537)
		self._btnActionMoveDown.Name = "btnActionMoveDown"
		self._btnActionMoveDown.Size = System.Drawing.Size(25, 25)
		self._btnActionMoveDown.TabIndex = 17
		self._btnActionMoveDown.UseVisualStyleBackColor = True
		# 
		# btnActionMoveUp
		# 
		self._btnActionMoveUp.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnActionMoveUp.Enabled = False
		self._btnActionMoveUp.ImageIndex = 12
		self._btnActionMoveUp.Location = System.Drawing.Point(658, 511)
		self._btnActionMoveUp.Name = "btnActionMoveUp"
		self._btnActionMoveUp.Size = System.Drawing.Size(25, 25)
		self._btnActionMoveUp.TabIndex = 16
		self._btnActionMoveUp.UseVisualStyleBackColor = True
		# 
		# btnRulesetReparse
		# 
		self._btnRulesetReparse.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._btnRulesetReparse.ImageIndex = 15
		self._btnRulesetReparse.Location = System.Drawing.Point(655, 30)
		self._btnRulesetReparse.Name = "btnRulesetReparse"
		self._btnRulesetReparse.Size = System.Drawing.Size(25, 25)
		self._btnRulesetReparse.TabIndex = 6
		self._btnRulesetReparse.UseVisualStyleBackColor = True
		# 
		# pictureBox2
		# 
		self._pictureBox2.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._pictureBox2.BackColor = System.Drawing.Color.Black
		self._pictureBox2.Location = System.Drawing.Point(55, 76)
		self._pictureBox2.Name = "pictureBox2"
		self._pictureBox2.Size = System.Drawing.Size(400, 1)
		self._pictureBox2.TabIndex = 7
		self._pictureBox2.TabStop = False
		# 
		# lblRulesetOriginalText
		# 
		self._lblRulesetOriginalText.AutoSize = True
		self._lblRulesetOriginalText.Location = System.Drawing.Point(22, 36)
		self._lblRulesetOriginalText.Name = "lblRulesetOriginalText"
		self._lblRulesetOriginalText.Size = System.Drawing.Size(28, 13)
		self._lblRulesetOriginalText.TabIndex = 4
		self._lblRulesetOriginalText.Text = "Text"
		# 
		# txtRulesetReparse
		# 
		self._txtRulesetReparse.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._txtRulesetReparse.Location = System.Drawing.Point(56, 33)
		self._txtRulesetReparse.Name = "txtRulesetReparse"
		self._txtRulesetReparse.Size = System.Drawing.Size(594, 20)
		self._txtRulesetReparse.TabIndex = 5
		# 
		# btnRulesetRuleRemove
		# 
		self._btnRulesetRuleRemove.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._btnRulesetRuleRemove.ImageIndex = 18
		self._btnRulesetRuleRemove.Location = System.Drawing.Point(446, 308)
		self._btnRulesetRuleRemove.Name = "btnRulesetRuleRemove"
		self._btnRulesetRuleRemove.Size = System.Drawing.Size(104, 23)
		self._btnRulesetRuleRemove.TabIndex = 12
		self._btnRulesetRuleRemove.Text = "Remove"
		self._btnRulesetRuleRemove.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnRulesetRuleRemove.UseVisualStyleBackColor = True
		# 
		# btnRulesetRuleUpdate
		# 
		self._btnRulesetRuleUpdate.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._btnRulesetRuleUpdate.ImageIndex = 15
		self._btnRulesetRuleUpdate.Location = System.Drawing.Point(238, 308)
		self._btnRulesetRuleUpdate.Name = "btnRulesetRuleUpdate"
		self._btnRulesetRuleUpdate.Size = System.Drawing.Size(104, 23)
		self._btnRulesetRuleUpdate.TabIndex = 11
		self._btnRulesetRuleUpdate.Text = "Update"
		self._btnRulesetRuleUpdate.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnRulesetRuleUpdate.UseVisualStyleBackColor = True
		# 
		# btnRulesetRuleClear
		# 
		self._btnRulesetRuleClear.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._btnRulesetRuleClear.ImageIndex = 7
		self._btnRulesetRuleClear.Location = System.Drawing.Point(550, 308)
		self._btnRulesetRuleClear.Name = "btnRulesetRuleClear"
		self._btnRulesetRuleClear.Size = System.Drawing.Size(104, 23)
		self._btnRulesetRuleClear.TabIndex = 13
		self._btnRulesetRuleClear.Text = "Clear Rules"
		self._btnRulesetRuleClear.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnRulesetRuleClear.UseVisualStyleBackColor = True
		# 
		# commentLabel1
		# 
		self._commentLabel1.AutoSize = True
		self._commentLabel1.Location = System.Drawing.Point(337, 8)
		self._commentLabel1.Name = "commentLabel1"
		self._commentLabel1.Size = System.Drawing.Size(54, 13)
		self._commentLabel1.TabIndex = 2
		self._commentLabel1.Text = "Comment:"
		# 
		# txtRulesetComment
		# 
		self._txtRulesetComment.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._txtRulesetComment.Location = System.Drawing.Point(397, 4)
		self._txtRulesetComment.Name = "txtRulesetComment"
		self._txtRulesetComment.Size = System.Drawing.Size(284, 20)
		self._txtRulesetComment.TabIndex = 3
		# 
		# btnRulesetRuleAdd
		# 
		self._btnRulesetRuleAdd.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._btnRulesetRuleAdd.ImageIndex = 17
		self._btnRulesetRuleAdd.Location = System.Drawing.Point(342, 308)
		self._btnRulesetRuleAdd.Name = "btnRulesetRuleAdd"
		self._btnRulesetRuleAdd.Size = System.Drawing.Size(104, 23)
		self._btnRulesetRuleAdd.TabIndex = 10
		self._btnRulesetRuleAdd.Text = "Add"
		self._btnRulesetRuleAdd.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnRulesetRuleAdd.UseVisualStyleBackColor = True
		# 
		# nameLabel1
		# 
		self._nameLabel1.AutoSize = True
		self._nameLabel1.Location = System.Drawing.Point(53, 8)
		self._nameLabel1.Name = "nameLabel1"
		self._nameLabel1.Size = System.Drawing.Size(38, 13)
		self._nameLabel1.TabIndex = 0
		self._nameLabel1.Text = "Name:"
		# 
		# txtRulesetName
		# 
		self._txtRulesetName.Location = System.Drawing.Point(97, 4)
		self._txtRulesetName.Name = "txtRulesetName"
		self._txtRulesetName.Size = System.Drawing.Size(234, 20)
		self._txtRulesetName.TabIndex = 1
		# 
		# dgvRulesetRules
		# 
		self._dgvRulesetRules.AllowUserToAddRows = False
		self._dgvRulesetRules.AllowUserToDeleteRows = False
		self._dgvRulesetRules.AllowUserToResizeRows = False
		self._dgvRulesetRules.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._dgvRulesetRules.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill
		self._dgvRulesetRules.BackgroundColor = System.Drawing.SystemColors.Window
		self._dgvRulesetRules.Columns.AddRange(System.Array[System.Windows.Forms.DataGridViewColumn](
			[self._dataGridViewTextBoxColumn3,
			self._dgvtcRulesetRuleValue]))
		self._dgvRulesetRules.Location = System.Drawing.Point(11, 89)
		self._dgvRulesetRules.MultiSelect = False
		self._dgvRulesetRules.Name = "dgvRulesetRules"
		self._dgvRulesetRules.ReadOnly = True
		self._dgvRulesetRules.RowHeadersVisible = False
		self._dgvRulesetRules.RowHeadersWidth = 25
		self._dgvRulesetRules.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect
		self._dgvRulesetRules.Size = System.Drawing.Size(643, 179)
		self._dgvRulesetRules.TabIndex = 8
		# 
		# dataGridViewTextBoxColumn3
		# 
		self._dataGridViewTextBoxColumn3.DataPropertyName = "Field"
		self._dataGridViewTextBoxColumn3.HeaderText = "Field"
		self._dataGridViewTextBoxColumn3.Name = "dataGridViewTextBoxColumn3"
		self._dataGridViewTextBoxColumn3.ReadOnly = True
		# 
		# dgvtcRulesetRuleValue
		# 
		self._dgvtcRulesetRuleValue.DataPropertyName = "Value"
		self._dgvtcRulesetRuleValue.HeaderText = "Value"
		self._dgvtcRulesetRuleValue.Name = "dgvtcRulesetRuleValue"
		self._dgvtcRulesetRuleValue.ReadOnly = True
		self._dgvtcRulesetRuleValue.SortMode = System.Windows.Forms.DataGridViewColumnSortMode.NotSortable
		# 
		# dgvRulesetActions
		# 
		self._dgvRulesetActions.AllowUserToAddRows = False
		self._dgvRulesetActions.AllowUserToDeleteRows = False
		self._dgvRulesetActions.AllowUserToResizeRows = False
		self._dgvRulesetActions.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._dgvRulesetActions.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill
		self._dgvRulesetActions.BackgroundColor = System.Drawing.SystemColors.Window
		self._dgvRulesetActions.Columns.AddRange(System.Array[System.Windows.Forms.DataGridViewColumn](
			[self._dataGridViewTextBoxColumn2,
			self._dgvtcRulesetActionValue]))
		self._dgvRulesetActions.Location = System.Drawing.Point(12, 350)
		self._dgvRulesetActions.MultiSelect = False
		self._dgvRulesetActions.Name = "dgvRulesetActions"
		self._dgvRulesetActions.ReadOnly = True
		self._dgvRulesetActions.RowHeadersVisible = False
		self._dgvRulesetActions.RowHeadersWidth = 25
		self._dgvRulesetActions.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect
		self._dgvRulesetActions.Size = System.Drawing.Size(642, 214)
		self._dgvRulesetActions.TabIndex = 15
		# 
		# dataGridViewTextBoxColumn2
		# 
		self._dataGridViewTextBoxColumn2.DataPropertyName = "Field"
		self._dataGridViewTextBoxColumn2.HeaderText = "Field"
		self._dataGridViewTextBoxColumn2.Name = "dataGridViewTextBoxColumn2"
		self._dataGridViewTextBoxColumn2.ReadOnly = True
		# 
		# dgvtcRulesetActionValue
		# 
		self._dgvtcRulesetActionValue.DataPropertyName = "Value"
		self._dgvtcRulesetActionValue.HeaderText = "Value"
		self._dgvtcRulesetActionValue.Name = "dgvtcRulesetActionValue"
		self._dgvtcRulesetActionValue.ReadOnly = True
		self._dgvtcRulesetActionValue.SortMode = System.Windows.Forms.DataGridViewColumnSortMode.NotSortable
		# 
		# btnRulesetActionAdd
		# 
		self._btnRulesetActionAdd.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnRulesetActionAdd.ImageIndex = 17
		self._btnRulesetActionAdd.Location = System.Drawing.Point(342, 603)
		self._btnRulesetActionAdd.Name = "btnRulesetActionAdd"
		self._btnRulesetActionAdd.Size = System.Drawing.Size(104, 23)
		self._btnRulesetActionAdd.TabIndex = 20
		self._btnRulesetActionAdd.Text = "Add"
		self._btnRulesetActionAdd.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnRulesetActionAdd.UseVisualStyleBackColor = True
		# 
		# label5
		# 
		self._label5.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._label5.AutoSize = True
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(456, 68)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(68, 13)
		self._label5.TabIndex = 7
		self._label5.Text = "Rule Mode"
		# 
		# label2
		# 
		self._label2.AutoSize = True
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(13, 70)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(39, 13)
		self._label2.TabIndex = 7
		self._label2.Text = "Rules"
		# 
		# btnRulesetActionClear
		# 
		self._btnRulesetActionClear.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnRulesetActionClear.ImageIndex = 7
		self._btnRulesetActionClear.Location = System.Drawing.Point(550, 603)
		self._btnRulesetActionClear.Name = "btnRulesetActionClear"
		self._btnRulesetActionClear.Size = System.Drawing.Size(104, 23)
		self._btnRulesetActionClear.TabIndex = 22
		self._btnRulesetActionClear.Text = "Clear Actions"
		self._btnRulesetActionClear.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnRulesetActionClear.UseVisualStyleBackColor = True
		# 
		# pictureBox1
		# 
		self._pictureBox1.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._pictureBox1.BackColor = System.Drawing.Color.Black
		self._pictureBox1.Location = System.Drawing.Point(67, 337)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(607, 1)
		self._pictureBox1.TabIndex = 7
		self._pictureBox1.TabStop = False
		# 
		# label3
		# 
		self._label3.AutoSize = True
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(15, 330)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(49, 13)
		self._label3.TabIndex = 14
		self._label3.Text = "Actions"
		# 
		# btnRulesetActionUpdate
		# 
		self._btnRulesetActionUpdate.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnRulesetActionUpdate.ImageIndex = 15
		self._btnRulesetActionUpdate.Location = System.Drawing.Point(238, 603)
		self._btnRulesetActionUpdate.Name = "btnRulesetActionUpdate"
		self._btnRulesetActionUpdate.Size = System.Drawing.Size(104, 23)
		self._btnRulesetActionUpdate.TabIndex = 19
		self._btnRulesetActionUpdate.Text = "Update"
		self._btnRulesetActionUpdate.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnRulesetActionUpdate.UseVisualStyleBackColor = True
		# 
		# btnRulesetActionRemove
		# 
		self._btnRulesetActionRemove.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnRulesetActionRemove.ImageIndex = 18
		self._btnRulesetActionRemove.Location = System.Drawing.Point(446, 603)
		self._btnRulesetActionRemove.Name = "btnRulesetActionRemove"
		self._btnRulesetActionRemove.Size = System.Drawing.Size(104, 23)
		self._btnRulesetActionRemove.TabIndex = 21
		self._btnRulesetActionRemove.Text = "Remove"
		self._btnRulesetActionRemove.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnRulesetActionRemove.UseVisualStyleBackColor = True
		# 
		# pnlGroups
		# 
		self._pnlGroups.Controls.Add(self._tabGroupTabs)
		self._pnlGroups.Controls.Add(self._lblGroupOverview)
		self._pnlGroups.Controls.Add(self._commentLabel)
		self._pnlGroups.Controls.Add(self._txtGroupComment)
		self._pnlGroups.Controls.Add(self._nameLabel)
		self._pnlGroups.Controls.Add(self._txtGroupName)
		self._pnlGroups.Dock = System.Windows.Forms.DockStyle.Fill
		self._pnlGroups.Location = System.Drawing.Point(0, 0)
		self._pnlGroups.Name = "pnlGroups"
		self._pnlGroups.Size = System.Drawing.Size(688, 633)
		self._pnlGroups.TabIndex = 3
		# 
		# tabGroupTabs
		# 
		self._tabGroupTabs.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._tabGroupTabs.Controls.Add(self._tabPage3)
		self._tabGroupTabs.Controls.Add(self._tabGrpRuleset)
		self._tabGroupTabs.Location = System.Drawing.Point(3, 112)
		self._tabGroupTabs.Name = "tabGroupTabs"
		self._tabGroupTabs.SelectedIndex = 0
		self._tabGroupTabs.Size = System.Drawing.Size(685, 518)
		self._tabGroupTabs.TabIndex = 16
		# 
		# tabPage3
		# 
		self._tabPage3.Controls.Add(self._label19)
		self._tabPage3.Controls.Add(self._btnGroupRulesetRemove)
		self._tabPage3.Controls.Add(self._btnGroupGroupRemove)
		self._tabPage3.Controls.Add(self._btnGroupRulesetMoveDown)
		self._tabPage3.Controls.Add(self._button1)
		self._tabPage3.Controls.Add(self._dgvGroupRulesets)
		self._tabPage3.Controls.Add(self._btnGroupRulesetMoveUp)
		self._tabPage3.Controls.Add(self._dgvGroupGroups)
		self._tabPage3.Controls.Add(self._btnGroupGroupMoveDown)
		self._tabPage3.Controls.Add(self._btnGroupRulesetAdd)
		self._tabPage3.Controls.Add(self._dataGridView5)
		self._tabPage3.Controls.Add(self._btnGroupGroupMoveUp)
		self._tabPage3.Controls.Add(self._btnGroupGroupAdd)
		self._tabPage3.Controls.Add(self._label8)
		self._tabPage3.Controls.Add(self._button2)
		self._tabPage3.Controls.Add(self._label13)
		self._tabPage3.Controls.Add(self._label7)
		self._tabPage3.Location = System.Drawing.Point(4, 22)
		self._tabPage3.Name = "tabPage3"
		self._tabPage3.Padding = System.Windows.Forms.Padding(3)
		self._tabPage3.Size = System.Drawing.Size(677, 492)
		self._tabPage3.TabIndex = 0
		self._tabPage3.Text = "Groups & Rulesets"
		self._tabPage3.UseVisualStyleBackColor = True
		# 
		# label19
		# 
		self._label19.AutoSize = True
		self._label19.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label19.Location = System.Drawing.Point(6, 7)
		self._label19.Name = "label19"
		self._label19.Size = System.Drawing.Size(134, 16)
		self._label19.TabIndex = 4
		self._label19.Text = "Groups In This Group"
		self._label19.UseMnemonic = False
		# 
		# btnGroupRulesetRemove
		# 
		self._btnGroupRulesetRemove.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupRulesetRemove.Enabled = False
		self._btnGroupRulesetRemove.ImageIndex = 18
		self._btnGroupRulesetRemove.Location = System.Drawing.Point(560, 459)
		self._btnGroupRulesetRemove.Name = "btnGroupRulesetRemove"
		self._btnGroupRulesetRemove.Size = System.Drawing.Size(83, 23)
		self._btnGroupRulesetRemove.TabIndex = 15
		self._btnGroupRulesetRemove.Text = "Remove"
		self._btnGroupRulesetRemove.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnGroupRulesetRemove.UseVisualStyleBackColor = True
		# 
		# btnGroupGroupRemove
		# 
		self._btnGroupGroupRemove.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupGroupRemove.Enabled = False
		self._btnGroupGroupRemove.ImageIndex = 18
		self._btnGroupGroupRemove.Location = System.Drawing.Point(560, 209)
		self._btnGroupGroupRemove.Name = "btnGroupGroupRemove"
		self._btnGroupGroupRemove.Size = System.Drawing.Size(83, 23)
		self._btnGroupGroupRemove.TabIndex = 9
		self._btnGroupGroupRemove.Text = "Remove"
		self._btnGroupGroupRemove.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnGroupGroupRemove.UseVisualStyleBackColor = True
		# 
		# btnGroupRulesetMoveDown
		# 
		self._btnGroupRulesetMoveDown.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupRulesetMoveDown.Enabled = False
		self._btnGroupRulesetMoveDown.ImageIndex = 13
		self._btnGroupRulesetMoveDown.Location = System.Drawing.Point(649, 427)
		self._btnGroupRulesetMoveDown.Name = "btnGroupRulesetMoveDown"
		self._btnGroupRulesetMoveDown.Size = System.Drawing.Size(25, 25)
		self._btnGroupRulesetMoveDown.TabIndex = 13
		self._btnGroupRulesetMoveDown.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._button1.Enabled = False
		self._button1.ImageIndex = 18
		self._button1.Location = System.Drawing.Point(560, 209)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(83, 23)
		self._button1.TabIndex = 9
		self._button1.Text = "Remove"
		self._button1.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._button1.UseVisualStyleBackColor = True
		# 
		# dgvGroupRulesets
		# 
		self._dgvGroupRulesets.AllowUserToAddRows = False
		self._dgvGroupRulesets.AllowUserToDeleteRows = False
		self._dgvGroupRulesets.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._dgvGroupRulesets.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill
		self._dgvGroupRulesets.BackgroundColor = System.Drawing.SystemColors.Window
		self._dgvGroupRulesets.ClipboardCopyMode = System.Windows.Forms.DataGridViewClipboardCopyMode.Disable
		self._dgvGroupRulesets.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
		self._dgvGroupRulesets.Location = System.Drawing.Point(1, 254)
		self._dgvGroupRulesets.MultiSelect = False
		self._dgvGroupRulesets.Name = "dgvGroupRulesets"
		self._dgvGroupRulesets.RowHeadersWidth = 25
		self._dgvGroupRulesets.RowHeadersWidthSizeMode = System.Windows.Forms.DataGridViewRowHeadersWidthSizeMode.DisableResizing
		self._dgvGroupRulesets.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect
		self._dgvGroupRulesets.Size = System.Drawing.Size(642, 197)
		self._dgvGroupRulesets.TabIndex = 11
		# 
		# btnGroupRulesetMoveUp
		# 
		self._btnGroupRulesetMoveUp.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupRulesetMoveUp.Enabled = False
		self._btnGroupRulesetMoveUp.ImageIndex = 12
		self._btnGroupRulesetMoveUp.Location = System.Drawing.Point(649, 401)
		self._btnGroupRulesetMoveUp.Name = "btnGroupRulesetMoveUp"
		self._btnGroupRulesetMoveUp.Size = System.Drawing.Size(25, 25)
		self._btnGroupRulesetMoveUp.TabIndex = 12
		self._btnGroupRulesetMoveUp.UseVisualStyleBackColor = True
		# 
		# dgvGroupGroups
		# 
		self._dgvGroupGroups.AllowUserToAddRows = False
		self._dgvGroupGroups.AllowUserToDeleteRows = False
		self._dgvGroupGroups.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._dgvGroupGroups.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill
		self._dgvGroupGroups.BackgroundColor = System.Drawing.SystemColors.Window
		self._dgvGroupGroups.ClipboardCopyMode = System.Windows.Forms.DataGridViewClipboardCopyMode.Disable
		self._dgvGroupGroups.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
		self._dgvGroupGroups.Location = System.Drawing.Point(3, 30)
		self._dgvGroupGroups.MultiSelect = False
		self._dgvGroupGroups.Name = "dgvGroupGroups"
		self._dgvGroupGroups.RowHeadersWidth = 25
		self._dgvGroupGroups.RowHeadersWidthSizeMode = System.Windows.Forms.DataGridViewRowHeadersWidthSizeMode.DisableResizing
		self._dgvGroupGroups.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect
		self._dgvGroupGroups.Size = System.Drawing.Size(642, 173)
		self._dgvGroupGroups.TabIndex = 5
		# 
		# btnGroupGroupMoveDown
		# 
		self._btnGroupGroupMoveDown.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupGroupMoveDown.Enabled = False
		self._btnGroupGroupMoveDown.ImageIndex = 13
		self._btnGroupGroupMoveDown.Location = System.Drawing.Point(649, 178)
		self._btnGroupGroupMoveDown.Name = "btnGroupGroupMoveDown"
		self._btnGroupGroupMoveDown.Size = System.Drawing.Size(25, 25)
		self._btnGroupGroupMoveDown.TabIndex = 7
		self._btnGroupGroupMoveDown.UseVisualStyleBackColor = True
		# 
		# btnGroupRulesetAdd
		# 
		self._btnGroupRulesetAdd.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupRulesetAdd.ImageIndex = 17
		self._btnGroupRulesetAdd.Location = System.Drawing.Point(475, 459)
		self._btnGroupRulesetAdd.Name = "btnGroupRulesetAdd"
		self._btnGroupRulesetAdd.Size = System.Drawing.Size(83, 23)
		self._btnGroupRulesetAdd.TabIndex = 14
		self._btnGroupRulesetAdd.Text = "Add"
		self._btnGroupRulesetAdd.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnGroupRulesetAdd.UseVisualStyleBackColor = True
		# 
		# dataGridView5
		# 
		self._dataGridView5.AllowUserToAddRows = False
		self._dataGridView5.AllowUserToDeleteRows = False
		self._dataGridView5.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill
		self._dataGridView5.BackgroundColor = System.Drawing.SystemColors.Window
		self._dataGridView5.ClipboardCopyMode = System.Windows.Forms.DataGridViewClipboardCopyMode.Disable
		self._dataGridView5.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
		self._dataGridView5.Location = System.Drawing.Point(3, 30)
		self._dataGridView5.MultiSelect = False
		self._dataGridView5.Name = "dataGridView5"
		self._dataGridView5.RowHeadersWidth = 25
		self._dataGridView5.RowHeadersWidthSizeMode = System.Windows.Forms.DataGridViewRowHeadersWidthSizeMode.DisableResizing
		self._dataGridView5.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect
		self._dataGridView5.Size = System.Drawing.Size(642, 173)
		self._dataGridView5.TabIndex = 5
		# 
		# btnGroupGroupMoveUp
		# 
		self._btnGroupGroupMoveUp.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupGroupMoveUp.Enabled = False
		self._btnGroupGroupMoveUp.ImageIndex = 12
		self._btnGroupGroupMoveUp.Location = System.Drawing.Point(649, 152)
		self._btnGroupGroupMoveUp.Name = "btnGroupGroupMoveUp"
		self._btnGroupGroupMoveUp.Size = System.Drawing.Size(25, 25)
		self._btnGroupGroupMoveUp.TabIndex = 6
		self._btnGroupGroupMoveUp.UseVisualStyleBackColor = True
		# 
		# btnGroupGroupAdd
		# 
		self._btnGroupGroupAdd.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupGroupAdd.ImageIndex = 17
		self._btnGroupGroupAdd.Location = System.Drawing.Point(475, 209)
		self._btnGroupGroupAdd.Name = "btnGroupGroupAdd"
		self._btnGroupGroupAdd.Size = System.Drawing.Size(83, 23)
		self._btnGroupGroupAdd.TabIndex = 8
		self._btnGroupGroupAdd.Text = "Add"
		self._btnGroupGroupAdd.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnGroupGroupAdd.UseVisualStyleBackColor = True
		# 
		# label8
		# 
		self._label8.AutoSize = True
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(5, 232)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(143, 16)
		self._label8.TabIndex = 10
		self._label8.Text = "Rulesets In This Group"
		self._label8.UseMnemonic = False
		# 
		# button2
		# 
		self._button2.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._button2.ImageIndex = 17
		self._button2.Location = System.Drawing.Point(475, 209)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(83, 23)
		self._button2.TabIndex = 8
		self._button2.Text = "Add"
		self._button2.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._button2.UseVisualStyleBackColor = True
		# 
		# label13
		# 
		self._label13.AutoSize = True
		self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(6, 7)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(134, 16)
		self._label13.TabIndex = 4
		self._label13.Text = "Groups In This Group"
		self._label13.UseMnemonic = False
		# 
		# label7
		# 
		self._label7.AutoSize = True
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(5, 232)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(143, 16)
		self._label7.TabIndex = 10
		self._label7.Text = "Rulesets In This Group"
		self._label7.UseMnemonic = False
		# 
		# tabGrpRuleset
		# 
		self._tabGrpRuleset.Controls.Add(self._btnGroupFiltersMoveDown)
		self._tabGrpRuleset.Controls.Add(self._btnGroupFiltersMoveUp)
		self._tabGrpRuleset.Controls.Add(self._comboBox2)
		self._tabGrpRuleset.Controls.Add(self._btnGroupDefaultMoveDown)
		self._tabGrpRuleset.Controls.Add(self._btnGroupDefaultMoveUp)
		self._tabGrpRuleset.Controls.Add(self._pictureBox3)
		self._tabGrpRuleset.Controls.Add(self._btnGroupFilterRemove)
		self._tabGrpRuleset.Controls.Add(self._btnGroupFilterUpdate)
		self._tabGrpRuleset.Controls.Add(self._btnGroupFilterClear)
		self._tabGrpRuleset.Controls.Add(self._btnGroupFilterAdd)
		self._tabGrpRuleset.Controls.Add(self._dgvGroupFilters)
		self._tabGrpRuleset.Controls.Add(self._dgvGroupDefaults)
		self._tabGrpRuleset.Controls.Add(self._btnGroupDefaultAdd)
		self._tabGrpRuleset.Controls.Add(self._label21)
		self._tabGrpRuleset.Controls.Add(self._label22)
		self._tabGrpRuleset.Controls.Add(self._btnGroupDefaultClear)
		self._tabGrpRuleset.Controls.Add(self._pictureBox4)
		self._tabGrpRuleset.Controls.Add(self._label23)
		self._tabGrpRuleset.Controls.Add(self._btnGroupDefaultUpdate)
		self._tabGrpRuleset.Controls.Add(self._btnGroupDefaultRemove)
		self._tabGrpRuleset.Location = System.Drawing.Point(4, 22)
		self._tabGrpRuleset.Name = "tabGrpRuleset"
		self._tabGrpRuleset.Padding = System.Windows.Forms.Padding(3)
		self._tabGrpRuleset.Size = System.Drawing.Size(677, 488)
		self._tabGrpRuleset.TabIndex = 1
		self._tabGrpRuleset.Text = "Filters & Defaults"
		self._tabGrpRuleset.UseVisualStyleBackColor = True
		# 
		# btnGroupFiltersMoveDown
		# 
		self._btnGroupFiltersMoveDown.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupFiltersMoveDown.Enabled = False
		self._btnGroupFiltersMoveDown.ImageIndex = 13
		self._btnGroupFiltersMoveDown.Location = System.Drawing.Point(646, 140)
		self._btnGroupFiltersMoveDown.Name = "btnGroupFiltersMoveDown"
		self._btnGroupFiltersMoveDown.Size = System.Drawing.Size(25, 25)
		self._btnGroupFiltersMoveDown.TabIndex = 45
		self._btnGroupFiltersMoveDown.UseVisualStyleBackColor = True
		# 
		# btnGroupFiltersMoveUp
		# 
		self._btnGroupFiltersMoveUp.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupFiltersMoveUp.Enabled = False
		self._btnGroupFiltersMoveUp.ImageIndex = 12
		self._btnGroupFiltersMoveUp.Location = System.Drawing.Point(646, 114)
		self._btnGroupFiltersMoveUp.Name = "btnGroupFiltersMoveUp"
		self._btnGroupFiltersMoveUp.Size = System.Drawing.Size(25, 25)
		self._btnGroupFiltersMoveUp.TabIndex = 44
		self._btnGroupFiltersMoveUp.UseVisualStyleBackColor = True
		# 
		# comboBox2
		# 
		self._comboBox2.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._comboBox2.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Items.AddRange(System.Array[System.Object](
			["AND",
			"OR"]))
		self._comboBox2.Location = System.Drawing.Point(541, 8)
		self._comboBox2.Name = "comboBox2"
		self._comboBox2.Size = System.Drawing.Size(102, 21)
		self._comboBox2.TabIndex = 43
		# 
		# btnGroupDefaultMoveDown
		# 
		self._btnGroupDefaultMoveDown.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupDefaultMoveDown.Enabled = False
		self._btnGroupDefaultMoveDown.ImageIndex = 13
		self._btnGroupDefaultMoveDown.Location = System.Drawing.Point(647, 375)
		self._btnGroupDefaultMoveDown.Name = "btnGroupDefaultMoveDown"
		self._btnGroupDefaultMoveDown.Size = System.Drawing.Size(25, 25)
		self._btnGroupDefaultMoveDown.TabIndex = 37
		self._btnGroupDefaultMoveDown.UseVisualStyleBackColor = True
		# 
		# btnGroupDefaultMoveUp
		# 
		self._btnGroupDefaultMoveUp.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupDefaultMoveUp.Enabled = False
		self._btnGroupDefaultMoveUp.ImageIndex = 12
		self._btnGroupDefaultMoveUp.Location = System.Drawing.Point(647, 349)
		self._btnGroupDefaultMoveUp.Name = "btnGroupDefaultMoveUp"
		self._btnGroupDefaultMoveUp.Size = System.Drawing.Size(25, 25)
		self._btnGroupDefaultMoveUp.TabIndex = 36
		self._btnGroupDefaultMoveUp.UseVisualStyleBackColor = True
		# 
		# pictureBox3
		# 
		self._pictureBox3.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._pictureBox3.BackColor = System.Drawing.Color.Black
		self._pictureBox3.Location = System.Drawing.Point(96, 18)
		self._pictureBox3.Name = "pictureBox3"
		self._pictureBox3.Size = System.Drawing.Size(353, 1)
		self._pictureBox3.TabIndex = 24
		self._pictureBox3.TabStop = False
		# 
		# btnGroupFilterRemove
		# 
		self._btnGroupFilterRemove.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupFilterRemove.ImageIndex = 18
		self._btnGroupFilterRemove.Location = System.Drawing.Point(461, 210)
		self._btnGroupFilterRemove.Name = "btnGroupFilterRemove"
		self._btnGroupFilterRemove.Size = System.Drawing.Size(104, 23)
		self._btnGroupFilterRemove.TabIndex = 32
		self._btnGroupFilterRemove.Text = "Remove"
		self._btnGroupFilterRemove.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnGroupFilterRemove.UseVisualStyleBackColor = True
		# 
		# btnGroupFilterUpdate
		# 
		self._btnGroupFilterUpdate.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupFilterUpdate.ImageIndex = 15
		self._btnGroupFilterUpdate.Location = System.Drawing.Point(253, 210)
		self._btnGroupFilterUpdate.Name = "btnGroupFilterUpdate"
		self._btnGroupFilterUpdate.Size = System.Drawing.Size(104, 23)
		self._btnGroupFilterUpdate.TabIndex = 31
		self._btnGroupFilterUpdate.Text = "Update"
		self._btnGroupFilterUpdate.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnGroupFilterUpdate.UseVisualStyleBackColor = True
		# 
		# btnGroupFilterClear
		# 
		self._btnGroupFilterClear.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupFilterClear.ImageIndex = 7
		self._btnGroupFilterClear.Location = System.Drawing.Point(565, 210)
		self._btnGroupFilterClear.Name = "btnGroupFilterClear"
		self._btnGroupFilterClear.Size = System.Drawing.Size(104, 23)
		self._btnGroupFilterClear.TabIndex = 33
		self._btnGroupFilterClear.Text = "Clear Rules"
		self._btnGroupFilterClear.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnGroupFilterClear.UseVisualStyleBackColor = True
		# 
		# btnGroupFilterAdd
		# 
		self._btnGroupFilterAdd.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupFilterAdd.ImageIndex = 17
		self._btnGroupFilterAdd.Location = System.Drawing.Point(357, 210)
		self._btnGroupFilterAdd.Name = "btnGroupFilterAdd"
		self._btnGroupFilterAdd.Size = System.Drawing.Size(104, 23)
		self._btnGroupFilterAdd.TabIndex = 30
		self._btnGroupFilterAdd.Text = "Add"
		self._btnGroupFilterAdd.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnGroupFilterAdd.UseVisualStyleBackColor = True
		# 
		# dgvGroupFilters
		# 
		self._dgvGroupFilters.AllowUserToAddRows = False
		self._dgvGroupFilters.AllowUserToDeleteRows = False
		self._dgvGroupFilters.AllowUserToResizeRows = False
		self._dgvGroupFilters.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._dgvGroupFilters.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill
		self._dgvGroupFilters.BackgroundColor = System.Drawing.SystemColors.Window
		self._dgvGroupFilters.Columns.AddRange(System.Array[System.Windows.Forms.DataGridViewColumn](
			[self._Field]))
		self._dgvGroupFilters.Location = System.Drawing.Point(8, 31)
		self._dgvGroupFilters.MultiSelect = False
		self._dgvGroupFilters.Name = "dgvGroupFilters"
		self._dgvGroupFilters.ReadOnly = True
		self._dgvGroupFilters.RowHeadersVisible = False
		self._dgvGroupFilters.RowHeadersWidth = 25
		self._dgvGroupFilters.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect
		self._dgvGroupFilters.Size = System.Drawing.Size(635, 137)
		self._dgvGroupFilters.TabIndex = 28
		# 
		# Field
		# 
		self._Field.DataPropertyName = "Field"
		self._Field.HeaderText = "Field"
		self._Field.Name = "Field"
		self._Field.ReadOnly = True
		# 
		# dgvGroupDefaults
		# 
		self._dgvGroupDefaults.AllowUserToAddRows = False
		self._dgvGroupDefaults.AllowUserToDeleteRows = False
		self._dgvGroupDefaults.AllowUserToResizeRows = False
		self._dgvGroupDefaults.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._dgvGroupDefaults.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill
		self._dgvGroupDefaults.BackgroundColor = System.Drawing.SystemColors.Window
		self._dgvGroupDefaults.Columns.AddRange(System.Array[System.Windows.Forms.DataGridViewColumn](
			[self._dataGridViewTextBoxColumn1]))
		self._dgvGroupDefaults.Location = System.Drawing.Point(8, 263)
		self._dgvGroupDefaults.MultiSelect = False
		self._dgvGroupDefaults.Name = "dgvGroupDefaults"
		self._dgvGroupDefaults.ReadOnly = True
		self._dgvGroupDefaults.RowHeadersVisible = False
		self._dgvGroupDefaults.RowHeadersWidth = 25
		self._dgvGroupDefaults.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect
		self._dgvGroupDefaults.Size = System.Drawing.Size(635, 135)
		self._dgvGroupDefaults.TabIndex = 35
		# 
		# dataGridViewTextBoxColumn1
		# 
		self._dataGridViewTextBoxColumn1.DataPropertyName = "Field"
		self._dataGridViewTextBoxColumn1.HeaderText = "Field"
		self._dataGridViewTextBoxColumn1.Name = "dataGridViewTextBoxColumn1"
		self._dataGridViewTextBoxColumn1.ReadOnly = True
		# 
		# btnGroupDefaultAdd
		# 
		self._btnGroupDefaultAdd.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupDefaultAdd.ImageIndex = 17
		self._btnGroupDefaultAdd.Location = System.Drawing.Point(338, 437)
		self._btnGroupDefaultAdd.Name = "btnGroupDefaultAdd"
		self._btnGroupDefaultAdd.Size = System.Drawing.Size(104, 23)
		self._btnGroupDefaultAdd.TabIndex = 40
		self._btnGroupDefaultAdd.Text = "Add"
		self._btnGroupDefaultAdd.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnGroupDefaultAdd.UseVisualStyleBackColor = True
		# 
		# label21
		# 
		self._label21.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self._label21.AutoSize = True
		self._label21.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label21.Location = System.Drawing.Point(461, 11)
		self._label21.Name = "label21"
		self._label21.Size = System.Drawing.Size(68, 13)
		self._label21.TabIndex = 25
		self._label21.Text = "Rule Mode"
		# 
		# label22
		# 
		self._label22.AutoSize = True
		self._label22.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label22.Location = System.Drawing.Point(10, 12)
		self._label22.Name = "label22"
		self._label22.Size = System.Drawing.Size(77, 13)
		self._label22.TabIndex = 26
		self._label22.Text = "Group Rules"
		# 
		# btnGroupDefaultClear
		# 
		self._btnGroupDefaultClear.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupDefaultClear.ImageIndex = 7
		self._btnGroupDefaultClear.Location = System.Drawing.Point(546, 437)
		self._btnGroupDefaultClear.Name = "btnGroupDefaultClear"
		self._btnGroupDefaultClear.Size = System.Drawing.Size(104, 23)
		self._btnGroupDefaultClear.TabIndex = 42
		self._btnGroupDefaultClear.Text = "Clear Actions"
		self._btnGroupDefaultClear.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnGroupDefaultClear.UseVisualStyleBackColor = True
		# 
		# pictureBox4
		# 
		self._pictureBox4.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._pictureBox4.BackColor = System.Drawing.Color.Black
		self._pictureBox4.Location = System.Drawing.Point(103, 249)
		self._pictureBox4.Name = "pictureBox4"
		self._pictureBox4.Size = System.Drawing.Size(560, 1)
		self._pictureBox4.TabIndex = 27
		self._pictureBox4.TabStop = False
		# 
		# label23
		# 
		self._label23.AutoSize = True
		self._label23.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label23.Location = System.Drawing.Point(12, 242)
		self._label23.Name = "label23"
		self._label23.Size = System.Drawing.Size(87, 13)
		self._label23.TabIndex = 34
		self._label23.Text = "Group Actions"
		# 
		# btnGroupDefaultUpdate
		# 
		self._btnGroupDefaultUpdate.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupDefaultUpdate.ImageIndex = 15
		self._btnGroupDefaultUpdate.Location = System.Drawing.Point(234, 437)
		self._btnGroupDefaultUpdate.Name = "btnGroupDefaultUpdate"
		self._btnGroupDefaultUpdate.Size = System.Drawing.Size(104, 23)
		self._btnGroupDefaultUpdate.TabIndex = 39
		self._btnGroupDefaultUpdate.Text = "Update"
		self._btnGroupDefaultUpdate.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnGroupDefaultUpdate.UseVisualStyleBackColor = True
		# 
		# btnGroupDefaultRemove
		# 
		self._btnGroupDefaultRemove.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnGroupDefaultRemove.ImageIndex = 18
		self._btnGroupDefaultRemove.Location = System.Drawing.Point(442, 437)
		self._btnGroupDefaultRemove.Name = "btnGroupDefaultRemove"
		self._btnGroupDefaultRemove.Size = System.Drawing.Size(104, 23)
		self._btnGroupDefaultRemove.TabIndex = 41
		self._btnGroupDefaultRemove.Text = "Remove"
		self._btnGroupDefaultRemove.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnGroupDefaultRemove.UseVisualStyleBackColor = True
		# 
		# lblGroupOverview
		# 
		self._lblGroupOverview.AutoSize = True
		self._lblGroupOverview.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lblGroupOverview.Location = System.Drawing.Point(13, 9)
		self._lblGroupOverview.Name = "lblGroupOverview"
		self._lblGroupOverview.Size = System.Drawing.Size(268, 39)
		self._lblGroupOverview.TabIndex = 6
		self._lblGroupOverview.Text = "Group Overview"
		self._lblGroupOverview.UseMnemonic = False
		# 
		# commentLabel
		# 
		self._commentLabel.AutoSize = True
		self._commentLabel.Location = System.Drawing.Point(7, 89)
		self._commentLabel.Name = "commentLabel"
		self._commentLabel.Size = System.Drawing.Size(54, 13)
		self._commentLabel.TabIndex = 2
		self._commentLabel.Text = "Comment:"
		self._commentLabel.UseMnemonic = False
		# 
		# txtGroupComment
		# 
		self._txtGroupComment.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._txtGroupComment.Location = System.Drawing.Point(67, 86)
		self._txtGroupComment.Name = "txtGroupComment"
		self._txtGroupComment.Size = System.Drawing.Size(587, 20)
		self._txtGroupComment.TabIndex = 3
		# 
		# nameLabel
		# 
		self._nameLabel.AutoSize = True
		self._nameLabel.Location = System.Drawing.Point(7, 63)
		self._nameLabel.Name = "nameLabel"
		self._nameLabel.Size = System.Drawing.Size(38, 13)
		self._nameLabel.TabIndex = 0
		self._nameLabel.Text = "Name:"
		self._nameLabel.UseMnemonic = False
		# 
		# txtGroupName
		# 
		self._txtGroupName.Location = System.Drawing.Point(67, 60)
		self._txtGroupName.Name = "txtGroupName"
		self._txtGroupName.Size = System.Drawing.Size(248, 20)
		self._txtGroupName.TabIndex = 1
		# 
		# pnlGeneral
		# 
		self._pnlGeneral.Controls.Add(self._btnCollectionRulesetMoveDown)
		self._pnlGeneral.Controls.Add(self._btnCollectionRulesetMoveUp)
		self._pnlGeneral.Controls.Add(self._btnCollectionGroupMoveDown)
		self._pnlGeneral.Controls.Add(self._btnCollectionGroupMoveUp)
		self._pnlGeneral.Controls.Add(self._label20)
		self._pnlGeneral.Controls.Add(self._label4)
		self._pnlGeneral.Controls.Add(self._label18)
		self._pnlGeneral.Controls.Add(self._txtCollectionNotes)
		self._pnlGeneral.Controls.Add(self._textBox2)
		self._pnlGeneral.Controls.Add(self._txtCollectionAuthor)
		self._pnlGeneral.Controls.Add(self._label17)
		self._pnlGeneral.Controls.Add(self._label14)
		self._pnlGeneral.Controls.Add(self._label15)
		self._pnlGeneral.Controls.Add(self._label16)
		self._pnlGeneral.Controls.Add(self._btnCollectionRulesetAdd)
		self._pnlGeneral.Controls.Add(self._btnCollectionGroupAdd)
		self._pnlGeneral.Controls.Add(self._dgvCollectionRulesets)
		self._pnlGeneral.Controls.Add(self._btnCollectionRulesetsRemove)
		self._pnlGeneral.Controls.Add(self._dgvCollectionGroups)
		self._pnlGeneral.Controls.Add(self._btnCollectionGroupRemove)
		self._pnlGeneral.Dock = System.Windows.Forms.DockStyle.Fill
		self._pnlGeneral.Location = System.Drawing.Point(0, 0)
		self._pnlGeneral.Name = "pnlGeneral"
		self._pnlGeneral.Size = System.Drawing.Size(688, 633)
		self._pnlGeneral.TabIndex = 2
		self._pnlGeneral.Visible = False
		# 
		# btnCollectionRulesetMoveDown
		# 
		self._btnCollectionRulesetMoveDown.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnCollectionRulesetMoveDown.Enabled = False
		self._btnCollectionRulesetMoveDown.ImageIndex = 13
		self._btnCollectionRulesetMoveDown.Location = System.Drawing.Point(650, 421)
		self._btnCollectionRulesetMoveDown.Name = "btnCollectionRulesetMoveDown"
		self._btnCollectionRulesetMoveDown.Size = System.Drawing.Size(25, 25)
		self._btnCollectionRulesetMoveDown.TabIndex = 10
		self._btnCollectionRulesetMoveDown.UseVisualStyleBackColor = True
		# 
		# btnCollectionRulesetMoveUp
		# 
		self._btnCollectionRulesetMoveUp.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnCollectionRulesetMoveUp.Enabled = False
		self._btnCollectionRulesetMoveUp.ImageIndex = 12
		self._btnCollectionRulesetMoveUp.Location = System.Drawing.Point(650, 395)
		self._btnCollectionRulesetMoveUp.Name = "btnCollectionRulesetMoveUp"
		self._btnCollectionRulesetMoveUp.Size = System.Drawing.Size(25, 25)
		self._btnCollectionRulesetMoveUp.TabIndex = 9
		self._btnCollectionRulesetMoveUp.UseVisualStyleBackColor = True
		# 
		# btnCollectionGroupMoveDown
		# 
		self._btnCollectionGroupMoveDown.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnCollectionGroupMoveDown.Enabled = False
		self._btnCollectionGroupMoveDown.ImageIndex = 13
		self._btnCollectionGroupMoveDown.Location = System.Drawing.Point(650, 231)
		self._btnCollectionGroupMoveDown.Name = "btnCollectionGroupMoveDown"
		self._btnCollectionGroupMoveDown.Size = System.Drawing.Size(25, 25)
		self._btnCollectionGroupMoveDown.TabIndex = 4
		self._btnCollectionGroupMoveDown.UseVisualStyleBackColor = True
		# 
		# btnCollectionGroupMoveUp
		# 
		self._btnCollectionGroupMoveUp.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnCollectionGroupMoveUp.Enabled = False
		self._btnCollectionGroupMoveUp.ImageIndex = 12
		self._btnCollectionGroupMoveUp.Location = System.Drawing.Point(650, 205)
		self._btnCollectionGroupMoveUp.Name = "btnCollectionGroupMoveUp"
		self._btnCollectionGroupMoveUp.Size = System.Drawing.Size(25, 25)
		self._btnCollectionGroupMoveUp.TabIndex = 3
		self._btnCollectionGroupMoveUp.UseVisualStyleBackColor = True
		# 
		# label20
		# 
		self._label20.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left
		self._label20.AutoSize = True
		self._label20.Location = System.Drawing.Point(20, 530)
		self._label20.Name = "label20"
		self._label20.Size = System.Drawing.Size(35, 13)
		self._label20.TabIndex = 15
		self._label20.Text = "Notes"
		# 
		# label4
		# 
		self._label4.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left
		self._label4.AutoSize = True
		self._label4.Location = System.Drawing.Point(479, 502)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 13)
		self._label4.TabIndex = 10
		self._label4.Text = "Compatible Version:"
		# 
		# label18
		# 
		self._label18.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left
		self._label18.AutoSize = True
		self._label18.Location = System.Drawing.Point(20, 499)
		self._label18.Name = "label18"
		self._label18.Size = System.Drawing.Size(35, 13)
		self._label18.TabIndex = 10
		self._label18.Text = "Name"
		# 
		# txtCollectionNotes
		# 
		self._txtCollectionNotes.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._txtCollectionNotes.Location = System.Drawing.Point(67, 530)
		self._txtCollectionNotes.Multiline = True
		self._txtCollectionNotes.Name = "txtCollectionNotes"
		self._txtCollectionNotes.Size = System.Drawing.Size(612, 96)
		self._txtCollectionNotes.TabIndex = 16
		# 
		# textBox2
		# 
		self._textBox2.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left
		self._textBox2.Location = System.Drawing.Point(585, 499)
		self._textBox2.Name = "textBox2"
		self._textBox2.ReadOnly = True
		self._textBox2.Size = System.Drawing.Size(93, 20)
		self._textBox2.TabIndex = 14
		# 
		# txtCollectionAuthor
		# 
		self._txtCollectionAuthor.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left
		self._txtCollectionAuthor.Location = System.Drawing.Point(67, 495)
		self._txtCollectionAuthor.Name = "txtCollectionAuthor"
		self._txtCollectionAuthor.Size = System.Drawing.Size(162, 20)
		self._txtCollectionAuthor.TabIndex = 14
		# 
		# label17
		# 
		self._label17.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left
		self._label17.AutoSize = True
		self._label17.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label17.Location = System.Drawing.Point(7, 475)
		self._label17.Name = "label17"
		self._label17.Size = System.Drawing.Size(70, 16)
		self._label17.TabIndex = 13
		self._label17.Text = "Author Info"
		# 
		# label14
		# 
		self._label14.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left
		self._label14.AutoSize = True
		self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.Location = System.Drawing.Point(18, 295)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(199, 16)
		self._label14.TabIndex = 7
		self._label14.Text = "Orphaned Rulesets In Collection"
		# 
		# label15
		# 
		self._label15.AutoSize = True
		self._label15.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label15.Location = System.Drawing.Point(14, 62)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(127, 16)
		self._label15.TabIndex = 1
		self._label15.Text = "Groups In Collection"
		# 
		# label16
		# 
		self._label16.AutoSize = True
		self._label16.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label16.Location = System.Drawing.Point(13, 9)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(452, 39)
		self._label16.TabIndex = 0
		self._label16.Text = "Ruleset Collection Overview"
		# 
		# btnCollectionRulesetAdd
		# 
		self._btnCollectionRulesetAdd.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnCollectionRulesetAdd.ImageIndex = 17
		self._btnCollectionRulesetAdd.Location = System.Drawing.Point(484, 452)
		self._btnCollectionRulesetAdd.Name = "btnCollectionRulesetAdd"
		self._btnCollectionRulesetAdd.Size = System.Drawing.Size(79, 23)
		self._btnCollectionRulesetAdd.TabIndex = 11
		self._btnCollectionRulesetAdd.Text = "Add"
		self._btnCollectionRulesetAdd.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnCollectionRulesetAdd.UseVisualStyleBackColor = True
		# 
		# btnCollectionGroupAdd
		# 
		self._btnCollectionGroupAdd.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnCollectionGroupAdd.ImageIndex = 17
		self._btnCollectionGroupAdd.Location = System.Drawing.Point(484, 262)
		self._btnCollectionGroupAdd.Name = "btnCollectionGroupAdd"
		self._btnCollectionGroupAdd.Size = System.Drawing.Size(79, 23)
		self._btnCollectionGroupAdd.TabIndex = 5
		self._btnCollectionGroupAdd.Text = "Add"
		self._btnCollectionGroupAdd.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnCollectionGroupAdd.UseVisualStyleBackColor = True
		# 
		# dgvCollectionRulesets
		# 
		self._dgvCollectionRulesets.AllowUserToAddRows = False
		self._dgvCollectionRulesets.AllowUserToDeleteRows = False
		self._dgvCollectionRulesets.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._dgvCollectionRulesets.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill
		self._dgvCollectionRulesets.BackgroundColor = System.Drawing.SystemColors.Window
		self._dgvCollectionRulesets.ClipboardCopyMode = System.Windows.Forms.DataGridViewClipboardCopyMode.Disable
		self._dgvCollectionRulesets.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
		self._dgvCollectionRulesets.Location = System.Drawing.Point(14, 317)
		self._dgvCollectionRulesets.MultiSelect = False
		self._dgvCollectionRulesets.Name = "dgvCollectionRulesets"
		self._dgvCollectionRulesets.RowHeadersWidth = 25
		self._dgvCollectionRulesets.RowHeadersWidthSizeMode = System.Windows.Forms.DataGridViewRowHeadersWidthSizeMode.DisableResizing
		self._dgvCollectionRulesets.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect
		self._dgvCollectionRulesets.Size = System.Drawing.Size(630, 129)
		self._dgvCollectionRulesets.TabIndex = 8
		self._dgvCollectionRulesets.TabStop = False
		# 
		# btnCollectionRulesetsRemove
		# 
		self._btnCollectionRulesetsRemove.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnCollectionRulesetsRemove.Enabled = False
		self._btnCollectionRulesetsRemove.ImageIndex = 18
		self._btnCollectionRulesetsRemove.Location = System.Drawing.Point(565, 452)
		self._btnCollectionRulesetsRemove.Name = "btnCollectionRulesetsRemove"
		self._btnCollectionRulesetsRemove.Size = System.Drawing.Size(79, 23)
		self._btnCollectionRulesetsRemove.TabIndex = 12
		self._btnCollectionRulesetsRemove.Text = "Remove"
		self._btnCollectionRulesetsRemove.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnCollectionRulesetsRemove.UseVisualStyleBackColor = True
		# 
		# dgvCollectionGroups
		# 
		self._dgvCollectionGroups.AllowUserToAddRows = False
		self._dgvCollectionGroups.AllowUserToDeleteRows = False
		self._dgvCollectionGroups.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._dgvCollectionGroups.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill
		self._dgvCollectionGroups.BackgroundColor = System.Drawing.SystemColors.Window
		self._dgvCollectionGroups.ClipboardCopyMode = System.Windows.Forms.DataGridViewClipboardCopyMode.Disable
		self._dgvCollectionGroups.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
		self._dgvCollectionGroups.Location = System.Drawing.Point(11, 83)
		self._dgvCollectionGroups.MultiSelect = False
		self._dgvCollectionGroups.Name = "dgvCollectionGroups"
		self._dgvCollectionGroups.RowHeadersWidth = 25
		self._dgvCollectionGroups.RowHeadersWidthSizeMode = System.Windows.Forms.DataGridViewRowHeadersWidthSizeMode.DisableResizing
		self._dgvCollectionGroups.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect
		self._dgvCollectionGroups.Size = System.Drawing.Size(633, 173)
		self._dgvCollectionGroups.TabIndex = 2
		self._dgvCollectionGroups.TabStop = False
		# 
		# btnCollectionGroupRemove
		# 
		self._btnCollectionGroupRemove.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnCollectionGroupRemove.Enabled = False
		self._btnCollectionGroupRemove.ImageIndex = 18
		self._btnCollectionGroupRemove.Location = System.Drawing.Point(565, 262)
		self._btnCollectionGroupRemove.Name = "btnCollectionGroupRemove"
		self._btnCollectionGroupRemove.Size = System.Drawing.Size(79, 23)
		self._btnCollectionGroupRemove.TabIndex = 6
		self._btnCollectionGroupRemove.Text = "Remove"
		self._btnCollectionGroupRemove.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnCollectionGroupRemove.UseVisualStyleBackColor = True
		# 
		# tabTemplateManager
		# 
		self._tabTemplateManager.Controls.Add(self._txtTemplateAdd)
		self._tabTemplateManager.Controls.Add(self._btnTemplatesRuleActionAdd)
		self._tabTemplateManager.Controls.Add(self._btnTemplatesClear)
		self._tabTemplateManager.Controls.Add(self._btnTemplateRename)
		self._tabTemplateManager.Controls.Add(self._btnTemplateAdd)
		self._tabTemplateManager.Controls.Add(self._btnTemplatesRemoveTemplate)
		self._tabTemplateManager.Controls.Add(self._btnTemplatesRuleActionClear)
		self._tabTemplateManager.Controls.Add(self._btnTemplatesRuleActionUpdate)
		self._tabTemplateManager.Controls.Add(self._btnTemplatesRuleActionRemove)
		self._tabTemplateManager.Controls.Add(self._dataGridView1)
		self._tabTemplateManager.Controls.Add(self._cmbTemplates)
		self._tabTemplateManager.Controls.Add(self._listBox1)
		self._tabTemplateManager.Location = System.Drawing.Point(4, 22)
		self._tabTemplateManager.Name = "tabTemplateManager"
		self._tabTemplateManager.Padding = System.Windows.Forms.Padding(3)
		self._tabTemplateManager.Size = System.Drawing.Size(914, 635)
		self._tabTemplateManager.TabIndex = 2
		self._tabTemplateManager.Text = "Template Manager"
		self._tabTemplateManager.UseVisualStyleBackColor = True
		# 
		# txtTemplateAdd
		# 
		self._txtTemplateAdd.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left
		self._txtTemplateAdd.Location = System.Drawing.Point(11, 582)
		self._txtTemplateAdd.Name = "txtTemplateAdd"
		self._txtTemplateAdd.Size = System.Drawing.Size(136, 20)
		self._txtTemplateAdd.TabIndex = 43
		# 
		# btnTemplatesRuleActionAdd
		# 
		self._btnTemplatesRuleActionAdd.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnTemplatesRuleActionAdd.ImageIndex = 17
		self._btnTemplatesRuleActionAdd.Location = System.Drawing.Point(642, 582)
		self._btnTemplatesRuleActionAdd.Name = "btnTemplatesRuleActionAdd"
		self._btnTemplatesRuleActionAdd.Size = System.Drawing.Size(88, 23)
		self._btnTemplatesRuleActionAdd.TabIndex = 40
		self._btnTemplatesRuleActionAdd.Text = "Add"
		self._btnTemplatesRuleActionAdd.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnTemplatesRuleActionAdd.UseVisualStyleBackColor = True
		# 
		# btnTemplatesClear
		# 
		self._btnTemplatesClear.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left
		self._btnTemplatesClear.ImageIndex = 7
		self._btnTemplatesClear.Location = System.Drawing.Point(107, 552)
		self._btnTemplatesClear.Name = "btnTemplatesClear"
		self._btnTemplatesClear.Size = System.Drawing.Size(92, 23)
		self._btnTemplatesClear.TabIndex = 37
		self._btnTemplatesClear.Text = "Clear"
		self._btnTemplatesClear.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnTemplatesClear.UseVisualStyleBackColor = True
		# 
		# btnTemplateRename
		# 
		self._btnTemplateRename.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left
		self._btnTemplateRename.Enabled = False
		self._btnTemplateRename.ImageIndex = 15
		self._btnTemplateRename.Location = System.Drawing.Point(176, 581)
		self._btnTemplateRename.Name = "btnTemplateRename"
		self._btnTemplateRename.Size = System.Drawing.Size(23, 23)
		self._btnTemplateRename.TabIndex = 38
		self._btnTemplateRename.UseVisualStyleBackColor = True
		# 
		# btnTemplateAdd
		# 
		self._btnTemplateAdd.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left
		self._btnTemplateAdd.Enabled = False
		self._btnTemplateAdd.ImageIndex = 17
		self._btnTemplateAdd.Location = System.Drawing.Point(153, 581)
		self._btnTemplateAdd.Name = "btnTemplateAdd"
		self._btnTemplateAdd.Size = System.Drawing.Size(23, 23)
		self._btnTemplateAdd.TabIndex = 38
		self._btnTemplateAdd.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnTemplateAdd.UseVisualStyleBackColor = True
		# 
		# btnTemplatesRemoveTemplate
		# 
		self._btnTemplatesRemoveTemplate.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left
		self._btnTemplatesRemoveTemplate.ImageIndex = 18
		self._btnTemplatesRemoveTemplate.Location = System.Drawing.Point(11, 552)
		self._btnTemplatesRemoveTemplate.Name = "btnTemplatesRemoveTemplate"
		self._btnTemplatesRemoveTemplate.Size = System.Drawing.Size(92, 23)
		self._btnTemplatesRemoveTemplate.TabIndex = 36
		self._btnTemplatesRemoveTemplate.Text = "Remove"
		self._btnTemplatesRemoveTemplate.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnTemplatesRemoveTemplate.UseVisualStyleBackColor = True
		# 
		# btnTemplatesRuleActionClear
		# 
		self._btnTemplatesRuleActionClear.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnTemplatesRuleActionClear.Enabled = False
		self._btnTemplatesRuleActionClear.ImageIndex = 7
		self._btnTemplatesRuleActionClear.Location = System.Drawing.Point(818, 582)
		self._btnTemplatesRuleActionClear.Name = "btnTemplatesRuleActionClear"
		self._btnTemplatesRuleActionClear.Size = System.Drawing.Size(88, 23)
		self._btnTemplatesRuleActionClear.TabIndex = 35
		self._btnTemplatesRuleActionClear.Text = "Clear"
		self._btnTemplatesRuleActionClear.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnTemplatesRuleActionClear.UseVisualStyleBackColor = True
		# 
		# btnTemplatesRuleActionUpdate
		# 
		self._btnTemplatesRuleActionUpdate.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnTemplatesRuleActionUpdate.Enabled = False
		self._btnTemplatesRuleActionUpdate.ImageIndex = 15
		self._btnTemplatesRuleActionUpdate.Location = System.Drawing.Point(554, 582)
		self._btnTemplatesRuleActionUpdate.Name = "btnTemplatesRuleActionUpdate"
		self._btnTemplatesRuleActionUpdate.Size = System.Drawing.Size(88, 23)
		self._btnTemplatesRuleActionUpdate.TabIndex = 39
		self._btnTemplatesRuleActionUpdate.Text = "Update"
		self._btnTemplatesRuleActionUpdate.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnTemplatesRuleActionUpdate.UseVisualStyleBackColor = True
		# 
		# btnTemplatesRuleActionRemove
		# 
		self._btnTemplatesRuleActionRemove.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right
		self._btnTemplatesRuleActionRemove.Enabled = False
		self._btnTemplatesRuleActionRemove.ImageIndex = 18
		self._btnTemplatesRuleActionRemove.Location = System.Drawing.Point(730, 582)
		self._btnTemplatesRuleActionRemove.Name = "btnTemplatesRuleActionRemove"
		self._btnTemplatesRuleActionRemove.Size = System.Drawing.Size(88, 23)
		self._btnTemplatesRuleActionRemove.TabIndex = 33
		self._btnTemplatesRuleActionRemove.Text = "Remove"
		self._btnTemplatesRuleActionRemove.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText
		self._btnTemplatesRuleActionRemove.UseVisualStyleBackColor = True
		# 
		# dataGridView1
		# 
		self._dataGridView1.AllowUserToAddRows = False
		self._dataGridView1.AllowUserToDeleteRows = False
		self._dataGridView1.AllowUserToResizeRows = False
		self._dataGridView1.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self._dataGridView1.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill
		self._dataGridView1.BackgroundColor = System.Drawing.SystemColors.Window
		self._dataGridView1.Location = System.Drawing.Point(205, 33)
		self._dataGridView1.MultiSelect = False
		self._dataGridView1.Name = "dataGridView1"
		self._dataGridView1.ReadOnly = True
		self._dataGridView1.RowHeadersWidth = 25
		self._dataGridView1.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect
		self._dataGridView1.Size = System.Drawing.Size(701, 513)
		self._dataGridView1.TabIndex = 31
		# 
		# cmbTemplates
		# 
		self._cmbTemplates.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._cmbTemplates.FormattingEnabled = True
		self._cmbTemplates.Items.AddRange(System.Array[System.Object](
			["Action Templates",
			"Rule Templates"]))
		self._cmbTemplates.Location = System.Drawing.Point(11, 6)
		self._cmbTemplates.Name = "cmbTemplates"
		self._cmbTemplates.Size = System.Drawing.Size(188, 21)
		self._cmbTemplates.TabIndex = 30
		# 
		# listBox1
		# 
		self._listBox1.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left
		self._listBox1.DisplayMember = "Name"
		self._listBox1.FormattingEnabled = True
		self._listBox1.IntegralHeight = False
		self._listBox1.Location = System.Drawing.Point(11, 33)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(188, 513)
		self._listBox1.TabIndex = 29
		# 
		# tabSearch
		# 
		self._tabSearch.Controls.Add(self._toolStripContainer2)
		self._tabSearch.Location = System.Drawing.Point(4, 22)
		self._tabSearch.Name = "tabSearch"
		self._tabSearch.Padding = System.Windows.Forms.Padding(3)
		self._tabSearch.Size = System.Drawing.Size(914, 635)
		self._tabSearch.TabIndex = 1
		self._tabSearch.Text = "Search"
		self._tabSearch.UseVisualStyleBackColor = True
		# 
		# toolStripContainer2
		# 
		# 
		# toolStripContainer2.ContentPanel
		# 
		self._toolStripContainer2.ContentPanel.Controls.Add(self._dataGridView3)
		self._toolStripContainer2.ContentPanel.Controls.Add(self._label6)
		self._toolStripContainer2.ContentPanel.Size = System.Drawing.Size(908, 604)
		self._toolStripContainer2.Dock = System.Windows.Forms.DockStyle.Fill
		self._toolStripContainer2.Location = System.Drawing.Point(3, 3)
		self._toolStripContainer2.Name = "toolStripContainer2"
		self._toolStripContainer2.Size = System.Drawing.Size(908, 629)
		self._toolStripContainer2.TabIndex = 1
		self._toolStripContainer2.Text = "toolStripContainer2"
		# 
		# toolStripContainer2.TopToolStripPanel
		# 
		self._toolStripContainer2.TopToolStripPanel.Controls.Add(self._tsSearch)
		# 
		# dataGridView3
		# 
		self._dataGridView3.AllowUserToAddRows = False
		self._dataGridView3.AllowUserToDeleteRows = False
		self._dataGridView3.AllowUserToOrderColumns = True
		self._dataGridView3.AllowUserToResizeRows = False
		self._dataGridView3.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill
		self._dataGridView3.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
		self._dataGridView3.Dock = System.Windows.Forms.DockStyle.Fill
		self._dataGridView3.Location = System.Drawing.Point(0, 31)
		self._dataGridView3.Name = "dataGridView3"
		self._dataGridView3.ReadOnly = True
		self._dataGridView3.RowHeadersVisible = False
		self._dataGridView3.Size = System.Drawing.Size(908, 573)
		self._dataGridView3.TabIndex = 4
		# 
		# label6
		# 
		self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label6.Dock = System.Windows.Forms.DockStyle.Top
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(0, 0)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(908, 31)
		self._label6.TabIndex = 3
		self._label6.Text = "Search Results:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# tsSearch
		# 
		self._tsSearch.Dock = System.Windows.Forms.DockStyle.None
		self._tsSearch.GripStyle = System.Windows.Forms.ToolStripGripStyle.Hidden
		self._tsSearch.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._toolStripLabel1,
			self._tscbSearchType,
			self._toolStripSeparator4,
			self._tsLabelSearchField,
			self._tscbSearchField,
			self._tsLabelSearchModifier,
			self._tscbSearchModifier,
			self._tslblSearchValue,
			self._tstbValue,
			self._tsbRunSearch,
			self._toolStripSeparator5]))
		self._tsSearch.Location = System.Drawing.Point(0, 0)
		self._tsSearch.Name = "tsSearch"
		self._tsSearch.Size = System.Drawing.Size(908, 25)
		self._tsSearch.Stretch = True
		self._tsSearch.TabIndex = 0
		# 
		# toolStripLabel1
		# 
		self._toolStripLabel1.Name = "toolStripLabel1"
		self._toolStripLabel1.Size = System.Drawing.Size(82, 22)
		self._toolStripLabel1.Text = "Search Mode: "
		# 
		# tscbSearchType
		# 
		self._tscbSearchType.Items.AddRange(System.Array[System.Object](
			["Rule/Action Parameter Search",
			"Group/Ruleset Name Search",
			"Search All"]))
		self._tscbSearchType.Name = "tscbSearchType"
		self._tscbSearchType.Size = System.Drawing.Size(121, 25)
		# 
		# toolStripSeparator4
		# 
		self._toolStripSeparator4.Name = "toolStripSeparator4"
		self._toolStripSeparator4.Size = System.Drawing.Size(6, 25)
		# 
		# tsLabelSearchField
		# 
		self._tsLabelSearchField.Name = "tsLabelSearchField"
		self._tsLabelSearchField.Size = System.Drawing.Size(32, 22)
		self._tsLabelSearchField.Text = "Field"
		self._tsLabelSearchField.Visible = False
		# 
		# tscbSearchField
		# 
		self._tscbSearchField.Name = "tscbSearchField"
		self._tscbSearchField.Size = System.Drawing.Size(95, 23)
		self._tscbSearchField.Visible = False
		# 
		# tsLabelSearchModifier
		# 
		self._tsLabelSearchModifier.Name = "tsLabelSearchModifier"
		self._tsLabelSearchModifier.Size = System.Drawing.Size(52, 22)
		self._tsLabelSearchModifier.Text = "Modifier"
		self._tsLabelSearchModifier.Visible = False
		# 
		# tscbSearchModifier
		# 
		self._tscbSearchModifier.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._tscbSearchModifier.Name = "tscbSearchModifier"
		self._tscbSearchModifier.Size = System.Drawing.Size(95, 23)
		self._tscbSearchModifier.Visible = False
		# 
		# tslblSearchValue
		# 
		self._tslblSearchValue.Name = "tslblSearchValue"
		self._tslblSearchValue.Size = System.Drawing.Size(36, 22)
		self._tslblSearchValue.Text = "Value"
		# 
		# tstbValue
		# 
		self._tstbValue.Name = "tstbValue"
		self._tstbValue.Size = System.Drawing.Size(95, 25)
		# 
		# tsbRunSearch
		# 
		self._tsbRunSearch.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
		self._tsbRunSearch.Image = resources.GetObject("tsbRunSearch.Image")
		self._tsbRunSearch.ImageTransparentColor = System.Drawing.Color.Magenta
		self._tsbRunSearch.Name = "tsbRunSearch"
		self._tsbRunSearch.Size = System.Drawing.Size(23, 22)
		self._tsbRunSearch.Text = "Search"
		# 
		# toolStripSeparator5
		# 
		self._toolStripSeparator5.Name = "toolStripSeparator5"
		self._toolStripSeparator5.Size = System.Drawing.Size(6, 25)
		# 
		# statusStrip1
		# 
		self._statusStrip1.Location = System.Drawing.Point(0, 668)
		self._statusStrip1.Name = "statusStrip1"
		self._statusStrip1.Size = System.Drawing.Size(922, 22)
		self._statusStrip1.TabIndex = 2
		self._statusStrip1.Text = "statusStrip1"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(922, 690)
		self.Controls.Add(self._statusStrip1)
		self.Controls.Add(self._tabControl1)
		self.Name = "MainForm"
		self.Text = "DataManagerGUI"
		self._tabControl1.ResumeLayout(False)
		self._tabEdit.ResumeLayout(False)
		self._splitContainer1.Panel1.ResumeLayout(False)
		self._splitContainer1.Panel2.ResumeLayout(False)
		self._splitContainer1.EndInit()
		self._splitContainer1.ResumeLayout(False)
		self._toolStripContainer1.BottomToolStripPanel.ResumeLayout(False)
		self._toolStripContainer1.BottomToolStripPanel.PerformLayout()
		self._toolStripContainer1.ContentPanel.ResumeLayout(False)
		self._toolStripContainer1.ResumeLayout(False)
		self._toolStripContainer1.PerformLayout()
		self._toolStrip1.ResumeLayout(False)
		self._toolStrip1.PerformLayout()
		self._pnlRulesets.ResumeLayout(False)
		self._pnlRulesets.PerformLayout()
		self._pictureBox2.EndInit()
		self._dgvRulesetRules.EndInit()
		self._dgvRulesetActions.EndInit()
		self._pictureBox1.EndInit()
		self._pnlGroups.ResumeLayout(False)
		self._pnlGroups.PerformLayout()
		self._tabGroupTabs.ResumeLayout(False)
		self._tabPage3.ResumeLayout(False)
		self._tabPage3.PerformLayout()
		self._dgvGroupRulesets.EndInit()
		self._dgvGroupGroups.EndInit()
		self._dataGridView5.EndInit()
		self._tabGrpRuleset.ResumeLayout(False)
		self._tabGrpRuleset.PerformLayout()
		self._pictureBox3.EndInit()
		self._dgvGroupFilters.EndInit()
		self._dgvGroupDefaults.EndInit()
		self._pictureBox4.EndInit()
		self._pnlGeneral.ResumeLayout(False)
		self._pnlGeneral.PerformLayout()
		self._dgvCollectionRulesets.EndInit()
		self._dgvCollectionGroups.EndInit()
		self._tabTemplateManager.ResumeLayout(False)
		self._tabTemplateManager.PerformLayout()
		self._dataGridView1.EndInit()
		self._tabSearch.ResumeLayout(False)
		self._toolStripContainer2.ContentPanel.ResumeLayout(False)
		self._toolStripContainer2.TopToolStripPanel.ResumeLayout(False)
		self._toolStripContainer2.TopToolStripPanel.PerformLayout()
		self._toolStripContainer2.ResumeLayout(False)
		self._toolStripContainer2.PerformLayout()
		self._dataGridView3.EndInit()
		self._tsSearch.ResumeLayout(False)
		self._tsSearch.PerformLayout()
		self.ResumeLayout(False)
		self.PerformLayout()

