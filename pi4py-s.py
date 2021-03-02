#!/usr/bin/env python


# Copyright (C) 2017 Bibliotheca Alexandrina <http://www.bibalex.org/>

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

# This is the serial implementation.  See pi4py-p.py for the parallel
# implementation based on MPI.

# This code was initially adapted from this guide [3] published on the
# University of Oregon's Department of Physics on the Advanced Projects
# Lab's wiki.

# [1] https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
# [2] https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz
# [3] http://hank.uoregon.edu/wiki/index.php/Serial_and_Parallel_Pi_Calculation


from __future__ import division
import sys
import time
from decimal import *
getcontext().prec = 50

def approxipi(n):
  pi = 0
  for i in range(n+1):
    sign = 1 if i % 2 == 0 else -1
    pi += Decimal(sign * 2 * 3 ** (.5-i)) / Decimal(2 * i + 1)
  return pi

def main():
  n = 100000 if len(sys.argv) == 1 else int(sys.argv[1])
  pi = approxipi(n)
  print("pi = {}, terms = {}".format(pi, n))

if __name__ == '__main__':
  main()
