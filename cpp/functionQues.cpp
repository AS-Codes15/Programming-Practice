#include <iostream>
using namespace std;

//sum of digits of a number
// int digitSum(int num){
//     int digSum = 0;

//     while(num > 0){
//         int digit = num % 10;
//         num = num / 10;

//         digSum += digit;
//     }

//     return digSum;

// }

// int main(){
//      cout << "sum = " << digitSum(123) << endl;

//      return 0;
// }


//binomial coefficient

int factorial(int n){
    int fact = 1;

    for (int i = 1; i <= n; i++)
    {
        fact *= i;
    }

    return fact;
}

int nCr(int n, int r){
    int fact_n = factorial(n);
    int fact_r = factorial(r);
    int fact_n_r = factorial(n-r);

    return fact_n/(fact_r * fact_n_r);
}

int main(){
    int n = 8;
    int r = 2;

    cout << nCr(n,r) << endl;

    return 0;
}

