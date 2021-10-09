a, c = map(int, input().split())
while a != 0:
    alt_final = list(map(int, input().split()))
    
    tot = 0
    minimo = alt_final[0]
    for i in range(1, c):
        if minimo < alt_final[i]:
            tot +=  (alt_final[i] - minimo)

        minimo = alt_final[i]
            
    tot +=  (a - minimo)
    print(tot)
    a, c = map(int, input().split())
