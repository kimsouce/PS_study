from collections import deque


def bfs(x, y):
  q = deque()
  b = []
  q.append([x, y, 20])
  b.append([x, y, 20])
  while q:
    x, y, beer = q.popleft()  
    if x == f_x and y==f_y:  #페스티벌에 도착
      print('happy')
      return
    for nx, ny in point:
      if [nx, ny, 20] not in b:
        len = abs(nx-x) + abs(ny-y)
        if len <= beer*50:  #맥주가 20병 있는데 50미터마다 한병씩 먹음 #가는 길은 20*50을 넘어서는 안됨
          q.append([nx, ny, 20])
          b.append([nx, ny, 20])
  print('sad')
  return

t = int(input())
for _ in range(t):
  n = int(input())
  h_x, h_y = map(int, input().split())
  point=[]  #편의점과 페스티발 좌표를 담음
  for _ in range(n):
    s_x, s_y = map(int, input().split())
    point.append([s_x, s_y])
  f_x, f_y = map(int, input().split())
  point.append([f_x, f_y])
  bfs(h_x, h_y)  #집에서부터 페스티벌 까지의 최단거리 찾기



'''
#오류코드 수정 필요
from collections import deque

dx = [0, 0, -1, 1]  #LRUD
dy = [-1, 1, 0, 0] 


def bfs(x, y):  #최단거리 찾기(맥주가 떨어지지 않도록 편의점을 들리면서 페스티벌에 도착할 수 있는가)
  while q:
    x, y = q.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]

      if 0<=nx<f_x and 0<=ny<f_y and (map[nx][ny] ==1 or map[nx][ny] == 2) :
        if nx % 20 != 0 or ny % 20 != 0:
          map[nx][ny] = 3
        else:
          q.append((nx, ny))

def mood():
  for i in range(f_x):
    for j in range(f_y):
      tmp = map[i][j]
      if tmp ==3:
        print('sad')
      else:
        print('happy')


t = int(input())
for _ in range(t):
  n = int(input())
  h_x, h_y = list(map(int, input().split()))  #home의 x좌표 y좌표
  for _ in range(n):
    s_x, s_y = map(int, input().split())  #shop의 x좌표 y좌표
  f_x, f_y = map(int, input().split())  #fetival의 x좌표 y좌표

  map = [[0]*(f_y+1) for _ in range(f_x+1)]
  map[s_x][s_y] = 1
  map[f_x][f_y] = 2

  q = deque()
  for i in range(f_x):
    for j in range(f_y):
      if map[i][j] ==1 or map[i][j] ==2:
        q.append((i, j))

  bfs(0, 0)
  mood()
  '''
