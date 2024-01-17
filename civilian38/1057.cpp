#include <iostream>
using namespace std;

int main() {
    int participants = 0, first = 0, second = 0;
    cin >> participants >> first >> second;
    int repeat = 0;
    while(first != second){
        if(participants == 1){
            cout << -1;
            repeat = 0;
            break;
        }
        repeat++;
        first = (first - 1) / 2 + 1;
        second = (second - 1) / 2 + 1;
        participants = participants / 2 + (participants % 2);
    }

    if(repeat){
        cout << repeat;
    }
    return 0;
}