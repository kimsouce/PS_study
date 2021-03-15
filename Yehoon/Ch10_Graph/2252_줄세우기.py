#위상정령
from collections import deque

n, m = map(int, input().split())
indegree = [0]*(n+1)
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    # a->b
    graph[a].append(b)
    # b의 진입차수 +1
    indegree[b] += 1

def topology():
    result = []
    q = deque()

    #진입 차수가 0인 노드를 큐에 먼저 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            #진입 했으니 차수 1 뺴주기
            indegree[i] -= 1

            if indegree[i]==0:
                q.append(i)
    for i in result:
        print(i, end=' ')
topology()
