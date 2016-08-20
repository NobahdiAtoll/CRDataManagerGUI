using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml.Linq;

namespace DataManagerGUI
{
    public abstract class dmTemplate : IEquatable<dmTemplate>
    {
        public string Name { get; set; }
        public ParameterType Type { get; private set; }
        public SortableBindingList<DataManagerGUI.dmParameters> Items { get; set; }

        public override string ToString()
        {
            string strReturn = "";
            for (int i = 0; i < Items.Count; i++)
            {
                strReturn += Items[i].Compile();
                if (i < Items.Count - 1) strReturn += ",";
            }
            return strReturn;
        }

        private dmTemplate()
        {
            this.Name = "GenericTemplate";
            this.Items = new SortableBindingList<dmParameters>();
        }

        public dmTemplate(string strParameters, ParameterType itemType)
            : this(itemType)
        {
            Parse(strParameters, itemType);
        }

        public dmTemplate(string strName, ParameterType itemType, string strParameters)
            : this(strParameters, itemType)
        {
            this.Name = strName;
        }

        public dmTemplate(ParameterType itemType)
            : this()
        {
            this.Type = itemType;
        }

        public dmTemplate(string[] strTemplateInfo)
            : this((ParameterType)Enum.Parse(typeof(ParameterType), strTemplateInfo[0]))
        {
            if (strTemplateInfo.Length > 1)
            {
                    Parse(strTemplateInfo[1], this.Type);
            }
        }

        public void Parse(string strTemplate, ParameterType dmParameterType)
        {
            string[] tmpParameters = strTemplate.Split(new string[] { ">>,<<", "<<", ">>" }, StringSplitOptions.RemoveEmptyEntries);
            for (int i = 0; i < tmpParameters.Length; i++)
            {
                DataManagerGUI.dmParameters tmpParameterItem = null;
                switch (dmParameterType)
                { 
                    case ParameterType.Rule:
                        tmpParameterItem = new dmRule(tmpParameters[i]);
                        break;
                    case ParameterType.Action:
                        tmpParameterItem = new dmAction(tmpParameters[i]);
                        break;
                }

                this.Items.Add(tmpParameterItem);
            }
        }

        public void FromXML(XElement xParameters)
        {
            this.Type = (ParameterType)Enum.Parse(typeof(ParameterType), xParameters.Attribute("type").Value, true);
            this.Name = xParameters.Attribute("name").Value;
            foreach (XElement item in xParameters.Elements("item"))
            {
                if (this.Type == ParameterType.Rule)
                    Items.Add(new dmRule(item));
                if (this.Type == ParameterType.Action)
                    Items.Add(new dmAction(item));
            }
        }


        public XElement ToXML(string strElementName)
        {
            XElement xReturn;
            if (this.GetType() == typeof(dmRuleTemplate))
                xReturn = new XElement("RuleTemplate");
            else
                xReturn = new XElement("ActionTemplate");

            xReturn.Add(new XAttribute("name", this.Name));
            xReturn.Add(new XAttribute("type", Enum.GetName(typeof(ParameterType), this.Type).ToLower()));
            
            foreach (dmParameters item in this.Items)
                xReturn.Add(item.ToXML("item"));

            return xReturn;
        }

        public bool Equals(dmTemplate other)
        {
            return this.Type == other.Type && this.Name == other.Name;
        }
    }

    public class dmRuleTemplate : dmTemplate
    {
        public dmRuleTemplate(XElement xParameters)
            : base(ParameterType.Rule)
        {
            FromXML(xParameters);
        }

        public dmRuleTemplate(string strTemplateName, string strCSVList)
            : base(strTemplateName, ParameterType.Rule, strCSVList) { }

        public dmRuleTemplate()
            : base(ParameterType.Rule) { }
    }

    public class dmActionTemplate : dmTemplate
    {
        public dmActionTemplate(XElement xParameters)
            :base(ParameterType.Action)
        {
            FromXML(xParameters);
        }

        public dmActionTemplate(string strTemplateName, string strCSVList)
            : base(strTemplateName, ParameterType.Action, strCSVList) { }

        public dmActionTemplate()
            : base(ParameterType.Action) { }
    }
}
