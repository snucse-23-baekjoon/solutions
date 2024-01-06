#include <iostream>
using namespace std;

int main() {
    int people = 0;
    int max_people = 0;
    for(int i = 0; i < 4; i++){
        int in_train = 0, out_train = 0;
        cin >> out_train >> in_train;
        people += in_train - out_train;
        if (people > max_people){
            max_people = people;
        }
    }
    cout << max_people;
    return 0;
}