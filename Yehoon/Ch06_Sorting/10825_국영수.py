n = int(input())
score = []

for i in range(n):
    name, korean, english, math = input().split()
    score.append([name, int(korean), int(english), int(math)])

score = sorted(score, key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in score:
    print(i[0])