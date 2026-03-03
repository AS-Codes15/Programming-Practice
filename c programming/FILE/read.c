#include <stdio.h>

int main(){
    FILE *fptr;
    fptr = fopen("test.txt","r");

    //char ch;

    // int ch;

    // fscanf(fptr, "  %d",&ch);
    // printf("characters: %d\n",ch);

    // fscanf(fptr, "  %d",&ch);
    // printf("characters: %d\n",ch);

    // fscanf(fptr, "  %d",&ch);
    // printf("characters: %d\n",ch);

    // printf("%c\n",fgetc(fptr));
    // printf("%c\n",fgetc(fptr));
    // printf("%c\n",fgetc(fptr));
    // printf("%c\n",fgetc(fptr));
    // printf("%c\n",fgetc(fptr));

    char ch;
    ch = fgetc(fptr);
    while(ch!=EOF){
        printf("%c",ch);
        ch = fgetc(fptr);
    }

    fclose(fptr);
}