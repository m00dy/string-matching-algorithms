#include <stdio.h>
#define ASIZE 256
#define WORD_SIZE 64

void BNDM(char *x, int m, char *y, int n) {
  int B[ASIZE];
  int i, j, s, d, last;
  if (m > WORD_SIZE)
    error("BNDM");

  /* Pre processing */
  memset(B,0,ASIZE*sizeof(int));
  s=1;
  for (i=m-1; i>=0; i--){
    B[x[i]] |= s;
    s <<= 1;
  }

  /* Searching phase */
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
    else{
      // printf("%d",j);
    }
       }
       d <<= 1;
     }
     j += last;
   }
  }
