import sys

input = sys.stdin.readline
n = int(input())
house = list(map(int, input().split()))
house.sort()

print(house[(n-1)//2])

#시간초과 코드

# result = [0]*len(house)
# for i in range(len(house)):
#     tmp = [house[i]] * len(house)
#     for j in range(len(house)):
#         result[i] += (abs(house[j]-tmp[j]))
# print(house[result.index(min(result))])