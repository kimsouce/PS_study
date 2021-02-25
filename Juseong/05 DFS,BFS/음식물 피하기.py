import sys
sys.setrecursionlimit(10000)
dx, dy = [-1,1,0,0], [0,0,-1,1]
def dfs(x,y):
    check[x][y] = 1
    global cnt
    cnt +=1
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]
        if (0<=nx<n) and (0<=ny<m):
            if tongro[nx][ny] == 1 and check[nx][ny] == 0:
                dfs(nx,ny)

n, m, k = map(int, input().split())

tongro = [[0] * (m) for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    tongro[r-1][c-1] = 1

check = [[0] * (m) for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(m):
        if tongro[i][j] == 1 and check[i][j] == 0:
            cnt = 0
            dfs(i,j)
            answer = max(answer, cnt)

print(answer)


