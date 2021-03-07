t = int(input())

for _ in range(t):
    data = input()  # ABC
    first = ''
    second = ''
    if len(data) % 2 == 0:  # data의 길이가 짝수일 때,
        for i in range(len(data)):
            if i % 2 == 0:
                first += data[i]  # AC
            else:
                second += data[i]  # B
        print(first)
        print(second)
    else:  # data의 길이가 홀수일 때,
        for i in range(len(data)):
            if i % 2 == 0:
                first += data[i]  # AC
            else:
                second += data[i]  # B
        print(first+second)
        print(second+first)

# 함수이용
# def op(data):
#     first = ''
#     second = ''
#     for i in range(len(data)):
#         if i % 2 == 0:
#             first += data[i]
#         else:
#             second += data[i]
#     return (first, second)

# t = int(input())

# for _ in range(t):
#     data = input()
#     if len(data) % 2 == 0:  # data의 길이가 짝수일 때,
#         first, second = op(data)
#         print(first)
#         print(second)
#     else:  # data의 길이가 홀수일 때,
#         first, second = op(data)
#         print(first+second)
#         print(second+first)
