#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#define SIZE 100000
#define MAX 1000000
using namespace std;

int N, M, K;
int ans[SIZE], idx[SIZE];
pair<int, int> qry[SIZE];

struct counter {
    int arr[SIZE], repeat[MAX] = {0};
    int left = 0, right = -1, count = 0;
    void move(int left_tar, int right_tar) {
        if (right_tar < right) {
            while (right_tar < right)
                if (!--repeat[arr[right--]]) count--;
        } else {
            while (right < right_tar)
                if (!repeat[arr[++right]]++) count++;
        } if (left_tar < left) {
            while (left_tar < left)
                if (!repeat[arr[--left]]++) count++;
        } else {
            while (left < left_tar)
                if (!--repeat[arr[left++]]) count--;
        }
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
    
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> cnt.arr[i]; cnt.arr[i]--;
    } cin >> M; K = sqrt(N);
    for (int i = 0; i < M; i++) {
        cin >> qry[i].first >> qry[i].second;
        qry[i].first--; qry[i].second--; idx[i] = i;
    } sort(idx, idx + M, compare);

    for (int i = 0; i < M; i++) {
        pair<int, int> q = qry[idx[i]];
        cnt.move(q.first, q.second);
        ans[idx[i]] = cnt.count;
    } for (int i = 0; i < M; i++)
        cout << ans[i] << '\n';

    return 0;
}
