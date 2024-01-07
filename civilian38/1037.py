#include <iostream>
using namespace std;

int main() {
    int repeat = 0;
    cin >> repeat;
    char path[51];
    cin >> path;
    for(int i = 0; i < repeat - 1; i++){
        char input[51];
        cin >> input;
        for(int j = 0; input[j] != '\0'; j++) {
            if (path[j] != input[j]){
                path[j] = '?';
            }
        }
    }
    cout << path;
    return 0;
}