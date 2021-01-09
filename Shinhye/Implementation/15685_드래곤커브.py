# x,y의 최댓값 100, 각 드래곤 커브가 연결된 선분 저장(좌표 저장)
visited = [[0]*101 for _ in range(101)]
n = int(input())

# 0(우), 1(상), 2(좌), 3(하)
# 여기선 x,y가 반대 개념, 애초에 반대로 저장
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 드래곤 커브 이동
for i in range(n):
    y, x, d, g = map(int, input().split())  # d 시작방향, g 세대

    # 세대별 방향 저장
    directions = [d]  # 0세대 방향 저장
    for _ in range(g):
        directions += [(i+1) % 4 for i in directions[::-1]]

    visited[x][y] = 1  # 첫 좌표 방문처리
    for direction in directions:
        # 방향을 통한 이동
        x = x + dx[direction]
        y = y + dy[direction]
        visited[x][y] = 1  # 좌표 방문처리


cnt = 0
for i in range(100):
    for j in range(100):
        # 네 꼭지점 방문처리 확인 후, cnt 증가
        if visited[i][j] and visited[i][j+1] and visited[i+1][j] and visited[i+1][j+1]:
            cnt += 1
print(cnt)

# 세대별 방향
# 0세대 : 0
# 1세대 : 0 1
# 2세대 : 01 21
# 3세대 : 0121 2321
# 4세대 : 01212321 23032321

# lst = [0]
# for _ in range(4):
#     lst += [(i+1) % 4 for i in lst[::-1]]
#     print(lst)
