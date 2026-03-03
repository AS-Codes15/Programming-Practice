#include <iostream>
#include <vector>
using namespace std;

// int main() {
//     //vector<int> vec;
//     //vector<int> vec = {1,2,3};
//     vector<int> vec(4,0);
//     cout << vec[0] << endl;
//     cout << vec[1] << endl;
//     cout << vec[2] << endl;
//     cout << vec[3] << endl;
// }


// for each
int main() {
    vector<char> vec= {'a','b','c','d'};

    for(char val : vec) {
        cout << val << endl;
    }

    return 0;
}