N, K = map(int, input().split())   
lis = []   
for _ in range(N):
    lis.append(int(input()))  

min_len = 1   # 최소 길이 = 1
max_len = max(lis)   # 최대 길이 = 가지고 있는 랜선 중 가장 긴 길이.

while min_len <= max_len:   # 이분 탐색 시작
    mid = (min_len+max_len)//2   # 중간 값 설정
    lan_num = 0   
    for i in lis:
        lan_num += i//mid   # 랜선을 mid 길이로 잘랐을 때, 잘라진 랜선의 개수
    if lan_num >= K:   # 필요한 랜선의 개수(K) 이상을 만들 수 있는 경우 --> 랜선의 길이가 더 커져도 된다는 것을 의미
        min_len = mid + 1   # mid+1부터 e까지 탐색
    else:   # 필요한 랜선의 개수(K)를 만들 수 없는 경우 --> 랜선 길이가 더 작아져야 한다는 것을 의미
        max_len = mid - 1   # s부터 mid-1까지 탐색

print(max_len)   # 이진탐색 끝나고 출력

