#서로소 집합을 활용한 사이클
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
parent = [0] * (n + 1)  # 부모 테이블 초기화

for i in range(1, n + 1):
    parent[i] = i

route = [list(map(int, input().split())) for _ in range(n)]
route.insert(0, 0)

tour_plan = list(map(int, input().split()))

cycle = False
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if route[i][j-1] == 1:
#             if find_parent(parent, i) == find_parent(parent, j):
#                 cycle = True
#                 break
#             else:
#                 union_parent(parent, i, j)

for i in tour_plan:
    for j in tour_plan:
        if route[i][j-1] == 1:
            if find_parent(parent, i) == find_parent(parent, j):
                cycle = True
                break
            else:
                union_parent(parent, i, j)
if cycle:
    print("YES")
else:
    print("NO")