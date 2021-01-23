n = int(input())

students = []
for i in range(n):
  data = input().split()
  students.append((data[0], int(data[1]), int(data[2]), int(data[3]))) #이름, 국, 영, 수  #점수에 int 씌워줘야 한다

students = sorted(students, key = lambda k: (-k[1], k[2], -k[3], k[0]))   # int의 경우 reverse를 하려면 앞에 - 만 붙여주면 된다(str인 경우는 reverse=Ture)


for data in students:
  print(data[0], sep="\n")
