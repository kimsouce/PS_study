from collections import deque

n, m= map(int, input().split())
indegree = [0] * (n+1)     #모든 노드에 대한 진입차수 0으로 초기화     #연결이 안되어 있다고 가정
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)      #정점 a 에서 b로의 간선 존재
    indegree[b] +=1     #b의 진입차수 1 증가

def topology_sort():
    result = []     #알고리즘 수행 결과를 담을 리스트
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:    #진입차수가 0인 노드를 큐에 삽입(시작 노드)
            q.append(i)
    
    while q:     #큐가 빌 때 까지 반복
        now = q.popleft()
        result.append(now)
        for j in graph[now]:     #해당 노드와 연결된 노드들에 대하여
            indegree[j] -= 1     #진입차수를 1 뺀다
            if indegree[j] == 0:     #진입차수가 0이 되는 노드를 큐에 삽입(다음 시작 노드)
                q.append(j)
                
    for k in result:
        print(k, end=' ')

topology_sort()



'''
질문: 왜 4번째 줄에서
indegree = [[0] for _ in range(n+1)] 라고 하면 안될까요...?

해결: indegree = [0 for _ in range(n+1)] 하면 
'''
