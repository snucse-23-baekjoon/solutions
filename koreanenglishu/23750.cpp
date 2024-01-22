#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef struct pair_int {int l; int p;} pi;
bool cmp(pi x, pi y) {
    if (x.l == y.l) return x.p > y.p;
    else return x.l > y.l;
}

int main() {
    // FOR TEST; REMOVE BEFORE SUBMISSION
    freopen("../input.txt", "r", stdin);

    int n, m; scanf("%d %d", &n, &m);
    pi player[n]; int group[m];
    for (int i = 0; i < n; i++)
        scanf(" %d %d", &player[i].l, &player[i].p);
    for (int i = 0; i < m; i++) scanf(" %d", &group[i]);
    sort(player, player + n, cmp);
    sort(group, group + m, greater<int>());

    int k = 1;
    ll ans = player[0].p;
    priority_queue<int> pq;
    for (int i = 0; i < m - 1; i++) {
        for (int j = 0; j < group[i]; j++) pq.push(player[k++].p);
        ans += pq.top(); pq.pop();
    }

    printf("%lld\n", ans);
    return 0;
}
