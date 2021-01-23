# 1,2,3,4 / 1
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m, k = map(int, input().split())
chk = [[0] * (m) for _ in range(n)]

waste = [[0] * (m) for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    waste[r-1][c-1] = 1


def locate(r, c):
    q = deque()
    q.append((r, c))
    # 연결되어 있지 않은 곳이라면 1로 다시 초기화
    cnt = 1
    chk[r][c] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not chk[nx][ny] and waste[nx][ny]:
                q.append((nx, ny))
                chk[nx][ny] = 1
                cnt += 1
    return cnt


result = 0
for i in range(n):
    for j in range(m):
        if not chk[i][j] and waste[i][j]:
            # 최대값으로 세팅
            result = max(result, locate(i, j))

print(result)
