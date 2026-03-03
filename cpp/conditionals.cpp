#include<iostream>
using namespace std;

// int main(){
//     int marks;
//     cout << "enter your marks: ";
//     cin >> marks;

//     if(marks >= 90){
//         cout << "A\n";
//     } else if(marks >= 80 && marks <90){
//         cout << "B\n";
//     } else{
//         cout << "C\n";
//     }

//     return 0;
// }


// To find a character is lowercase or uppercase
// int main(){
//     char ch;
//     cout <<"enter char: ";
//     cin >> ch;

//     if(ch >= 'a' && ch <= 'z'){
//         cout << "lowercase" << endl;
//     } else{
//         cout << "uppercase";
//     }

//     return 0;
// }

// other way

int main(){
    char ch;
    cout <<"enter char: ";
    cin >> ch;

    if(ch >= 65 && ch <= 90){
        cout << "uppercase" << endl;
    } else{
        cout << "lowercase";
    }

    return 0;
}

