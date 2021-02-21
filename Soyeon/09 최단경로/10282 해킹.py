##오류코드...


from heapq import heappop, heappush     #우선순위 큐를 구현하기 위해

def dijkstra(start):
  result = [float('inf')for _ in range(n)]     #start로 부터의 거리 값을 저장하기 위함
  result[start] = 0     #시작노드는 가중치가 없으므로 0
  que = []
  heappush(que, (result[start], start))     #시작노드부터 탐색
  while que:     #list(que)에 남아있는 노드가 없으면 종료
    wei, node = heappop(que)     #탐색해야 할 가중치(거리)와 노드를 가져옴
    if result[node]<wei:     #기존 노드에 저장된 가중치보다 새로운 가중치가 더 큰 경우 제외
      continue
    for fn, fw in graph[node]:
      if result[fn] > wei + fw:    #기존 노드에 저장된 가중치 > 새로운 경로로 노드에 도착했을 때 합한 가중치
        result[fn] = wei + fw
        heappush(que, (result[fn], fn))    #다음 인접 거리를 계산하기 위해 큐에 삽입         
    return result


t = int(input())
for _ in range(t):
  n, d, c = map(int, input().split())
  graph = [[]for _ in range(n)]
  for _ in range(d):
    a, b, s = map(int, input().split())
    graph[b-1].append((a-1, s))
  answer = dijkstra(c-1)
  max_answer = 0     #최종 감염되는데 걸리는 시간
  count = 0     #최종 감염되는 컴퓨터 개수
  for i in answer:
    if i != float('inf'):
      if max_answer < i:
        max_answer = i
      count += 1
  print(count, max_answer)
