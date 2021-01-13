n = int(input())

result = 0
while True:
    if n%5 == 0:
        #5kg 짜리로 최대한 많이 들기
        result += n//5
        print(result)
        break

    n -= 3 #n이 5의 배수가 될 때까지 3kg씩 빼주기
    result += 1
    if n<0:
        print(-1) #계속 3kg씩 빼줘도 5의 배수를 못 만들면 3과 5의 조합으로 만들 수 없는 수
        break
