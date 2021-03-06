n, k = map(int, input().split())

che = [False for _ in range(n+1)]
cnt = 0

for i in range(2,n+1):
        for j in range(i,n+1,i):
            if che[j] == False:
                che[j] = True
                cnt += 1

                if cnt == k:
                    print(j)
                    break



# che = [i for i in range(2, n+1)]
# removed = []
#
# while che:
#     p = min(che)
#     for j in che:
#         removed.append(p)
#         che.remove(p)
#
#         if j // p == 0:
#             removed.append(j)
#     print(che)
# print(removed[k-1])