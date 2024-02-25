#include <iostream>
#define MOD 1'073'741'824
#define MAX 2'001
using namespace std;

bool prm[MAX];
int mu[MAX], cop[MAX][MAX], mcp[MAX][MAX];

long long w(int s, int t) {
    long long ret = 0;
    for (int i = 1, j; i <= s; i = j + 1) {
        j = min(s / (s / i), s);
        ret = (ret + (cop[t][j] - cop[t][i - 1]) *
            (s / i) % MOD) % MOD;
    } return ret;
}

int main() {
    freopen("../input.txt", "r", stdin); // for input test

    mu[1] = 1;
    for (int i = 1; i < MAX; i++)
        for (int j = 2 * i; j < MAX; j += i)
            mu[j] -= mu[i];

    for (int i = 1; i < MAX; i++) {
        for (int j = 1; j < MAX; j++)
            cop[i][j] = 1;
        prm[i] = true;
    }

    for (int i = 2; i < MAX; i++) {
        if (!prm[i]) continue;
        for (int j = i; j < MAX; j += i) {
            prm[j] = false;
            for (int k = i; k < MAX; k += i)
                cop[j][k] = 0;
        } prm[i] = true;
    }

    for (int i = 1; i < MAX; i++)
        for (int j = 1; j < MAX; j++) {
            mcp[i][j] = mcp[i][j - 1] + mu[j] * cop[i][j];
            cop[i][j] += cop[i][j - 1];
        }
    
    int a, b, c;
    cin >> a >> b >> c;
    if (a > b) swap(a, b);
    if (b > c) swap(b, c);
    if (a > b) swap(a, b);

    long long ans = 0;
    for (int i = 1; i <= a; i++) {
        long long tmp = 0;
        for (int j = 1, k; j <= b; j = k + 1) {
            k = min(b / (b / j), b);
            k = min(c / (c / j), k);
            tmp = (tmp + (mcp[i][k] - mcp[i][j - 1]) * 
                w(b / j, i) % MOD * w(c / j, i) % MOD) % MOD;
        } ans = (ans + (a / i) * tmp % MOD) % MOD;
    } cout << ans << endl;
    return 0;
}
