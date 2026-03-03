#include <iostream>
#include <vector>
using namespace std;

// int main() {
//     //vector<char> vec= {'a','b','c','d'};

//     vector<int> vec;

//     //cout << "size = " << vec.size() << endl;

//     vec.push_back(25);
//     vec.push_back(26);
//     vec.push_back(27);
//     vec.push_back(28);

//     for(int val : vec) {
//         cout <<  val << " ";
//         cout << endl;
//     }

//     // cout << "size after push back = " << vec.size() << endl;
//     // vec.pop_back();
//     // cout << "size after pop back = " << vec.size() << endl;

//     cout << "value at front idx: " << vec.front() << endl;
//     cout << "value at last idx: " << vec.back() << endl;

//     cout << "value at 1st idx: " << vec.at(1) << endl;

//     return 0;
// }


//size and capacity
int main(){
    vector<int> vec;

    vec.push_back(0);
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(4);
    vec.push_back(5);

    cout << "size = " << vec.size() << endl;
    cout << "capacity= " << vec.capacity() << endl;


}