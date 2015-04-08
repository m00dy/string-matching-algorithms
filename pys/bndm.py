#!/usr/bin/python
import platform

def lookup_b_table(table,ch):
  if table.get(ch,-1) == -1:
    return table[-1]
  return table[ch]

def bndm_search(B,x,y):
  m = len(x)
  n = len(y)
  j=0;
  while (j <= n-m):
    i=m-1
    last=m
    d = ~0
    while (i>=0 and d!=0):
      d = d & lookup_b_table(B,y[j+i])
      #d = d & B[y[j+i]];
      i = i - 1
      if (d != 0):
        if (i >= 0):
          last = i+1
        else:
          print j#OUTPUT(j);
      d = d << 1
    j =j+ last


def machine_word_size():
    import sys
    num_bytes = 0
    maxint = sys.maxint
    while maxint > 0:
        maxint = maxint >> 8
        num_bytes += 1
    return num_bytes
#print machine_word_size()

def build_b_table(pattern):
  B={-1:0}
  m = len(pattern)
  s=1
  for i in range(m-1,-1,-1):
    B[pattern[i]] = B.get(pattern[i],0) | s
    s <<= 1
  return B

file = open('data/genome2.dat','rb')

pattern = "ATGTA"
print len(pattern)

B = build_b_table(pattern)
print B
subject = file.read()
bndm_search(B,pattern,subject)
