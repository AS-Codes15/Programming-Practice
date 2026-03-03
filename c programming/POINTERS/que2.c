#include <stdio.h>

void doWork(int a, int b, int *sum, int *prod, int *avg);

int main() {
    int a, b, sum, prod, avg;

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    doWork(a, b, &sum, &prod, &avg);

    printf("Sum = %d\nProduct = %d\nAverage = %d\n", sum, prod, avg);

    return 0;
}
void doWork(int a, int b, int *sum, int *prod, int *avg) {
    *sum = a + b;
    *prod = a * b;
    *avg = (a + b) / 2;
}