import sys

# +연산부분
def operate(num):
    tmp = ''
    result = 0
    for v in num:
        if v.isdigit(): 
            tmp += v
        elif v == '+':
            result += int(tmp)
            tmp = ''
        elif v == '-':
            break
    result += int(tmp)

    return result

num = sys.stdin.readline().rstrip()

result = 0

for i in range(len(num)):
    if i == 0 and num[0].isdigit(): # 처음 시작이 양수일때만 연산
        result += operate(num)
    if num[i] == '-': # 음수일때 뒤에꺼 연산
        result -= operate(num[i+1:])
    
print(result)
