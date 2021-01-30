import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
NList = list(map(int, input().split(" ")))
NList.sort()
M = int(input())
MList = list(map(int, input().split(" ")))

NList = Counter(NList)

for i in MList:
    print(NList[i], end= " ")
