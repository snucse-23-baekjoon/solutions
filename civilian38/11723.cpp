#include <iostream>
using namespace std;

bool myStringCmp(const char* arr1, const char* arr2) {
    for (int i = 0; arr1[i] != '\0' || arr2[i] != '\0'; ++i) {
        if (arr1[i] != arr2[i]) {
            return false;
        }
    }
    return true;
}

class set{
private:
    bool data[20]{};
public:
    set();
    void add(int x);
    void remove(int x);
    int check(int x);
    void toggle(int x);
    void all();
    void empty();
};

set::set(){
    for(int i = 0; i < 20; i++){
        data[i] = false;
    }
}

void set::add(int x) {
    data[x - 1] = true;
}

void set::remove(int x) {
    data[x - 1] = false;
}

int set::check(int x) {
    if(data[x - 1]){
        return 1;
    }
    return 0;
}

void set::toggle(int x) {
    if(data[x - 1]){
        data[x - 1] = false;
    } else {
        data[x - 1] = true;
    }
}

void set::all() {
    for(int i = 0; i < 20; i++){
        data[i] = true;
    }
}

void set::empty() {
    for(int i = 0; i < 20; i++){
        data[i] = false;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    set dt;
    int repeat = 0;
    cin >> repeat;

    for(int i = 0; i < repeat; i++){
        char operation[20];
        cin >> operation;
        if(myStringCmp(operation, "add")){
            int x;
            cin >> x;
            dt.add(x);
        } else if(myStringCmp(operation, "remove")){
            int x;
            cin >> x;
            dt.remove(x);
        } else if(myStringCmp(operation, "check")){
            int x;
            cin >> x;
            cout << dt.check(x) << '\n';
        } else if(myStringCmp(operation, "toggle")){
            int x;
            cin >> x;
            dt.toggle(x);
        } else if(myStringCmp(operation, "all")){
            dt.all();
        } else if(myStringCmp(operation, "empty")){
            dt.empty();
        }
    }
    return 0;
}