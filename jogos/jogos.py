import forca
import advinhacao

def jogar():
    print('***************************')
    print('******Escolha o jogo*******')
    print('***************************')
    jogo = int(input('(1) Adivinhacao (2) Forca: '))

    if(jogo == 1):
        advinhacao.jogar()
    else:
        forca.jogar()

if(__name__ == '__main__'):
    jogar()