N = int(input())
List = []   
for _ in range(N):
    List.append(int(input()))

List.sort()

mean = round(sum(List) / len(List))
median = List[N//2]
