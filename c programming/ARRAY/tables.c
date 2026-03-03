#include <stdio.h>

int main(){
    int table[2][10];

    for(int i=1; i<=10; i++){
        table[0][i] = 2*i;
        table[1][i] = 3*i;
    }

    for(int i=0; i<2; i++){
        for(int j=1; j<=10; j++){
            printf("%d\t",table[i][j]);
        }
        printf("\n");
    }
    return 0;

}