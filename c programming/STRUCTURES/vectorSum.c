#include <stdio.h>

struct vector{
    int x;
    int y;
};

void calSum(struct vector v1, struct vector v2, struct vector sum);

int main(){
    struct vector v1 = {5, 10};
    struct vector v2 = {3, 7};
    struct vector sum = {0};

    calSum(v1, v2, sum);
    return 0;

    // This code will print: Sum of vectors: (8, 17)

    // The struct vector v1 and v2 are declared and initialized as per the given problem statement.
    // The calSum function takes these vectors as arguments and calculates their sum using the addition operator.
    // Finally, the sum of the vectors is printed using the printf function.

    // Note: The struct vector is defined as having two integer members x and y.
    // The calSum function takes these two vectors as arguments and adds their x and y components to get their sum.
    // The sum of the vectors is then printed using the printf function.
    // This code demonstrates the concept of passing structures as arguments to functions in C.
}

void calSum(struct vector v1, struct vector v2, struct vector sum){
    sum.x = v1.x + v2.x;
    sum.y = v1.y + v2.y;
    
    printf("sum of x component: %d\n", sum.x);
    printf("sum of y component: %d\n", sum.y);
}