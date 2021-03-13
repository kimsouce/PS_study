from collections import deque

t = int(input())
# m의 값은 인덱스
for _ in range(t):
    n, m = map(int, input().split())
    # m : 몇 번째로 인쇄되었는지 궁금한 문서가
    # 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수
    # 0부터 시작
    priorities = list(enumerate(map(int, input().split())))

    q = deque(priorities)

    sort_lst = sorted(priorities, key=lambda x: x[1], reverse=True)

    cnt = 0

    while q:
        now = q.popleft()

        if now[1] == sort_lst[0][1]:  # 중요도가 같으면
            cnt += 1
            sort_lst.pop(0)
            if now[0] == m:
                break
        else:
            q.append(now)
    print(cnt)
