#!/bin/sh
#SBATCH --job-name=pi4py-p
#SBATCH --ntasks=24
#SBATCH --cpus-per-task=1
#SBATCH --time=00:15:00

mpirun -np 24 ./pi4py-p.py "$@"
