palavras = input().lower().split()
while(palavras[0] != '*'):
    letra = palavras[0][0]
    if all([letra==pal[0] for pal in palavras]):
        print('Y')
    else:
        print('N')
    
    palavras = input().lower().split()