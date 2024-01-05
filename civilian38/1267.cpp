#include <iostream>
using namespace std;

int main() {
    int young = 0, minsik = 0;
    int number = 0;
    cin >> number;

    for(int i = 0; i < number; i++){
        int length = 0;
        cin >> length;
        young += (length / 30 + 1) * 10;
        minsik += (length / 60 + 1) * 15;
    }

    if(young < minsik) { cout << "Y " << young; }
    else if (minsik < young) { cout << "M " << minsik; }
    else { cout << "Y M " << young; }
    return 0;
}