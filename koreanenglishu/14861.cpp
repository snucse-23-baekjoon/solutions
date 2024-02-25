#pragma GCC optimize("Ofast")
#include <iostream>
#define MOD 1'073'741'824
#define MAX 4'000'001

using namespace std;
typedef long long ll;

int f[MAX]; bool p[MAX];

void solve() {
    ll ans = 0, p, q;
    int n, m; cin >> n >> m;
    if (n > m) swap(n, m);
    for (int i = 1, j; i <= n;) {
        p = n / i; q = m / i;
        j = min(min(n / p, m / q), (ll) n);
        ans = (ans + ((f[j] - f[i - 1]) % MOD) *
            (((((p * p + p) / 2) % MOD) *
            (((q * q + q) / 2) % MOD)) % MOD)) % MOD;
        i = j + 1;
    } ans = (ans + MOD) % MOD;
    cout << ans << '\n';
}

int main() {
    cin.tie(0)->sync_with_stdio(0); // for fast I/O
    freopen("../input.txt", "r", stdin); // for input test

    for (int i = 1; i < MAX; i++) {f[i] = 1; p[i] = true;}
    for (ll i = 2; i < MAX; i++) {
        if (p[i]) {
            f[i] = (i - i * i) % MOD;
            for (ll j = 2 * i; j < MAX; j += i) {
                if (!((j / i) % (i * i))) f[j] = 0;
                else if (!((j / i) % i)) f[j] = 
                    (-f[j] * (i * ((i * i) % MOD) % MOD)) % MOD;
                else f[j] = (f[j] * ((i - i * i) % MOD)) % MOD;
                p[j] = false;
            }
        } f[i] = (f[i] + f[i - 1]) % MOD;
    }

    int T; cin >> T;
    while (T--) solve();
    return 0;
}
