import sys
input = sys.stdin.readline

t = int(input())

#data = [[], [1], [2,4,8,6], [9,7,1], [4,6], [5], [6], [9,3,1], [8,4,2,6], [9,1]]

for _ in range(t):
    a,b = map(int, input().split())
    a = a % 10

    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a*a) % 10)
    else:
        b = b % 4
        if b == 0:
            print((a**4) % 10)
        else:
            print((a**b) % 10)




#
# for _ in range(t):
#     a, b = map(int, input().split())
#     print((a**b) % 10)