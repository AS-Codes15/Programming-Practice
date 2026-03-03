#include <stdio.h>

int main(){
    FILE *fptr;
    fptr = fopen("sum.txt","r");

    int a,b;
    int sum;

    fscanf(fptr,"%d",a);
    fscanf(fptr,"%d",b);

    fclose(fptr);

    sum = a+b;
     
    fptr = fopen("sum.txt","w");
    fprintf(fptr,"%d",sum);

    fclose(fptr);

}