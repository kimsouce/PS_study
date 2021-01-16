import sys
sys.setrecursionlimit(10000)

n, m, k = map(int, input().split())
trash = [[0]*m for _ in range(n)]
for _ in range(k):
  x, y =map(int, input().split())
  x = x-1
  y = y-1  #행렬 인덱스 맞춰주기 위해
  trash[x][y] = 1


visited = [[False]*m for _ in range(n)]

dx = [0, 0, -1, 1]  #LRUD
dy = [-1, 1, 0, 0]

def search(x, y):
  global count
  visited[x][y] = True  #방문처리
  if trash[x][y] ==1:
    count +=1

  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]
    if 0 <= nx < n and 0 <= ny <m:
      if trash[nx][ny] ==1 and not visited[nx][ny]:
        search(nx, ny)

result = 0
for i in range(n):
  for j in range(m):
    if trash[i][j] ==1 and not visited[i][j]:
      count =0
      search(i, j)
      result = max(result, count)

print(result)
