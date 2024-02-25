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
    int count = 0; ball R, B;
    bool operator==(const query q) const {
        return R == q.R && B == q.B;
    } void move(int di, int dj) { count++;
        while (MAP(R) == '.' && !(R == B)) R.move(di, dj);
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

int bfs(query q) {
    queue<query> Q; Q.push(q);
    while (!Q.empty()) {
        if (Q.front().count < 10) {
            q = Q.front(); q.move(UP);
            if (q.clear()) return q.count;
            if (!q.over()) Q.push(q);
            q = Q.front(); q.move(DOWN);
            if (q.clear()) return q.count;
            if (!q.over()) Q.push(q);
            q = Q.front(); q.move(LEFT);
            if (q.clear()) return q.count;
            if (!q.over()) Q.push(q);
            q = Q.front(); q.move(RIGHT);
            if (q.clear()) return q.count;
            if (!q.over()) Q.push(q);
        } Q.pop();
    } return -1;
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

    int ans = bfs(q);
    cout << (ans > 0 ? 1 : 0) << '\n';
    return 0;
}
