#include <iostream>
using namespace std;

int main() {
    int repeat = 0, count = 0;
    cin >> repeat;
    for(int i = 0; i < repeat; i++){
        char word[101];
        bool alphabets[26] = {false};
        cin >> word;
        int rp = 0;
        while(word[rp] != '\0'){
            if(alphabets[word[rp] - 'a']){
                break;
            } else {
                int j = 0;
                alphabets[word[rp] - 'a'] = true;
                while(word[rp] == word[rp + j]){ j++; }
                rp += j;
            }
        }
        if(word[rp] == '\0'){
            count++;
        }
    }

    cout << count;
    return 0;
}