#80%에서 자꾸 에러......... 디버깅 필요

n = int(input())
m = int(input())

graph = []
connect = []
for _ in range(n+1):
  graph.append(list(map(int, input().split())))   #일단 input 그래프 받아주기

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      connect.append((i+1, j+1))   #연결 여부 파악하기 위한 새로운 그래프 생성

root = [0]     #인덱스를 1부터 시작하기 위해 0 추가
for k in range(1, n+1):
  root.append(k)

def find(s):
  if s != root[s]:     #자기자신이 자기자신의 부모노드가 아니라면  #즉, 진입하는 간선이 존재한다면
    root[s] = find(root[s])
  return root[s]

def union(u, v):
  node1 = find(u)
  node2 = find(v)
  root[node2] = node1

E = 0

while connect:     # connect원소가 비어질 때 까지만 while 문 돌도록 함  #while True 라고 하면 런타임 
  if E == n-1:
    print('YES')
    break
  u, v = connect.pop(0)
  if find(u) != find(v):     #노드 u와 노드 v가 다른 집합에 속해있으면
    union(u, v)
    E +=1

if E != n-1:
  print('NO')
