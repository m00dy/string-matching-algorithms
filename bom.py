#!/usr/bin/python

def getTransition(x,p,L,c):
  cell={}
  if (p > 0 and x[p - 1] == c):
      return(p - 1)
  else:
    cell = L[p]
    while (cell != None):
      if (x[cell['element']] == c):
        return cell['element']
      else:
        cell = cell['next'];
      return None
  return None

def setTransition(p,q,L):
  cell={}
  cell['elemen'] = q
  cell['next'] = L[p]
  L[p] = cell


def oracle(x, m, T,L):
   S=[]
   x=[]
   S[m] = m + 1
   for i in range(m,-1,-1):
     c = x[i - 1]
     p = S[i]
     q = getTransition(x, p, L, c)
     while p <= m and q == None:
       setTransition(p, i - 1, L)
       p = S[p]
       q = getTransition(x, p, L, c)

     if p == m:
       S[i-1] = m
     else:
       S[i-1] = q
     #S[i - 1] = (p == m + 1 ? m : q)
   p = 0
   while (p <= m):
      T[p] = True
      p = S[p]


def BOM(x,m,y,n):
  T=[]
  L=[]
  oracle(x, m, T, L);
  j = 0
  while (j <= n - m):
    i = m - 1
    p = m
    shift = m
    q = getTransition(x, p, L, y[i + j])
    while i + j >= 0 and q != None:
      p = q
      if (T[p] == TRUE):
        period = shift
        shift = i
      i = i -1
      q = getTransition(x, p, L, y[i + j])

    if (i < 0):
      print j
      shift = period
  j += shift


file = open('data/genome2.dat','rb')
subject = file.read()
pattern = "ATGTA"
BOM(pattern,len(pattern),subject,len(subject))
