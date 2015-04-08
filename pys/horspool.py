#!/usr/bin/python

def build_mismatch_table(pattern):
  print "Build mismatch table starts"
  table={}
  m = len(pattern)
  table[-1] = m
  for j in range(m-1):
    table[pattern[j]] = m -1 -j  
  print "Build mismatch table ends"
  return table    

def lookup_shift_table(table,ch):
  if table.get(ch,-1) == -1:
    return table[-1]
  return table[ch]

def horspool(subject,pattern):
  table = build_mismatch_table(pattern)
  m = len(pattern)
  n = len(subject)
  i = m - 1
  while i <= n-1:
    k = 0
    while k <= m -1 and pattern[m-1-k] == subject[i-k]:
      k = k + 1
    if k == m:
      return i-m+1
    else:
      i = i + lookup_shift_table(table,subject[i])
  return -1

def horspool_test(subject,pattern):
  table = build_mismatch_table("ATGTA")
  print table
  print lookup_shift_table(table,'A')
  print lookup_shift_table(table,'C')
  print lookup_shift_table(table,'G')
  print lookup_shift_table(table,'T')


print "File read starts"
file = open('data/genome.dat','rb')
subject = file.read()
print "File read ends"
#pattern = "ATGTATATATATATATATAATATATATATATATATATATATATATATA"
pattern = "ATGTA"

#print horspool(subject,"ATGTATATATATATATATAATATATATATATATATATATATATATATA")

from ctypes import cdll
bom_lib = cdll.LoadLibrary("horspool.so")
bom_lib.HORSPOOL(pattern,len(pattern),subject,len(subject))
