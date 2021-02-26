# 컴퓨터 연결 -> 그래프 이용
# 최소 비용 -> 크루스칼 알고리즘

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

#간선에 대한 정보 입력받기
for _ in range(m):
    a,b,cost = map(int, input().split())
    edges.append((cost, a,b))
edges.sort()

#간선을 하나씩 확인하며
for edge in edges:
    cost,a,b = edge
    #사이클이 발생하지 않은 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)