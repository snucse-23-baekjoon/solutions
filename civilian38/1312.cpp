#include <iostream>
using namespace std;

int main() {
    int num1 = 0, num2 = 0, num3 = 0;
    cin >> num1 >> num2 >> num3;
    while (num1 / num2){
        num1 = num1 % num2;
    }
    for (int i = 1; i < num3; i++){
        num1 = (num1 * 10) % num2;
    }
    cout << (10 * num1) / num2;
    return 0;
}