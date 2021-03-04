import sys
from collections import deque

input = sys.stdin.readline

n,m,k,x =map(int, input().split())

#도시 정보
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque([x])
distance = [-1] * (n+1)
distance[x] = 0

q.append([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)

