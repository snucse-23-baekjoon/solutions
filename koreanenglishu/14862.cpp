#pragma GCC optimize("Ofast")
#include <iostream>
#include <algorithm>
#define MOD 1'000'000'007
#define MAX_B 200'001
#define MAX_N 6

using namespace std;
typedef long long ll;

int i, j, k, phi[MAX_B], inv[MAX_B];

int fast_exp(int a, int b) {
    int c = 1 << 30; ll res = 1;
    while (c) {
        if (b & c) res = ((res * res) % MOD * a) % MOD;
        else res = (res * res) % MOD; c >>= 1;
    } return res;
}

void solve() {
    int N, M = MAX_B; cin >> N;
    int a[MAX_N], b[MAX_N]; ll den = 1;
    for (i = 1; i <= N; i++) {
        cin >> a[i] >> b[i]; a[i]--; M = min(b[i], M);
        den = (den * (b[i] - a[i])) % MOD;
    }

    int prd[MAX_B], zrs[MAX_B];
    for (i = 1; i <= M; i++) {
        prd[i] = 1; zrs[i] = 0;
    }

    for (k = 1; k <= N; k++) {
        int pa = a[k], pb = b[k];
        for (i = 1; i <= M;) {
            if (pa == pb) zrs[i]--;
            else prd[i] = ((ll) prd[i] * inv[pb - pa]) % MOD;
            pa = a[k] / i; pb = b[k] / i;
            if (pa == pb) zrs[i]++;
            else prd[i] = ((ll) prd[i] * (pb - pa)) % MOD;

            j = MAX_B;
            if (pa) j = min(a[k] / pa, j);
            if (pb) j = min(b[k] / pb, j);
            i = j + 1;
        }
    }

    ll tmp = 1, num = 0; k = 0;
    for (i = 1; i <= N; i++) tmp = (tmp * (b[i] - a[i])) % MOD;
    for (i = 1; i <= M; i++) {
        tmp = (tmp * prd[i]) % MOD; k += zrs[i];
        if (!k) num = (num + tmp * phi[i]) % MOD;
    }

    ll ans = (MOD - (num * fast_exp(den, MOD - 2)) % MOD) % MOD;
    cout << ans << '\n';
}

int main() {
    cin.tie(0)->sync_with_stdio(0); // for fast I/O
    freopen("../input.txt", "r", stdin); // for input test

    for (i = 0; i < MAX_B; i++) phi[i] = i;
    for (i = 1; i < MAX_B; i++) {
        for (j = 2 * i; j < MAX_B; j += i) phi[j] -= phi[i];
    }
    for (i = 1; i < MAX_B; i++) inv[i] = fast_exp(i, MOD - 2);

    int T; cin >> T;
    while (T--) solve();
    return 0;
}
