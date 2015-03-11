#!/usr/bin/python
import sys
import os
import timeit

"""
Instead of mmap, I spared additional swap space to fill 2gb bulk data.
"""

def brute_force(pattern,subject):
  m = len(subject)
  n = len(pattern)
  j = 0
  for x in subject:
    if x in ['\n','\r'] or ord(x) == 10:
      pass
    if x in ['a','t','g','c','A','T','G','C']:
      if x == pattern[j]:
        j = j + 1
      else:
        j = 0
    if j == n-1:
      return 1
  return -1     

file = open('data/genome.dat','rb')
subject = file.read()
pattern = 'CAAGCAATCCTCCTGCCTCAGCCTCACAAG'

print brute_force(pattern,subject)


