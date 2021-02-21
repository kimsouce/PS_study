##오류코드...


from heapq import heappop, heappush

def dijkstra(start):
  result = [float('inf')for _ in range(n)]
  result[start] = 0
  que = []
  heappush(que, (result[start], start))
  while que:
    wei, node = heappop(que)
    if result[node]<wei:
      continue
    for fn, fw in graph[node]:
      if result[fn] > wei + fw:
        result[fn] = wei + fw
        heappush(que, (result[fn], fn))             
    return result


t = int(input())
for _ in range(t):
  n, d, c = map(int, input().split())
  graph = [[]for _ in range(n)]
  for _ in range(d):
    a, b, s = map(int, input().split())
    graph[b-1].append((a-1, s))
  answer = dijkstra(c-1)
  max_answer = 0
  count = 0
  for i in answer:
    if i != float('inf'):
      if max_answer < i:
        max_answer = i
      count += 1
  print(count, max_answer)
