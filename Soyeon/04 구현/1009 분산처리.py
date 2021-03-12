import sys
input = sys.stdin.readline

t = int(input())
data = [[], [1], [2,4,8,6], [3,9,7,1], [4, 6], [5], [6], [7,9, 3, 1], [8, 4, 2, 6], [9, 1]]


for i in range(t):
    a, b = map(int, input().split())
    if a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        if b % 2 == 0:
            print(data[a][1])
        elif b % 2 == 1:
            print(a)
    elif a == 2 or a == 3 or a == 7 or a == 8:
        if b % 4 == 0:
            print(data[a][3])
        elif b % 4 == 1:
            print(data[a][0])
        elif b % 4 == 2:
            print(data[a][1])
        elif b % 4 == 3:
            print(data[a][2])
    elif a % 10 == 0:
        print(10)





# data = []
#
# for i in range(t):
#     a, b = map(int, input().split())
#     data.append(a**b)
#
# for i in data:
#     print(i % 10)