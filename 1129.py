alternativas = ['A', 'B', 'C', 'D', 'E']


n = int(input())

while n:
    for _ in range(n):
        respostas = [i for i, a in enumerate(input().split()) if int(a) <= 127]
        if len(respostas) != 1:
            print("*")
        else:
            print(alternativas[respostas[0]])
    n = int(input())