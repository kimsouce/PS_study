from collections import deque

m, n =map(int, input().split())
box = []
for _ in range(n):
  box.append(list(map(int, input().split())))

dx = [0, 0, -1, 1] #LRUD
dy = [-1, 1, 0, 0]

queue = deque()
for i in range(n):
  for j in range(m):
    if box[i][j] == 1:
       queue.append((i,j))
#과정 1 
#box를 돌면서 1(익은 토마토)가 있는지 확인
#있으면 해당 좌표를 큐에 추가

def tomato(x,y):
  while queue:
    x, y = queue.popleft()  #큐에 담은 1의 좌표를 하나씩 꺼내어 비교
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<m and box[nx][ny] ==0:  #1 옆에 0이 있으니까 
        box[nx][ny] = box[x][y] +1  #익음(0 -> 1)
        queue.append([nx, ny])  #해당 좌표는 1이 되었으므로 큐에 또 추가
#과정 2

def check():  
  done = 0
  for i in range(n):
    for j in range(m):
      tmp = box[i][j] 
      if tmp ==0:  #과정1과 과정2를 했는데도 0이 남아있으면 완전히 익지 않은 것임
        print('-1')
        return
      done = max(done, tmp)  #처음부터 완전히 익었거나, 과정 2에서 0 ->1과정을 통해 누적된 숫자 반환 
  print(done-1)  #처음 익어있는 토마토는 일수에 포함 X

tomato(0,0)
check()

