#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef struct query_1 {int i; ll v;} q1;
typedef struct query_2 {int k; int i; int j; int o;} q2;
typedef struct fenwick {
    size_t size; ll *tree;
    void init(size_t __size) {
        size = __size;
        if (tree) free(tree);
        tree = (ll *) calloc(size, sizeof(ll));
    }
    void update(int i, ll x) {
        for (i++; i <= size; i += i & -i)
            tree[i - 1] += x;
    }
    ll sum(int i, int j) {
        return __sum(j) - __sum(i);
    }
    ll __sum(int i) {
        ll a = 0;
        for (; i > 0; i -= i & -i)
            a += tree[i - 1];
        return a;
    }
} Fenwick;

bool cmp(q2 x, q2 y) {
    return x.k < y.k;
}

int main() {
    freopen("../input.txt", "r", stdin);

    int n, m, q; ll v;
    vector<q1> query1;
    vector<q2> query2;
    Fenwick tree;

    scanf("%d", &n);
    tree.init(n);

    for (int i = 0; i < n; i++) {
        scanf(" %lld", &v);
        tree.update(i, v);
    }

    int j = 0;
    scanf(" %d", &m);
    for (int i = 0; i < m; i++) {
        scanf(" %d", &q);
        if (q == 1) {
            q1 tmp;
            scanf(" %d %lld", &tmp.i, &tmp.v);
            query1.push_back(tmp);
        } else {
            q2 tmp; tmp.o = j++;
            scanf(" %d %d %d", &tmp.k, &tmp.i, &tmp.j);
            query2.push_back(tmp);
        }
    }

    vector<ll> answer(j); j = 0;
    sort(query2.begin(), query2.end(), cmp);
    for (; j < query2.size() && query2[j].k == 0; j++)
        answer[query2[j].o] = tree.sum(query2[j].i - 1, query2[j].j);
    for (int i = 0; i < query1.size(); i++) {
        v = query1[i].v - tree.sum(query1[i].i - 1, query1[i].i);
        tree.update(query1[i].i - 1, v);
        for (; j < query2.size() && query2[j].k == i + 1; j++)
            answer[query2[j].o] = tree.sum(query2[j].i - 1, query2[j].j);
    }

    for (int i =0; i < answer.size(); i++)
        printf("%lld\n", answer[i]);
    return 0;
}
