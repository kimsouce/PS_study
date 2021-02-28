from heapq import heappop, heappush     #리스트 내의 가장 작은 값을 가장 앞으로 옮기기 위해  #즉, 난이도가 쉬운 문제를 앞으로 보내기 위해
                                           #우선순위 큐: In 순서에 상관 없이 우선순위가 높은 데이터가 먼저 OUT 된다

n, m = map(int, input().split())
indegree = [0] * (n+1)     #진입차수 초기화     #연결되어 있지 않다고 가정
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)     #정점 a에서 b로 가는 간선이 존재할 때 
    indegree[b] +=1     #b의 진입차수 1 증가
    
def topology_sort():
    result = []
    que = []     #Heapq 사용 위한 빈 리스트 선언 
    
    for i in range(1, n+1):
        if indegree[i] == 0:     #진입차수가 0인 노드를 힙에 삽입
            heappush(que, i)     #삽입한 노드들에 대하여,i의 크기가 작을 수록 먼저 푸는 것이 유리하다 (쉬운 문제이기 때문)
            
    while que:     #리스트가 빌 때까지 반복
        now = heappop(que)     
        result.append(now)
        for j in graph[now]:      #해당 노드와 연결된 노드들에 대하여
            indegree[j] -=1       #진입차수를 1 뺀다
            if indegree[j] ==0:     #진입차수가 0이 되는 노드를 리스트에 삽입
                heappush(que, j)
                
    for k in result:
        print(k, end=' ')

topology_sort()   
