#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    int number = 0;
    cin >> number;

    for(int i = 1; i < number + 1; i++){
        q.push(i);
    }

    int last = q.front();
    q.pop();
    while(q.size()){
        last = q.front();
        q.push(last);
        q.pop();
        q.pop();
    }

    cout << last;
    return 0;
}