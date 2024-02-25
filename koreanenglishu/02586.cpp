#include <iostream>
#include <vector>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    int m, n; cin >> m >> n; int p[m], f[n];
    for (int i = 0; i < m; i++) cin >> p[i];
    for (int j = 0; j < n; j++) cin >> f[j];

    int pos[m + n]; char kind[m + n];
    for (int i = 0, j = 0; i + j < m + n;) {
        if (j == n) kind[i++ + j] = 'p';
        else if (i == m) kind[i + j++] = 'f';
        else if (p[i] < f[j]) kind[i++ + j] = 'p';
        else kind[i + j++] = 'f';
        if (kind[i + j - 1] == 'p') pos[i + j - 1] = p[i - 1];
        else pos[i + j - 1] = f[j - 1];
    }

    vector<int> layer[m + n];
    for (int i = 0, d = n; i < m + n; i++) {
        if (kind[i] == 'p') layer[d++].push_back(pos[i]);
        else layer[--d].push_back(pos[i]);
    }

    long long ans = 0;
    for (int i = 0; i < m + n; i++) {
        int l = layer[i].size(); int ps[l + 1]; ps[0] = 0;
        for (int j = 0; j < l; j++)
            ps[j + 1] = ps[j] + layer[i][j] * (j & 1 ? 1 : -1);
        if (l & 1) {int tmp = 1'000'001;
            for (int j = 0; j < l; j += 2) tmp = min(
                tmp, (long long) ps[j] + ps[j + 1] - ps[l]
            ); ans += tmp;
        } else ans += ps[l];
    }

    cout << ans << '\n';
    return 0;
}
