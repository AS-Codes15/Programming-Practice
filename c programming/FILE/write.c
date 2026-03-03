#include <stdio.h>

int main(){
    FILE *fptr;
    fptr = fopen("test.txt","w");

    // fprintf(fptr,"%c", 'R');
    // fprintf(fptr,"%c", 'O');
    // fprintf(fptr,"%c", 'H');
    // fprintf(fptr,"%c", 'I');
    // fprintf(fptr,"%c", 'T');

    // fprintf(fptr,"%c", 'S');
    // fprintf(fptr,"%c", 'h');
    // fprintf(fptr,"%c", 'A');
    // fprintf(fptr,"%c", 'R');
    // fprintf(fptr,"%c", 'M');
    // fprintf(fptr,"%c", 'A');

    fputs('m',fptr);
    fputs('i',fptr);

    fclose(fptr);
}