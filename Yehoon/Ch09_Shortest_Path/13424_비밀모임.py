import heapq
import sys
input = sys.stdin.readline
inf = int(1e9)
result = []
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    graph = [[inf]*(n+1) for _ in range(n+1)]
    # distance = [inf]*(n+1)

    for a in range(1, n + 1):
        for b in range(1, n + 2):
            if a == b:
                graph[a][b] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        # graph[a].append([b, c])
        # graph[b].append([a, c])
        graph[a][b] = c
        graph[b][a] = c

    k = int(input())
    k_start = list(map(int, input().split()))


    for x in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][x] + graph[x][b])

    tmp = [0]*(n+1)
    tmp[0] = inf
    for i in k_start:
        for j in range(1, n+1):
            tmp[j] += graph[i][j]
    result.append(tmp)
for i in range((len(result))):
    print(result[i].index(min(result[i][1:])))


    # def dijkstra(start):
    #     q = []
    #     heapq.heappush(q, [0, start])
    #     distance[start] = 0
    #
    #     while q:
    #         dist, now = heapq.heappop(q)
    #         if distance[now] < dist:
    #             continue
    #         for idx, cost in graph[now]:
    #             new_cost = dist + cost
    #             if new_cost < distance[idx]:
    #                 distance[idx] = new_cost
    #                 heapq.heappush(q, [new_cost, idx])



#     for i in k_start:
#         print(i)
#         dijkstra(i)
#         for j in range(1, n+1):
#             total_route[j] += distance[j]
#
#         min_route = inf
#         min_idx = 0
#         print(total_route)
#         for idx, val in enumerate(total_route):
#             if val == 0:
#                 continue
#             if min_route > val:
#                 min_route = val
#                 min_idx = idx
#     result.append(min_idx)
# print(result)
