def get_range(string1, string2):
    L = string1.count("L") + string2.count("L")
    O = string1.count("O") + string2.count("O")
    V = string1.count("V") + string2.count("V")
    E = string1.count("E") + string2.count("E")
    return ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100

import sys

myteam = sys.stdin.readline().rstrip()
repeatnum = int(sys.stdin.readline().rstrip())
victory = sys.stdin.readline().rstrip()

for _ in range(repeatnum - 1):
    team = sys.stdin.readline().rstrip()
    if get_range(myteam, victory) < get_range(myteam, team):
        victory = team
    elif get_range(myteam, victory) == get_range(myteam, team):
        victory = min(victory, team)
print(victory)