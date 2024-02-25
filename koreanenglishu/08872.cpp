#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#define SIZE 100'000

using namespace std;
typedef pair<int, int> pint;
typedef vector<int> vint;
typedef vector<pint> vpair;

int n, m, l, k, u, v, w, D[SIZE], B[SIZE];
bool V1[SIZE], V2[SIZE]; vpair G[SIZE];
vint diam, rad;

void dfs(int u, bool V[SIZE]) {
    V[u] = true;
    for (pint p: G[u]) {
        int v = p.first, w = p.second;
        if (V[v]) continue;
        D[v] = D[u] + w; B[v] = u;
        if (D[v] > D[k]) k = v; dfs(v, V);
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);
    
    cin >> n >> m >> l;
    for (int i = 0; i < m; i++) {
        cin >> u >> v >> w;
        G[u].push_back({v, w});
        G[v].push_back({u, w});
    }

    for (int i = 0; i < n; i++) {
        if (V1[i]) continue;
        D[k = i] = 0; B[i] = -1; dfs(i, V1);
        D[u = k] = 0; B[u] = -1; dfs(u, V2); v = k;
        diam.push_back(D[v]);
        int r = D[v];
        while ((k = B[k]) != -1) {
            r = min(r, max(D[k], D[v] - D[k]));
        } rad.push_back(r);
    }

    sort(diam.begin(), diam.end(), greater<int>());
    sort(rad.begin(), rad.end(), greater<int>());
    int ans = diam[0];
    if (rad.size() > 1) {
        ans = max(ans, rad[0] + rad[1] + l);
    } if (rad.size() > 2) {
        ans = max(ans, rad[1] + rad[2] + l + l); 
    } cout << ans << '\n';
    return 0;
}
