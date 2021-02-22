from heapq import heappush, heappop

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append((b-1, 1))
    
def dijkstra(s):
    result = [float('inf') for _ in range(n)]
    result[s] = 0
    que = []
    heappush(que, (result[s], s))
    while que:
        wei, node  = heappop(que)
        if result[node] < wei:
            continue
        for fn, fw in graph[node]:
            if result[fn] > wei + fw:
                result[fn] = wei + fw
                heappush(que, (result[fn], fn))
    return result

answer = dijkstra(x-1)
city = []
for i in range(len(answer)):
    if answer[i] == k:
        city.append(i+1)
if not city:     #만약 리스트가 비었으면
    print('-1')
for j in city:
    print(j, sep='|n')
