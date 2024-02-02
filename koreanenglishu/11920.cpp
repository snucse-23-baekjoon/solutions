#include <iostream>
#include <queue>

using namespace std;

int main() {
    // FOR FAST I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    // FOR TEST; REMOVE BEFORE SUBMISSION
    freopen("../input.txt", "r", stdin);

    int N, K, x;
    cin >> N >> K;
    priority_queue<int,
        vector<int>, greater<int>> pq;
    for (int i = 0; i < K; i++) {
        cin >> x; pq.push(x);
    }
    for (int i = 0; i < N - K; i++) {
        cin >> x; pq.push(x);
        cout << pq.top() << " "; pq.pop();
    }
    for (int i = 0; i < K; i++) {
        cout << pq.top() << " "; pq.pop();
    }
    cout << "\n";

    return 0;
}
