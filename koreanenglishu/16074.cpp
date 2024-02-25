#include <iostream>
#include <vector>
#include <algorithm>
#define MAXM 500
#define MAXN 500
#define MAXQ 100'000
#define SIZE 500'000
#define INT(x, y) ((x) * n + (y))
#define CHECK(x, y) (find(x) == find(y))
#define MEMBERS(x) (members[find(x)])
using namespace std;

struct query {int u, v;};
struct edge {int u, v, w;};
bool comp(edge e, edge f) {return e.w < f.w;}

int N, M, Q, m, n, u, v, w, k, a, b, c, d, fin;
int low[MAXQ], high[MAXQ], answers[MAXQ];
int parents[SIZE], members[SIZE];
int heights[MAXM][MAXN];

vector<int> indecies[SIZE];
vector<int> indecies_[SIZE];
query queries[MAXQ];
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
                answers[i] = e.w; fin++; continue;
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

    cin >> m >> n >> Q;
    N = m * n; M = 2 * m * n - m - n;
    for (int i = 0; i < Q; i++) {
        low[i] = 0; high[i] = M - 1;
    }

    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            cin >> heights[i][j];
    
    for (int i = 0; i < m - 1; i++)
        for (int j = 0; j < n; j++)
            edges[k++] = {
                INT(i, j), INT(i + 1, j),
                max(heights[i][j], heights[i + 1][j])
            };
    
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n - 1; j++)
            edges[k++] = {
                INT(i, j), INT(i, j + 1),
                max(heights[i][j], heights[i][j + 1])
            };

    sort(edges, edges + M, comp);

    for (int i = 0; i < Q; i++) {
        cin >> a >> b >> c >> d;
        a--; b--; c--; d--;
        if (a == c && b == d) {
            answers[i] = heights[a][b]; fin++;
        } else {
            queries[i] = {INT(a, b), INT(c, d)};
            indecies[(M - 1) / 2].push_back(i);
        }
    }

    while (fin < Q) kruskal();
    for (int i = 0; i < Q; i++)
        cout << answers[i] << '\n';
    return 0;
}
