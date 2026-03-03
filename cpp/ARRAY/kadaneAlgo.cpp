#include <iostream>
#include <vector>
using namespace std;

int main() {
    int currSum = 0, maxSum = INT32_MIN;
    int num[7] = {3,-4,5,4,-1,7,-8};

    for(int val : num) {
        currSum += val;
        maxSum = max(currSum, maxSum);
        if (currSum < 0)
        {
           currSum = 0;
        }
    }

    cout << maxSum << endl;

    return 0;
    
}