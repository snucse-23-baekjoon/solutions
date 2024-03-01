#include <iostream>
#include <vector>
#include <queue>
#define MAX 200'000
using namespace std;
using lint = long long;

int N, arr[MAX]; lint H, ans;
priority_queue<lint> lqueue;
priority_queue<lint, vector<
    lint>, greater<lint>> rqueue;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    cin >> N >> H;
    for (int i = 0; i < N; i++) cin >> arr[i];
    lqueue.push(arr[0]); rqueue.push(arr[0]);
    for (int i = 1; i < N; i++) {
        lint lopt = lqueue.top() - H * i;
        lint ropt = rqueue.top() + H * i;
        if (arr[i] < lopt) {
            lqueue.push(arr[i] + H * i);
            lqueue.push(arr[i] + H * i);
            lqueue.pop();
            rqueue.push(lopt - H * i);
            ans += lopt - arr[i];
        } else if (arr[i] > ropt) {
            rqueue.push(arr[i] - H * i);
            rqueue.push(arr[i] - H * i);
            rqueue.pop();
            lqueue.push(ropt + H * i);
            ans += arr[i] - ropt;
        } else {
            lqueue.push(arr[i] + H * i);
            rqueue.push(arr[i] - H * i);
        }
    }

    cout << ans << '\n';
    return 0;
}
