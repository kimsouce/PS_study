#runtime error
import sys
input = sys.stdin.readline
tmp = []
n = int(input())
arr =[]
for _ in range(n):
    arr.append(int(input()))


tmp.append(arr[0])
tmp.append(max(arr[0]+arr[1], arr[1]))
tmp.append(max(arr[0]+arr[2], arr[1]+arr[2]))

for i in range(3, n):
    tmp.append(max(tmp[i-2]+arr[i], tmp[i-3]+arr[i]+arr[i-1]))

print(tmp[-1])
