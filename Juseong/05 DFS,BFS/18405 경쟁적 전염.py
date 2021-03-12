# bfs같음
from collections import deque

n,k = map(int, input().split())
#2차원 그래프 정보 입력 받기

graph = [] #보드 전체 대한 정보를 담는 리스트
data = [] #바이러스에 대한 정보를 담는 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            #(바이러스 종류, 시간, 위치x, 위치y) 삽입
            data.append((graph[i][j],0, i,j))
data.sort()
q = deque(data)
dx, dy = [-1,1,0,0], [0,0,-1,1]
target_s,target_x,target_y = map(int, input().split())


#bfs 구현
while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #해당 위치로 이동할 수 있는 경우
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])



