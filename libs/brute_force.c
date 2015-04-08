#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define EOS '\0'

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

void BF(char *x, int m, char *y, int n) { 
  char *yb; 
  /* Searching */ 
  long int trobats=0;
  for (yb = y; *y != EOS; ++y) 
    if (memcmp(x, y, m) == 0) trobats++; 
  //printf("j=%d \n",y - yb);
  printf("trobats %d",trobats);
}

int main(int argc, char *argv[])
{
        char pattern[256];
	char filename[256];
	char *text;
	int  n;
	clock_t initemps;

	sprintf(pattern,"%s",argv[2]);
	sprintf(filename,"%s",argv[1]);
	    printf("pattern: %s \n",pattern);
	
	n = readfile(filename, &text);
	//	printf("text: %s \n",text);
	//printf("n=%d\n",n);
	initemps=clock();
	BF(pattern,strlen(pattern),text,n);
	printf( "Nombre de segons: %f s\n", (clock()-initemps)/(double)CLOCKS_PER_SEC );
	free(text);
        return 0;
}
