#pragma GCC optimize("O3")
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#define MAX 1E18
#define NODES 5001
#define C(x, y) (((y) - (x) - 1) * (PS[y] - PS[x]))

using namespace std;
struct pint {long long v, w;};
struct compare {
    bool operator() (pint p, pint q) {
        return p.w > q.w;
    }
};
typedef long long lint;
typedef vector<pint> vpint;
typedef priority_queue<pint,
    vector<pint>, compare> pqpint;

int N, B, S, R, u, v, w;
lint D1[NODES], D2[NODES];
vpint G1[NODES], G2[NODES];
lint PS[NODES], DP[NODES][NODES];

void dijkstra(int u, lint D[NODES], vpint G[NODES]) {
    for (int i = 1; i <= N; i++) D[i] = MAX; D[u] = 0;
    pqpint pq; pq.push({u, 0});
    while (pq.size()) {
        pint p = pq.top(); pq.pop();
        if (D[p.v] < p.w) continue;
        for (pint q: G[p.v]) {
            if (D[q.v] <= p.w + q.w) continue;
            D[q.v] = p.w + q.w;
            pq.push({q.v, D[q.v]});
        }
    }
}

void dnc(int t, int s, int e, int l, int r) {
    if (s > e) return;
    int m = (s + e) / 2, opt = l;
    for (int i = l; i < m; i++) 
        if (DP[t - 1][opt] + C(opt, m)
            > DP[t - 1][i] + C(i, m)) opt = i;
    DP[t][m] = DP[t - 1][opt] + C(opt, m);
    dnc(t, s, m - 1, l, opt);
    dnc(t, m + 1, e, opt, r);
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    cin >> N >> B >> S >> R;
    for (int i = 0; i < R; i++) {
        cin >> u >> v >> w;
        G1[u].push_back({v, w});
        G2[v].push_back({u, w});
    }

    dijkstra(B + 1, D1, G1);
    dijkstra(B + 1, D2, G2);

    for (int i = 1; i <= B; i++) {
        PS[i] = D1[i] + D2[i];
    } sort(PS + 1, PS + B + 1);
    for (int i = 1; i <= B; i++) {
        PS[i] += PS[i - 1];
        DP[1][i] = C(0, i);
    } for (int i = 2; i <= S; i++) {
        dnc(i, i, B, 0, B);
        if (!DP[i][B]) break;
    } cout << DP[S][B] << '\n';
    return 0;
}
