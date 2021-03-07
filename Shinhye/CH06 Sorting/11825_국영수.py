import sys
input = sys.stdin.readline

# 딕셔너리, 튜플은 정렬 사용X
students = [list(input().split()) for _ in range(int(input()))]

# 성적을 정수형으로 변환
# 방법1
for i in range(len(students)):
    students[i][1], students[i][2], students[i][3] = int(
        students[i][1]), int(students[i][2]), int(students[i][3])

'''
방법2
students = []
for i in range(int(input())):
    name, kor, eng, math = input().split()
    students.append([name, int(kor), int(eng), int(math)])

'''

# 국어(내림) -> 영어(오름) -> 수학(내림) -> 이름(오름)
# 방법1
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
# 방법2
# students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for names in students:
    print(names[0])
