#include <iostream>
using namespace std;

int main() {
    int num1 = 0, num2 = 0, num3 = 0;
    cin >> num1 >> num2 >> num3;
    int answer = 0;
    while(!(answer % 15 == num1 - 1 && answer % 28 == num2 - 1 && answer % 19 == num3 - 1)){
        answer++;
    }
    cout << answer + 1;
    return 0;
}