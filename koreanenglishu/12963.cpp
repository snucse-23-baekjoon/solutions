#include <iostream>
#define SIZE 2000
#define MOD 1'000'000'007
using namespace std;

int N, M, s, t, u, v;
int E[SIZE][2], P[SIZE];
bool U[SIZE];

int find(int x) {
    if (x != P[x]) P[x] = find(P[x]);
    return P[x];
}

void join(int x, int y) {
    x = find(x); y = find(y);
    if (x != y) P[x] = y;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    cin >> N >> M;
    for (int i = 0; i < M; i++)
        cin >> E[i][0] >> E[i][1];

    for (int i = 0; i < N; i++) P[i] = i;

    for (int i = M - 1; i > -1; i--) {
        s = find(0); t = find(N - 1);
        u = find(E[i][0]); v = find(E[i][1]);
        if (s == u && t == v ||
            s == v && t == u) U[i] = true;
        else join(u, v);
    }

    int ans = 0;
    for (int i = 0, j = 1; i < M;) {
        if (U[i]) ans = (ans + j) % MOD;
        i++; j = (j * 3LL) % MOD;
    } cout << ans << '\n';
    return 0;
}
