# 메모리 44704 / 시간 600ms
n = int(input())
n_lst = list(map(int, input().split()))  # a1, a2 ,,
m = int(input())
m_lst = list(map(int, input().split()))  # a안에 존재하는지 알아보는 리스트

n_lst.sort()


def b_search(target, start, end):
    # start, end - 인덱스, target - 찾을 원소
    while start <= end:
        mid = (start + end) // 2
        if n_lst[mid] == target:
            return 1
        elif n_lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for target in m_lst:
    result = b_search(target, 0, n-1)
    print(result)

# pypy3제출, sys사용
# 메모리 147140 / 시간 3688ms
'''
import sys
input = sys.stdin.readline

n = int(input())
n_nums = list(map(int, input().split()))
m = int(input())
m_nums = list(map(int, input().split()))

for num in m_nums:
    if num in n_nums:
        print(1)
    else:
        print(0)
'''
