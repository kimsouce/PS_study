# seriously 바보...?

n = int(input())
house = list(map(int, input().split()))
house.sort()

if len(house) % 2 == 1:
  print(house[len(house)//2])
else:
  print(house[(len(house)//2)-1])
  
  
  '''
  # 시간초과
n = int(input())
house = list(map(int, input().split()))
house = sorted(house, key = lambda k:k)

data_all = []

for i in range(len(house)):
  data = []  #각 i에 대하여 저장  #house1:[0, 4, 6, 8] house5:[4, 0, 2, 4] house7:[6, 2, 0, 2] house9:[8, 4, 2, 0]
  for j in range(len(house)):
    length = max(house[i], house[j]) - min(house[i], house[j])
    data.append(length)
  data_all.append(data)  #[[0, 4, 6, 8], [4, 0, 2, 4], [6, 2, 0, 2], [8, 4, 2, 0]]

result_all = []

for data in data_all:
  result = sum(data)  #18, 10, 10, 14
  result_all.append(result)  #[18, 10, 10, 14]

print(house[result_all.index(min(result_all))])  #result_all에서 가장 작은 값의 인덱스 반환  
#그 인덱스에 위치한 house리스트의 원소 반환
'''
