n = int(input())
minutes = list(map(int, input().split()))
minutes.sort()

pre_time = 0
total_time = 0
for _ in range(n):
    pre_time += minutes[_]
    total_time += pre_time

print(total_time)