reset_n = n = int(input())  # 26, 68, 84

cnt = 0

while True:
    tens = reset_n // 10  # 2, 6, 8, 4, 2
    ones = reset_n % 10  # 6, 8, 4, 2, 6
    result = (tens + ones) % 10  # 8, 4, 2, 6, 8

    reset_n = int(str(ones)+str(result))  # 68, 84, 42, 26
    cnt += 1

    if reset_n == n:
        print(cnt)
        break
