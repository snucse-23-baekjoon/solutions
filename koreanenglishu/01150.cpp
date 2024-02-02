#include <cstdio>
#include <queue>
#define MAX 100002

using namespace std;

typedef struct {
    int left, right, len;
} cable;

struct compare {
    bool operator() (cable a, cable b) {
        return a.len > b.len;
    }
};

int main() {
    // FOR TEST; REMOVE BEFORE SUBMISSION
    freopen("../input.txt", "r", stdin);

    int n, k, x1, x2, ans = 0;
    scanf("%d %d %d", &n, &k, &x1);

    cable arr[MAX];
    arr[n].left = n - 1;
    arr[n].right = n + 1;
    
    priority_queue<cable,
        vector<cable>, compare> pq;
    for (int i = 1; i < n; i++) {
        scanf(" %d", &x2);
        cable tmp = {i, i + 1, x2 - x1};
        arr[i] = tmp; arr[i].left--;
        pq.push(tmp); x1 = x2;
    }

    while (k--) {
        cable tmp = pq.top(); pq.pop();
        int left = tmp.left;
        int right = tmp.right;
        int len = tmp.len;
        while (
            left < 1 || right > n
            || right != arr[left].right
            || left != arr[right].left
        ) {
            tmp = pq.top(); pq.pop();
            left = tmp.left;
            right = tmp.right;
            len = tmp.len;
        }

        ans += len;
        int next_left = arr[left].left;
        int next_right = arr[right].right;
        arr[next_left].len += arr[right].len - len;
        arr[next_left].right = next_right;
        arr[next_right].left = next_left;

        tmp.left = next_left;
        tmp.right = next_right;
        tmp.len = arr[next_left].len;
        pq.push(tmp);
    }

    printf("%d\n", ans);
    return 0;
}
