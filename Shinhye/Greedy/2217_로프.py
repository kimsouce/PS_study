import sys
input = sys.stdin.readline

n = int(input())
ropes_weight = [int(input()) for _ in range(n)]

# 최대 중량 -> 역순
ropes_weight.sort(reverse=True)

for i in range(n):
    ropes_weight[i] = ropes_weight[i] * (i+1)

print(max(ropes_weight))
