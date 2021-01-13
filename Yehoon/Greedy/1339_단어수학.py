n = int(input())
alpha = []
for _ in range(n):
    alpha.append(input())


alpha_digit = {}
for alphabet in alpha:
    for i in range(len(alphabet)):
        if alphabet[i] not in alpha_digit.keys():
            alpha_digit[alphabet[i]] = 10 ** (len(alphabet[i:]) - 1)
        else:
            alpha_digit[alphabet[i]] += 10 ** (len(alphabet[i:]) - 1)

alpha_digit = sorted(alpha_digit.items(), key = lambda x:x[1], reverse=True)

result = 0
num = 9
for tmp in range(len(alpha_digit)):
    result += alpha_digit[tmp][1]*(num-tmp)

print(result)