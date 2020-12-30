n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = n  # 총 감독관은 시험장마다 1명씩 배치, cnt를 n으로 시작
for i in range(n):
    a[i] -= b
    if a[i] > 0:
        cnt += a[i] // c

        if a[i] % c != 0:
            cnt += 1


print(cnt)
