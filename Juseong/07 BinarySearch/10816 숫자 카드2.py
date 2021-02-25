from collections import Counter

n = int(input())
array = list(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

cnt = Counter(array)
for i in x:
    print(cnt[i], end=' ')
