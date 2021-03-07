n = int(input())
wait_time = list(map(int, input().split()))
wait_time.sort()  # 정렬 후, 앞에서부터 더해줘야 최솟값구할 수 있음
result = 0

for i in range(n):
    result += sum(wait_time[:i+1])
print(result)
