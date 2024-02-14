#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int number = 0;
    cin >> number;
    int* arr = new int[number];
    for(int i = 0; i < number; i++){
        cin >> arr[i];
    }
    sort(arr, arr + number);
    int answer = arr[0];
    for(int i = 1; i < number; i++){
        arr[i] += arr[i - 1];
        answer += arr[i];
    }
    cout << answer;
    return 0;
}