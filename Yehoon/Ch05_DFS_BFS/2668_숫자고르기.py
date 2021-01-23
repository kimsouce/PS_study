n = int(input())
graph = [int(input()) for i in range(n)]
graph.insert(0, 0)

visited = [False] * (n+1)
def dfs(graph, i, visited):
    #i = (3,0)
    #next = (1,0)
    next = graph[i[0]]

    #루프가 계속 돌면 종료
    if i[1] == 2 and next[1] == 2:
        visited[i[0]] = True
        visited[next[0]] = True
        return visited

    #루프 생성 전
    if i[1] < 2:
        next[1]+=1
        i[1]+=1
        dfs(graph, next, visited)

for i in range(1, n+1):
    tmp = [[i, 0] for i in graph]
    dfs(tmp, tmp[i], visited)

print(sum(visited))

valid = [i for i in range(1, len(visited)) if visited[i] == 1]
valid.sort()
for i in valid:
    print(i)



# def dfs(i):
#     x = under_row[i]
#     if tmp_visited[i] is False:
#         tmp_visited[i] = True
#         x = under_row[x]
#         dfs(x)
#     elif tmp_visited[i] is True and visited[i] is False and i==under_row[x]:
#         visited[i] = True
#         dfs(x)
#     else:
#         pass
#
#
# n = int(input())
# under_row = [int(input()) for i in range(n)]
# under_row.insert(0, 0)
# up_row = [i for i in range(n+1)]
#
# graph = list(zip(up_row, under_row))
#
# visited = [False]*(n+1)
# tmp_visited = visited.copy()
#
#
# for i in range(1, n+1):
#     dfs(i)
#
# print(sum(visited))
# for i in range(len(visited)):
#     if visited[i] is True:
#         print(i)