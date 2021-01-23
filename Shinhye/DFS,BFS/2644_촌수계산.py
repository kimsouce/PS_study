from collections import deque
q = deque()

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
chk = [0] * (n+1)

a = [[] for _ in range(n+1)]  # 인원수만큼 초기화(인접리스트)
for _ in range(m):
    p, c = map(int, input().split())
    a[p].append(c)
    a[c].append(p)


def relate():  # p1, p2관계 = 시작점, 끝점
    q.append(p1)

    while q:
        now = q.popleft()

        for i in a[now]:
            if not chk[i]:
                q.append(i)
                chk[i] = chk[now]+1

        if now == p2:
            return chk[p2]
    return -1


print(relate())
