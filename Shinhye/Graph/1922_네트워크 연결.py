# 크루스칼 알고리즘 : 모든 노드를 연결할 때, 최소의 비용으로 연결
# 모든 간선(비용)에 대하여 정렬 수행한 뒤, 가장 거리(비용)가 짧은 간선부터 집합에 포함시키기

import sys
input = sys.stdin.readline  # 352ms, 안쓰면 4852ms


def find_parent(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 떄까지 재귀적으로 호출 후, 갱신
    if computer[x] != x:
        computer[x] = find_parent(computer[x])
    return computer[x]


def union_parent(a, b):  # a, b컴퓨터 연결
    a = find_parent(a)
    b = find_parent(b)
    if a < b:  # 더 작은 노드(컴퓨터 번호)가 루트 노드가 되도록 설정
        computer[b] = a
    else:
        computer[a] = b


n = int(input())  # 컴퓨터(노드)의 수
m = int(input())  # 연결할 선의 수

computer = [0] * (n+1)  # 부모 테이블 초기화
for i in range(1, n+1):
    computer[i] = i  # 부모 테이블을 자기 자신으로 초기화

# 연결할 선을 담을 리스트
lines = []
# 연결할 선에 대한 정보 입력받기
for _ in range(m):
    a, b, cost = map(int, input().split())
    lines.append((cost, a, b))  # 비용순으로 정렬하기 위해 cost를 가장 먼저 써줌

# 선을 설치하는데 드는 비용순으로 정렬
lines.sort()

# 최종비용 담을 변수
result = 0
# 선을 하나씩 확인
for line in lines:
    cost, a, b = line
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

print(result)
