a = int(input())  # 원래 고기의 온도
b = int(input())  # 목표온도
c = int(input())  # 1도당 얼어있는 고기 데우는 시간
d = int(input())  # 얼어있는 고기 해동 시간
e = int(input())  # 얼어있지 않은 고기 해동 시간

time = 0
if a < 0:
    time += ((a*-1)*c)+d+(b*e)
else:
    time += (b-a) * e

print(time)
