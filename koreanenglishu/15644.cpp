#include <iostream>
#include <vector>
#include <queue>
#define UP -1, 0
#define DOWN 1, 0
#define LEFT 0, -1
#define RIGHT 0, 1
#define MAP(x) map[x.i][x.j]
using namespace std;

char map[10][10];

struct ball {
    int i, j;
    bool operator==(const ball b) const {
        return i == b.i && j == b.j;
    } void move(int di, int dj) {
        i += di; j += dj;
    }
};

struct query {
    vector<char> order; ball R, B;
    query operator=(const query q) const {
        vector<char> temp_order(order);
        return {temp_order, R, B};
    } bool operator==(const query q) const {
        return R == q.R && B == q.B;
    } void move(int di, int dj) {
        switch (2 * di + dj) {
            case -2: {order.push_back('U'); break;}
            case 2: {order.push_back('D'); break;}
            case -1: {order.push_back('L'); break;}
            case 1: {order.push_back('R'); break;}
        } while (MAP(R) == '.' && !(R == B)) R.move(di, dj);
        if (MAP(R) == 'O') R = {-1, -1};
        else R.move(-di, -dj);
        while (MAP(B) == '.' && !(R == B)) B.move(di, dj);
        if (MAP(B) == 'O') B = {-1, -1};
        else B.move(-di, -dj);
        if (R.i == -1) return;
        while (MAP(R) == '.' && !(R == B)) R.move(di, dj);
        if (MAP(R) == 'O') R = {-1, -1};
        else R.move(-di, -dj);
    } bool clear() {
        return R.i == -1 && B.i != -1;
    } bool over() {
        return B.i == -1;
    }
};

vector<char> bfs(query q) {
    queue<query> Q; Q.push(q);
    while (!Q.empty()) {
        if (Q.front().order.size() < 10) {
            query qu = Q.front(); qu.move(UP);
            if (qu.clear()) return qu.order;
            if (!qu.over()) Q.push(qu);
            query qd = Q.front(); qd.move(DOWN);
            if (qd.clear()) return qd.order;
            if (!qd.over()) Q.push(qd);
            query ql = Q.front(); ql.move(LEFT);
            if (ql.clear()) return ql.order;
            if (!ql.over()) Q.push(ql);
            query qr = Q.front(); qr.move(RIGHT);
            if (qr.clear()) return qr.order;
            if (!qr.over()) Q.push(qr);
        } Q.pop();
    } return {};
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    query q;
    int N, M; cin >> N >> M;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> map[i][j];
            if (map[i][j] == 'R') {
                q.R = {i, j}; map[i][j] = '.';
            } if (map[i][j] == 'B') {
                q.B = {i, j}; map[i][j] = '.';
            }
        }
    }

    vector<char> ans = bfs(q);
    if (!ans.size()) cout << -1;
    else {
        cout << ans.size() << '\n';
        for (char c: ans) cout << c;
    } cout << '\n';
    return 0;
}
