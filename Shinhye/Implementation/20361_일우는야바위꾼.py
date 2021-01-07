n, x, k = map(int, input().split())
attempts = [tuple(map(int, input().split())) for _ in range(k)]

cups = [0] * (n+1)  # 인덱스0은 쓰지않음, 공 위치 표시
cups[x] = 1  # 현재 공의 위치
for a, b in attempts:
    cups[a], cups[b] = cups[b], cups[a]  # 시도 한 번마다 위치 바꿔주기


print(cups.index(1))  # 현재 공이 있는 위치의 인덱스 반환
