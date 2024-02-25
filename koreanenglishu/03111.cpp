#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
using namespace std;

string A, R, T; int sz;
deque<char> pre, mid, suf;

bool comp() {
    if (mid.size() < A.size()) return false;
    deque<char>::iterator iter = mid.begin();
    for (char c: A) {
        if (c == *iter) iter++;
        else return false;
    } return true;
}

bool rcomp() {
    if (mid.size() < R.size()) return false;
    deque<char>::reverse_iterator iter = mid.rbegin();
    for (char c: R) {
        if (c == *iter) iter++;
        else return false;
    } return true;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    freopen("../input.txt", "r", stdin);

    cin >> A >> T; R = A; sz = A.size();
    reverse(R.begin(), R.end());
    for (char c: T) mid.push_back(c);

    while (true) {
        while (!comp()) {
            if (mid.empty()) break;
            pre.push_back(mid.front());
            mid.pop_front();
        } if (mid.empty()) break;
        for (int i = 0; i < sz; i++)
            mid.pop_front();
        
        for (int i = 1; i < sz; i++) {
            if (pre.empty()) break;
            mid.push_front(pre.back());
            pre.pop_back();
        } for (int i = 1; i < sz; i++) {
            if (suf.empty()) break;
            mid.push_back(suf.front());
            suf.pop_front();
        }

        while (!rcomp()) {
            if (mid.empty()) break;
            suf.push_front(mid.back());
            mid.pop_back();
        } if (mid.empty()) break;
        for (int i = 0; i < sz; i++)
            mid.pop_back();
        
        for (int i = 1; i < sz; i++) {
            if (suf.empty()) break;
            mid.push_back(suf.front());
            suf.pop_front();
        } for (int i = 1; i < sz; i++) {
            if (pre.empty()) break;
            mid.push_front(pre.back());
            pre.pop_back();
        }
    }

    for (char c: pre) cout << c;
    for (char c: suf) cout << c;
    cout << '\n';
    return 0;
}
