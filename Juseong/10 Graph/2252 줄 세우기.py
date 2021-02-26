#트리 구조 접근x


from collections import deque

# 방향 그래프에서 순서 고려 -> 위상정렬

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b



n,m = map(int, input().split())
indegree = [0] * (n+1) #모든 노드에 대한 진입차수는 0으로 초기화
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1 #a->b 이므로 b의 진입 차수를 +1 해준다.

#위상정렬 함수
def topology():
    result = []
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        #큐에서 꺼내기
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')
topology()



