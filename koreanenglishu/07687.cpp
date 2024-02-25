#include <bits/stdc++.h>
#define DIST(x, y) ((x) * (x) + (y) * (y))
#define MAX 2147483647
using namespace std;

void solve(int lx, int ly, int lz, int x, int y, int z) {
    if (x == 0 || x == lx) swap(x, z), swap(lx, lz);
    if (y == 0 || y == ly) swap(y, z), swap(ly, lz);
    if (z == 0) cout << DIST(x, y) << '\n';
    else cout << min({
        DIST(x + lz, y), DIST(x + ly, ly + lz - y),
        DIST(x, y + lz), DIST(y + lx, lx + lz - x)
    }) << '\n';
}

int main() {
    cin.tie(0)->sync_with_stdio(0); // FOR FAST I/O
    freopen("../input.txt", "r", stdin); // FOR INPUT TEST
    int lx, ly, lz, x, y, z;
    while (true) {
        cin >> lx >> ly >> lz >> x >> y >> z;
        if (!lx && !ly && !lz && !x && !y && !z) break;
        solve(lx, ly, lz, x, y, z);
    } return 0;
}
