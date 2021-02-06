from itertools import combinations
n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
target = 1
#무게는 1보다 크니까 조합해서 나올 수 있는 무게에서 +1만 추가 되면 측정할 수 없는 무게의 최소값

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
