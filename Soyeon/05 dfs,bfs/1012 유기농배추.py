import sys
sys.setrecursionlimit(10000)  #런타임 에러 방지  #파이썬에서 재귀함수 쓸 때는 항상 limit 걸어주기

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

t = int(input())
for _ in range(t):
  n ,m ,k = list(map(int, input().split()))
  field = [[0]*m for _ in range(n)]
  count = 0
  for _ in range(k):
    x,y =map(int, input().split())
    field[x][y] = 1
  for i in range(n):
    for j in range(m):
      if dfs(i,j) == True:
        count +=1
  print(count)
