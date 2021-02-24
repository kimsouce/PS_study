from heapq import heappop, heappush     #리스트 내의 가장 작은 값을 가장 앞으로 옮기기 위해  #즉, 난이도가 쉬운 문제를 앞으로 보내기 위해

n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] +=1
    
def topology_sort():
    result = []
    que = []
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            heappush(que, i)
            
    while que:
        now = heappop(que)
        result.append(now)
        for j in graph[now]:
            indegree[j] -=1
            if indegree[j] ==0:
                heappush(que, j)
                
    for k in result:
        print(k, end=' ')

topology_sort()   
