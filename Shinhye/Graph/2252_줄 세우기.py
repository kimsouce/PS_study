# 위상정렬 : 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘 = 사이클이 없는 방향 그래프
# 특징 : 답안은 여러 가지가 될 수 있다는 점(큐에 들어가는 원소 2개이상일 경우)
# EX) 선수과목을 고려한 학습순서 설정
from collections import deque
import sys
input = sys.stdin.readline  # 292ms -> sys안쓰면 4644ms

n, m = map(int, input().split())
indegree = [0] * (n+1)  # 진입차수 전부 0으로 세팅
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1  # 진입차수 1 증가


def topology_sort():
    result = []
    q = deque()

    # 처음 시작
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:  # 현재 노드(학생)에 연결된 간선(비교하고자 하는 학생)들 1씩 제거
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=" ")


topology_sort()
