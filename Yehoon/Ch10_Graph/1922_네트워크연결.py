# 크루스칼 최소 신장트리

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
parent = [0]*(n+1)
edges = []
result = 0

#부모 노드 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append([cost, a, b])

#비용 순으로 오름차순
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):

        union_parent(parent, a, b)
        result += cost
print(result)