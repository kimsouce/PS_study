import sys
input = sys.stdin.readline
N = int(input())
budget = list(map(int, input().split()))
M = int(input())
start, end = 0, max(budget)
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for i in budget:
        if i >= mid:
             tmp += mid
        else:
             tmp += i
    if tmp <= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
