#include  <stdio.h>
#include  <string.h>

void charCheck(char str[], char ch);

int main(){
    char str[100];
    char ch;
    scanf("%s", str);
    scanf(" %c", &ch);

    charCheck(str, ch);
    return 0;
}

void charCheck(char str[], char ch){
    for(int i=0; str[i]!='\0'; i++){
        if(str[i] == ch){
            printf("Character is present at index: %d", i);
            return;
        }
    }
    printf("Character is NOT present");

}