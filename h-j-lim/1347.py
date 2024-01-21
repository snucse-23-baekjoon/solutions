N = int(input())
inst = input()
hori, verti = N - 1, N - 1
hori_trail, verti_trail = [hori], [verti]
direction = (1, 0)
for x in inst:
    if x == 'L':
        direction = (-direction[1], direction[0])
    if x == 'R':
        direction = (direction[1], -direction[0])
    if x == 'F':
        verti += direction[0]
        hori += direction[1]
        hori_trail.append(hori)
        verti_trail.append(verti)
left, right = min(hori_trail), max(hori_trail)
top, down = min(verti_trail), max(verti_trail)
hori_trail = list(map(lambda y: y - left, hori_trail))
verti_trail = list(map(lambda y: y - top, verti_trail))
Map = [['#'] * (right - left + 1) for _ in range(down - top + 1)]
for i, j in zip(verti_trail, hori_trail):
    Map[i][j] = '.'
for row in Map:
    print(''.join(row))
