n = int(input())
houses = list(map(int, input().split()))
houses.sort()

# 기준 인덱스
pivot = 0
if (len(houses) % 2) == 0:
    pivot = len(houses) // 2
else:
    pivot = (len(houses) // 2)+1

print(houses[pivot-1])


# print(houses[(n-1)//2])
