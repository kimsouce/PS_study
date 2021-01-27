
#1. 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘음
#계수정렬 효과적이지 않음


#2. 탐색해야 하는 target이 많음
#이진 탐색 효과적이지 않음'


#먼저 받고 Counter 매서드 사용: 812ms
from collections import Counter
n = int(input())
card = input().split()
m = int(input())
array_M = input().split()

c = Counter(card)
for i in array_M:
  print(c[i], end=" ")
  
  
  
# Counter로 받고 if 문으로 나눠서 프린트: 756ms
from collections import Counter
n = int(input())
card = Counter(input().split())
m = int(input())
array_M = input().split()

for i in array_M:
  if i in card:
    print(card[i], end=" ")
  else:
    print(0, end=" ")
