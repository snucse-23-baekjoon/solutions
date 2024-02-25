#include <iostream>
#include <vector>
#define MAX 100000
using namespace std;
typedef vector<int> vi;

int N, K, M1, M2, M3;
int arr1[MAX], arr2[MAX], arr3[MAX];
vi pot1[20], pot2[20], pot3[MAX];
int cdy1[20], cdy2[20], cdy3[MAX];

void solve(
    int &M, int arr[MAX],
    vi pot[20], int cdy[20]
) {
    int X = (1 << 20) - 1;
    for (int i = 0; i < N; i++)
        X &= arr[i];
    if (X) {
        cdy[M] = X;
        for (int i = 0; i < N; i++) {
            pot[M].push_back(i + 1);
            arr[i] ^= X;
        } M++;
    }

    X = 1;
    while (X < arr[N - 1]) X <<= 1;
    if (X > arr[N - 1]) X >>= 1;
    while (X) {
        cdy[M] = X;
        for (int i = 0; i < N; i++) {
            if (arr[i] & X) {
                pot[M].push_back(i + 1);
                arr[i] ^= X;
            }
        } M++; X >>= 1;
    }
}

void print(
    int &M, vi pot[20], int cdy[20]
) {
    cout << M << '\n';
    for (int i = 0; i < M; i++) {
        cout << pot[i].size() << ' ';
        cout << cdy[i] << '\n';
        for (int p: pot[i])
            cout << p << ' ';
        cout << '\n';
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);

    cin >> N >> K;
    for (int i = 0; i < N; i++)
        arr1[i] = arr2[i] = arr3[i] = K + i;
    solve(M1, arr1, pot1, cdy1);

    cdy2[0] = N / 2;
    for (int i = N / 2; i < N; i++) {
        pot2[0].push_back(i + 1);
        arr2[i] -= N / 2;
    } M2++;
    solve(M2, arr2, pot2, cdy2);

    cdy3[0] = K;
    for (int i = 0; i < N; i++) {
        pot3[0].push_back(i + 1);
        arr3[i] -= K;
    } M3++;
    solve(M3, arr3, pot3, cdy3);

    int M = min(M1, min(M2, M3));
    if (M == M1) print(M1, pot1, cdy1);
    else if (M == M2) print(M2, pot2, cdy2);
    else print(M3, pot3, cdy3);

    return 0;
}
