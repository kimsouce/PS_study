n = int(input())

v = [[0]*101 for _ in range(101)]  #방문한 꼭짓점을 저장하기 위해 맵 초기화 (0<=x,y<=100)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]  #[R, U, L, D] 

for _ in range(n):
  x, y, d, g = map(int, input().split())
  v[x][y] = 1  #방문한 꼭짓점은 1로 표시
  moves = [d] #방향 저장
  for _ in range(g):
    moves +=((move+1)%4 for move in moves[::-1])  #이전세대 moves +  이전세대 moves원소를 거꾸로 정렬하고, 1씩 더한 후 4로 나눈 것
  for move in moves:
    nx = x + dx[move]  #이동
    ny = y + dy[move]
    v[nx][ny] = 1
    x, y = nx, ny

count = 0
for i in range(100):
  for j in range(100):
    if v[i][j] ==1 and v[i+1][j] ==1 and v[i][j+1] ==1 and v[i+1][j+1] ==1:  #굳이 변이 안생겨도 됨. 1 by 1 정사각형의 네 꼭짓점이 모두 방문되어 있으면 count 올려준다
      count +=1

print(count)
  

# 주의!!
# 다른 문제들과는 다르게, (열,행) 이라고 생각해야 한다. 
# (4,2)인 경우, 2행 4열임
# 다시말해 포맷은 행렬이지만, 좌표평면 위에서 x값과 y 값이라고 생각하면 된다.. 
# 그러므로 R =(1,0) U =(0,1) L =(-1,0) D =(0,-1) 이런식으로 기존 문제와 방향벡터도 다르게 설정해야 함
