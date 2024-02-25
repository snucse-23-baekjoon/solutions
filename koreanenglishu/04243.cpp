#include <iostream>
#include <cstring>
#define MAX 1E18
#define SIZE 100
using namespace std;
typedef long long lint;

int n, a;
lint x[SIZE], dp[SIZE][SIZE][2];

lint find(int s, int e, int f) {
    if (dp[s][e][f] != -1) return dp[s][e][f];
    if (s == 0 && e == n - 1) return dp[s][e][f] = 0;
    int c = f ? e : s; dp[s][e][f] = MAX;
    if (s > 0) dp[s][e][f] = min(dp[s][e][f],
        find(s - 1, e, 0) + (n - e + s - 1) * (x[c] - x[s - 1]));
    if (e < n - 1) dp[s][e][f] = min(dp[s][e][f], 
        find(s, e + 1, 1) + (n - e + s - 1) * (x[e + 1] - x[c]));
    return dp[s][e][f];
}

void solve() {
    cin >> n >> a; a--;
    for (int i = 1; i < n; i++) {
        cin >> x[i]; x[i] += x[i - 1];
    } memset(dp, -1, sizeof(dp));
    cout << min(
        find(a, a, 0), find(a, a, 1)
    ) << '\n';
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);
    int t; cin >> t; while (t--) solve(); 
    return 0;
}
