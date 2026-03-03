#include <stdio.h>
#include <string.h>

int main(){
    // char name[] = "Archana";

    // printf("length of name: %d\n", strlen(name));

    // char str1[] = "Hii";
    // char str2[] = "Bye";

    // strcpy(str1, str2);
    // puts(str1);

    char firstStr[100] = "Hello";
    char secondStr[] = "World";

    // strcat(firstStr, secondStr);
    // puts(firstStr);

    printf("comparision: %d\n", strcmp(firstStr, secondStr));
    printf("comparision: %d", strcmp(secondStr, firstStr));

    return 0;
 
}