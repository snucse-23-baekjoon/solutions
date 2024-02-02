#include <iostream>
#include <algorithm>
#include <cstring>
#define MAX_N 1000
#define MAX_W 10000
#define MIN(x, y) ((x) < (y) ? (x) : (y))

using namespace std;
typedef pair<int, int> pii;

int g_min = MAX_W;
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

int solve(int k) {
    if (visited[k]) return 0;
    int sum = 0, min = MAX_W, cnt = 0;
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

    int n, min = MAX_W; scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf(" %d", &weight[i]);
        g_min = MIN(g_min, weight[i]);
    }
    
    compress(n);
    memset(visited, false, sizeof(bool) * n);
    
    int ans = 0;
    for (int i = 0; i < n; i++)
        ans += solve(i);

    printf("%d\n", ans);
    return 0;
}
