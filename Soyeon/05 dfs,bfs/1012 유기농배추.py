


'''
#런타임에러.. 수정 필요
import sys
t = int(input())
for _ in range(t):
  n ,m ,k = list(map(int,sys.stdin.readline().split()))
  field = [[0]*m for _ in range(n)]
  for _ in range(k):
    x,y =map(int, input().split())
    field[x][y] = 1


def dfs(x,y):
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
  if field[x][y] ==1: 
    field[x][y] = 0
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False
  
count = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      count +=1

print(count) 
'''
