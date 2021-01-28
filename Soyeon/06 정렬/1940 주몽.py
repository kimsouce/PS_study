n = int(input())
m = int(input())
n_list = list(map(int, input().split()))

n_list = sorted(n_list, key = lambda k :k)  #오름차순으로 정렬  #어차피 완전탐색이라 정렬 안해줘도 무방.. 정렬 문제라서 정렬 해줌
count = 0
result = 0

while len(n_list) >0:   #n_list의 원소가 모두 없어질 때 까지 반복
  for i in n_list:
    result = m - i  
    n_list.remove(i)  # 중복으로 확인하지 않기 위해 n_list에서 이미 확인한 i를 제거해줌
    for j in n_list:
      if j == result:  #i+j=m이라고 할 때, m을 만들 수 있는 j가 리스트 안에 존재하면,
        count +=1   #count를 한개 올려줌 
      else:
        continue   #아니라면 다시 i 에 대한 for문으로 돌아감
print(count)




'''
#정렬을 사용해서 푼 코드
N = int(input())
M = int(input())
li = sorted(list(map(int, input().split())))
ans = 0
s, e = 0, len(li)-1

while s != e:
    if li[s] + li[e] == M:
        ans += 1
        e -= 1
    elif li[s] + li[e] < M:
        s += 1
    elif li[s] + li[e] > M:
        e -= 1
        
print(ans)

'''
