#pragma GCC optimize("Ofast")
#include <iostream>
#include <vector>
#include <queue>
#define MAX 300000
#define MOD 1000000007

using namespace std;

int main() {
    // FOR TEST; REMOVE BEFORE SUBMISSION
    freopen("../input.txt", "r", stdin);

    int N, K, P, a, b;
    scanf("%d %d %d", &N, &K, &P);

    int in_deg_max[MAX] = {0}, in_deg_min[MAX] = {0};
    vector<int> adj_list_max[MAX], adj_list_min[MAX];
    for (int i = 0; i < P; i++) {
        scanf(" %d %d", &a, &b);
        adj_list_max[b].push_back(a); in_deg_max[a]++;
        adj_list_min[a].push_back(b); in_deg_min[b]++;
    }

    priority_queue<int, vector<int>,
        greater<int> > queue_max, queue_min;
    for (int i = 0; i < K; i++) {
        if (!in_deg_max[i]) queue_max.push(i);
        if (!in_deg_min[i]) queue_min.push(i);
    }

    int coef[MAX] = {0};
    for (int i = 0; i < K; i++) {
        int j_max = queue_max.top(); queue_max.pop();
        int j_min = queue_min.top(); queue_min.pop();
        coef[j_max] += N - K + i; coef[j_min] -= K - i - 1;

        for (int k = 0; k < adj_list_max[j_max].size(); k++) {
            int l = adj_list_max[j_max][k]; in_deg_max[l]--;
            if (!in_deg_max[l]) queue_max.push(l);
        }
        for (int k = 0; k < adj_list_min[j_min].size(); k++) {
            int l = adj_list_min[j_min][k]; in_deg_min[l]--;
            if (!in_deg_min[l]) queue_min.push(l);
        }
    }

    long long n = 1, ans = 0;
    for (int i = 0; i < K; i++) {
        ans = (ans + (coef[i] * n) % MOD) % MOD;
        n = (n * N) % MOD;
    }

    if (ans < 0) ans += MOD;
    printf("%lld\n", ans);
    return 0;
}
