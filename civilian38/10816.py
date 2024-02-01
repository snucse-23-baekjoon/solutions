import sys

cards = dict()
sys.stdin.readline()
for number in sys.stdin.readline().split():
    if cards.get(number):
        cards[number] += 1
    else:
        cards[number] = 1

sys.stdin.readline()
for number in sys.stdin.readline().split():
    if cards.get(number):
        print(cards[number], end= ' ')
    else:
        print(0, end = ' ')