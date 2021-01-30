'''
#오류 코드
n,m = map(int, input().split())
blueray = list(map(int, input().split()))
blueray = sorted(blueray, key=lambda k : k)

start = max(blueray)
end = sum(blueray)
count = 0

while (start<=end):
  mid = (start+end)//2
  result = 0
  tmp = mid
  for i in range(len(blueray)):
    if blueray[i] >= tmp:
      count += 1
      tmp = mid
    else:
      tmp -= blueray[i]
  print(count)
  if count <= m:
    end = mid - 1
  else:
    result = mid 
    start = mid + 1

print(result)
'''
