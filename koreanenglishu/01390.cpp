#include <iostream>
#define MOD 1'000'000
using namespace std;

int T[8][8] = {
    {2, 2, 4, 2, 5, 5, 3, 3},
    {1, 1, 2, 1, 2, 3, 2, 2},
    {1, 1, 1, 1, 1, 2, 3, 2},
    {1, 1, 1, 1, 1, 2, 3, 2},
    {4, 4, 7, 4, 6, 7, 7, 5},
    {2, 2, 2, 2, 2, 2, 2, 2},
    {4, 4, 5, 4, 7, 7, 6, 7},
    {1, 1, 2, 1, 3, 2, 1, 1}
}, M[8][8] = {
    {1, 0, 0, 0, 0, 0, 0, 0},
    {0, 1, 0, 0, 0, 0, 0, 0},
    {0, 0, 1, 0, 0, 0, 0, 0},
    {0, 0, 0, 1, 0, 0, 0, 0},
    {0, 0, 0, 0, 1, 0, 0, 0},
    {0, 0, 0, 0, 0, 1, 0, 0},
    {0, 0, 0, 0, 0, 0, 1, 0},
    {0, 0, 0, 0, 0, 0, 0, 1}
}, I[8] = {
    2, 1, 1, 1, 4, 2, 4, 1
};

void mul(int A[8][8], int B[8][8]) {
    int C[8][8];
    for (int i = 0; i < 8; i++)
        for (int j = 0; j < 8; j++) {
            C[i][j] = 0;
            for (int k = 0; k < 8; k++)
                C[i][j] = (C[i][j] + (long long)
                    A[i][k] * B[k][j] % MOD) % MOD;
        }
    for (int i = 0; i < 8; i++)
        for (int j = 0; j < 8; j++)
            A[i][j] = C[i][j];
}

int main() {
    int N; cin >> N; int K = N / 4 - 1;
    if (N & 3) {cout << "0\n"; return 0;}
    for (int i = 1 << 6; i; i >>= 1) {
        if (K & i) {mul(M, M); mul(M, T);}
        else mul(M, M);
    }

    int ans = 0;
    for (int i = 0; i < 8; i++)
        for (int j = 0; j < 8; j++)
            ans = (ans + M[i][j] * I[j]) % MOD;

    cout << ans << '\n';
    return 0;
}