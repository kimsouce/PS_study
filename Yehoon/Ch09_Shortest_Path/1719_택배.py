import heapq
import sys
input = sys.stdin.readline
inf = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
idx_graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, m + 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [inf] * (n + 1)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # if distance[now] < dist:
        #     continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                idx_graph[i[0]][start] = now


for i in range(1, n+1):
    dijkstra(i)

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            print("-", end=" ")
        else:
            print(idx_graph[i][j], end=" ")
    print()

# 플루이드 아님!!
# #플루이드 점화식
# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             # if str(graph[a][b]).isdigit() and str(graph[a][k]).isdigit() and str(graph[b][k]).isdigit():
#             if a!=b and a!=k and b!=k and graph[a][b] <= graph[a][k]+graph[k][b]:
#                 print("if:", graph[a][b], graph[a][k]+graph[k][b])
#                 idx_graph[a][b] = b
#             elif a!=b and a!=k and b!=k and graph[a][b] > graph[a][k]+graph[k][b]:
#                 print("else:", graph[a][b], graph[a][k] + graph[k][b])
#                 graph[a][b] = graph[a][k] + graph[k][b]
#                 idx_graph[a][b] = k
#
# for a in range(1, n+1):
#     for b in range(1, n+1):
#         print(idx_graph[a][b], end=" ")
#     print()
