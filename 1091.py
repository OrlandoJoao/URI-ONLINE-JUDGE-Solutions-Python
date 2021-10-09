k = int(input())

while (k != 0):
    n, m = map(int, input().split())

    for i in range(k):
        x, y = map(int, input().split())
        if n==x or m==y:
            print("divisa")
        elif n < x and m < y:
            print("NE")
        elif n > x and m < y:
            print("NO")
        elif n > x  and m > y:
            print("SO")
        else:
            print("SE")
            
    k = int(input())
