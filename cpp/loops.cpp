#include <iostream>
using namespace std;

// int main(){
//     int count = 1;
//     while (count <= 5)
//     {
//         cout << count << " ";
//         count+=1;
//     }
    
// }

// int main(){
//     int n = 3;
//     for (int i = 0; i < n; i++)
//     {
//         cout << i << " ";
//     }
    
// }

// sum of numbers from 1 to 10;
// int main(){
//     int n = 10;
//     int sum = 0;
//     for (int i = 1; i <= n; i++)
//     {
//         if(i ==  6){
//             break;
//         } else
//         {
//             sum += i;
//         }
//     }

//     cout << "sum : " << sum << endl;

//     return 0;
    
// }


// sum of all odd number from 1 to n
// int main(){
//     int n;
//     cout << "enter the value of n: ";
//     cin >> n;

//     int sum = 0;
//     for (int i = 1; i <= n; i++)
//     {
//         if(i % 2 != 0){
//             sum += i;
//         } 
//     }

//     cout << "sum : " << sum << endl;

//     return 0;
    
// }


int main(){
    int n = 10;
    int i = 1;

    do
    {
        cout << i << " ";
        i++ ;
    } while (i <= n);

    return 0 ;
    
}
