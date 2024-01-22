#include <stdio.h>
#include <stdlib.h>

typedef long long ll;
typedef struct fenwick {
    int size;
    ll *tree_a0, *tree_a1, *tree_a2;
    void init(int __size) {
        size = __size;
        tree_a0 = (ll *) calloc(size, sizeof(ll));
        tree_a1 = (ll *) calloc(size, sizeof(ll));
        tree_a2 = (ll *) calloc(size, sizeof(ll));
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
    void update_point(int i, ll x) {
        __update(tree_a0, i, x * 2);
    }
    void update(int l, int r) {
        ll L = (ll) l, R = (ll) r;
        __update(tree_a0, l, L * L - l);
        __update(tree_a1, l, -2 * L + 1);
        __update(tree_a2, l, 1);
        __update(tree_a0, r, R * R - 2 * R * L + R);
        __update(tree_a1, r, 2 * L - 1);
        __update(tree_a2, r, -1);
    }
    ll check(int i) {
        ll a = 0;
        a -= __sum(tree_a0, i);
        a -= __sum(tree_a1, i) * i;
        a -= __sum(tree_a2, i) * i * i;
        a += __sum(tree_a0, i + 1);
        a += __sum(tree_a1, i + 1) * (i + 1);
        a += __sum(tree_a2, i + 1) * (i + 1) * (i + 1);
        return a / 2;
    }
} Fenwick;

int main() {
    freopen("../input.txt", "r", stdin);

    int n; ll x;
    scanf("%d", &n);
    Fenwick tree;
    tree.init(n);

    for (int i = 0; i < n; i++) {
        scanf(" %lld", &x);
        tree.update_point(i, x);
    }
    
    int q, a, b, c;
    scanf(" %d", &q);
    for (int i = 0; i < q; i++) {
        scanf(" %d", &a);
        if (a == 1) {
            scanf(" %d %d", &b, &c);
            tree.update(b - 1, c);
        } else {
            scanf(" %d", &b);
            printf("%lld\n", tree.check(b - 1));
        }
    }
    return 0;
}
