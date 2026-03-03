#include <iostream>
using namespace std;

// int add(int n){
//     int sum = 0;

//     for (int i = 1; i <= n; i++)
//     {
//         sum += i;
//     }

//     return sum;
// }

// int main(){
//     int n;
//     cout << " enter n: ";
//     cin >> n;

//     cout << "sum =" << add(n) << endl;

//     return 0;
// }


//factorial
int factorial(int n){
    int fact = 1;

    for (int i = 1; i <= n; i++)
    {
        fact *= i;
    }

    return fact;
}

int main(){
    int n;
    cout << " enter n: ";
    cin >> n;

    cout << "factorial =" << factorial(n) << endl;

    return 0;
}