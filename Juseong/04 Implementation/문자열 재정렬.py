data = input()

sorted_data = []
value = 0

for i in data:
    if i.isalpha():
        sorted_data.append(i)
    else:
        value += int(i)


sorted_data.sort()

if value != 0:
    sorted_data.append(str(value))
# int형태로는 리스트에 삽입할 수 없다.

print(''.join(sorted_data))

