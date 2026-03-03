#include <stdio.h>

void swap(int x, int y);
void _swap(int *x, int *y);

int main(){
    int x = 5, y = 10;

    swap(x, y);
    printf("x = %d, y = %d\n", x, y);

    _swap(&x, &y);
    printf("x = %d, y = %d\n", x, y);

    return 0;
}

void swap(int x, int y){
    int temp = x;
    x = y;
    y = temp;
    printf("x = %d, y = %d\n", x, y);
}
void _swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
    
}