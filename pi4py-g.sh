#!/bin/sh
<<<<<<< HEAD
#SBATCH --job-name=pi4py_cuda
=======
#SBATCH --job-name=pi4py-g
>>>>>>> 49bb5ee5367f04116f542d8f90d196f01b40452e
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:15:00

<<<<<<< HEAD
nvprof python pi4py-g.py "$@"
=======
nvprof ./pi4py-g.py "$@"
>>>>>>> 49bb5ee5367f04116f542d8f90d196f01b40452e
