#include <iostream>
#include <algorithm>
#include <queue>
#define MAX 200'000
using namespace std;
using lint = long long;

void solve() {
    lint N, D, C[MAX]; cin >> N >> D;
    for (int i = 0; i < N; i++) cin >> C[i];
    sort(C, C + N);

    priority_queue<lint> Q;
    lint ans = 0, opt; Q.push(C[0]);
    for (int i = 1; i < N; i++) {
        opt = max(Q.top(), 0LL) + D * i;
        if (C[i] < opt) {
            Q.push(C[i] - D * i);
            Q.push(C[i] - D * i);
            Q.pop();
            ans += opt - C[i];
        } else {
            Q.push(C[i] - D * i);
        }
    }

    cout << ans << '\n';
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);
    int Z; cin >> Z; while (Z--) solve();
    return 0;
}
