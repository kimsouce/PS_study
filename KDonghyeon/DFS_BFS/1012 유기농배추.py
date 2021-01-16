import collections
import sys
sys.setrecursionlimit(50000)
dx=[-1,0,1,0] # 좌, 우
dy=[0,1,0,-1] # 위, 아래

test_case = int(input())
conut = 0
def dfs(x,y):
    farm[x][y] = 0
    for i in range(4): # 4방향을 돌면서, 주변(상,하,좌,우)에 배추가 있는지 check
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx >= M or ny <0 or ny >= N: 
            continue  # 기준을 초과 또는 미달하면 pass
        if farm[nx][ny] == 1:
            dfs(nx,ny) # 근처에 배추가 있으면 dfs로 재귀
def solve():
    count = 0
    for i in range(M): 
        for j in range(N): # 전체 matrix를 확인하며 1(=배추)의 유무를 확인
            if farm[i][j] == 1: # 만약 배추가 있다면
                dfs(i,j) # dfs를 통해 인접한 배추를 check
                count += 1 # dfs가 시작되면, 주변 (상하,좌,우)는 모두 1개의 영역으로 count
    print(count) # 재귀를 통한 dfs 탐색이 끝난 후, 얻은 값을 출력 ( 최종 )

for _ in range(test_case):
    M,N,K = map(int, input().split()) 
    farm =[[0]*N for _ in range(M)] # farm(=matrix)를 0으로 initialization
    for _ in range(K):
        X, Y = map(int, input().split())
        farm[X][Y]=1 # farm(=matrix) 속의 배추 위치를 1로 전환
    solve()
