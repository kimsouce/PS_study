n = int(input())
rgb = []
for _ in range(n):
    rgb.append(list(map(int, input().split())))

for i in range(1, n):
    # i번째 집을 빨간색으로 칠할 경우 최솟값(초록, 파랑)
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
    # i번째 집을 초록색으로 칠할 경우 최솟값(빨강, 파랑)
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
    # i번째 집을 파란색으로 칠할 경우 최솟값(빨강, 초록)
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]

# 최종 최소값
print(min(rgb[n-1]))
