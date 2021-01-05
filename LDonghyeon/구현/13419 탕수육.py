def calc(word):
    first = ''
    second = ''
    for i in range(len(word)):
        if i % 2 == 0:
            first += word[i]
        else:
            second += word[i]
    return (first,second)


N = int(input())
result = []

for _ in range(N):
    word = input()

    if (len(word) % 2) == 1: # 홀수 일떄
        word *= 2
        first, second = calc(word)

    else: # 짝수 일때
        first,second = calc(word)
    result.append(first)
    result.append(second)

for v in result:
    print(v)