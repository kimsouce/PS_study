k, n = map(int, input().split())
lan = []
for _ in range(k):
  lan.append(int(input()))

lan = sorted(lan, key = lambda k:k)
start = 1    #최소 '길이' 이므로 0아니고 1    #히든 케이스에 걸림(런타임 에러 Zero division)
end = max(lan)


while (start<=end):
  count = 0
  mid = (start+end)//2
  for i in lan:
    count += i//mid    #i를 mid만큼 자른 횟수 더해줌
  if count < n:
    end = mid-1
  else:
    start = mid + 1


print(end)    #조건을 만족하는 최대의 랜선 길이를 찾음


