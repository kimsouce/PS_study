#한 점에서 최단경로 -> 다익스트라
import sys
import heapq

input = sys.stdin.readline
inf = int(1e9)

V, E = map(int, input().split())
k = int(input())

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(V+1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [inf] * (V+1)

#모든 간선 정보 입력받기
for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        #현재 노드를 이미 처리한 적이 있다면 무시
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)

for i in range(1,V+1):
    if distance[i] == inf:
        print('INF')
    else:
        print(distance[i])
