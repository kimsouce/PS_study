n = int(input())

stairs = [0]  # 인덱스 맞추기 위해 0번째 인덱스 설정
for _ in range(n):
    stairs.append(int(input()))

dp = [0] * 301  # 계단의 최대 갯수 300 + 1

for i in range(1, n+1):  # 1,2,3번째 항 설정
    if i == 1:
        # 1번 계단을 밟는 경우 - 1가지
        dp[i] = stairs[i]

    elif i == 2:
        # 2번 계단 밟는 경우 - 2가지(1,2번 밟기 / 2번 바로 밟기) 중 최댓값
        dp[i] = max(stairs[1] + stairs[2], stairs[2])

    elif i == 3:
        # 3번 계단 밟는 경우 - 2가지(1,3번 밟기 / 2,3번 밟기) 중 최댓값
        dp[i] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
    else:
        # 점화식
        # n번 계단 밟는 경우 - 2가지
        # (n번, n-1번, n-3번 밟기 / n번, n-2번 밟기)
        dp[i] = max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i]+dp[i-2])
print(dp[n])

# ----------------

# # 런타임 에러(IndexError)
# n = int(input())
# stairs = [int(input()) for _ in range(n)]

# dp = []
# dp.append(stairs[0])
# dp.append(max(stairs[0] + stairs[1], stairs[1]))
# dp.append(max(stairs[0] + stairs[2], stairs[1]+stairs[2]))

# for i in range(3, n):
#     dp.append(max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2]))
# print(dp[-1])
