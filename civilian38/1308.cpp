#include <iostream>
using namespace std;

int days(int year, int month){
    if(month == 2){
        if (year % 400 == 0) { return 29; }
        else {
            if (year % 100 == 0) { return 28; }
            else {
                if (year % 4 == 0) { return 29; }
                else { return 28; }
            }
        }
    }
    else {
        switch (month) {
            case 1: return 31;
            case 3: return 31;
            case 4: return 30;
            case 5: return 31;
            case 6: return 30;
            case 7: return 31;
            case 8: return 31;
            case 9: return 30;
            case 10: return 31;
            case 11: return 30;
            case 12: return 31;
        }
    }
    return -1;
}

bool is_over(int current_year, int current_month, int current_date, int next_year, int next_month, int next_date){
    if(next_year - current_year > 1000){
        return true;
    } else if (next_year - current_year == 1000){
        if(next_month > current_month){
            return true;
        } else if (next_month == current_month){
            if(next_date >= current_date){
                return true;
            }
        }
    }
    return false;
}

int main() {
    int today_year = 0, today_month = 0, today_date = 0;
    int next_year = 0, next_month = 0, next_date = 0;
    cin >> today_year >> today_month >> today_date;
    cin >> next_year >> next_month >> next_date;
    if (is_over(today_year, today_month, today_date, next_year, next_month, next_date)){
        cout << "gg";
    } else {
        int d_day = 0;
        while(next_year > today_year){
            d_day += days(today_year, today_month) - today_date + 1;
            today_month++;
            if(today_month > 12){
                today_year++;
                today_month = 1;
            }
            today_date = 1;
        }
        while (next_month > today_month){
            d_day += days(today_year, today_month) - today_date + 1;
            today_date = 1;
            today_month++;
        }
        d_day += next_date - today_date;
        cout << "D-" << d_day;
    }

    return 0;
}