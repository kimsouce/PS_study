
### 알게된 내용들

11047. 개행으로 입력받기

<pre>
<code>
coins = []
for i in range(n):
  coins.append(int(input()))
</code>
</pre>

1931. 람다함수

<pre>
<code>
datas = sorted(datas, key=lambda k:k[0])
datas = sorted(datas, key=lambda k:k[1])
</code>
</pre>

15685. 리스트 append

<pre>
<code>
moves +=((move+1)%4 for move in moves[::-1])
</code>
</pre>

3048. 딕셔너리

<pre>
<code>
dir = {} #딕셔너리 사용 #key값과 value값을 설정하기 위해
for ant in ants[0]:
  dir[ant] = 0 # 첫번째 그룹의 value는 0이다
for ant in ants[1]:
  dir[ant] = 1 # 두번째 그룹의 value는 1이다
</code>
</pre>

2644. 인접행렬 만들기

<pre>
<code>
for _ in range(m):
  x, y = map(int, input().split())
  family[x].append(y)
  family[y].append(x)
</code>
</pre>
