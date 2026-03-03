#include  <stdio.h>
#include  <string.h>

int vowels(char str[]);
int main(){
    char str[100];
    scanf("%s", str);

    printf("Number of vowels: %d\n", vowels(str));
    return 0;
}

int vowels(char str[]){
    int count = 0;
    
    for(int i=0; i<strlen(str); i++){
        if ((str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u') || (str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' || str[i] == 'U'))
        {
            count++;
        }
    }
    return count;
}