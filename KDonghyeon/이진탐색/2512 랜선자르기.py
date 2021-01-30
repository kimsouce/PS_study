import sys
K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(lan) #이분탐색 처음과 끝위치

while start <= end:
    mid = (start + end) // 2
    lines = 0 #랜선 수
    for i in lan:
        lines += i // mid 
    if lines >= N: 
        start = mid + 1
    else:
        end = mid - 1
print(end)
