n, m = map(int, input().split())
lab = []
for i in range(n):
    lab.append(list(map(int, input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
temp = [[0] *m for _ in range(n)]
#바이러스 같은건 dfs
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0<= ny < n:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

#안전한 영역 계산
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = lab[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        result = max(result, get_score())
        return