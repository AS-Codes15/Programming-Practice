#include <iostream>
using namespace std;

int linearSearch(int arr[], int size, int target) {
    for(int i=0; i<size; i++){
        if (arr[i]==target)
        {
            return i;
        }
    }
    return -1;
}

int main() {
    int size = 5;
    int arr[] = {9,77,29,31,32};
    int target = 21;
    int result = linearSearch(arr, size, target);
    cout << result << endl;

    return 0;
}