A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

freeze = 0
count = 0

while A != B:
    if A < 0:
        count += (-1 * A ) * C
        A -= A
        
    elif A == 0 and freeze == 0:
        count += D
        freeze = 1
        
    else:
        count += (B - A) * E
        A += (B - A)
    
print(count)