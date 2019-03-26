#!/bin/sh
#SBATCH --job-name=multiprocessing
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=24
#SBATCH --time=00:15:00

./pi4py-m.py "$@"
