month, date, year, time = input().split()
date = int(date[:-1])
year = int(year)
hour, minute = tuple(map(int,time.split(':')))

day_left = 365
if year % 400 == 0:
    day_left = 366
else:
    if year % 100 != 0:
        if year % 4 == 0:
            day_left = 366

convert = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}
month = convert[month]
days = [31,28,31,30,31,30,31,31,30,31,30,31]

time = 0
for i in range(12):
    if i < month - 1:
        time += days[i] * 24 * 60
        if i == 1:
            if day_left == 366:
                time += 24 * 60

time += ((date - 1) * 24 * 60) + (hour * 60) + minute
print(100 * time / (day_left * 24 * 60))