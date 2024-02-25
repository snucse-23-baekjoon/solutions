#include <iostream>
#define SIZE 100'000
#define C(x, y) \
    (((y) - (x)) * T[y] + V[x])

using namespace std;
typedef long long lint;

int N, D; lint ans;
lint T[SIZE], V[SIZE];

void DnC(int s, int e, int l, int r) {
    if (s >= e) return;
    int m = (s + e) / 2;
    int opt = max(l, m - D);
    int sup = min(m + 1, r);
    for (int i = opt; i < sup; i++)
        if (C(opt, m) < C(i, m)) opt = i;
    ans = max(ans, C(opt, m));
    DnC(s, m, l, opt + 1);
    DnC(m + 1, e, opt, r);
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    cin >> N >> D;
    for (int i = 0; i < N; i++) cin >> T[i];
    for (int i = 0; i < N; i++) cin >> V[i];

    DnC(0, N, 0, N);
    cout << ans << '\n';
    return 0;
}
