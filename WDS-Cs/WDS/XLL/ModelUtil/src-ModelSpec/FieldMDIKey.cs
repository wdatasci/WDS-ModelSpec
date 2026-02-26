/* Java >>> *
package com.WDataSci.JniPMML;

import com.WDataSci.WDS.Util;
/* <<< Java */
/* C# >>> */
using System;

using static WDS.JavaXCs;

namespace WDS.ModelSpec
{
/* <<< C# */

public interface FieldMDIKey<T>
{
    //Java public 
    T MappedKey();
    //Java public 
    Boolean hasMapKey();
    //Java public 
    void MapToMapKey(T arg)
        //throws com.WDataSci.WDS.WDSException
        ;
}

/* C# >>> */
}
/* <<< C# */
