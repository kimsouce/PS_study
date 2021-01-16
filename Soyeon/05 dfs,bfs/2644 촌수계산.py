from collections import deque

n = int(input())
p_1, p_2 = map(int, input().split())
m = int(input())
family = [[] for _ in range(n+1)]  #인접리스트 만들기 위해, n+1인 이유는 맨 위에 빈리스트 
visited = [False] *(n+1)  #각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)

for _ in range(m):
  x, y = map(int, input().split())
  family[x].append(y)
  family[y].append(x)

def check(v, target):
  count = 0
  q = deque([[v, count]]) # [7, 0] [2, 1] [1, 2] [8, 2] [9, 2] [3, 3]
  while q:
    value = q.popleft()
    v = value[0]
    count = value[1]
    if v == target:
      return count

    if not visited[v]:  #방문 리스트에 해당 노드가 없으면(노드 4, 5, 6에 대하여 ) 
      count +=1
      visited[v] = True
      for e in family[v]:
        if not visited[e]:
          q.append([e, count])
  return -1


print(check(p_1, p_2))
