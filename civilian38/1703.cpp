#include <iostream>
using namespace std;

int main() {
    int age = 0;
    cin >> age;
    while (age != 0){
        int branch = 1;
        for(int i = 0; i < age; i++){
            int split = 0, cut = 0;
            cin >> split >> cut;
            branch *= split;
            branch -= cut;
        }
        cout << branch << endl;
        cin >> age;
    }
    return 0;
}