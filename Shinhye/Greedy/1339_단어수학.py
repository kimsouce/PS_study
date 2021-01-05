n = int(input())
alphabet = [input() for _ in range(n)]
# ['GCF', 'ACDEB']
dict = {}

# 자릿값을 10의 지수혀앹로 저장
for alpha in alphabet:
    cnt = 0
    for a in alpha:
        if a not in dict:
            dict[a] = 10 ** (len(alpha) - 1 - cnt)
        elif a in dict:
            dict[a] += 10 ** (len(alpha) - 1 - cnt)
        cnt += 1

# values값들을 기준으로 내림차순 정렬
dict_list = sorted(list(dict.values()), reverse=True)

result = 0
# 정렬된 값들을 9부터 배정해주기
for i in range(len(dict_list)):
    result += dict_list[i] * (9-i)

print(result)
