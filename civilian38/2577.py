arr = [int(input()) for _ in range(3)]
number = arr[0] * arr[1] * arr[2]
answers = [0 for _ in range(10)]
while number:
    answers[number % 10] += 1
    number = number // 10
any(map(print, answers))