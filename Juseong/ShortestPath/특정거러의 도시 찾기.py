#한 점에서 최단거리 -> 다익스트라
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
n, m, k, x = map(int, input().split())
#각 노드에 연결되는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n+1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)
#모든 간선 정보를 입력받기
for _ in range(m):
    a,b= map(int, input().split())
    graph[a].append((b,1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된 경우 무시
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(x)
result = []

for idx, val in enumerate(distance):
    if val == k:
        result.append(idx)

if len(result) != 0:
    for i in result:
        print(i)
else:
    print(-1)