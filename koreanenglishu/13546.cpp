#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <cmath>
using namespace std;

#define SIZE 100'001
#define BKT_SIZE 333
#define LEN(x) x.back() - x.front()

int N, M, K, SQN;
int idx[SIZE], ans[SIZE];
pair<int, int> qry[SIZE];

bool compare(int x, int y) {
    pair<int, int> p = qry[x], q = qry[y];
    if (p.first / SQN == q.first / SQN)
        return p.second < q.second;
    return p.first < q.first;
}

struct max_finder {
    int l = 0, r = -1;
    int arr[SIZE]; list<int> lst[SIZE];
    int cnt[SIZE] = {0}, bkt[BKT_SIZE] = {0};
    void add(int x) {cnt[x]++; bkt[x / SQN]++;}
    void rem(int x) {cnt[x]--; bkt[x / SQN]--;}

    void move(int lt, int rt) {
        if (rt < r) while (rt < r) {
            list<int> &L = lst[arr[r--]];
            rem(LEN(L)); L.pop_back();
            if (!L.empty()) add(LEN(L));
        } else while (r < rt) {
            list<int> &L = lst[arr[++r]];
            if (!L.empty()) rem(LEN(L));
            L.push_back(r); add(LEN(L));
        } if (lt < l) while (lt < l) {
            list<int> &L = lst[arr[--l]];
            if (!L.empty()) rem(LEN(L));
            L.push_front(l); add(LEN(L));
        } else while (l < lt) {
            list<int> &L = lst[arr[l++]];
            rem(LEN(L)); L.pop_front();
            if (!L.empty()) add(LEN(L));
        }
    }

    int find() {
        int i = N / SQN; while (!bkt[i]) i--;
        int j = min((i + 1) * SQN, N) - 1;
        while (!cnt[j]) j--; return j;
    }
} finder;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    cin >> N >> K; SQN = sqrt(N);
    for (int i = 0; i < N; i++) cin >> finder.arr[i];

    cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> qry[i].first >> qry[i].second;
        qry[i].first--; qry[i].second--; idx[i] = i;
    } sort(idx, idx + M, compare);

    for (int i = 0; i < M; i++) {
        pair<int, int> q = qry[idx[i]];
        finder.move(q.first, q.second);
        ans[idx[i]] = finder.find();
    } for (int i = 0; i < M; i++)
        cout << ans[i] << '\n';

    return 0;
}
