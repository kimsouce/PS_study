from collections import deque
q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
toms = [list(map(int, input().split())) for _ in range(n)]

# 토마토가 익어있는 부분에서 시작
for i in range(n):
    for j in range(m):
        if toms[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 안에 있으면서, 안익은 토마토가 있다면
        if 0 <= nx < n and 0 <= ny < m and toms[nx][ny] == 0:
            toms[nx][ny] = toms[x][y] + 1
            q.append((nx, ny))


result = -2  # 비교를 위한 변수
flag = 0  # 안익은게 있는지 체크할 변수
for i in range(n):
    for j in range(m):
        if toms[i][j] == 0:
            flag = 1
        result = max(result, toms[i][j])

if flag == 1:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)  # 시작일부터 +1하니까 1빼기
