#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    long long x = 0, y = 0;
    cin >> x >> y;
    long long z = (100 * y) / x;
    if(z >= 99){
        cout << -1;
    } else {
        long long front = 1;
        long long back = x;
        while((100 * (back + y)) / (back + x) <= z){
            back += x;
        }

        while(front < back){
            long long front_length = (100 * (y + front)) / (x + front);
            long long back_length = (100 * (y + back)) / (x + back);
            if(front + 1 == back){
                if(front_length >= z + 1){
                    back = front;
                } else {
                    front = back;
                }
            }
            long long pin = (front + back) / 2;
            long long nz = (100 * (y + pin)) / (x + pin);
            if(nz < z + 1){
                front = pin;
            } else {
                back = pin;
            }
        }
        cout << front;
    }
    return 0;
}