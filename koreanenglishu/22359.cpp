#include <iostream>
#define MAX 1024

using namespace std;

char arr[MAX][MAX];

void fill(int dr, int dc, int r, int c, char ch) {
    if (r != 0 || c != 0) arr[0 + dr][0 + dc] = ch;
    if (r != 1 || c != 0) arr[1 + dr][0 + dc] = ch;
    if (r != 0 || c != 1) arr[0 + dr][1 + dc] = ch;
    if (r != 1 || c != 1) arr[1 + dr][1 + dc] = ch;
}

void solve(int dr, int dc, int r, int c, int sz) {
    if (sz == 2) {
        char ch = (dr + dc) % 4 ? 'b' : 'a';
        fill(dr, dc, r, c, ch); return;
    }

    int hf = sz >> 1;
    int rh = r < hf ? 0 : 1, ch = c < hf ? 0 : 1;
    fill(dr + hf - 1, dc + hf - 1, rh, ch, 'c');

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
    // FOR TEST; REMOVE BEFORE SUBMISSION
    freopen("../input.txt", "r", stdin);

    int t, k, a, b;
    scanf("%d %d", &t, &k);

    int sz = 1 << k;
    while (t--) {
        scanf(" %d %d", &a, &b);
        arr[--a][--b] = '@';
        solve(0, 0, a, b, sz);

        for (int i = 0; i < sz; i++) {
            for (int j = 0; j < sz; j++) {
                printf("%c", arr[i][j]);
            }
            printf("\n");
        }
    }

    return 0;
}
