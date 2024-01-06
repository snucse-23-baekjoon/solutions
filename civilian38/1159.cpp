#include <iostream>
#include <map>
using namespace std;

int main() {
    map<char, int> letter;
    for(char let = 'a'; let <= 'z'; let++){
        letter[let] = 0;
    }
    int repeat = 0;
    cin >> repeat;

    for(int i = 0; i < repeat; i++){
        char name[31];
        cin >> name;
        letter[name[0]] += 1;
    }

    char out[27];
    int length = 0;
    for(char let = 'a';  let <= 'z'; let++){
        if(letter[let] >= 5){
            out[length++] = let;
            out[length] = '\0';
        }
    }

    if(length == 0){
        cout << "PREDAJA";
    } else {
        cout << out;
    }
    return 0;
}