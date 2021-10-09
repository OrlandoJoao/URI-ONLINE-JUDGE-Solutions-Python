while True:
    try:
        n = int(input())

        dic = {}
        for _ in range(n):
            t, ed  = input().split()
            
            dic[t] = dic.get(t, [0, 0])
            if ed == 'E':
               dic[t][0] += 1
            else:
                dic[t][1] += 1

        print(sum([min(e, d) for e, d in dic.values()]))

    except EOFError:
        break
