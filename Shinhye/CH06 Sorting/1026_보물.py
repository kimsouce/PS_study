n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

sum = 0
for i in range(n):
    sum += a[i] * max(b)
    b.pop(b.index(max(b)))

print(sum)

# b_re = sorted(b, reverse=True)

# sum = 0
# for i in range(n):
#     sum += a[i] * b_re[i]
# print(sum)
