n = int(input())
rope = []
for i in range(n):
  rope.append(int(input()))

rope.sort(reverse=True) #로프가 가장 무거운 것 부터 따져준다 

for i in range(n):
  rope[i] = rope[i] * (i+1) #로프가 버틸 수 있는 최대 중량 * 버틸 수 있는 로프 개수 -1
rope.sort(reverse=True) #최대값 찾기 위해 -2
  
print(rope[0])


#오답
'''
n = int(input())
rope = []
for i in range(n):
  rope.append(int(input()))

rope.sort()

weight = rope[0] * n #아무 생각 없이 (로프가 버틸 수 있는 최대 중량이 가장 작은 것 *로프개수) 해줌.. 이렇게 하면 안된다
print(weight)
'''

#예시
#rope = [100, 80, 60, 20, 10]
#1번 연산 = [100*1, 80*2, 60*3, 20*4, 10*5]
#2번 정렬 = [180, 160, 100, 100, 80]
#최댓값 = 180(세번째로프*3)
