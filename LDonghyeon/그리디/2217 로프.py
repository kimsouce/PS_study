N = int(input())

weight = []
for _ in range(N):
    weight.append(int(input()))

weight.sort(reverse = True)
max_weight = 0
for i in range(len(weight)):
    temp = weight[i] * (i + 1)
    if max_weight > temp:
        continue
    else:
        max_weight = temp

print(max_weight)    
