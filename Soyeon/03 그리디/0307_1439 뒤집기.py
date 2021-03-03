s = input()

def search(s):
  count = 0    #행동 횟수 
  for i in range(len(s)-1):
    if s[i] == s[i+1]:     #앞뒤가 같을 때는 지나치기
      continue
    else:     #아닐 때 뒤집는 횟수 1씩 늘리기
      count +=1
  if count % 2 == 0:     #011000  #010100  #01010100 #짝수번 바뀔 때
    print(count//2)
  else:     #01100101 #홀수번 바뀔 때
    print(count//2+1)

search(s)
