from collections import Counter
import sys
input = sys.stdin.readline

# 방법1 - 이진탐색(python - 7736ms / pypy3 - 2244ms)


def b_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if note1[mid] == target:  # target과 같으면 1반환
            return 1
        elif note1[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0  # target과 다르면 0반환


t = int(input())
for _ in range(t):  # 테스트케이스만큼 반복문 돌리기
    n = int(input())
    note1 = list(map(int, input().split()))
    note1.sort()
    m = int(input())
    note2 = list(map(int, input().split()))
    for s in note2:
        print(b_search(s, 0, n-1))

# 방법2 - list -> set(pypy3 - 1368ms)
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    note1 = set(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    for note in note2:
        if note in note1:
            print(1)
        else:
            print(0)

# 방법3 - Counter(python - 2344ms / pypy3 - 1864ms)
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    note1 = list(map(int, input().split()))
    note1.sort()
    m = int(input())
    note2 = list(map(int, input().split()))

    note1 = Counter(note1)
    for s in note2:
        if s in note1:
            print(1)
        else:
            print(0)
