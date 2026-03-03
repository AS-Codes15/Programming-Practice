#include <iostream>
using namespace std;

int main(){
    int n=6;
    for (int i = 0; i < n; i++)
    {
        // for space
        for (int k = 0; k < n-i-1; k++)
        {
            cout << " ";
        }

        //for num1
        for(int j = 1; j <= i+1; j++)
        {
            cout << j;
        }

        //for num2
        for(int j=i; j>0; j--){
            cout << j;
        }   

        cout << endl;    
    }

    return 0;
}