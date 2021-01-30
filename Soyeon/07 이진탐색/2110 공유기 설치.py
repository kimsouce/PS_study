n, c = map(int, input().split())
house = []
for _ in range(n):
  house.append(int(input()))

house = sorted(house, key = lambda k:k)

start = 1    #어차피 공유기 사이의 거리가 1일때가 가장 짧을 것. 
end = house[-1] - house[0]    #house를 한번 sorting 해줬기 때문에 x_1과 x_n의 사이의 걸이가 가장 길 것. 

while (start<=end):
  mid = (start + end)//2
  count = 1
  pivot = house[0]    #리스트의 가장 처음부터 따져줌

  for i in range(1, len(house)):
    if house[i] >= pivot+mid:    #pivot집과 mid만큼의 거리차를 갖는 (아니면 그보다 멀리있는) 집이 존재하면
      count +=1   #공유기를 설치함
      pivot = house[i]    #그리고 다음 pivot으로 해당 집을 선택   #이 과정 반복
  if c > count:    #만약 공유기를 설치한 집(count)가 c보다 작으면
    end = mid -1    #더 많은 공유기를 설치해야 하므로 mid값을 더 작게 해줌
  else:
    start = mid +1    #그게 아니라면 더 적은 공유기를 설치해야 하므로 mid값을 더 크게 해줌
print(end)    #최대 거리 반환


