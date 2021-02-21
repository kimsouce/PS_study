from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = int(1e9)

# 도시개수, 도로개수, 거리정보, 출발도시 번호
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

distance = [INF] * (N+1)


def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))


dijkstra(X)

result = []
for i in range(1, N+1):
    if distance[i] == K:
        result.append(str(i))

if not result:
    print(-1)
else:
    print('\n'.join(result))
