#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

typedef long long ll;
typedef struct fenwick {
    int size;
    ll *tree_a0, *tree_a1;
    void init(int __size) {
        size = __size;
        tree_a0 = (ll *) calloc(size, sizeof(ll));
        tree_a1 = (ll *) calloc(size, sizeof(ll));
    }
    void __update(ll tree[], int i, ll x) {
        for (i++; i <= size; i += i & -i)
            tree[i - 1] += x;
    }
    ll __sum(ll tree[], int i) {
        ll a = 0;
        for (; i > 0; i -= i & -i)
            a += tree[i - 1];
        return a;
    }
    void update(int i, int j, ll x) {
        __update(tree_a0, i, i * -x);
        __update(tree_a0, j, j * x);
        __update(tree_a1, i, x);
        __update(tree_a1, j, -x);
    }
    ll sum(int i, int j) {
        ll a = 0;
        a -= __sum(tree_a0, i) + __sum(tree_a1, i) * i;
        a += __sum(tree_a0, j) + __sum(tree_a1, j) * j;
        return a;
    }
} Fenwick;

int main() {
    freopen("../input.txt", "r", stdin);

    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);

    ll x; Fenwick tree; tree.init(n);
    for (int i = 0; i < n; i++) {
        scanf(" %lld", &x);
        tree.update(i, i + 1, x);
    }

    int a, b, c; ll d;
    for (int i = 0; i < m + k; i++) {
        scanf(" %d", &a);
        if (a == 1) {
            scanf(" %d %d %lld", &b, &c, &d);
            tree.update(b - 1, c, d);
        }
        if (a == 2) {
            scanf(" %d %d", &b, &c);
            printf("%lld\n", tree.sum(b - 1, c));
        }
    }

    return 0;
}
