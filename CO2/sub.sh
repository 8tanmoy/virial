#!/bin/bash
#$ -l h_rt=90:00:00     # Specify the hard time limit for the job
#$ -P cui-buchem        # project name
#$ -N co2-gen         # job name
#$ -e co2-gen.err     # error file name
#$ -j y                 # merge console out and error in same file
#$ -V
#$ -pe omp 1            # request parallel env with 8 cores
# -pe mpi_1_tasks_per_node 1    # mpi_12_tasks_per_node 144 will take 12 nodes

module load intel/2018
#module load openmpi/3.0.0_intel-2018

cd $PWD
/usr3/graduate/tanmoy/packages/c43a1/exec/em64t_M/charmm < rotate_at_grid.inp > rotate_at_grid.out
wait
rm rotate_at_grid.*

