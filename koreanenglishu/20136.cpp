#include <cstdio>
#include <cstring>
#include <unordered_set>
#include <queue>
using namespace std;

int main() {
    // FOR TEST; REMOVE BEFORE SUBMISSION
    freopen("../input.txt", "r", stdin);

    int n, k; scanf("%d %d", &n, &k);
    int app[k], next[k], temp[k];
    for (int i = 0; i < k; i++) {
        scanf(" %d", &app[i]);
        app[i]--; temp[i] = k;
    }
    for (int i = k - 1; i > -1; i--) {
        next[i] = temp[app[i]];
        temp[app[i]] = i;
    }
    
    int i = 0, j, ans = 0;
    unordered_set<int> set;
    priority_queue<int> pq;
    for (; i < k && set.size() < n; i++) {
        set.insert(app[i]); pq.push(next[i]);
    }
    for (; i < k; i++) {
        if (set.find(app[i]) == set.end()) {
            j = pq.top(); pq.pop();
            if (j < k) set.erase(app[j]);
            set.insert(app[i]); ans++;
        }
        pq.push(next[i]);
    }

    printf("%d\n", ans);
    return 0;
}
