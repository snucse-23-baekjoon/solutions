#include <iostream>
using namespace std;

void infect(int number, int computer, int* infection, int** connection){
    for(int i = 0; i < number; i++){
        if(connection[computer][i] == 1){
            if (infection[i] == 0){
                infection[i] = 1;
                infect(number, i, infection, connection);
            }
        }
    }
}

int main() {
    int number = 0, repeat = 0;
    cin >> number >> repeat;
    int** connection = new int*[number];
    for(int i = 0; i < number; i++){
        connection[i] = new int[number];
        for(int j = 0; j < number; j++){
            connection[i][j] = 0;
        }
    }

    for(int i = 0; i < repeat; i++){
        int computer1 = 0, computer2 = 0;
        cin >> computer1 >> computer2;
        connection[computer1 - 1][computer2 - 1] = 1;
        connection[computer2 - 1][computer1 - 1] = 1;
    }

    int *infected = new int[number];
    for(int i = 0; i < number; i++){
        infected[i] = 0;
    }

    infect(number, 0, infected, connection);

    int count = -1;
    for(int i = 0; i < number; i++){
        if (infected[i] == 1){
            count++;
        }
    }

    if(count == -1){
        count = 0;
    }
    cout << count;

    delete[] infected;
    for (int i = 0; i < number; ++i) {
        delete[] connection[i];
    }
    delete[] connection;
    return 0;
}