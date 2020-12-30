n = int(input())
time = list(map(int, input().split()))

time.sort() #필요한 시간이 짧은 사람부터 인출 하는 것이 유리
waiting = 0
result = 0

for i in time:
  waiting += i #인출에 필요한 시간
  result +=waiting #n명의 사람이 인출하는데 걸리는 총 

print(result)
