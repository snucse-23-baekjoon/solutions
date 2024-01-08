#include <iostream>
using namespace std;

int calculator(int base, int left){
    if (base < left){
        return base * base + calculator(base + 1, left - base);
    }
    return base * left;
}

int main() {
    int num1 = 0, num2 = 0;
    cin >> num1 >> num2;
    cout << calculator(1, num2) - calculator(1, num1 - 1);
    return 0;
}