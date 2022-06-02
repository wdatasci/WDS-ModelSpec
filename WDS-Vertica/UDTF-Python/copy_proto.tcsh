#!/usr/bin/tcsh 

set target=$1

set srcname=$2

set srcpath=$3


mkdir -p ${target}

cp -ar ${srcpath}/. ${target}


foreach x ( `find ${target} -type f ` )
    set xp=${x:h}
    set xn=${x:t}
    set newn=`echo "${xn}" | sed -e "s/${srcname}/${target}/g"`
    echo ${xp} ${x} ${xn} ${newn}
    /bin/mv ${x} ${xp}/tmp
    cat ${xp}/tmp | sed -e "s/${srcname}/${target}/g" >! ${xp}/${newn}
    /bin/rm ${xp}/tmp
end



