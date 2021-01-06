n, x, k = map(int, input().split())
moves = []
for _ in range(k):
	move.append(list(map(int, input().split())))

array= [0]*n
array[x-1] = 1 #공이 들어있는 인덱스에만 1을 저장

for move in moves:
	array[moves[0] -1], array[moves[1]-1] = array[moves[1]-1], array[moves[0]-1] #스왑
print(array.index(1)+1) 


'''
#시간 초과 난 코드..
n, x, k = map(int, input().split())
array=[]
for i in range(n):
  if i ==x-1:
    array.append(1)
  else:
    array.append(0)
    
for _ in range(k):
  a, b = map(int, input().split())
  for j in range(len(array)):
    if j == a-1:
      array[j], array[b-1] = array[b-1], array[j]

print((array.index(1))+1)

#시간 복잡도..?
'''
