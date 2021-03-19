import sys
input = sys.stdin.readline


n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        #왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1] #계속 dp테이블을 갱신시킨다.
        #바로 위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = dp[i-1][j]

        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n-1]))
