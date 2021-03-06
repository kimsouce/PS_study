n, l = map(int, input().split())
point = list(map(int, input().split()))
point = sorted(point, key = lambda k:k)

count = 0
tape = 0

for i in range(n):
  if point[i] <= tape:   #2. 만약 테이프로 막을 수 있다면
    continue    #3. 계속
  count += 1    #4. 아니라면 테이프 개수 하나 늘려주고
  tape = point[i] + (l-1)  #1. 테이프로 현재 위치에서 l-1(좌우 0.5씩)만큼 떨어져 있는 곳까지 막을 수 있다   #5. 테이프 길이 초기화

print(count)



'''
#오답코드

n, l = map(int, input().split())
point = list(map(int, input().split()))
point = sorted(point, key = lambda k : k)

count = 1 
def check(l):
  global count 
  tmp = l
  for i in range(len(point)-1):
    if tmp < 0:
      tmp = l
      count += 1
    else:
      interval = point[i+1] - point[i] + 1    #처음에는 이렇게 간격으로 풀어보려 했으나, 변수가 너무 많음
      tmp -= interval 

check(l)
print(count)
'''

