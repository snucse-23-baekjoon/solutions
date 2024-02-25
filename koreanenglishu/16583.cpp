#include <iostream>
#include <vector>
#define SIZE 100'001
using namespace std;

struct bmr {int u, v, w;};
int N, M, u, v, ord[SIZE];
vector<int> graph[SIZE];
vector<bmr> bmrs;

bool dfs(int x, int p) {
    static int cnt = 1;
    ord[x] = cnt++;
    vector<int> chds;
    for (int y: graph[x]) {
        if (y == p) continue;
        if (!ord[y]) {if (dfs(y, x)) chds.push_back(y);}
        else if (ord[x] < ord[y]) chds.push_back(y);
    }

    int i = 0;
    while (i + 1 < chds.size()) {
        u = chds[i]; v = chds[i + 1];
        bmrs.push_back({u, x, v}); i += 2;
    } if (i < chds.size() && p) {
        bmrs.push_back({chds[i], x, p});
        return false;
    } return true;
} 

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    cin >> N >> M;
    for (int i = 1; i <= M; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for (int i = 1; i <= N; i++)
        if (!ord[i]) dfs(i, 0);
    
    cout << bmrs.size() << '\n';
    for (bmr b: bmrs) {
        cout << b.u << ' ';
        cout << b.v << ' ';
        cout << b.w << '\n';
    } return 0;
}
