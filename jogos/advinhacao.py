import random


def jogar():

    print('*********************************')
    print('Bem vindo ao jogo de adivinhacao!')
    print('*********************************')


    numero_secreto = random.randrange(1,100)
    total_de_tentativas = 0
    pontos = 1000

    print('Nível de dificuldade')
    print('(1) Fácil (2) Médio (3) Difícil')
    nivel = int(input('Digite o nível de dificuldade: '))

    if( nivel == 1):
        total_de_tentativas = 19
    elif( nivel == 2):
        total_de_tentativas = 9
    else:
        total_de_tentativas = 4

    for rodada in range(0, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada + 1, total_de_tentativas + 1))
        chute_str = input("Digite o seu número de 1 a 100: ")

        print("Voce digitou ", chute_str)
        chute = int(chute_str)
        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100')
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if acertou:
            print(f"você acertou, {pontos}")
            break
        else:
            if(maior):
                print(f"Você errou: Seu chute foi maior")
            elif(menor):
                print("Você errou: Seu chute foi menor")
            pontos_perdidos = int(abs(chute - numero_secreto))
            pontos = pontos - pontos_perdidos
        rodada += 1

    print('Fim de Jogo')

if(__name__ == '__main__'):
    jogar()