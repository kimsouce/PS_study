n = int(input())     #노드의 수
m = int(input())     #간선의 수
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))     #a컴퓨터와 b컴퓨터가 연결되어 있다(a에서 b로 가는 경로가 존재한다)


node = [0]      #인덱스를 1부터 시작하기 위해 0을 미리 추가해줌
graph = sorted(graph, key=lambda k :k[2])     #weight 기준으로 간선 정보 정렬

for i in range(1, n+1):
    node.append(i)

def find(s):     
    if s != node[s]:     #자기자신이 자기자신의 부모노드가 아니라면   #즉, 진입하는 간선이 존재한다면 
        node[s] = find(node[s])     #해당 노드의 부모 노드를 찾아줌   
    return node[s]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    node[root2] = root1     #root1이 root2의 부모노드
    
E = 0     #간선의 개수가 V-1이 되면 while문 멈추기 위해
cost = 0     #최소비용 구하기 위해

while True:
    if E == n-1:
        break
    u, v, w = graph.pop(0)     #sorting한 graph의 첫번쩨(cost가 가장 적은 원소) 반환
    if find(u) != find(v):     #노드 u와 노드 v가 다른 집합에 속해있으면 
        union(u, v)
        cost += w
        E +=1
        
print(cost)
