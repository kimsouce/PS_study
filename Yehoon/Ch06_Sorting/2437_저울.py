from itertools import combinations
n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
target = 1
for i in range(len(num_list)):
    if target < num_list[i]:
        break
    target += num_list[i]
print(target)

# 합의 조합
# combi = []
# for i in range(n):
#     tmp = combinations(num_list, i)
# print(tmp)
# combi = list(set(combi))
# total = [i for i in range(sum(num_list)+1)]
# result = [value for value in total if value not in combi]
# print(min(result))
