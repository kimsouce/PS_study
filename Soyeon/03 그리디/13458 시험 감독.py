n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
count = 0

for i in a: #리스트 a에 있는 값들을 하나씩 비교
    i -= b 
    count +=1 #총감독관은 무조건 한 명 존재해야 하므로, 한번 빼고 count 올려줌
    if i >0:
      count += i//c
      if i%c !=0:
        count +=1
print(count)


#오답 
'''
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
count = 0
result = 0


for i in a:
    i -= b
    count +=1
    if i !=0: # 처음에 i가 0이 아닐때 라고 놓으니까, 테스트케이스 2번 만에 오류가 났다. i>0랑 무슨 차이인지 모르겠다.. 
      if i//c == 0: #몫이 0일 때(즉 c가 i보다 클 때)를 따로 빼주었는데, 이 경우는 i%c != 0 여기에 포함됨으로 필요 없는 것 같다. 
        count += 1
      else:
        count += i//c
        if i%c !=0:
          count +=1
print(count)
'''
