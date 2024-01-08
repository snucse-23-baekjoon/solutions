#include <iostream>
using namespace std;

int main() {
    int alphabets[26] = {0};
    char word[1000001];
    cin >> word;
    int point = 0;
    while (word[point] != '\0'){
        if ('a' <= word[point] && word[point] <= 'z'){
            alphabets[word[point] - 'a'] += 1;
        } else {
            alphabets[word[point] - 'A'] += 1;
        }
        point++;
    }

    int max_index = 0, max_count = 0;
    for(int i = 0; i < 26; i++){
        if (alphabets[i] > alphabets[max_index]){
            max_index = i;
            max_count = 1;
        } else if (alphabets[i] == alphabets[max_index]){
            max_count++;
        }
    }

    if(max_count == 1){
        cout << char(max_index + 'A');
    } else {
        cout << "?";
    }
    return 0;
}