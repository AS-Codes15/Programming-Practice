#include <iostream>
#include <vector>
using namespace std;

//To find max subarray
// int main() {
//     int n = 5;
//     int arr[n] ={1,2,3,4,5};

//     for(int st=0; st<n; st++) {
//         for(int end=st; end<n; end++) {
//             for(int i=st; i<=end; i++) {
//                 cout << arr[i];
//             }

//             cout << " ";
//         }
//         cout << endl;
//     }

//     return 0;
// }


//To find max sub array sum
int main() {
    int n = 5;
    int arr[n] ={1,2,3,4,5};

    int maxSum = INT32_MIN;

    for(int st=0; st<n; st++) {
        int currSum = 0;
        for(int end=st; end<n; end++) {
           currSum = arr[end];
           maxSum = max(currSum, maxSum);
        }
    }

    cout << "max subarray sum = " << maxSum << endl;

    return 0;
}