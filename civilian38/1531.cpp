#include <iostream>
using namespace std;

void printmap(int map[][100]){
    for(int i = 0; i < 100; i++){
        for(int j = 0; j < 100; j++){
            cout << map[i][j] << ' ';
        }
        cout << endl;
    }
}

int main() {
    int map[100][100] = {0};
    int repeat = 0, minimum = 0, count = 0;
    cin >> repeat >> minimum;
    for(int i = 0; i < repeat; i++){
        int start_x, start_y, end_x, end_y;
        cin >> start_x >> start_y >> end_x >> end_y;
        for(int j = start_x - 1; j < end_x; j++){
            for(int k = start_y - 1; k < end_y; k++){
                map[j][k] += 1;
                if(map[j][k] > minimum && map[j][k] <= repeat){
                    count++;
                    map[j][k] += repeat;
                }
            }
        }
    }
    cout << count;
    return 0;
}