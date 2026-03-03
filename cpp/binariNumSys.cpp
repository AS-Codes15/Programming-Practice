#include <iostream>
using namespace std;

//deimal to binary
int decTobin(int decNum) {
    int ans = 0, pow = 1;

    while (decNum > 0)
    {
        int rem = decNum % 2;
        decNum /= 2;

        ans += (rem * pow);
        pow *= 10;
    }

    return ans;
}

//binary to decimal
int binToDec(int binNum){
    int ans = 0, pow = 1;

    while (binNum > 0)
    {
        int rem = binNum % 10;
        ans += (rem * pow); 
        
        binNum /= 10;
        pow *= 2;
    }

    return ans;
}


int main(){
    //int decNum = 10;
    int binNum =101;

    //cout << decTobin(decNum) << endl;
    cout << binToDec(binNum) << endl;

    return 0;
}
