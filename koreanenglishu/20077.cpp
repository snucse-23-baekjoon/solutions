#include <iostream>
#include <vector>
#define MAX 1'000'000'000

using namespace std;
typedef long long lint;
typedef vector<int> vint;

lint min_total_length(vint r, vint b) {
    int m = r.size(), n = b.size();
    int min_r[m], min_b[n], idx[m + n + 1];
    lint sum_r[m], sum_b[n], dp[m + n];
    char col[m + n];
    
    for (int p = 0, q = 0; p < m; p++) {
        min_r[p] = MAX + 1;
        while (q < n && b[q] < r[p]) q++;
        if (q > 0) min_r[p] = min(min_r[p], r[p] - b[q - 1]);
        if (q < n) min_r[p] = min(min_r[p], b[q] - r[p]);
        if (p > 0) sum_r[p] = sum_r[p - 1] + r[p];
        else sum_r[p] = r[p];
    } for (int p = 0, q = 0; q < n; q++) {
        min_b[q] = MAX + 1;
        while (p < m && r[p] < b[q]) p++;
        if (p > 0) min_b[q] = min(min_b[q], b[q] - r[p - 1]);
        if (p < m) min_b[q] = min(min_b[q], r[p] - b[q]);
        if (q > 0) sum_b[q] = sum_b[q - 1] + b[q];
        else sum_b[q] = b[q];
    }

    for (int p = 0, q = 0; p + q < m + n;) {
        int i = p + q, j = i - 1, d;
        if (q == n) {d = min_r[p++]; col[i] = 'r';}
        else if (p == m) {d = min_b[q++]; col[i] = 'b';}
        else if (r[p] < b[q]) {d = min_r[p++]; col[i] = 'r';}
        else {d = min_b[q++]; col[i] = 'b';}
        while (j > -1 && col[j] == col[i]) j = idx[j] - 1;
        int k = (i - j + 1) / 2; idx[i] = j;
        dp[i] = (i > 0 ? dp[i - 1] : 0) + d;
        if (j > -1) dp[i] = min(dp[i],
            (j > 0 ? dp[j - 1] : 0) + abs(
                sum_r[p - 1] - (p - k > 0 ? sum_r[p - k - 1] : 0)
                - sum_b[q - 1] + (q - k > 0 ? sum_b[q - k - 1] : 0)
            )
        );
    }
    
    return dp[m + n - 1];
}

// for test
int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    int m, n, x; cin >> m >> n; vint r, b;
    for (int i = 0; i < m; i++) {
        cin >> x; r.push_back(x);
    } for (int i = 0; i < n; i++) {
        cin >> x; b.push_back(x);
    }

    cout << min_total_length(r, b) << '\n';
    return 0;
}
