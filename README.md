# pi4py

This code repository contains serial and parallel Python implementations
of the Leibniz formula for approximating the value of pi.

The [Leibniz formula for
pi](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80) is
attributed to [Gottfried Wilhelm Leibniz
(1646-1716)](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz).
The formula goes as follows:

1 - 1/3 + 1/5 - 1/7 + 1/9 - ... = pi/4

Code in this repository was initially adapted from [this
guide](http://hank.uoregon.edu/wiki/index.php/Serial_and_Parallel_Pi_Calculation)
published on the University of Oregon's Department of Physics on the
Advanced Projects Lab's wiki.

This code repository was put together by the High-Performance computing
(HPC) group at the [Bibliotheca Alexandrina](https://www.bibalex.org) to
be used as training material for HPC users.

To run the serial implementation:

```
time ./pi4py-s.py 1000000
```

To run it in parallel via Slurm:

```
sbatch pi4py-p.sh 1000000
```

To watch the job in the queue:

```
watch squeue
```

To check elapsed time after the job finishes:

```
sacct -Xo jobid,jobname,elapsed
```

To run the gpu version via Slurm, 2 arrguments need to be passed, number of terms, and number of GPU threads:

```
sbatch pi4py-g.sh  100000000 10000
```  

In the example above 100000000 is the number of terms and 10000 is the number of GPU threads.
