import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
NList = list(map(int, input().split(" ")))
NList.sort()
M = int(input())
MList = list(map(int, input().split(" ")))

dic = dict()

for i in NList:
    try :
        dic[i] += 1
    except :
        dic[i] = 1

for i in MList:
    try:
        print(dic[i], end =" ")
    except:
        print(0, end= " ")
print()
