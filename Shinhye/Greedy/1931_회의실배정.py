import sys
input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    start, end = map(int, input().split())
    lst.append((start, end))

lst = sorted(lst, key=lambda x: x[0])  # 시작시간 정렬
lst = sorted(lst, key=lambda x: x[1])  # 시작시간 정렬된 상태로 종료시간 정렬

cnt = e = 0
for start, end in lst:
    if start >= e:
        cnt += 1
        e = end
print(cnt)
