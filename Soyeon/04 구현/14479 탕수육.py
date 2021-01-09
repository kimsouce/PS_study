a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

time = 0

while a <b:
  if a<0:
    a +=1
    time +=c
  if a==0:
    time +=d  #고기의 온도가 0이되면 온도를 높이지 않고, 해동시간만 더해준다.
  if a>=0:
    a +=1
    time +=e



print(time)
