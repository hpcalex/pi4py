#!/usr/bin/env python

n = 100
workers = 10
for x in range(workers):
  print(range(x, n, workers))
