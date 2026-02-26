/* Java >>> *
package com.WDataSci.JniPMML;

import WDS.Util;
import org.dmg.pmml.FieldName;

/* <<< Java */
/* C# >>> */

using System;

using WDS;
using FieldName = WDS.ModelSpec.FieldName;

using static WDS.JavaXCs;

namespace WDS.ModelSpec
{
/* <<< C# */


    //Java public class FieldMD extends FieldBaseMD implements XDataFieldKeyInterface<FieldName>
    //C#
    public class FieldMD : FieldBaseMD, FieldMDIKey<FieldName>
    {

        public FieldName MapKey = null;

        public FieldName MappedKey() { return this.MapKey; }

        public String MappedKeyValue() {
            if (this.hasMapKey())
                return this.MapKey.getValue();
            else
                return null;
        }

        public Boolean hasMapKey()
        {
            return (this.MapKey != null);
        }

        public void MapToMapKey(FieldName aFieldName)
        //throws WDS.WDSException
        {
            this.MapKey = new FieldName(new_String(aFieldName.getValue()));
        }

        public FieldMD MapToMapKey(String aFieldStringName)
        {
            this.MapKey = new FieldName(new_String(aFieldStringName));
            return this;
        }

        public FieldMD()
            //C#
            : base()
        {
            //Java super();
        }

        public FieldMD(FieldMD arg)
            //C#
            : base(arg)
        //throws WDS.WDSException, Exception
        {
            //Java super(arg);
            if ( arg.MapKey != null )
                this.MapKey = new FieldName(new_String(arg.MapKey.getValue()));
        }

        /* Java >>> *
        public FieldMD(String Name, int hclass, int hlength, int horder, int hsign)
        throws WDS.WDSException, Exception
        {
            super(Name, hclass, hlength, horder, hsign);
        }
        /* <<< Java */

        public Boolean Equals(FieldMD arg)
        {
            //C#
            if ( !base.Equals(arg) ) return false;
            //Java if ( !super.Equals(arg) ) return false;
            if ( !WDS.Util.MatchingNullity(this.MapKey, arg.MapKey) ) return false;
            if ( this.MapKey != null && !this.MapKey.getValue().equals(arg.MapKey.getValue()) )
                return false;
            return true;
        }

        public void Copy(FieldMD arg)
        //throws WDS.WDSException, Exception
        {
            //C#
            base.Copy(arg);
            //Java super.Copy(arg);
            if ( arg.MapKey == null ) this.MapKey = null;
            else this.MapKey = new FieldName(new_String(arg.MapKey.getValue()));
        }

    }

    /* C# >>> */
}
/* <<< C# */
