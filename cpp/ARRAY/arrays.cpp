#include <iostream>
using namespace std;

// int main(){
//     //int a[5];
//     //double price[] = {63,311,32,22};
//     // int marks[5] = {90,87,76,88,85};
//     // int size = 5;

//     int size = 5;
//     int marks[size];

//     for (int i = 0; i < size; i++){
//         cin >> marks[i];
//     }

//     for (int i = 0; i < size; i++){
//         cout << marks[i] << endl;
//     }
    
//     return 0;

//  }


//To find smallest and largest
// int main() {
//     int size = 5;
//     int numbers[size];
//     int smallest = INT32_MAX;
//     int largest = INT32_MIN;
//     // int sIdx;
//     // int lIdx;

//     for (int i = 0; i < size; i++){
//         cin >> numbers[i];
//     }
     
//     for (int i = 0; i < size; i++){
//         // if(numbers[i] < smallest) {
//         //     smallest = numbers[i];
//         // } 

//         smallest = min(numbers[i], smallest);
//         largest = max(numbers[i], largest);

//     }

//     cout << "smallest : " << smallest << endl;
//     cout << "largest : " << largest << endl;
//     return 0;

// }


//Pass by reference

void changeArr(int arr[],int size) {
    cout << "in function" << endl;
    for(int i=0; i<size; i++){
        arr[i] = 2*arr[i];
        cout << arr[i] << endl;
    }
}
int main() {
    int arr[] = {2,3,4};

    changeArr(arr, 3);

    cout << "in main" << endl;
    for(int i=0; i<3; i++) {
        cout << arr[i] << endl;
    }

    return 0 ;
}