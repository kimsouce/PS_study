n, k = map(int, input().split())
coins = []
for i in range(n):
  coins.append(int(input())) #개행으로 입력받기

count = 0
coins.sort(reverse=True) #가치가 큰 동전부터 나누어야 하기 때문

for n in coins:
  count += k//n
  k %=n
    

print(count)
