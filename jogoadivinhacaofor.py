import random

def jogar():

    print("**********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("**********************************")


    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Díficil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1) :
        total_tentativas = 30
    elif (nivel == 2):
        total_tentativas = 15
    else:
        total_tentativas = 10


    for rodada in range(1, total_tentativas + 1):
        print("tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite um número entre 1 e 100!: ")
        print("Você digitou o número:", chute_str)
        chute = int(chute_str)  # convertendo um valor de str para int

        if(chute < 1 or chute > 101):
            print("Você deve digitar um número entre 1 e 150!")
            continue
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        acertou = chute == numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior!")
            elif (menor):
                print("Você errou! O seu chute foi menor!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    if (rodada == total_tentativas):
        print("O número secreto era: {}".format(numero_secreto))
    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar()
