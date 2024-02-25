#include <bits/stdc++.h>
#define FIB(i) ((i) < 0 ? fib[175 + (i)] : fib[i])
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0); // FOR FAST I/O
    freopen("../input.txt", "r", stdin); // FOR INPUT TEST

    long long fib[175];
    fib[1] = fib[174] = 1;
    for (int i = 2; i < 88; i++) {
        fib[i] = fib[175 - i] = fib[i - 1] + fib[i - 2];
        if (!(i & 1)) fib[175 - i] *= -1;
    }

    int n, p; cin >> n >> p;
    if (p > 87) {
        cout << 0 << '\n';
        return 0;
    }

    long long ans = 0, t[p][p];
    for (int i = 0; i < p; i++)
        for (int j = 0; j < p; j++)
            cin >> t[i][j];
    
    for (int i = p - 88; i < 89 - p; i++) {
        bool flag = true;
        for (int j = 0; j < p; j++) {
            for (int k = 0; k < p; k++) {
                if (t[j][k] != FIB(i - j + k))
                    {flag = false; break;}
            } if (!flag) break;
        } if (flag) {
            if (i > 0) ans += max(n - p - i + 2, 0);
            else ans += max(n - p + i, 0);
        }
    }
    
    cout << ans << '\n';
    return 0;
}
