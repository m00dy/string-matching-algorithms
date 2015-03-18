#!/usr/bin/python

"""
int getTransition(char *x, int p, List L[], char c) {
   List cell;
   if (p > 0 && x[p - 1] == c)
      return(p - 1);
   else {
      cell = L[p];
      while (cell != NULL)
         if (x[cell->element] == c)
            return(cell->element);
         else
            cell = cell->next;
      return(UNDEFINED);
   }
}
"""
def getTransition(x,p,L,c):
  cell={}
  if (p > 0 and type(x) == type('') and x[p - 1] == c):
      return(p - 1)
  else:
    cell = L.get(p,None)
    while (cell != None):
      if (type(x) == type('') and x[cell.get('element',None)] == c):
        return cell.get('element',None)
      else:
        cell = cell.get('next',None);
    return None

"""
void setTransition(int p, int q, List L[]) {
   List cell;

   cell = (List)malloc(sizeof(struct _cell));
   if (cell == NULL)
      error("BOM/setTransition");
   cell->element = q;
   cell->next = L[p];
   L[p] = cell;
}
"""

def setTransition(p,q,L):
  cell={}
  cell['element'] = q
  cell['next'] = L.get(p,None)
  L[p] = cell

"""
void oracle(char *x, int m, char T[], List L[]) {
   int i, p, q;
   int S[XSIZE + 1];
   char c;

   S[m] = m + 1;
   for (i = m; i > 0; --i) {
      c = x[i - 1];
      p = S[i];
      while (p <= m &&
             (q = getTransition(x, p, L, c)) ==
             UNDEFINED) {
         setTransition(p, i - 1, L);
         p = S[p];
      }
      S[i - 1] = (p == m + 1 ? m : q);
   }
   p = 0;
   while (p <= m) {
      T[p] = TRUE;
      p = S[p];
   }
}

"""
def oracle(x, m, T,L):
   S={}
   x={}
   S[m] = m + 1
   for i in range(m,-1,-1):
     c = x.get(i - 1,None)
     p = S.get(i,None)
     q = getTransition(x, p, L, c)
     while p <= m and q == None:
       setTransition(p, i - 1, L)
       p = S.get(p,None)
       q = getTransition(x, p, L, c)

     if p == m+1:
       S[i-1] = m
     else:
       S[i-1] = q
     #S[i - 1] = (p == m + 1 ? m : q)
   p = 0
   while (p <= m):
      T[p] = True
      p = S.get(p,None)
"""
void BOM(char *x, int m, char *y, int n) {
   char T[XSIZE + 1];
   List L[XSIZE + 1];
   int i, j, p, period, q, shift;

   /* Preprocessing */
   memset(L, NULL, (m + 1)*sizeof(List));
   memset(T, FALSE, (m + 1)*sizeof(char));
   oracle(x, m, T, L);

   /* Searching */
   j = 0;
   while (j <= n - m) {
      i = m - 1;
      p = m;
      shift = m;
      while (i + j >= 0 &&
             (q = getTransition(x, p, L, y[i + j])) !=
             UNDEFINED) {
         p = q;
         if (T[p] == TRUE) {
            period = shift;
            shift = i;
         }
         --i;
      }
      if (i < 0) {
         OUTPUT(j);
         shift = period;
      }
      j += shift;
   }
}
"""

def BOM(x,m,y,n):
  T={}
  L={}
  oracle(x, m, T, L);
  j = 0
  period = 0
  shift = 0
  while (j <= n - m):
    i = m - 1
    p = m
    shift = m
    c = y[i+j]
    q = getTransition(x, p, L, c)
    while i + j >= 0 and q != None:
      p = q
      if (T[p] == True):
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
