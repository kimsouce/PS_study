# 서로소 집합 : 공통 원소가 없는 두 집합
# 서로소 집합 자료구조 : 서로소 부분집합들로 나눠진 원소들의 연결을 확인해 부모 노드를 찾을 수 있는 자료구조

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)  # 쓰지않으면 런타임 에러 (RecursionError)


def find(x):  # 부모 노드 찾기
    if parent[x] != x:  # 루트 노드를 찾을 때까지 호출
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):  # a, b연결
    a = find(a)
    b = find(b)
    if a < b:  # 큰 노드가 작은 노드를 가르키도록 부모테이블 갱신
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(n+1):  # 0부터 시작, n+1개
    parent[i] = i  # 자기 자신으로 초기화


for _ in range(m):
    check, a, b = map(int, input().split())

    if check == 0:  # a,b의 집합을 합침
        union(a, b)

    else:  # 이미 같은 집합(check == 1)
        if find(a) == find(b):  # 루트노드가 일치하면
            print('YES')
        else:
            print('NO')
