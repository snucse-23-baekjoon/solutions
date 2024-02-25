#include <iostream>
#include <vector>
#define SIZE 100
using namespace std;

struct edge {int i, u, v;};
struct match {int i1, i2;};
int N, M, u, v, ord[SIZE];
vector<edge> graph[SIZE];
vector<match> matches;

bool dfs(edge e) {
    static int cnt = 1;
    ord[e.v] = cnt++;
    vector<int> chds;
    for (auto f: graph[e.v]) {
        if (e.i == f.i) continue;
        if (!ord[f.v]) {
            if (dfs(f)) chds.push_back(f.i);
        } else if (ord[e.v] < ord[f.v])
            chds.push_back(f.i);
    }

    int i = 0;
    while (i + 1 < chds.size()) {
        int i1 = chds[i], i2 = chds[i + 1];
        matches.push_back({i1, i2}); i += 2;
    } if (i < chds.size() && e.i != -1) {
        matches.push_back({chds[i], e.i});
        return false;
    } return true;
} 

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    cin >> N >> M;
    if (M & 1) {
        cout << "impossible\n";
        return 0;
    } for (int i = 0; i < M; i++) {
        cin >> u >> v;
        graph[u].push_back({i, u, v});
        graph[v].push_back({i, v, u});
    }

    for (int i = 0; i < N; i++)
        if (!ord[i]) dfs({-1, -1, i});
    if (matches.size() != M / 2) {
        cout << "impossible\n";
        return 0;
    } for (match m: matches)
        cout << m.i1 << ' ' << m.i2 << '\n';
    return 0;
}
