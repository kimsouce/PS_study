import sys
N, K = map(int, sys.stdin.readline().split())
money = []
for _ in range(N):
    money.append(int(sys.stdin.readline()))
money.reverse()

count = 0
for v in money:
    if (K // v) > 0:
        count += (K // v)
        K %= v
print(count)