using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml.Linq;

namespace DataManagerGUI
{
    public abstract class dmNode
    {
        public dmNode Parent { get; set; }
         protected string _name;
        public virtual string Name  {get; set;}
        public virtual string Comment { get; set; }

        public dmNode(dmNode dmnParent)
        {
            Clear();
        }

        public dmNode(dmNode dmnParent, string[] strParameters, int nStartIndex)
        {
            this.Parent = dmnParent;
        }

        public dmNode(dmNode dmnParent, XElement xParameters)
        {
            this.Parent = dmnParent;
            FromXML(xParameters);
        }

        public virtual void FromXML(XElement xParameters)
        {
            if (xParameters.Attribute("name") != null)
                this.Name = xParameters.Attribute("name").Value;
            if (xParameters.Attribute("comment") != null)
            {
                this.Comment = xParameters.Attribute("comment").Value;
            }
        }
        
        public virtual XElement ToXML(string strElementName)
        {
            XElement xReturn = new XElement(strElementName);
            if (!string.IsNullOrEmpty(this.Name))
                xReturn.Add(new XAttribute("name", this.Name));
            if (!string.IsNullOrEmpty(this.Comment))
                xReturn.Add(new XAttribute("comment", this.Comment));

            return xReturn;
        }

        public virtual void Clear()
        {
            this.Name = "";
            this.Comment = "";
        }
    }
}
