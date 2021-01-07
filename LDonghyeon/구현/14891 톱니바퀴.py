from collections import deque

def check_left(n, dir):
    if n < 1:
        return 
    else:
        if deqs[n + 1][6] != deqs[n][2]:
            check_left(n - 1, -dir)
            deqs[n].rotate(dir)

        else:
            return

def check_right(n, dir):
    if n > 4:
        return 
    else:
        if deqs[n - 1][2] != deqs[n][6]:
            check_right(n + 1, -dir)
            deqs[n].rotate(dir)

        else:
            return

deqs = {}
for i in range(1,5):
    deqs[i] = deque(list(input()))

K = int(input())

for _ in range(K):
    num, direction = map(int, input().split())
    check_left(num - 1, -direction)
    check_right(num + 1, -direction)
    deqs[num].rotate(direction)
    
    
    
count = 0
for i in range(1,len(deqs)+1):
    if i == 1 and deqs[i][0] == '1':
        count += 1
    elif i == 2 and deqs[i][0] == '1':
        count += 2
    elif i == 3 and deqs[i][0] == '1':
        count += 4
    elif i == 4 and deqs[i][0] == '1':
        count += 8
print(count) 