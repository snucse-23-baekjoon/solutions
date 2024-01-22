#include <stdio.h>
#include <memory.h>
#include <vector>
#include <algorithm>
#define MAX 1000000

using namespace std;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<pi> vp;

typedef struct fenwick {
    int len;
    int tree[MAX];

    int lt(int i) {
        return sum(i);
    }

    int gt(int i) {
        return sum(len) - sum(i + 1);
    }

    void init(int l) {
        len = l;
        memset(tree, 0, sizeof tree);
    }

    void update(int i, int d) {
        for (i++; i <= len; i += i & -i)
            tree[i - 1] += d;
    }

    int sum(int i) {
        int a = 0;
        for (; i > 0; i -= i & -i)
            a += tree[i - 1];
        return a;
    }
} Fenwick;

Fenwick tree;
int lt[MAX], gt[MAX];

bool compare(pi a, pi b) {
    if (a.first == b.first)
        return a.second < b.second;
    return a.first < b.first;
}

void scan(int arr[], int len) {
    for (int i = 0; i < len; i++)
        scanf(" %d", &arr[i]);
}

void compress(int arr[], int len) {
    pi tmp1[len], tmp2[len];
    for (int i = 0; i < len; i++) {
        tmp1[i].first = arr[i];
        tmp1[i].second = i;
    }
    sort(tmp1, tmp1 + len, compare);
    for (int i = 0; i < len; i++) {
        tmp2[i].first = tmp1[i].second;
        if (i && tmp1[i - 1].first == tmp1[i].first)
            tmp2[i].second = tmp2[i - 1].second;
        else tmp2[i].second = i;
    }
    sort(tmp2, tmp2 + len, compare);
    for (int i = 0; i < len; i++)
        arr[i] = tmp2[i].second;
}

bool match(int arr[], int i, int j) {
    return tree.lt(arr[i]) == lt[j] 
        && tree.gt(arr[i]) == gt[j];
}

int main() {
    int n, m, x;
    scanf("%d %d", &n, &m);

    int p[n], t[m];
    scan(p, n); scan(t, m);
    compress(p, n); compress(t, m);

    tree.init(n);
    for (int i = 0; i < n; i++) {
        tree.update(p[i], 1);
        lt[i] = tree.lt(p[i]);
        gt[i] = tree.gt(p[i]);
    }

    int j = 0;
    tree.init(n);
    int fail[n]; fail[0] = 0;
    for (int i = 1; i < n; i++) {
        tree.update(p[i], 1);
        while (j && !match(p, i, j)) {
            for (int k = i - j; k < i - fail[j - 1]; k++)
                tree.update(p[k], -1);
            j = fail[j - 1];
        }
        if (match(p, i, j))
            fail[i] = ++j;
    }
    
    tree.init(m);
    vi answer; j = 0;
    for (int i = 0; i < m; i++) {
        tree.update(t[i], 1);
        while (j && !match(t, i, j)) {
            for (int k = i - j; k < i - fail[j - 1]; k++)
                tree.update(t[k], -1);
            j = fail[j - 1];
        }
        if (match(t, i, j)) {
            if (j == n - 1) {
                for (int k = i - j; k <= i - fail[j]; k++)
                    tree.update(t[k], -1);
                answer.push_back(i - n + 2);
                j = fail[j];
            } else j++;
        }
    }

    if (answer.empty()) printf("0");
    for (int i = 0; i < answer.size(); i++)
        printf("%d ", answer[i]);
    printf("\n");

    return 0;
}
