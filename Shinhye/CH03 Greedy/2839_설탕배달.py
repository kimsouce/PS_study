import sys
input = sys.stdin.readline

n = int(input())

cnt = 0

while True:
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break  # 5의 배수일 땐, 5만 사용한 게 최솟값, 뒤의 코드 무시
    n -= 3  # 5로 안나눠지면 3 빼기
    cnt += 1
    if n < 0:
        print(-1)
        break
