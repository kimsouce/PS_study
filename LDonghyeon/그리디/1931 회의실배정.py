import sys
N = int(sys.stdin.readline())

time = []
for _ in range(N):
    time.append(list(map(int,sys.stdin.readline().split())))

time.sort(key = lambda x : (x[1],x[0]))

count = 1
end = time[0][1]

for i in range(1,len(time)):
    if end <= time[i][0] or (end <= time[i][0] and time[i][0] == time[i][1]):
        end = time[i][1]
        count+=1
    
print(count)