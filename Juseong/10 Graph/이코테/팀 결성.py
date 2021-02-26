def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int, input().split())
indegree = [0] * (n+1) #부모 테이블 초기화

#부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

#각 연산을 하나씩 확인
for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent,a,b)
    elif oper == 1:
        if find_parent(parent,a) == find_parent(parent,b):
            print('Yes')
        else:
            print('No')