#include <iostream>
using namespace std;

int main() {
    int target, initial_pulse, max_pulse, inc_pulse, dec_pulse;
    int pulse, minute = 0;
    cin >> target >> initial_pulse >> max_pulse >> inc_pulse >> dec_pulse;
    pulse = initial_pulse;
    if (max_pulse - initial_pulse < inc_pulse){
        minute = -1;
        target = 0;
    }

    while(target > 0){
        if (pulse + inc_pulse <= max_pulse){
            pulse += inc_pulse;
            target--;
        } else {
            pulse -= dec_pulse;
            if (pulse < initial_pulse){
                pulse = initial_pulse;
            }
        }
        minute++;
    }
    cout << minute;
    return 0;
}