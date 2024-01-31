#include <iostream>
using namespace std;

int print_now(int* arr, int length, int target){
    int count = 0, i = 0;
    while(true){
        int max = arr[i % length], max_index = i % length;
        for(int j = i + 1; j < i + length; j++){
            int current = j % length;
            if(max < arr[current]){
                max = arr[current];
                max_index = current;
            }
        }

        count++;
        if(max_index == target){
            return count;
            break;
        }

        arr[max_index] = -1;
        i = max_index;
    }
}

int main() {
    int repeat = 0;
    cin >> repeat;
    for(int i = 0; i < repeat; i++){
        int docs = 0, index = 0;
        cin >> docs >> index;
        int* arr = new int[docs];
        for(int j = 0; j < docs; j++){
            cin >> arr[j];
        }

        cout << print_now(arr, docs, index) << "\n";
        delete[] arr;
    }

    return 0;
}