import sys
# 재귀함수 사용시의 런타임에러 방지
# 설정하지 않을 경우 1000회가 기본
sys.setrecursionlimit(10000)

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    # 주변에 배추있는지 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위를 벗어날 경우
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # 배추가 심어져 있는 경우
        if maps[nx][ny] == 1:
            # 방문처리
            maps[nx][ny] = 0
            dfs(nx, ny)


t = int(input())

for _ in range(t):
    # m 가로(열), n 세로(행)
    m, n, k = map(int, input().split())

    # 배추정보 입력받기
    maps = [[0]*m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        maps[x][y] = 1

    worms = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                dfs(i, j)
                # 주변에 연결된 배추가 더이상 없으면 +1
                worms += 1
    print(worms)
