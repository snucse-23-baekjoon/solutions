#include <iostream>
#include <queue>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0); // for fast I/O
    freopen("../input.txt", "r", stdin); // for input test

    long long ans = 0;
    priority_queue<int> pq;
    int n, a; cin >> n >> a;
    int b[n]; pq.push(a); b[0] = a;
    for (int i = 1; i < n; i++) {
        cin >> a; a -= i;
        if (a < pq.top()) {
            ans += pq.top() - a; pq.pop();
            pq.push(a); pq.push(a);
        } else pq.push(a);
        b[i] = pq.top() + i;
    } for (int i = n - 1; i; i--) {
        b[i - 1] = min(b[i - 1], b[i] - 1);
    } for (int i = 0; i < n; i++) {
        cout << b[i] << '\n';
    } return 0;
}
