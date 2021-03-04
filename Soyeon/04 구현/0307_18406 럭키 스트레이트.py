n = input()

def Lucky_straight(n):
  right = 0
  left = 0
  for i in range(len(n)):
    if i < len(n)//2:
      right += int(n[i])     #str로 받았기 때문에 int로 씌워줘야 함
    else:
      left += int(n[i])
  if right == left:
    print('LUCKY')
  else:
    print('READY')

Lucky_straight(n)
    
