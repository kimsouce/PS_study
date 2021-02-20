import heapq
import sys
input = sys.stdin.readline
inf = int(1e9)

n, m, k, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [inf]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append([b, 1])

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for idx, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[idx]:
                distance[idx] = new_cost
                heapq.heappush(q, [new_cost, idx])
dijkstra(start)

result = []
for idx, val in enumerate(distance):
    if val == k:
        result.append(idx)

if len(result) != 0:
    for i in result:
        print(i)
else:
    print(-1)