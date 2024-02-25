#include <iostream>
using namespace std;

void hanoi(int k, int src, int aux, int dst) {
    if (!k) return;
    hanoi(k - 1, src, dst, aux);
    cout << src << ' ' << dst << '\n';
    hanoi(k - 1, aux, src, dst);
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int K; cin >> K; cout << (1 << K) - 1 << '\n';
    hanoi(K, 1, 2, 3); return 0;
}
