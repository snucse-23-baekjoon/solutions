#include <iostream>
#include <cstring>
#define MAX_N 1000000
#define MAX_W 6500
#define MIN(x, y) ((x) < (y) ? (x) : (y))

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;

ll g_min = MAX_W;
int weight_unsorted[MAX_N], weight[MAX_N];
int inv_a[MAX_N], inv_b[MAX_N], perm[MAX_N];
bool visited[MAX_N];

bool comp(pii a, pii b) {
    return a.first < b.first;
}

ll solve(int k) {
    if (visited[k]) return 0;
    ll sum = 0, min = MAX_W, cnt = 0;
    while (!visited[k]) {
        visited[k] = true;
        sum += weight[k];
        min = MIN(min, weight[k]);
        cnt++; k = perm[k];
    }
    return MIN(
        sum + min * (cnt - 2),
        sum + min + g_min * (cnt + 1)
    );
}

int main() {
    // FOR TEST; REMOVE BEFORE SUBMISSION
    freopen("../input.txt", "r", stdin);

    int n, k; scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf(" %d", &weight_unsorted[i]);
        g_min = (ll) MIN(g_min, weight_unsorted[i]);
    }
    for (int i = 0; i < n; i++)
        {scanf(" %d", &k); inv_a[k - 1] = i;}
    for (int i = 0; i < n; i++)
        {scanf(" %d", &k); inv_b[k - 1] = i;}
    
    memset(visited, false, sizeof(bool) * n);
    for (int i = 0; i < n; i++) {
        weight[inv_a[i]] = weight_unsorted[i];
        perm[inv_a[i]] = inv_b[i];
    }
    
    ll ans = 0;
    for (int i = 0; i < n; i++)
        ans += solve(i);

    printf("%lld\n", ans);
    return 0;
}
