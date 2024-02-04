#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;
    int* arr = new int[n];
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    int close = m;
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            for(int k = j + 1; k < n; k++){
                if(arr[i] + arr[j] + arr[k] <= m && m - (arr[i] + arr[j] + arr[k]) < close){
                    close = m - (arr[i] + arr[j] + arr[k]);
                }
            }
        }
    }

    cout << m - close;
    return 0;
}