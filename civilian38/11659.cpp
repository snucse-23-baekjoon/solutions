#include <iostream>
using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> n >> m;
    int* arr = new int[n];
    int* cummulative = new int[n + 1];
    cummulative[0] = 0;

    for(int i = 0; i < n; i++){
        cin >> arr[i];
        cummulative[i + 1] = cummulative[i] + arr[i];
    }

    for(int i = 0; i < m; i++){
        int front, back;
        cin >> front >> back;
        cout << cummulative[back] - cummulative[front - 1] << '\n';
    }

    delete[] arr;
    delete[] cummulative;
    return 0;
}