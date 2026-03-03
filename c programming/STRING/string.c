#include <stdio.h>
void printArr(char arr[]);
int main(){
    char name[] = {'A','R','C','H','A','\0'};
    // char name[] = "ARCHA";
    printf("Name: %s\n", name);

    char firstName[] = "Archana";
    char lastName[] = "Sharma";
    printArr(firstName);
    printArr(lastName);

    return 0;

}

void printArr(char arr[]){
    for(int i=0; arr[i]!=0; i++){
        printf("%c", arr[i]);
    }
    printf("\n");

}


