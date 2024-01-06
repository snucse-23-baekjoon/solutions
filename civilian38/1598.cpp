#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    int num1 = 0, num2 = 0;
    cin >> num1 >> num2;
    num1--;
    num2--;
    cout << abs((num1 / 4) - (num2 / 4)) + abs((num1 % 4) - (num2 % 4));
    return 0;
}