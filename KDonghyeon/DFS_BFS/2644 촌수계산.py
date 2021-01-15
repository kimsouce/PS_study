import collections

def bfs(v):
    q = collections.deque()
    visited = [False]*(n+1)
    q.append(v)
    visited[v] = True
    level = 0
    while q:
        level += 1
        for _ in range(len(q)):
            v = q.popleft()
            if v == end:
                return level - 1
            for j in relation[v]:
                if not(visited[j]):
                    visited[j] = True
                    q.append(j)
    return -1

n = int(input())
start, end = map(int, input().split())
m = int(input())
relation = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

print(bfs(start))
