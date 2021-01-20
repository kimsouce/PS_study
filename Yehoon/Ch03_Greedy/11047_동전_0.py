coins, value = map(int, input().split())
coin_type = []
for _ in range(coins):
    coin_type.append(int(input()))

#액수가 큰 동전부터 나누기
coin_type.sort(reverse=True)
count = 0
for coin in coin_type:
    count += value//coin
    value %= coin

print(count)
