#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef struct pair_int {int a; int b;} pi;
bool cmp(pi x, pi y) {return x.b < y.b;}

int main() {
    // FOR TEST: REMOVE BEFORE SUBMISSION
    freopen("../input.txt", "r", stdin);

    int n; scanf("%d", &n); pi arr[n];
    for (int i = 0; i < n; i++) scanf(" %d", &arr[i].a);
    for (int i = 0; i < n; i++) scanf(" %d", &arr[i].b);
    sort(arr, arr + n, cmp);

    ll ans = arr[0].a; priority_queue<int> pq;
    for (int i = 1; i < n - 1; i += 2) {
        pq.push(arr[i].a); pq.push(arr[i + 1].a);
        ans += pq.top(); pq.pop();
    }

    printf("%lld\n", ans);
    return 0;
}
