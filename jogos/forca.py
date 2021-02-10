

def jogar():
    print('***************************')
    print('Bem vindo ao jogo da forca!')
    print('***************************')

    palavra_secreta = 'banana'
    enforcou = False
    advinhou = False

    while(not enforcou and not advinhou):
        print('jogando')
        letra_buscada = input('Insira uma letra')
        for letra in palavra_secreta:
            if(letra.lower() == letra_buscada.lower()):
                print(f'encontrei a letra {letra_buscada}')

if(__name__ == '__main__'):
    jogar()