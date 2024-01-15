#include <iostream>
using namespace std;

int main() {
    int num;
    cin >> num;
    char number[11];
    int index = 0;
    while(num){
        number[index] = '0' + (num % 10);
        number[index + 1] = '\0';
        num /= 10;
        index++;
    }
    int length = 0;
    for(int i = 0; number[i] != '\0'; i++){
        length++;
    }

    for(int i = 0; i < length; i++){
        for(int j = 0; j < length - 1 - i; j++){
            if(number[j] < number[j + 1]){
                char temp = number[j];
                number[j] = number[j + 1];
                number[j + 1] = temp;
            }
        }
    }
    for(int i = 0; i < index; i++){
        num *= 10;
        num += number[i] - '0';
    }

    cout << num;
    return 0;
}