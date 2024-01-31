#include <iostream>
using namespace std;

int main() {
    int number = 0;
    cin >> number;

    bool checker = true;
    for(int i = 1; i <= number; i++){
        int count = i;
        int tmp = i;
        while(tmp){
            count += tmp % 10;
            tmp /= 10;
        }

        if(count == number){
            cout << i;
            checker = false;
            break;
        }
    }

    if(checker){
        cout << 0;
    }
    return 0;
}