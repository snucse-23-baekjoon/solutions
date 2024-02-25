#include <iostream>
#define MAX 500002
using namespace std;

int S[MAX], T[MAX], min_S[MAX], min_T[MAX];
long long sum_S[MAX], sum_T[MAX], DP[2 * MAX];
int J[2 * MAX]; char K[2 * MAX];

int main() {
    cin.tie(0)->sync_with_stdio(0); // for fast I/O
    freopen("../input.txt", "r", stdin); // for input test
    
    int M, N; cin >> M >> N;
    for (int i = 1; i <= M; i++) {
        cin >> S[i];
        sum_S[i] = sum_S[i - 1] + S[i];
    } for (int i = 1; i <= N; i++) {
        cin >> T[i];
        sum_T[i] = sum_T[i - 1] + T[i];
    }
    
    S[0] = T[0] = -1'000'000'001;
    S[M + 1] = T[N + 1] = 2'000'000'001;
    for (int p = 1, q = 1; p <= M; p++) {
        while (T[q] < S[p]) q++;
        min_S[p] = min(S[p] - T[q - 1], T[q] - S[p]);
    } for (int p = 1, q = 1; q <= N; q++) {
        while (S[p] < T[q]) p++;
        min_T[q] = min(T[q] - S[p - 1], S[p] - T[q]);
    }

    for (int p = 0, q = 0, i = 1; i <= M + N; i++) {
        int d;
        if (S[p + 1] < T[q + 1]) {
            p++; K[i] = 's'; d = min_S[p];
        } else {
            q++; K[i] = 't'; d = min_T[q];
        }
        
        int j = i - 2;
        while (j >= 0 && K[j + 1] == K[i]) j = J[j + 1] - 1;
        J[i] = j;

        int k = (i - j) / 2;
        DP[i] = DP[i - 1] + d;
        if (j >= 0) DP[i] = min(
            DP[i], DP[j] + abs(
                sum_S[p] - sum_S[p - k] 
                - sum_T[q] + sum_T[q - k]
            )
        );
    }

    cout << DP[M + N] << '\n';
    return 0;
}
