n =int(input())
m = int(input())
friends = {}
invite = set()  

for _ in range(m):
  a, b = map(int, input().split())
  if a not in friends:
    friends[a] = []  #각 친구들에 대해 빈 리스트를 선언  #2의 친구들은 friends[2]에 담김
  if b not in friends:
    friends[b] = []
  friends[a].append(b)
  friends[b].append(a)

for a in friends[1]:  #상근이의 친구 담기
  invite.add(a)
  if a not in friends:
    continue
  else:
    for b in friends[a]:  #상근이 친구의 친구 담기
      invite.add(b)


print(len(invite)-1)

'''
#오답 코드

n = int(input())
m = int(input())
friends = []  
invited = []
add=[]
new_list = []

for _ in range(m):
  a, b = map(int, input().split())
  friends.append([a,b])

for i in range(m):
  if friends[i][0] ==1:
    invited.append(friends[i][1])  #상근이의 친구 담기

for i in range(m):   
  for j in invited:
    if friends[i][0] == j:
      add.append(friends[i][1])  #상근이 친구의 친구 담기

result = invited + add  #합해서
for v in result:
  if v not in new_list:
    new_list.append(v)  #중복이 있으면 빼준다

print(len(new_list))
'''
