df = [2,3,4,6,7,8]
p = df.pop()

for j in df:
    print(j)
    if j // p == 0:
        df.remove(j)
        print(df)