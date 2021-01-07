t = int(input())
games=[]
for _ in range(t):
  games.append(input())

for game in games:
    if len(game) %2 == 0: #문자열의 길이가 짝수일 때
      print(game[0::2])  #인덱스가 0인것 부터 2씩 증가하면서 가져온다
      print(game[1::2])  #인덱스가 1인것 부터 2씩 증가면서 가져온다
    else:
      print(game[0::2],game[1::2], sep='')  #sep='' 안붙여주면 공백이 출력되기 때문
      print(game[1::2],game[0::2],sep='')
