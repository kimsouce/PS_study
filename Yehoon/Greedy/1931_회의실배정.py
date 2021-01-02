n = int(input())
meeting_time = [tuple(map(int, input().split())) for _ in range(n)]

meeting_time.sort(key=lambda x: (x[1], x[0]))
# print(meeting_time)
count = 0
end_time = 0
for start, end in meeting_time:
    if end_time <= start:
        #전 회의 끝나는 시간이 다음 회의 시작하는 시간보다 같거나 으면 다음 회의 시작
        count += 1
        end_time = end
        #끝나는 시간 업데이트

print(count)