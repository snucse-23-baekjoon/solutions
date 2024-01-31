#include <iostream>
using namespace std;

bool in_range(int x, int y){
    if(0 <= x && x <= 7 && 1 <= y && y <= 8){
        return true;
    }
    return false;
}

int main() {
    int repeat = 0;
    char king_x = 0, king_y = 0, stone_x = 0, stone_y = 0;
    char king[3], stone[3];
    cin >> king >> stone >> repeat;
    king_x = king[0] - 'A';
    king_y = king[1] - '0';
    stone_x = stone[0] - 'A';
    stone_y = stone[1] - '0';
    for(int i = 0; i < repeat; i++){

        int inc_x = 0, inc_y = 0;
        int index = 0;
        char input[3];
        cin >> input;
        while (input[index] != '\0'){
            switch (input[index]) {
                case 'R': inc_x++; break;
                case 'L': inc_x--; break;
                case 'B': inc_y--; break;
                case 'T': inc_y++; break;
            }
            index++;
        }

        if(in_range(king_x + inc_x, king_y + inc_y)){
            if(king_x + inc_x == stone_x && king_y + inc_y == stone_y){
                if(in_range(stone_x + inc_x, stone_y + inc_y)){
                    king_x += inc_x;
                    king_y += inc_y;
                    stone_x += inc_x;
                    stone_y += inc_y;
                }
            } else {
                king_x += inc_x;
                king_y += inc_y;
            }
        }
    }
    king[0] = king_x + 'A';
    king[1] = king_y + '0';
    king[2] = '\0';
    stone[0] = stone_x + 'A';
    stone[1] = stone_y + '0';
    stone[2] = '\0';
    cout << king << endl << stone;
    return 0;
}