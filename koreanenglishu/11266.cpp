#include <iostream>
#include <vector>
#define SIZE 10'001
using namespace std;

int V, E, u, v;
int idx[SIZE];
bool art[SIZE];
vector<int> graph[SIZE];

int dfs(int u, bool root) {
    static int cnt = 1;
    int child = 0;
    int par = idx[u] = cnt++;
    for (int v: graph[u]) {
        if (idx[v]) {
            par = min(par, idx[v]);
            continue;
        } int par_v = dfs(v, false);
        if (!root && idx[u] <= par_v)
            art[u] = true;
        par = min(par, par_v);
        child++;
    } if (root && child > 1)
        art[u] = true;
    return par;
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
        if (!idx[u]) dfs(u, true);
    
    int cnt = 0;
    for (int u = 1; u <= V; u++)
        if (art[u]) cnt++;
    cout << cnt << '\n';
    for (int u = 1; u <= V; u++)
        if (art[u]) cout << u << ' ';
    cout << '\n';
    return 0;
}
