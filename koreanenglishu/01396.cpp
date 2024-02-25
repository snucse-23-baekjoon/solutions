#include <iostream>
#include <vector>
#include <algorithm>
#define SIZE 100'000
#define CHECK(x, y) (find(x) == find(y))
#define MEMBERS(x) (members[find(x)])
using namespace std;

struct query {int u, v;};
struct answer {int w, n;};
struct edge {int u, v, w;};
bool comp(edge e, edge f) {return e.w < f.w;}

int N, M, Q, u, v, w, fin;
int parents[SIZE], members[SIZE];
int low[SIZE], high[SIZE];
vector<int> indecies[SIZE];
vector<int> indecies_[SIZE];
query queries[SIZE];
answer answers[SIZE];
edge edges[SIZE];

int find(int u) {
    if (parents[u] == u) return u;
    return parents[u] = find(parents[u]);
}

void merge(int u, int v) {
    u = find(u); v = find(v);
    if (u != v) {
        if (members[u] < members[v]) swap(u, v);
        members[u] += members[v];
        parents[v] = u;
    }
}

void kruskal() {
    int cnt = 0; bool flag = false;
    for (int i = 0; i < N; i++) {
        parents[i] = i; members[i] = 1;
    } for (int mid = 0; mid < M; mid++) {
        edge e = edges[mid]; merge(e.u, e.v);
        for (int i: indecies[mid]) {
            query q = queries[i];
            if (low[i] == high[i]) {
                if (CHECK(q.u, q.v))
                    answers[i] = {e.w, MEMBERS(q.u)};
                else answers[i] = {-1, 0};
                fin++; continue;
            } if (CHECK(q.u, q.v)) high[i] = mid;
            else low[i] = mid + 1;
            indecies_[
                (low[i] + high[i]) / 2
            ].push_back(i); cnt++;
            if (cnt + fin == Q) {
                flag = true; break;
            }
        } if (flag) break;
    }

    for (int i = 0; i < M; i++) {
        indecies[i] = indecies_[i];
        indecies_[i].clear();
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        low[i] = 0; high[i] = M - 1;
    } for (int i = 0; i < M; i++) {
        cin >> u >> v >> w; u--; v--;
        edges[i] = {u, v, w};
    } sort(edges, edges + M, comp);

    cin >> Q;
    for (int i = 0; i < Q; i++) {
        cin >> u >> v; u--; v--;
        queries[i] = {u, v};
        indecies[(M - 1) / 2].push_back(i);
    }

    while (fin < Q) kruskal();
    for (int i = 0; i < Q; i++) {
        answer a = answers[i];
        if (!a.n) cout << -1 << '\n';
        else cout << a.w << ' ' << a.n << '\n';
    }

    return 0;
}
