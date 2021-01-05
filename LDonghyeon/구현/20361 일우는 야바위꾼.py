N, X, K = map(int,input().split())

changes = []
for _ in range(K):
    changes.append(list(map(int, input().split())))

ball = [0] * N
ball[X - 1] = 1

for change in changes:
    ball[change[0] - 1], ball[change[1] - 1] = ball[change[1] - 1], ball[change[0] - 1]
print(ball.index(1) + 1)