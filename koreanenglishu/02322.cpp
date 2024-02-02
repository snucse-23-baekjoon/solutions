#include <iostream>
#include <algorithm>
#include <cstring>
#define MAX_N 100000
#define MAX_W 1 << 30
#define MIN(x, y) ((x) < (y) ? (x) : (y))

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;

ll g_min = MAX_W;
int weight[MAX_N], perm[MAX_N];
bool visited[MAX_N];

bool comp(pii a, pii b) {
    return a.first < b.first;
}

void compress(int n) {
    pii temp[MAX_N];
    for (int i = 0; i < n; i++) {
        temp[i].first = weight[i];
        temp[i].second = i;
    }
    sort(temp, temp + n, comp);
    for (int i = 0; i < n; i++) {
        temp[i].first = temp[i].second;
        temp[i].second = i;
    }
    sort(temp, temp + n, comp);
    for (int i = 0; i < n; i++)
        perm[i] = temp[i].second;
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

    int n; scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf(" %d", &weight[i]);
        g_min = (ll) MIN(g_min, weight[i]);
    }
    
    compress(n);
    memset(visited, false, sizeof(bool) * n);
    
    ll ans = 0;
    for (int i = 0; i < n; i++)
        ans += solve(i);

    printf("%lld\n", ans);
    return 0;
}
