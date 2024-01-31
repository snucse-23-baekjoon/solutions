#include <iostream>
using namespace std;

int less_pick(int num1, int num2){
    if(num1 == -1) {
        return num2;
    } else if(num2 == -1){
        return num1;
    }
    if(num1 < num2){
        return num1;
    }
    return num2;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int target = 0;
    cin >> target;
    int count = 5;
    int arr[5] = {-1, -1, 1,-1, 1};
    if(target < count){
        cout << arr[target - 1];
    } else {
        while(target > count){
            count++;
            int next1 = -1, next2 = -1;
            if(arr[0] != -1){
                next1 = arr[0] + 1;
            }
            if(arr[2] != -1){
                next2 = arr[2] + 1;
            }
            for(int i = 0; i < 4; i++){
                arr[i] = arr[i + 1];
            }
            arr[4] = less_pick(next1, next2);
        }
        cout << arr[4];
    }
    return 0;
}