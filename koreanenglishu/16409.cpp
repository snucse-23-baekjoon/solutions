#include <iostream>
#include <cstring>
#define MAX 10'000'001
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0); // FOR FAST I/O
    freopen("../input.txt", "r", stdin); // FOR INPUT TEST

    int mu[MAX]; memset(mu, 0, sizeof(mu)); mu[1] = 1;
    for (int i = 1; i < MAX; i++) {
        for (int j = 2 * i; j < MAX; j += i) mu[j] -= mu[i];
    }

    long long a, b, c, d; cin >> a >> b >> c >> d;
    int m = b < d ? b : d; long long ans = 0;
    for (int i = 1; i <= m; i++) {
        ans += mu[i] * (b / i - (a - 1) / i)
            * (d / i - (c - 1) / i);
    }
    
    cout << ans << "\n";
    return 0;
}
