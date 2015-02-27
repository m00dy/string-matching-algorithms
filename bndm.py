#!/usr/bin/python

"""
j=0;
  while (j <= n-m){
    i=m-1; last=m;
    d = ~0;
    while (i>=0 && d!=0) {
      d &= B[y[j+i]];
      i--;
      if (d != 0){
        if (i >= 0)
          last = i+1;
        else
          OUTPUT(j);
      }
       d <<= 1;
    }
     j += last;
  }
"""


def build_b_table(pattern):
  B={}
  m = len(pattern)
  s=1
  for i in range(m-1,-1,-1):
    B[pattern[i]] = B.get(pattern[i],0) | s
    s <<= 1
  return B

print build_b_table("ATGTA")
