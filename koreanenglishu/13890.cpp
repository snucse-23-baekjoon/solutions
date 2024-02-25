#include <iostream>
#include <cstring>
#include <vector>
#define MAX 80'001
#define POW4(x) ((x) * (x) * (x) * (x))
using namespace std;

void print_int128(__int128_t x) {
    vector<int> stk;
    while (x) {
        stk.push_back(x % 10);
        x /= 10;
    }
    while (!stk.empty()) {
        cout << stk.back();
        stk.pop_back();
    }
    cout << "\n";
}

int main() {
    cin.tie(0)->sync_with_stdio(0); // FOR FAST I/O
    freopen("../input.txt", "r", stdin); // FOR INPUT TEST

    int mu[MAX]; memset(mu, 0, sizeof(mu)); mu[1] = 1;
    for (int i = 1; i < MAX; i++) {
        for (int j = 2 * i; j < MAX; j += i) mu[j] -= mu[i];
        mu[i] += mu[i - 1];
    }

    for (int _ = 0; _ < 4; _++) {
        int n; long long ans = 0; cin >> n;
        for (int i = 1, j; i <= n; i = j + 1) {
            j = min(n / (n / i), n);
            ans += (mu[j] - mu[i - 1]) * POW4((long long) n / i);
        }
        cout << ans << "\n";
    }

    int n; __int128_t ans = 0; cin >> n;
    for (int i = 1, j; i <= n; i = j + 1) {
        j = min(n / (n / i), n);
        ans += (mu[j] - mu[i - 1]) * POW4((__int128_t) n / i);
    }
    print_int128(ans);

    return 0;
}
