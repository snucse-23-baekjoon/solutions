#include <cstdio>

void solve(int x) {
    static int c = 0;
    for (int i = x; i > 0; i--)
        printf("%d ", c + i);
    c += x;
}

int main() {
    // FOR TEST; REMOVE BEFORE SUBMISSION
    freopen("../input.txt", "r", stdin);

    int N, M, K;
    scanf("%d %d %d", &N, &M, &K);
    if (N < M + K - 1 || M * K < N) {
        printf("-1\n"); return 0;
    }

    solve(K);
    if (M == 1) {
        printf("\n"); return 0;
    }

    int q = (N - K) / (M - 1);
    int a = (N - K) % (M - 1);
    int b = (M - 1) - a;
    for (int i = 0; i < a; i++) solve(q + 1);
    for (int i = 0; i < b; i++) solve(q);
    printf("\n"); return 0;
}
