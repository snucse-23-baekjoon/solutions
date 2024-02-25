#include <iostream>
using namespace std;

int arr[128][128], cnt = 1;

void fill(int dr, int dc, int r, int c) {
    if (r != 0 || c != 0) arr[0 + dr][0 + dc] = cnt;
    if (r != 1 || c != 0) arr[1 + dr][0 + dc] = cnt;
    if (r != 0 || c != 1) arr[0 + dr][1 + dc] = cnt;
    if (r != 1 || c != 1) arr[1 + dr][1 + dc] = cnt;
    cnt++;
}

void solve(int dr, int dc, int r, int c, int sz) {
    if (sz == 2) {fill(dr, dc, r, c); return;}

    int hf = sz >> 1;
    int rh = r < hf ? 0 : 1, ch = c < hf ? 0 : 1;
    fill(dr + hf - 1, dc + hf - 1, rh, ch);

    if (rh != 0 || ch != 0) solve(dr, dc, hf - 1, hf - 1, hf);
    else solve(dr, dc, r, c, hf);
    if (rh != 1 || ch != 0) solve(dr + hf, dc, 0, hf - 1, hf);
    else solve(dr + hf, dc, r - hf, c, hf);
    if (rh != 0 || ch != 1) solve(dr, dc + hf, hf - 1, 0, hf);
    else solve(dr, dc + hf, r, c - hf, hf);
    if (rh != 1 || ch != 1) solve(dr + hf, dc + hf, 0, 0, hf);
    else solve(dr + hf, dc + hf, r - hf, c - hf, hf);
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    int k, a, b, sz; cin >> k >> b >> a;
    sz = 1 << k; a = sz - a; b = b - 1;
    arr[a][b] = -1; solve(0, 0, a, b, sz);

    for (int i = 0; i < sz; i++) {
        for (int j = 0; j < sz; j++) {
            cout << arr[i][j] << ' ';
        } cout << '\n';
    }

    return 0;
}
