#include <iostream>
using namespace std;

int main() {
    int repeat = 0;
    cin >> repeat;
    for(int i = 0; i < repeat; i++){
        int number = 0;
        cin >> number;
        int *ones = new int[number + 1];
        int *zeros = new int[number + 1];
        ones[0] = 0;
        ones[1] = 1;
        zeros[0] = 1;
        zeros[1] = 0;
        for(int j = 2; j < number + 1; j++){
            ones[j] = ones[j - 1] + ones[j - 2];
            zeros[j] = zeros[j - 1] + zeros[j - 2];
        }
        cout << zeros[number] << " " << ones[number] << endl;
    }
    return 0;
}