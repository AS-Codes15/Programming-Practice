#include <stdio.h>

int main(){
    int n;
    printf("enter the  value of n (n>2): ");
    scanf("%d",&n);

    int fib[n];
    fib[0] = 0;
    fib[1] = 1;
    printf("%d %d ", fib[0], fib[1]);

    for(int i=2; i<n; i++) {
        fib[i] = fib[i-1] + fib[i-2];
        printf("%d\t", fib[i]);
    }

    return 0;

    // This code will print the first n Fibonacci numbers.
    // If you want to print the nth Fibonacci number, replace n with n-1 in the above code.
    // If you want to print the first m Fibonacci numbers, replace n with m in the above code.
    // If you want to print the sum of the first n Fibonacci numbers, replace n with n-1 in the above code.
    // If you want to print the product of the first n Fibonacci numbers, replace n with n-1 in the above code.
    // If you want to print the average of the first n Fibonacci numbers, replace n with n-1 in the above code.
    // If you want to print the maximum value in the first n Fibonacci numbers, replace n with n-1 in the above code.
}