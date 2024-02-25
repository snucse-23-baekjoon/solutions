#include <iostream>
#include <algorithm>
#include <cstring>
#define MAX 1E18
#define SIZE 301
using namespace std;
typedef long long lint;

int n, m, a, x[SIZE];
lint dp[SIZE][SIZE][2];

lint find(int s, int e, int f, int k) {
    if (!k) return 0;
    if (dp[s][e][f] != -1) return dp[s][e][f];
    if (s == 0 && e == n - 1) return dp[s][e][f] = 0;
    int c = f ? e : s; dp[s][e][f] = MAX;
    if (s > 0) dp[s][e][f] = min(dp[s][e][f],
        find(s - 1, e, 0, k - 1) + k * (x[c] - x[s - 1]));
    if (e < n - 1) dp[s][e][f] = min(dp[s][e][f],
        find(s, e + 1, 1, k - 1) + k * (x[e + 1] - x[c]));
    return dp[s][e][f];
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);
    cin >> n >> m; bool z = false;
    for (int i = 0; i < n; i++) {
        cin >> x[i]; if (!x[i]) z = true;
    } if (!z) x[n++] = 0; sort(x, x + n);
    while (x[a] != 0) a++;
    lint tmp, ans = 0;
    for (int k = 0; k < n; k++) {
        memset(dp, -1, sizeof(dp));
        tmp = min(find(a, a, 0, k), find(a, a, 1, k));
        tmp = m * k - tmp + (z ? m : 0);
        ans = max(ans, tmp);
    } cout << ans << '\n';
    return 0;
}
