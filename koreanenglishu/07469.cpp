#include <iostream>
#include <vector>
#include <algorithm>
#define SIZE 262'144
#define MAX 1'000'000'000
#define ALL(vec) vec.begin(), vec.end()
using namespace std;

int N, M, arr[SIZE];
vector<int> mst[SIZE];

void build_mst(int node, int start, int end) {
    vector<int> &curr = mst[node];
    if (start + 1 == end) {
        curr.push_back(arr[start]); return;
    } int mid = (start + end + 1) / 2;
    build_mst(2 * node + 1, start, mid);
    build_mst(2 * node + 2, mid, end);

    const vector<int>
        &left = mst[2 * node + 1], 
        &right = mst[2 * node + 2];
    curr.resize(left.size() + right.size());
    merge(ALL(left), ALL(right), curr.begin());
}

int count(
    int node, int start, int end,
    int left, int right, int value
) {
    if (end <= left || right <= start) return 0;
    if (left <= start && end <= right) {
        const vector<int> &curr = mst[node];
        return lower_bound(ALL(curr), value) - curr.begin();
    } int mid = (start + end + 1) / 2;
    return count(2 * node + 1, start, mid, left, right, value)
        + count(2 * node + 2, mid, end, left, right, value);
}

int query(
    int start, int end,
    int left, int right, int value
) {
    if (start + 1 == end) return start;
    int mid = (start + end) / 2;
    if (count(0, 0, N, left, right, mid) >= value) {
        return query(start, mid, left, right, value);
    } else {
        return query(mid, end, left, right, value);
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    cin >> N >> M;
    for (int i = 0; i < N; i++) cin >> arr[i];
    build_mst(0, 0, N);

    for (int i = 0, a, b, c; i < M; i++) {
        cin >> a >> b >> c;
        cout << query(-MAX, MAX + 1, a - 1, b, c) << '\n';
    }

    return 0;
}
