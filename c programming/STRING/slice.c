#include  <stdio.h>
#include  <string.h>

void slice(char str[], int satrt,int  end);

int main() {
    char str[100];
    int n,m;

    scanf("%s\n", str);
    scanf("%d\n %d", &n, &m);

    slice(str,n,m);
}

void slice(char str[],int start, int end) {


    char slicedStr[100] ;
    int j=0;
    for (int i = start; i <= end; i++) {
        slicedStr[j] = str[i];
        j++;
    
    }
    slicedStr[j] = '\0';

    printf("Sliced String: %s\n", slicedStr);
}