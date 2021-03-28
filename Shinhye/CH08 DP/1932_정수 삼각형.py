n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]
# 각 층의 맨 왼쪽, 맨 오른쪽은 바로 윗층의 숫자를
# 나머지는 바로 윗층의 최댓값 더하기
for i in range(1, n):  # [0][0]은 초항
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i-1][j]
        elif j == len(dp[i])-1:
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[n-1]))
