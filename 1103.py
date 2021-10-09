h1, m1, h2, m2 = map(int, input().split())

while not(h1 == h2 == m1 == m2 == 0):
    t1 = h1*60+m1
    t2 = h2*60+m2
    if t1 > t2:
        print((24*60)-t1+t2)
    else:
        print(t2-t1)
    h1, m1, h2, m2 = map(int, input().split())
