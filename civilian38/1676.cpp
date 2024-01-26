#include <iostream>
using namespace std;

int fact(int num){
    int original = num;
    if(num < 5){
        return 0;
    }
    int count = 0;
    while(num % 5 == 0){
        count++;
        num /= 5;
    }
    return count + fact(original - 1);
}

int main() {
    int number = 0;
    cin >> number;
    cout << (fact(number));

    return 0;
}