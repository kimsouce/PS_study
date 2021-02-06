#점화식 a[i] = max(a[i]+a[i-2]+a[i-3], a[i]+a[i-1]+a[i])

n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))
tmp = [0]
tmp.append(wine[0])
if n>1:
    tmp.append(wine[1] + wine[0])

for i in range(3, n+1):
    tmp.append(max(tmp[i-2]+wine[i-1], tmp[i-3]+wine[i-2]+wine[i-1], tmp[i-1]))
print(tmp[-1])