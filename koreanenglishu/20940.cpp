#pragma GCC optimize("Ofast")
#include <iostream>
#define MAX 1'000'001

using namespace std;
typedef long long ll;

int N, K;
int phi[MAX], fnc[MAX], inv[31];
bool prm[MAX];

int fast_exp(int a, int b) {
    int c = 1 << 30; ll res = 1;
    while (c) {
        if (b & c) res = ((res * res) % K * a) % K;
        else res = (res * res) % K; c >>= 1;
    } return res;
}

ll sum1(ll a) {
    ll ret = (a * inv[3] % K + inv[2]) % K;
    ret = (ret * a % K + inv[6]) % K;
    ret = ret * a % K; return ret;
}

ll sum2(ll a) {
    ll ret = (a * inv[20] % K + inv[4]) % K;
    ret = (ret * a % K + 5LL * inv[12] % K) % K;
    ret = (ret * a % K + inv[4]) % K;
    ret = (ret * a % K + inv[30]) % K;
    ret = ret * a % K; return ret;
}

int main() {
    freopen("../input.txt", "r", stdin); // for input test

    cin >> N >> K;
    for (int i = 1; i <= N; i++) {
        phi[i] = i; fnc[i] = 1; prm[i] = true;
    }
    for (ll i = 1; i <= N; i++) {
        for (int j = 2 * i; j <= N; j += i) phi[j] -= phi[i];
        if (i == 1 || !prm[i]) continue;
        fnc[i] = (fnc[i] * (i - i * i)) % K;
        for (int j = 2 * i; j <= N; j += i) {
            prm[j] = false; int a = j, b = 1;
            while (!(a % i)) {a /= i; b *= i;}
            fnc[j] = (fnc[j] * ((b * (1 - i)) % K)) % K;
        }
    }
    for (int i = 1; i <= 30; i++) {
        inv[i] = fast_exp(i, K - 2);
    }

    cout << sum2(N) << '\n';
    ll gcd = 0, lcm = 0, ans;
    for (ll i = 1; i <= N; i++) {
        ll q = N / i, r = N % i;
        ll tmp1 = i * sum1(q) % K;
        tmp1 = (tmp1 - q * q % K * (i - r - 1) % K) % K;
        gcd = (gcd + phi[i] * tmp1 % K) % K;
        ll tmp2 = i * sum2(q) % K;
        tmp2 = (tmp2 - q * q % K * (q + 1) % K * 
            (q + 1) % K * inv[4] % K * (i - r - 1) % K) % K;
        lcm = (lcm + fnc[i] * tmp2 % K) % K;
    }
    ans = (K + (gcd * lcm) % K) % K;
    cout << ans << '\n';
    return 0;
}
