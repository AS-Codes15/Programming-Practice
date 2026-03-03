#include <stdio.h>
#include <string.h>

void salting(char paassword[]);
void main(){
    char password[100];
    scanf("%s", password);

    salting(password);
}

void salting(char password[]){
    char salt[]="123";
    char newPassword[200];

    strcpy(newPassword,password);
    strcat(newPassword,salt);

    printf("Salted Password: %s\n", newPassword);


}