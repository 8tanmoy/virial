#!/bin/bash
#generates configs
for((i=0;i<=500;i++))
do
	org=`echo "2.2 + $i*0.05" | bc -l`
	echo $org
	mkdir r_$org
	cd r_$org
	cp ../rotate.inp ./
	sed "s/_DIST_/$org/g" rotate.inp > rotate_at_grid.inp
	rm rotate.inp
	cp ../sccdftb.dat ./
	cp ../sub.sh ./
	qsub sub.sh
	#/usr3/graduate/tanmoy/packages/c43a1/exec/em64t_M/charmm < rotate_$org.inp > rotate_$org.out
	#rm rotate_$org.out rotate_$org.inp
	cd ../
done
