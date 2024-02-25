#include <iostream>
#include <vector>
#define SIZE 10'000

using namespace std;
typedef pair<int, int> pint;
typedef vector<pint> vpair;

int ans = 0;
vpair graph[SIZE];
bool visited[SIZE];

int dfs(int u) {
    visited[u] = true;
    pint dist = make_pair(0, 0);
    for (int i = 0; i < graph[u].size(); i++) {
        int v = graph[u][i].first;
        int d = graph[u][i].second;
        if (visited[v]) continue;
        d += dfs(v);
        if (d > dist.first) {
            dist.second = dist.first;
            dist.first = d;
        } else if (d > dist.second) {
            dist.second = d;
        }
    } ans = max(ans, dist.first + dist.second);
    return dist.first;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    int n, u, v, d; cin >> n;
    for (int i = 1; i < n; i++) {
        cin >> u >> v >> d; u--; v--;
        graph[u].push_back(make_pair(v, d));
        graph[v].push_back(make_pair(u, d));
    }

    dfs(0);
    cout << ans << '\n';
    return 0;
}
