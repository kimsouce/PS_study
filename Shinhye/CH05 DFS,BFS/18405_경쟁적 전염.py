from collections import deque

dx = [1, -1, 0, 0]
dy = dx[::-1]  # dx의 역순

n, k = map(int, input().split())
virus = [list(map(int, input().split())) for _ in range(n)]  # 바이러스 위치
s, x, y = map(int, input().split())  # s는 제한시간

data = []  # 바이러스의 데이터를 담아 정렬해줄 리스트

for i in range(n):
    for j in range(n):
        if virus[i][j] != 0:  # 바이러스가 존재한다면
            # 바이러스에 대한 정보(바이러스 종류, 시간, 좌표)를 data리스트에 넣기
            data.append((virus[i][j], 0, i, j))

# 번호가 오름차순으로 증식하니, 큐에 넣기 전, 정렬 후, 넣기
data.sort()
q = deque(data)

while q:
    typeOfV, time, a, b = q.popleft()

    # 주어진 시간만큼만 바이러스퍼지게 하기
    if s == time:
        break

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if virus[nx][ny] == 0:  # 바이러스가 퍼지지 않았다면
                virus[nx][ny] = typeOfV
                q.append((typeOfV, time+1, nx, ny))

print(virus[x-1][y-1])
