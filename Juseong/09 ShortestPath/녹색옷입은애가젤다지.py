#한점에서 최단거리 -> 다익스트라
import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
print = sys.stdout.write

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dijkstra(n, array, distance):
    q = []
    heapq.heappush(q, (0,0,0))
    distance[0][0] = 0
    while q:
        d, x, y = heapq.heappop(q)
        if distance[x][y] < d:
            continue
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: #
                continue
            nd = d + array[nx][ny]
            if distance[nx][ny] > nd:
                distance[nx][ny] = nd
                heapq.heappush(q, (nd, nx,ny))
    return distance[n-1][n-1] + array[0][0]

cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0:
        break
    array = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]
    print('Problem %d: %d\n' %(cnt, dijkstra(n, array, distance)))



