# 1121

def esquerda(orientacao):
    ordem = ['N', 'O', 'S', 'L']
    if ordem.index(orientacao) == 3:
        return ordem[0]
    else:
        return ordem[ordem.index(orientacao)+1]
    

def direita(orientacao):
    ordem = ['N', 'L', 'S', 'O']
    if ordem.index(orientacao) == 3:
        return ordem[0]
    else:
        return ordem[ordem.index(orientacao)+1]

def pode_andar(mapa, m, n, novoX, novoY):
    if novoX < 0 or novoY < 0 or novoX == n or novoY == m:
        return False
    if mapa[novoX][novoY] == '#':
        return False
    
    return True

n, m, s = map(int, input().split())

while n != 0:
    mapa = []
    ponto = [0, 0]
    orientacao = ''
    for i in range(n):
        linha = input()
        if 'N' in linha:
            orientacao = 'N'
            ponto = [i, linha.index('N')]
        elif 'S' in linha:
            orientacao = 'S'
            ponto = [i, linha.index('S')]
        elif 'L' in linha:
            orientacao = 'L'
            ponto = [i, linha.index('L')]
        elif 'O' in linha:
            orientacao = 'O'
            ponto = [i, linha.index('O')]

        mapa.append(linha)

    caminho = input()
    tot_cartas = 0
    
    for c in caminho:
        if c == 'E':
            orientacao = esquerda(orientacao)
        elif c == 'D':
            orientacao = direita(orientacao)
        else:
            if orientacao == 'N':
                if pode_andar(mapa, m, n, ponto[0]-1, ponto[1]):
                    ponto[0] -=1
            elif orientacao == 'S':
                if pode_andar(mapa, m, n, ponto[0]+1, ponto[1]):
                    ponto[0] +=1
            elif orientacao == 'O':
                if pode_andar(mapa, m, n, ponto[0], ponto[1]-1):
                    ponto[1] -=1
            else:
                if pode_andar(mapa, m, n, ponto[0], ponto[1]+1):
                    ponto[1] +=1
            if mapa[ponto[0]][ponto[1]] == '*':
                mapa[ponto[0]] = mapa[ponto[0]][:ponto[1]]+'.'+mapa[ponto[0]][ponto[1]+1:]
                tot_cartas +=1
            
    print(tot_cartas)
    n, m, s = map(int, input().split())

