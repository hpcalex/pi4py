#!/usr/bin/env python


# Copyright (C) 2018 Bibliotheca Alexandrina <http://www.bibalex.org/>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# This program approximates the value of pi using the Leibniz formula.

# The Leibniz formula for pi [1] is attributed to Gottfried Wilhelm
# Leibniz (1646-1716) [2].  The formula goes as follows:

# 1 - 1/3 + 1/5 - 1/7 + 1/9 - ... = pi/4

# This program expects a single argument on th ecommand line: an integer
# >= 1 indicating the number of terms to compute on the series.

# This is the parallel implementation based on MPI.  See pi4py-s.py for
# the serial implementation.

# This code was initially adapted from this guide [3] published on the
# University of Oregon's Department of Physics on the Advanced Projects
# Lab's wiki.

# [1] https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
# [2] https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz
# [3] http://hank.uoregon.edu/wiki/index.php/Serial_and_Parallel_Pi_Calculation

import sys
import numpy
import pycuda.autoinit
import pycuda.driver as drv
from decimal import *
from pycuda.compiler import SourceModule

mod = SourceModule("""
#include <stdio.h>
#include <math.h>

__global__ void cuda_pi4py(int *a, int len, double *ans)
{
  for(int i = 0; i < len; i++)
  {
     int term = *(a + (2 * i));
     float partpi = pow(-1.0, (double)term) / (2 * term + 1);
     ans[0] += partpi;
  }
}
""")

cuda_pi4py = mod.get_function("cuda_pi4py")
n = 100000 if len(sys.argv) < 2 else int(sys.argv[1])
threads = 100 if len(sys.argv) < 3 else int(sys.argv[2])

termsplits = []
ans = numpy.zeros(1, dtype=numpy.float64)

for x in range(threads):
    termsplits.append(range(x, n, threads))

for data in enumerate(termsplits):
    cuda_pi4py(
        drv.In(numpy.asarray(data[1])),
        numpy.int32(len(data[1])),
        drv.Out(ans),
        block=(1, 1, 1))

pi = Decimal(4 * ans[0])
print("pi = {}, terms = {}, number of threads = {}".format(pi, n, threads))
