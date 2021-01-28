import sys
from collections import Counter
input = sys.stdin.readline

# Counter사용
n = int(input())
s_have = list(map(int, input().split()))
m = int(input())
search = list(map(int, input().split()))
s_have = Counter(s_have)  # 딕셔너리 반환

for s in search:
    print(s_have[s], end=" ")  # key값을 통한 value출력

#
# # 시간초과
# n = int(input())
# s_have = list(map(int, input().split()))
# m = int(input())
# search = list(map(int, input().split()))

# s_have.sort()


# def b_search(target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if target == s_have[mid]:
#             return target  # 원소값 반환
#         elif target > s_have[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return 0

# for target in search:
#     result = b_search(target, 0, n-1)
#     print(s_have.count(result), end=" ")
