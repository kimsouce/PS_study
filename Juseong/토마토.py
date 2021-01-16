m, n = map(int, input().split())
box = []
for _ in range(n):
    box.append(list(map(int, input().split())))


dx, dy = [-1,1,0,0], [0,0,-1,1]

from collections import deque
queue = deque()

def bfs():
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if (0<=nx<n) and (0<=ny<m) and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append([nx,ny])

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i,j])
bfs()
result =0
for a in range(n):
    for b in range(m):
        res = box[a][b]
        if res == 0:
            print(-1)
            result = max(result, res)
print(result - 1)
