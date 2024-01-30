#include <iostream>
using namespace std;

long long max_length(long long* arr, long long length){
    long long max = arr[0];
    for(long long i = 1; i < length; i++){
        if(max < arr[i]){
            max = arr[i];
        }
    }
    return max;
}

long long whole_length(long long* arr, long long length, long long cut){
    long long count = 0;
    for(long long i = 0; i < length; i++){
        long long temp = arr[i] - cut;
        if(temp > 0) {
            count += temp;
        }
    }
    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long long n, m;
    cin >> n >> m;
    auto* trees = new long long[n];
    for(long long i = 0; i < n; i++){
        cin >> trees[i];
    }
    long long front = 0, back = max_length(trees, n);
    while(front < back){
        long long frt_len = whole_length(trees, n, front);
        long long back_len = whole_length(trees, n, back);
        if(front + 1 == back){
            if(back_len >= m){
                front = back;
            } else {
                back = front;
            }
            break;
        }
        long long pin = (front + back) / 2;
        long long pin_len = whole_length(trees, n, pin);
        if(pin_len >= m){
            front = pin;
        } else {
            back = pin;
        }
    }

    cout << front;

    delete[] trees;
    return 0;
}