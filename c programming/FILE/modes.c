#include <stdio.h>

int main(){

    FILE *fptr;
    // fptr = fopen("file.txt","r");
     fptr = fopen("newFile.txt","w");

    if(fptr==NULL){
        printf("file does not exist\n");
    }
    else{
        fclose(fptr);
    }
}