import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 도시의 개수 N, 버스의 개수 M
N = int(input())
M = int(input())

# 도시에 연결되어 있는 버스정보 담을 리스트
graph = [[] for _ in range(N+1)]
# 도시에 연결되어 있는 버스정보 담기
for _ in range(M):
    # a : 버스의 출발 도시 번호
    # b : 도착지의 도시번호
    # c : 버스 비용
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 최소 비용(최단거리) 테이블 모두 무한으로 초기화
distance = [INF] * (N+1)

# 구하고자 하는 구간 출발점(start)의 도시번호, 도착점(end)의 도시번호
start, end = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

print(distance[end])
