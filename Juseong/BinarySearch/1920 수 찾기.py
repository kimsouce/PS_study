n = int(input())
js = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

for i in target:
    if i in js:
        print('1', end='\n')
    else:
        print('0', end='\n')
