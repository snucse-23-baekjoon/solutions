#include <iostream>
using namespace std;


int main() {
    int n, k;
    cin >> n >> k;
    int* coins = new int[n];
    for(int i = 0; i < n; i++){
        cin >> coins[i];
    }

    int count = 0;
    for(int i = n - 1; i > -1; i--){
        while(k >= coins[i]){
            k -= coins[i];
            count++;
        }
    }

    cout << count;
    return 0;
}