x = int(input())
d = [0] * (x+1) # 최소 연산 개수 저장할 리스트

for i in range(2, x+1):
    # -1, /3, /2했을 때, 최소값을 d[i]에 갱신
    d[i] = d[i-1]+1 
    
    if i % 3 == 0: 
        d[i] = min(d[i], d[i//3] + 1)
    if i % 2 == 0: 
        d[i] = min(d[i], d[i//2] + 1)
print(d[x])

