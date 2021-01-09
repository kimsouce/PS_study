
n_1, n_2 = map(int, input().split())
ants= []
for _ in range(2):
  ants.append(list(input()))
t = int(input())

dir = {} #딕셔너리 사용 #key값과 value값을 설정하기 위해
for ant in ants[0]:
  dir[ant] = 0 # 첫번째 그룹의 value는 0이다
for ant in ants[1]:
  dir[ant] = 1 # 두번째 그룹의 value는 1이다

ants = ants[0][::-1] + ants[1] #FIFO 맞춰주기 위해

for _ in range(t):
  i =0
  while i<len(ants) -1:
    if dir[ants[i]] == 0 and dir[ants[i+1]] ==1:
      ants[i], ants[i+1] = ants[i+1], ants[i]
      i +=1  #다음 인덱스 확인하기 위해
    i +=1  #len-1 보다 클 경우 while문 빠져나오기 위해


for ant in ants:
  print(ant, end='')  #각 원소를 공백없이 출력
  

''' 
#오답
n_1, n_2 = map(int, input().split())
ants= []
for _ in range(2):
  ants.append(list(input()))
t = int(input())

ants = ants[0][::-1] + ants[1]
move = [0] * (n_1) + [1] * (n_2)  #리스트 초기화로 풀어보려고 함 #방향에 따라 오른쪽으로 가는 개미는 0, 왼쪽으로 가는 개미는 1

for _ in range(t):
  for i in range(len(move)-1):
    if move[i] ==0 and move[i+1] ==1:
      ants[i], ants[i+1] = ants[i+1], ants[i] #안바뀜.. 


print(ants)
'''


