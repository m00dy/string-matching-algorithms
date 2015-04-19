#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define ASIZE 256

void preBmBc(char *x, int m, int bmBc[]) {
   int i;
 
   for (i = 0; i < ASIZE; ++i)
      bmBc[i] = m;
   for (i = 0; i < m - 1; ++i)
      bmBc[x[i]] = m - i - 1;
}

long readfile(char *filename, char *text[])
{
	FILE *fin;
	long len;
	int i = 0;
	char c;
	
	if (!(fin = fopen(filename, "r"))) {
		fprintf (stderr, "I can't open the file: %s\n", filename);
		exit(1);
	}
	// llegim el nombre de caracters que hi ha al fitxer
	fseek(fin, 0, SEEK_END);
	len = ftell(fin);
	fseek(fin, 0, SEEK_SET);
	// demanem memoria per la variable text
	*text = malloc(len + 1);
        // bucle per llegir el fitxer
	while ((c = (fgetc(fin))) != EOF) {
	  if ((c=='a')||(c=='c')||(c=='g')||(c=='t')||(c=='A')||(c=='C')||(c=='G')||(c=='T')){
	    (*text)[i] = c;
	    //printf("text[%d] = %c\n", i, (*text)[i]);
	    i++;
	  }
	}
	fclose(fin);
	return i;
}

void HORSPOOL(char *x, int m, char *y, int n) {
   int j, bmBc[ASIZE];
   char c;

   /* Preprocessing */
    preBmBc(x, m, bmBc);

   /* Searching */
   j = 0;
   while (j <= n - m) {
      c = y[j + m - 1];
      if (x[m - 1] == c && memcmp(x, y + j, m - 1) == 0){
      //printf("j=%d \n",j);
      }

      j += bmBc[c];
   }
}
