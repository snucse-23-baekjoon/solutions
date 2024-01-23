#include <iostream>
using namespace std;

int main() {
    int repeat = 0;
    cin >> repeat;
    for(int i = 0; i < repeat; i++){
        int number = 0;
        cin >> number;
        int arr[3] = {1, 2, 4};
        int count = 3;

        if(number <= 3){
            cout << arr[number - 1] << endl;
        } else {
            while(count < number){
                int sum = arr[0] + arr[1] + arr[2];
                arr[0] = arr[1];
                arr[1] = arr[2];
                arr[2] = sum;
                count++;
            }
            cout << arr[2] << endl;
        }
    }

    return 0;
}