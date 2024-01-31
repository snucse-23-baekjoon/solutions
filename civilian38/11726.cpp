#include <iostream>
using namespace std;

int main() {
    int number = 0;
    cin >> number;

    int arr[2] = {1, 2};
    int count = 2;

    if(number <= count){
        cout << arr[number - 1];
    } else {
        while(count < number){
            int sum = (arr[0] + arr[1]) % 10007;
            arr[0] = arr[1];
            arr[1] = sum;
            count++;
        }
        cout << arr[1];
    }
}