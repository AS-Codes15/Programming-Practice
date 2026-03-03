#include <iostream>
using namespace std;

// int main(){
//     int n = 4;
//     for (int i = 0; i < n; i++)
//     {
//         for (int j = i + 1; j > 0; j--)
//         {
//             cout << j << " ";
//         }

//         cout << endl;
        
//     }

//     return 0 ;
    
// }


// int main(){
//     int n = 4;

//     char ch = 'A';
//     for (int i = 0; i < n; i++)
//     {
//         for (int j = i + 1; j > 0; j--)
//         {
//             cout << ch<< " ";
//             ch ++;
//         }

//         cout << endl;
        
//     }

//     return 0 ;
    
// }


// INVERTED TRIANGLE

int main(){
    int n = 4;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i; j++)                      //for space
        {
           cout << " ";
        }

        for(int j =0; j < n - i; j++){
            cout << i+1 ;
        }

        cout << endl;
        
    }

    return 0 ;
    
}