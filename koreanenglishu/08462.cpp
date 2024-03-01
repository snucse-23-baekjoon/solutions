#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#define SIZE 100001
#define MAX 1000001
using namespace std;

int N, M, K, idx[SIZE];
long long ans[SIZE];
pair<int, int> qry[SIZE];

struct counter {
    long long power = 0;
    int left = 0, right = -1;
    int arr[SIZE], cnt[MAX] = {0};

    void add(long long x) {
        power += (2 * ++cnt[x] - 1) * x;
    }
    
    void rem(long long x) {
        power -= (2 * cnt[x]-- - 1) * x;
    }

    void move(int ltar, int rtar) {
        if (rtar < right) while (rtar < right) rem(arr[right--]);
        else while (right < rtar) add(arr[++right]);
        if (ltar < left) while (ltar < left) add(arr[--left]);
        else while (left < ltar) rem(arr[left++]);
    }
} cnt;

bool compare(int x, int y) {
    pair<int, int> p = qry[x], q = qry[y];
    if (p.first / K == q.first / K)
        return p.second < q.second;
    return p.first < q.first;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);
    
    cin >> N >> M; K = sqrt(N);
    for (int i = 0; i < N; i++) {
        cin >> cnt.arr[i];
    } for (int i = 0; i < M; i++) {
        cin >> qry[i].first >> qry[i].second;
        qry[i].first--; qry[i].second--; idx[i] = i;
    } sort(idx, idx + M, compare);

    for (int i = 0; i < M; i++) {
        pair<int, int> q = qry[idx[i]];
        cnt.move(q.first, q.second);
        ans[idx[i]] = cnt.power;
    } for (int i = 0; i < M; i++)
        cout << ans[i] << '\n';

    return 0;
}
