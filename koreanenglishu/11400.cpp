#include <iostream>
#include <vector>
#include <algorithm>
#define SIZE 100'001
using namespace std;

int V, E, u, v;
int idx[SIZE];
vector<int> graph[SIZE];
vector<pair<int, int>> art;

int dfs(int u, int p) {
    static int cnt = 1;
    int par = idx[u] = cnt++;
    for (int v: graph[u]) {
        if (v == p) continue;
        if (idx[v]) {
            par = min(par, idx[v]);
            continue;
        } int par_v = dfs(v, u);
        if (idx[u] < par_v) {
            if (u < v) art.push_back({u, v});
            else art.push_back({v, u});
        } par = min(par, par_v);
    } return par;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    cin >> V >> E;
    for (int i = 0; i < E; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    } for (int u = 1; u <= V; u++)
        if (!idx[u]) dfs(u, 0);
    
    sort(art.begin(), art.end());
    cout << art.size() << '\n';
    for (auto p: art) {
        cout << p.first << ' ';
        cout << p.second << '\n';
    } return 0;
}
