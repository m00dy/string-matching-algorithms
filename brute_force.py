#!/usr/bin/python
import sys
import os
import timeit

"""
Instead of mmap, I spared additional swap space to fill 2gb bulk data.
"""

def wrapper(func, *args, **kwargs):
  def wrapped():
    return func(*args, **kwargs)
  return wrapped


def brute_force(pattern,subject):
  j = 0
  for x in subject:
    if x in ['a','c','t','g','A','C','T','G']:
       if x == pattern[j]:
         j=j+1
       else:
         j=0
    if j == len(pattern)-1:
      print "Found"
      return 1
  print "Not Found"
  return -1

if len(sys.argv) < 2:
   print "Not enough arguments"
else:
   pattern = sys.argv[1]
   print "looking for " + pattern
   print "starting to read file"
   file = open('data/genome.dat','rb')
   subject = file.read()
   print "File read ends"
   print "Size of pattern " + str(len(pattern))
   print "Size of subject " + str(len(subject))
   print brute_force(pattern,subject)
   #wrapped = wrapper(brute_force, pattern,subject)
   #print timeit.timeit(wrapped,number=1)

