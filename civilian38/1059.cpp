#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int length = 0;
    cin >> length;
    int * arr = new int[length];
    for(int i = 0; i < length; i++){
        cin >> arr[i];
    }
    sort(arr, arr + length);
    int inc = 0;
    cin >> inc;

    if(length == 1){
        int prior = inc - 1;
        int next = arr[0] - 1 - inc;
        cout << prior * next + prior + next;
    } else {
        int minimum = 0;
        int maximum = arr[0];

        for(int i = 0; i < length - 1; i++){
            if(minimum == inc){
                cout << 0;
                inc = 0;
                break;
            }
            if(minimum < inc && inc < maximum){
                break;
            }
            minimum = arr[i];
            maximum = arr[i + 1];
        }
        if (maximum == inc){
            cout << 0;
            inc = 0;
        }
        if(inc){
            int prior = inc - minimum - 1;
            int next = maximum - 1 - inc;
            cout << prior * next + prior + next;
        }
    }
    return 0;
}