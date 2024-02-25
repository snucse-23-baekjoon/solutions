#include <iostream>
using namespace std;

int N, B, C;
bool K[18][18], M[18][18];

void reset() {
    C = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            M[i][j] = K[i][j];
}

void toggle(int i, int j) {
    C++;
    M[i][j] ^= true;
    if (i > 0) M[i - 1][j] ^= true;
    if (i < N - 1) M[i + 1][j] ^= true;
    if (j > 0) M[i][j - 1] ^= true;
    if (j < N - 1) M[i][j + 1] ^= true;
}

bool check() {
    bool ret = true;
    for (int i = 0; i < N; i++)
        ret &= !M[N - 1][i];
    return ret;
}

int main() {
    cin.tie(0)->sync_with_stdio(0); // for fast I/O
    freopen("../input.txt", "r", stdin); // for input test

    cin >> N; B = 325;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> K[i][j];
    
    int MAX = 1 << N;
    for (int b = 0; b < MAX; b++) {
        reset();
        for (int j = 0; j < N; j++)
            if (b & (1 << j)) toggle(0, j);
        for (int i = 1; i < N; i++)
            for (int j = 0; j < N; j++)
                if (M[i - 1][j]) toggle(i, j);
        if (check()) B = min(B, C);
    }
    
    if (B == 325) B = -1;
    cout << B << '\n';
    return 0;
}
