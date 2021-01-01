import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    pick = 1  # 1위는 반드시 채용
    ranks = [tuple(map(int, input().split())) for _ in range(n)]

    # 서류 기준 정렬
    ranks = sorted(ranks, key=lambda x: x[0])
    c = ranks[0][1]  # 기준등수(서류1위의 면접등수)

    # 인터뷰 순위만 비교
    for cv, interview in ranks:
        if c > interview:
            pick += 1
            c = interview
    print(pick)
