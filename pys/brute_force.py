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
  for ch in subject:
    if ch == '\n':
      pass

    if ch in ['C','G','T','A']:
      if ch == pattern[j]:
        j = j + 1
      else:
        j = 0
    if j == n:
      return 1

  return -1


file = open('data/genome.dat','rb')
subject = file.read()
pattern = 'ATGTATATATATATATATAATATATATATATATATATATATATATATA'

from ctypes import cdll
bom_lib = cdll.LoadLibrary("brute_force.so")
bom_lib.BF(pattern,len(pattern),subject,len(subject))

#print brute_force(pattern,subject)


