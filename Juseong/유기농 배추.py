import sys
sys.setrecursionlimit(10000)

t = int(input())
m, n, k = map(int, input().split())

bat = [[0]* m for _ in range(n)]
# 배추 정보 입력 받기
for _ in range(k):
    b, a = map(int, input().split())
    bat[a][b] = 1

dx,dy = [-1,1,0,0], [0,0,-1,1]


def dfs(x,y):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if (0<=nx<n) and (0<=ny<m):
            if bat[nx][ny] == 1:
                visited[nx][ny] = 0
                dfs(nx,ny)
cnt = 0
for i in range(n):
    for j in range(m):
        if bat[i,j] == 1:
            bat[i][j] = 0
            cnt += 1
            dfs(i,j)

print(cnt)
