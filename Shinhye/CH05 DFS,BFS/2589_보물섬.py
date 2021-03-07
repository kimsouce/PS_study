from collections import deque
import sys
input = sys.stdin.readline
q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

row, col = map(int, input().split())
maps = [input() for _ in range(row)]
distance = 0


def bfs(x, y):
    global distance
    # 최단거리 구한 후, 배열 초기화 시키기
    chk = [[0] * col for _ in range(row)]
    q.append((x, y))
    chk[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:  # 범위 안
                if maps[nx][ny] == 'L' and chk[nx][ny] == 0:
                    chk[nx][ny] = chk[x][y] + 1
                    q.append((nx, ny))
                    distance = max(distance, chk[nx][ny])


# maps탐색하면서, 육지(L)면 bfs탐색하기
for i in range(row):
    for j in range(col):
        if maps[i][j] == 'L':
            bfs(i, j)  # 시작점

print(distance-1)
