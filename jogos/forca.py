

def jogar():
    print('***************************')
    print('Bem vindo ao jogo da forca!')
    print('***************************')

    palavra_secreta = 'banana'.lower()
    enforcou = False
    advinhou = False

    erros = 0

    letras_acertadas = ['_' for letras in palavra_secreta]
    print(*letras_acertadas)

    while(not enforcou and not advinhou):
        letra_buscada = input('Insira uma letra: ').strip().lower()
        index = 0
        if letra_buscada in palavra_secreta:
            for letra in palavra_secreta:
                if letra == letra_buscada:
                    print(f'encontrei a letra {letra_buscada} na posicao {index}')
                    letras_acertadas[index] = letra.lower()
                index += 1
            print(*letras_acertadas)
        else:
            erros += 1

        enforcou = erros >= 6
        advinhou = '_' not in letras_acertadas

    print('Você acertou!') if advinhou else print('Você foi enforcado')

if(__name__ == '__main__'):
    jogar()