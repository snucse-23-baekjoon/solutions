#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

#define SIZE 100'000
#define BKT_SIZE 333
#define ALL(x) x.begin(), x.end()

int n, i, j, k;
int N, M, K, arr[SIZE];
vector<int> bkt[BKT_SIZE];

int count() {
    int ans = 0;
    cin >> i >> j >> k;
    for (i--; i % K && i < j; i++) if (arr[i] > k) ans++;
    if (i == j) return ans;

    for (; j % K; j--) if (arr[j - 1] > k) ans++;
    for (int l = i / K; l < j / K; l++) ans +=
        bkt[l].end() - upper_bound(ALL(bkt[l]), k);
    return ans;
}

void update() {
    cin >> i >> k; i--;
    auto it = lower_bound(
        ALL(bkt[i / K]), arr[i]);
    *it = arr[i] = k;
    sort(ALL(bkt[i / K]));
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    cin >> N; K = 2 * sqrt(N);
    for (int i = 0; i < N; i++) cin >> arr[i];
    for (int i = 0; i <= N / K; i++) {
        for (int j = 0; j < K && i * K + j < N; j++)
            bkt[i].push_back(arr[i * K + j]);
        sort(ALL(bkt[i]));
    }

    cin >> M;
    while (M--) {
        cin >> n;
        if (n == 1) cout << count() << '\n';
        if (n == 2) update();
    }

    return 0;
}