n = int(input())
city = list(map(int, input().split()))   #지방의 예산 요청
m = int(input())   #총 예산

city = sorted(city, key = lambda k : k)   #이진탐색 전 정렬
start = 0
end = max(city)

result = 0    #최적의 예산(상한액) 구하기 위한 변수 선언
while (start<=end):
  total = 0    #예산합 계산을 위한 변수 선언
  mid = (start+end)//2
  for i in city:
    if i < mid:    #요청한 예산이 mid값보다 작을 때
      total += i    #i 더해줌
    else:    #요청한 예산이 mid보다 클 때
      total += mid    #상한액 더해줌
  if total>m:    #만약 예산합이 총예산보다 크면
    end = mid-1    # 더 작은 mid값을 구해주기 위해 끝점을 더 작은 값으로 옮겨줌
  else:    
    result = mid     #최적의 예산을 mid값으로 반환하고
    start = mid +1    #상한액을 구하기 위해 시작점을 더 큰 값으로 옮겨줌

print(result)    #end 출력해도 같은 결과 



