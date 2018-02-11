#!/bin/sh
#SBATCH --job-name=pi4py-p
#SBATCH --ntasks=24
#SBATCH --cpus-per-task=1
#SBATCH --time=00:15:00

mpirun -np "$SLURM_NTASKS" ./pi4py-p.py "$@"
