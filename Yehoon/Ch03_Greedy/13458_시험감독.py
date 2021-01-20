n = int(input())
tester = list(map(int, input().split()))
master, sub = map(int, input().split())

cnt = 0
for num in tester:
    num -= master
    cnt += 1
    if num > 0:
        cnt += (num//sub)
        num -= sub * (num // sub)
        if num%sub!=0:
            cnt += 1

print(cnt)