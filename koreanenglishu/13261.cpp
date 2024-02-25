#include <iostream>
#define MAX_G 801
#define MAX_L 8001
#define C(x, y) \
    (((y) - (x)) * (S[y] - S[x]))

using namespace std;
typedef long long lint;

int L, G;
lint S[MAX_L], DP[MAX_G][MAX_L];

void dnc(int g, int s, int e, int l, int r) {
    if (s > e) return;
    int m = (s + e) / 2, opt = l;
    for (int i = l; i < m; i++) 
        if (DP[g - 1][opt] + C(opt, m)
            > DP[g - 1][i] + C(i, m)) opt = i;
    DP[g][m] = DP[g - 1][opt] + C(opt, m);
    dnc(g, s, m - 1, l, opt);
    dnc(g, m + 1, e, opt, r);
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    cin >> L >> G;
    for (int i = 1; i <= L; i++) {
        cin >> S[i]; S[i] += S[i - 1];
        DP[1][i] = C(i, 0);
    } for (int i = 2; i <= G; i++)
        dnc(i, 0, L, 0, L);
    
    cout << DP[G][L] << '\n';
    return 0;
}
