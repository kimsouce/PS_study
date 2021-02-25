k, n = map(int, input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))

cnt = 0
start = 0
end = max(lan)

while (start<=end):
    total = 0
    mid = (start+end)//2
    for i in lan:
        total += (i//mid)
    if total<k:
        end = mid -1
    else:
        cnt = mid
        start = mid+1
print(cnt)
