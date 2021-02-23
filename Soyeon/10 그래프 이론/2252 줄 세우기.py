from collections import deque

n, m= map(int, input().split())
indegree = [0] * (n+1)     
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)      #a가 b 앞에 서야 하므로 que에서 먼저 pop 되어야 한다   #즉, 위상순서가 앞이어야 한다
    indegree[b] +=1

def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for j in graph[now]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)
                
    for k in result:
        print(k, end=' ')

topology_sort()



'''
질문: 왜 4번째 줄에서
indegree = [[0] for _ in range(n+1)] 라고 하면 안될까요...?

해결: indegree = [0 for _ in range(n+1)] 하면 
'''
