jog, rod = map(int, input().split())

pontos = list(map(int, input().split()))
soma_pontos = [sum([pontos[j] for j in range(i, jog*rod, jog)]) for i in range(jog)]
soma_pontos = soma_pontos[::-1]
print(len(soma_pontos)-soma_pontos.index(max(soma_pontos)))




