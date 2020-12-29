N = int(input())
time = list(map(int,input().split()))

time.sort()
sum_arr = []
for i in range(1, len(time)):
    sum_arr.append(sum(time[:i])+time[i])

print(sum(sum_arr) + time[0])
