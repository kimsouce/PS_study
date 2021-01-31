import sys
input=sys.stdin.readline

n,m=map(int,input().split())
lesson=list(map(int,input().split()))
# print(lesson)
l=max(lesson)
r=sum(lesson)
ans=sys.maxsize
while l<=r:
    mid=(l+r)//2
    cnt=0
    sum=0
    for i in range(len(lesson)):
        if sum+lesson[i]>mid:
            cnt+=1
            sum=0
        sum+=lesson[i]
    if sum:
        cnt+=1

    if cnt>m: 
        l=mid+1
    else:
        ans=min(ans,mid)
        r=mid-1
print(ans)


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
