#include <iostream>
#include <vector>
#include <algorithm>
#define SIZE 262144
#define ALL(vec) \
    vec.begin(), vec.end()
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

    vector<int> &left = mst[2 * node + 1], 
                &right = mst[2 * node + 2];
    curr.resize(left.size() + right.size());
    merge(ALL(left), ALL(right), curr.begin());
}

int query(
    int node, int start, int end,
    int left, int right, int value
) {
    if (end <= left || right <= start) return 0;
    if (left <= start && end <= right) {
        vector<int> &curr = mst[node];
        return curr.end() - lower_bound(ALL(curr), value);
    } int mid = (start + end + 1) / 2;
    return query(2 * node + 1, start, mid, left, right, value)
        + query(2 * node + 2, mid, end, left, right, value);
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    cin >> N;
    for (int i = 0; i < N; i++) cin >> arr[i];
    build_mst(0, 0, N);

    cin >> M;
    for (int i = 0, a = 0, b, c, d; i < M; i++) {
        cin >> b >> c >> d;
        b ^= a; c ^= a; d ^= a;
        a = query(0, 0, N, b - 1, c, d + 1);
        cout << a << '\n';
    }
    
    return 0;
}
