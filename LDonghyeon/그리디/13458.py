N = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())

supervisor = 0

for stu in A:
    #총감독관
    stu -= B
    supervisor += 1

    #부감독관
    if stu > 0:
        if (stu / C) > (stu // C):
            supervisor += (stu // C + 1)
        else:
            supervisor += (stu // C)

print(supervisor)