import sys
sys.setrecursionlimit(10000)

t = int(input())

def dfs(x):
    visited[x] = True
    forward = case[x]
    if visited[forward] == False:
        dfs(forward)

for i in range(t):
    n = int(input())
    case = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    result = 0

    for i in range(1,n+1):
        if visited[i] == False:
            dfs(i)
            result += 1
    print(result)
