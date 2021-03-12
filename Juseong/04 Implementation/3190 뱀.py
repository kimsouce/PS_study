n = int(input())

board = [[0] *(n+1) for _ in range(n+1)]
k = int(input())
for i in range(k):
    a,b = map(int, input().split())
    board[a][b] = 1


l = int(input())
info =[]

for i in range(l):
    x, c = input().split()
    info.append((int(x),c))

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def turn(direction):
    if c == 'L':
        direction = (di)

def simulate():
    x,y = 1, 1
    board[x][y] = 2 #뱀이 존재하는 위치는 2
    direction = 0
    time = 0
    index = 0
    q = [(x,y)] #뱀이 차지하고 있는 위치 정보
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        #맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1<=nx<=n and 1<=ny<=n and board[nx][ny]!=2:
            #사과가 없다면 이동후 꼬리 줄임
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx,ny))
                px, py = q.pop(0)
                board[px][py] = 0
            #사과가 있다면 꼬리 그대로
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
        else:
            tile += 1
            break
        x,y = nx, ny
        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
    return time
print(simulate())



