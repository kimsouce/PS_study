n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True)  # 역순으로 정렬해야 가장 가치가 큰 동전의 종류를 먼저 나눌 수 있음

cnt = 0
for coin in coins:
    if coin <= k:
        cnt += k // coin
        k = k % coin

print(cnt)
