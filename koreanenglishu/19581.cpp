#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#define SIZE 100'000

using namespace std;
typedef pair<int, int> pint;
typedef vector<pint> vpair;
typedef queue<int> qint;

int n, u, v, w; int D[SIZE];
bool V[SIZE]; vpair G[SIZE]; qint Q;

pint bfs(int u, int r = -1) {
    memset(V, false, sizeof(V));
    memset(D, 0, sizeof(D));
    if (r != -1) V[r] = true;
    Q.push(u);

    while (!Q.empty()) {
        int u = Q.front();
        Q.pop(); V[u] = true;
        for (pint p: G[u]) {
            int v = p.first, w = p.second;
            if (V[v]) continue;
            D[v] = D[u] + w; Q.push(v);
        }
    }

    int *v = max_element(D, D + n);
    return {v - D, *v};
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    cin >> n;
    for (int i = 1; i < n; i++) {
        cin >> u >> v >> w; u--; v--;
        G[u].push_back({v, w});
        G[v].push_back({u, w});
    }

    u = bfs(0).first;
    v = bfs(u).first;
    cout << max(
        bfs(u, v).second,
        bfs(v, u).second
    ) << '\n';
    return 0;
}
