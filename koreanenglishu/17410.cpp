#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

#define MAX 10'001
#define SIZE 100'000
#define BKT_SIZE 333
#define ALL(x) x.begin(), x.end()

int n, i, j, k;
int N, M, K, arr[SIZE];
int bkt[BKT_SIZE][MAX];

int count() {
    int ans = 0;
    cin >> i >> j >> k;
    for (i--; i % K && i < j; i++) if (arr[i] > k) ans++;
    if (i == j) return ans;

    for (; j % K; j--) if (arr[j - 1] > k) ans++;
    for (int l = i / K; l < j / K; l++) ans += bkt[l][k];
    return ans;
}

void update() {
    cin >> i >> k; i--; int *b = bkt[i / K];
    if (arr[i] < k) for (int j = arr[i]; j < k; j++) b[j]++;
    else for (int j = k; j < arr[i]; j++) b[j]--;
    arr[i] = k;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    cin >> N; K = 2 * sqrt(N);
    for (int i = 0; i < N; i++) cin >> arr[i];
    for (int i = 0; i <= N / K; i++) {
        for (int j = 0; j < K && i * K + j < N; j++)
            bkt[i][arr[i * K + j] - 1]++;
        for (int j = MAX - 1; j > 0; j--)
            bkt[i][j - 1] += bkt[i][j];
    }

    cin >> M;
    while (M--) {
        cin >> n;
        if (n == 1) update();
        if (n == 2) cout << count() << '\n';
    }

    return 0;
}