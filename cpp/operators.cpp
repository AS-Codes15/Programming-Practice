#include<iostream>
using namespace std;

// ARITHMETIC OPERATOR
// int main(){
//     int a=10, b=5;

//     cout << "sum = "<< (a+b) << endl;
//     cout << "subtr = "<< (a-b) << endl;
//     cout << "mult = "<< (a*b) << endl;
//     cout << "div = "<< (a/b) << endl;
//     cout << "modulo = "<< (a%b) << endl;

// }

//RELATIONAL OPERATOR
// int main(){

//     cout << (3 < 5) << endl;
//     cout << (3 <= 5) << endl;
//     cout << (3 > 5) << endl;
//     cout << (3 >= 5) << endl;
//     cout << (3 == 5) << endl;
//     cout << (3 != 5) << endl;

// }

//LOGICAL OPERATOR
// int main(){

//     cout << !(3 < 5) << endl;
//     cout << ( (3 < 5) && (3 > 5)) << endl;
//     cout << ( (3 < 5) || (3 > 5)) << endl;

// }


//sum of two numbers
int main(){
    int a,b;
    cout << "enter a: ";
    cin >> a;

    cout << "enter b: ";
    cin >> b;

    int sum = a+b;
    cout << "sum: " << sum << endl;
}