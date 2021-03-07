n = input()
p = len(n) // 2
left = 0
right = 0

for i in n[:p]:
    left += int(i)
for j in n[p:]:
    right += int(j)

if left == right:
    print("LUCKY")
else:
    print("READY")
