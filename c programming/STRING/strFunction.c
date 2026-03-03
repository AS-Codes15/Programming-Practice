#include <stdio.h>

int main(){

    char str[100];

    //gets(str);                      //outdated function
    fgets(str, 100, stdin);
    puts(str);                           //gives new line automatically
    return 0;
}