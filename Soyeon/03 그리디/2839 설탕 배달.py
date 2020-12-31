n = int(input())
count = 0

while True:
  if (n%5) ==0:
    count += n//5
    print(count)
    break #5kg짜리를 최대한 많이 들기 위해
  n -=3 #n이 5의 배수가 아니라면 5의 배수가 될 때 까지 3kg만큼씩 줄인다 -1
  count +=1 
  if n<0:
    print('-1')
    break #1의 과정을 반복하다가 5의 배수가 나오지 못한 채, n이 0보다 작아지면 3kg과 5kg으로 만들 수 없는 정수이다. 따라서 -1을 프린트 해준다
    
    
    #오답
    '''
    n = int(input())
count = 0

while n >=5:
  while n %5 !=0:
    n -=3
    count +=1
  count +=n//5
  n %=5

if n==3:
  count +=1

if n %5 !=0: # 이 구문 때문에 1,2,4인 경우는 고려된다
  count -=1
  '''
  #이런식으로 해주면 3과 5보다 크지만, 3과 5로 만들 수 없는 정수인 경우가 고려되지 않는다
  #예: 7
