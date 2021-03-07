k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]

start, end = 1, max(lans)


while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for lan in lans:
        cnt += (lan // mid)
    if cnt < n:  # 더 작은 값으로 mid값 설정 가능
        end = mid - 1
    else:
        start = mid + 1
print(end)
