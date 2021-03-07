
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())  # 시작 노드
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = [INF] * (V+1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)  # 튜플형태
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 (INF가 아니라면 방문한 것)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
