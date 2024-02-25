#include <iostream>
#include <cstring>
#define MAX 1E18
#define SIZE 1001
using namespace std;
typedef long long lint;

int n, m;
int x[SIZE], w[SIZE];
lint dp[SIZE][SIZE][2];

lint find(int s, int e, int f) {
    if (dp[s][e][f] != -1) return dp[s][e][f];
    if (s == 1 && e == n) return dp[s][e][f] = 0;
    int c = f ? e : s; dp[s][e][f] = MAX;
    if (s > 1) dp[s][e][f] = min(dp[s][e][f],
        find(s - 1, e, 0) + (w[n] - w[e] + w[s - 1]) * (x[c] - x[s - 1]));
    if (e < n) dp[s][e][f] = min(dp[s][e][f],
        find(s, e + 1, 1) + (w[n] - w[e] + w[s - 1]) * (x[e + 1] - x[c]));
    return dp[s][e][f];
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        cin >> x[i] >> w[i];
        w[i] += w[i - 1];
    } memset(dp, -1, sizeof(dp));
    cout << min(
        find(m, m, 0), find(m, m, 1)
    ) << '\n';
    return 0;
}
