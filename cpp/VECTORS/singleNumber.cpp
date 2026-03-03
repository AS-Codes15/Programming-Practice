#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> vec = {1,2,3,1,2};
    int ans =0;

    for( int val : vec) {
        ans ^= val;
    }

    cout << ans << endl;
}