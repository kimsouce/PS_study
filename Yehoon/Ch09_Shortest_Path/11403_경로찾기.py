import sys
input = sys.stdin.readline
inf = int(1e9)
n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for k in range(n):
    for a in range(n):
        for b in range(n):
            #a->k =1 , k->b =1 이면 a->b 간선이 존재한다는 뜻
            if matrix[a][k] and matrix[k][b]:
                matrix[a][b] = 1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()