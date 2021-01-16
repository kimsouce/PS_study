r, c = map(int, input().split())
maps = [list(input()) for _ in range(r)]

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 늑대 주변에 양이 있는 경우 체크할 변수
flag = 0

for x in range(r):
    for y in range(c):
        # 늑대가 있을 경우
        if maps[x][y] == 'W':
            # 탐색
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                # 좌표를 벗어날 경우
                if nx < 0 or ny < 0 or nx == r or ny == c:
                    continue

                # 만약, 탐색한 값에 양이 있을 경우
                elif maps[nx][ny] == 'S':
                    flag = 1
                    break

        # 양이 있을 경우
        elif maps[x][y] == 'S':
            continue

        # 늑대도 양도 아닌 경우(.) D로 치환
        else:
            maps[x][y] = 'D'

# 늑대 주변에 양이 있는 경우
if flag:
    print(0)

# 늑대 주변에 양이 없을 때
else:
    print(1)
    for i in maps:
        print(''.join(i))
