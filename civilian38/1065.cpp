#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int repeat = 0;
    cin >> repeat;
    int count = - 1;
    for(int a = 0; a < 10; a++){
        if(a <= repeat){
            count++;
        }
        for(int d = -9; d < 10; d++){
            int number = a;
            if(
                    (a + d) > 0 &&
                    (a + d) < 10 &&
                    number + (10 * (a + d)) <= repeat
                ){
                number += 10 * (a + d);
                count++;
            }
            if(
                    (a + (2 * d)) > 0 &&
                    (a + (2 * d)) < 10 &&
                    number + (100 * (a + (2 * d))) <= repeat
               ){
                number += 100 * (a + (2 * d));
                count++;
            }
        }
    }
    cout << count;
    return 0;
}