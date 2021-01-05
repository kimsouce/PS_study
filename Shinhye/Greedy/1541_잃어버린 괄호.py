# - 뒷부분은 묶어서 연산해줘야 최솟값을 만들 수 있음

# 55-50+40
data = input().split('-')
# - 기준으로 분리
# - 뒷부분은 따로 더해서 빼주기

result = []
for data_s in data:  # 55, 50+40
    cnt = 0
    num = data_s.split('+')  # 50, 40
    for n in num:
        cnt += int(n)
    result.append(cnt)
for i in range(1, len(result)):
    result[0] -= result[i]
    # 첫 번째로 들어간 값은 +숫자값이므로 거기서 빼줌

print(result[0])
