computer = int(input())
network_num = int(input())
network_lines = [[0] * computer for i in range(computer)]
visited = [0 for i in range(computer)]
count = 0

for i in range(network_num):
    a, b = map(int, input().split())
    network_lines[a - 1][b - 1] = 1
    network_lines[b - 1][a - 1] = 1
def dfs(line):
    visited[line] = 1
    for i in range(computer):
        if network_lines[line][i] == 1 and visited[i] == 0:
            dfs(i)
dfs(0)
for i in range(1, computer):
    if visited[i] == 1:
        count += 1
print(count)

