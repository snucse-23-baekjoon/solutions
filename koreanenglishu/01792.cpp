#include <iostream>
#include <cstring>
#define MAX 50001
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0); // FOR FAST I/O
    freopen("../input.txt", "r", stdin); // FOR INPUT TEST

    int psum[MAX]; psum[0] = 0;
    int mu[MAX]; memset(mu, 0, sizeof(mu)); mu[1] = 1;
    for (int i = 1; i < MAX; i++) {
        for (int j = 2 * i; j < MAX; j += i) mu[j] -= mu[i];
        psum[i] = psum[i - 1] + mu[i];
    }

    int n, a, b, d; cin >> n;
    while (n--) {
        cin >> a >> b >> d; if (a > b) swap(a, b);
        int da = a / d, db = b / d, ans = 0;
        int ia = 1, qa, ja, ib, qb, jb;
		while (ia <= da) {
			qa = da / ia; ja = min(da / qa, da); ib = ia;
            while (ib <= ja) {
                qb = db / ib; jb = min(db / qb, ja);
                ans += (psum[jb] - psum[ib - 1]) * qa * qb;
                ib = jb + 1;
            }
            ia = ja + 1;
		}
        cout << ans << "\n";
    }

    return 0;
}
