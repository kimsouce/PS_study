from heapq import heappop, heappush

V, E = map(int, input().split())
k = int(input())
graph = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u-1].append((v-1, w))

def dijkstra(s):
    result = [float('inf')for _ in range(V)]
    result[s] = 0
    que = []
    heappush(que, (result[s], s))
    while que:
      wei, node = heappop(que)
      if result[node] < wei:
        continue
      for fn, fw in graph[node]:
          if result[fn] > wei + fw:
              result[fn] = wei + fw
              heappush(que, (result[fn], fn))
    return result

answer = dijkstra(k-1)
for i in answer:
    print('INF' if i == float('inf') else i)
