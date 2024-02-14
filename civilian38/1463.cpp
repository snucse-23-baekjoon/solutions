#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    unordered_map<int, int> dictionary;
    dictionary[1] = 0;
    dictionary[2] = 1;
    dictionary[3] = 1;

    int number = 0, count = 3;
    cin >> number;
    if(number <= 3){
        cout << dictionary[number];
    } else {
        while(count < number){
            count++;
            int next = dictionary[count - 1] + 1;
            if(count % 3 == 0 && dictionary[count / 3] + 1 < next){
                next = dictionary[count / 3] + 1;
            }
            if(count % 2 == 0 && dictionary[count / 2] + 1 < next){
                next = dictionary[count / 2] + 1;
            }
            dictionary[count] = next;
        }
        cout << dictionary[count];
    }
    return 0;
}