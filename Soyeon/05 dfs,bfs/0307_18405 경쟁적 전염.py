from collections import deque

n, k = map(int, input().split())
graph = []
info = [] #바이러스 정보 및 위치를 큐에 받아줌
for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      info.append((graph[i][j], 0, i, j)) #바이러스 종류, 시간, 행 번호, 열 번호
info.sort()  #바이러스 번호가 낮은 순서대로 정렬
que = deque(info)
s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0] #상하좌우
dy = [0, 0, -1, 1]

while que:
  v, sec, no_x, no_y = que.popleft()
  if sec == s:
    break
  for k in range(4):
    nx = no_x + dx[k]
    ny = no_y + dy[k]
    if 0<=nx and 0<=ny and nx<n and ny<n:
      if graph[nx][ny] == 0:
        graph[nx][ny] = v
        que.append((v, sec+1, nx, ny))
print(graph[x-1][y-1])
