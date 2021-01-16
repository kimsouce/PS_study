import sys
from collections import deque
input = sys.stdin.readline # input보다 엄청나게 빠름 => 입출력이 많을 때 사용하자.

dx = [1, -1, 0 ,0] 
dy = [0, 0, 1, -1]
# m이 가로 n이 세로
m, n = map(int, input().split())
farm = []

for i in range(n):
    farm.append(list(map(int, input().split())))

queue = deque()

for i in range(n):
    for j in range(m):
        if farm[i][j] == 1:
            queue.append([i,j])

def bfs():
    global queue
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and farm[x][y] == 0:
                farm[x][y] = farm[a][b]+1
                queue.append([x,y])

def check():
    answer = 0
    for i in range(n):
        for j in range(m):
            tmp = farm[i][j]
            if tmp == 0: # 다 돌았을 때, 0이 있다는 것은 숙성이 불가능한 토마토가 있다는 것과 같다.
                print(-1)
                return
            answer = max(answer, tmp)
            print(answer)
    print(answer-1)
bfs()
check()
