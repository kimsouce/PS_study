import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M= int(input())
MList = list(map(int, input().split()))
A.sort() # 오름차순으로 정렬

for i in MList:
    start = 0
    end = N-1
    target = i
    answer = 0
    while (start <= end):
        mid = (start+end) // 2
        if A[mid] == target:
            answer = 1
            break
        elif target < A[mid]:
            end = mid-1
        else:
            start = mid+1
    print(answer)
