n = int(input())
student = []
for _ in range(n):
    [name, kor, eng, math] = map(str, input().split())
    student.append([name, int(kor), int(eng),int(math)])


student_sorted = sorted(student, key = lambda x : (-x[1], x[2], -x[3], x[0]))

for _ in student_sorted:
    print(student[0])