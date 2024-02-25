#include <iostream>
#include <string>
#define MAX 1000002
using namespace std;

int N, Q; string S;
int Rsum[MAX], Psum[MAX];
int Prng[MAX], locs[MAX];
long long Dsum[MAX];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    cin >> N >> Q >> S; int j = 0;
    for (int i = 0; i < N; i++) {
        Rsum[i + 1] = Rsum[i] + (S[i] == 'R');
        Psum[i + 1] = Psum[i] + (S[i] == 'P');
        if (S[i] == 'R') {
            for (int k = j + 1; k < i + 2; k++)
                Prng[k] = Psum[i + 1] - Psum[j];
            j = i + 1;
        } if (S[i] != '.')
            locs[Rsum[i + 1] + Psum[i + 1]] = i + 1;
    }
    
    long long M = Rsum[N] + Psum[N] + 1;
    for (int k = j + 1; k < N + 1; k++)
        Prng[k] = Psum[N] - Psum[j];
    locs[M] = N + 1;

    for (int i = 0; i < M; i++)
        Dsum[i + 1] = Dsum[i] + (long long)
            (i + 1) * (locs[i + 1] - locs[i]);

    int p, q;
    long long r, t;
    while (Q--) {
        cin >> q;
        r = Psum[q] + Rsum[q] + 1;
        if (Rsum[N] == 0) {
            if (2 * Psum[q] < Psum[N]) {
                p = 2 * Psum[q] + 1;
                t = locs[r] - q
                    + 2 * Dsum[r] - locs[r]
                    + 4 * r * (locs[2 * r - 1] - locs[r])
                    - 2 * (Dsum[2 * r - 1] - Dsum[r]);
            } else {
                p = 2 * (Psum[N] - Psum[q]);
                t = locs[r] - q
                    + (2 * M + 1) * (locs[M] - locs[r])
                    - 2 * (Dsum[M] - Dsum[r])
                    + 2 * (Dsum[r] - Dsum[2 * r - M])
                    - 2 * (2 * r - M) * (locs[r] - locs[2 * r - M]);
            }
        } else if (Rsum[q] == 0) {
            if (2 * Psum[q] < Prng[q]) {
                p = 2 * Psum[q] + 1;
                t = 2 * Dsum[r] - q
                    + 4 * r * (locs[2 * r - 1] - locs[r])
                    - 2 * (Dsum[2 * r - 1] - Dsum[r]);
            } else {
                p = Prng[q];
                t = 2 * Dsum[r] - q
                    + 4 * r * (locs[p + 1] - locs[r])
                    - 2 * (Dsum[p + 1] - Dsum[r]);
            }
        } else if (Rsum[q] == Rsum[N]) {
            if (2 * (Psum[N] - Psum[q]) < Prng[q]) {
                p = 2 * (Psum[N] - Psum[q]);
                t = locs[r] - q
                    + (2 * M + 1) * (locs[M] - locs[r])
                    - 2 * (Dsum[M] - Dsum[r])
                    + 2 * (Dsum[r] - Dsum[2 * r - M])
                    - 2 * (2 * r - M) * (locs[r] - locs[2 * r - M]);
            } else {
                p = Prng[q];
                t = locs[r] - q
                    + (2 * M + 1) * (locs[M] - locs[r])
                    - 2 * (Dsum[M] - Dsum[r])
                    + 2 * (Dsum[r] - Dsum[M - p - 1])
                    - 2 * (2 * r - M) * (locs[r] - locs[M - p - 1]);
            }
        } else {p = Prng[q]; t = -1;}
        cout << p << ' ' << t << '\n';
    } return 0;
}
