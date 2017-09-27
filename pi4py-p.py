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

# This is the parallel implementation based on MPI.  See pi4py-s.py for
# the serial implementation.

# This code was initially adapted from this guide [3] published on the
# University of Oregon's Department of Physics on the Advanced Projects
# Lab's wiki.

# [1] https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
# [2] https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz
# [3] http://hank.uoregon.edu/wiki/index.php/Serial_and_Parallel_Pi_Calculation


from __future__ import division
import sys
import time
from mpi4py import MPI
from decimal import *
getcontext().prec = 50

def termsum(data):
  sum = 0
  for i in data:
    sign = 1 if i % 2 == 0 else -1
    sum += Decimal(sign * 2 * 3 ** (.5-i)) / Decimal(2 * i + 1)
  return sum

def main():
  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()

  if rank == 0: # head node
    n = 100000 if len(sys.argv) == 1 else int(sys.argv[1])
    size = comm.Get_size()
    workers = size - 1
    termsplits = []

    for x in range(workers):
      termsplits.append(xrange(x, n, workers))

    for y, data in enumerate(termsplits):
      dest = y + 1
      if dest == size:
        pass
      else:
        comm.send(data, dest=dest)

    pi = 0
    for y in range(workers):
      source = y + 1
      partpi = comm.recv(source=source)
      print("Received partial pi approximation from source: {}".format(source))
      pi += partpi
    print("pi = {}, terms = {}, MPI size = {}".format(pi, n, size))
  else:
    data = comm.recv(source=0)
    partpi = termsum(data)
    comm.send(partpi, dest=0)

if __name__ == '__main__':
  main()
