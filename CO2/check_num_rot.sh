#!/bin/bash
#generates configs
for((i=0;i<=500;i++))
do
        org=`echo "2.2 + $i*0.05" | bc -l`
        echo $org
        cd r_$org
        num=`cat en_$org.dat | wc -l`
	echo $num
	if [ $num -ne 400000 ]
	then
		echo $org
		#running the job again
		#sed "s/_DIST_/$org/g" ../rotate.inp > rotate_at_grid.inp
		#rm en*
		#qsub sub.sh
	fi
        cd ../
done
