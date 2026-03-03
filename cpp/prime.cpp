#include <iostream>
using namespace std;

int main(){
    int n;
    bool isPrime = true;
    cout << "enter n: ";
    cin >> n;

    for(int i = 2; i < n; i++){             // i*i <= n
        if(n % i == 0){
            isPrime = false;
            break;
        }
    }

    if (isPrime == true)
    {
        cout << "prime number" << endl;
    } else{
        cout << "non prime number\n";
    }

    return 0;

}