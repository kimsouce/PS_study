n = int(input())
datas = []
count = 0
end_time = 0

for i in range(n):
  x, y =map(int, input().split())
  datas.append((x, y))

datas = sorted(datas, key=lambda k:k[0]) #시작 시간을 기준으로 정렬 -1
datas = sorted(datas, key=lambda k:k[1]) #끝나는 시간을 기준으로 다시한번 정렬 -2 

for data in datas:
  if data[0] >=end_time:
    end_time = data[1]
    count +=1

print(count)

#이렇게 이해하기
#datas = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8)]
#1정렬 = [(0, 6), (1, 4), (3, 5), (3, 8), (5, 7)]
#2정렬 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8)] 
