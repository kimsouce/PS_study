food_times = [int(i) for i in str(input())[1:-1].split(",")]
k = int(input())

cnt = 0
idx = len(food_times)

def mukbang(cnt, idx, food_times):
    if cnt == k:
        return idx+1

    if idx == len(food_times):
        cnt += 1
        idx = 0
        return mukbang(cnt, idx, food_times)

    if food_times[idx] == 0:
        cnt += 1
        idx += 1
        return mukbang(cnt, idx, food_times)

    cnt += 1
    idx += 1
    food_times[idx] -= 1
    return mukbang(cnt, idx, food_times)
print(mukbang(cnt, idx, food_times))