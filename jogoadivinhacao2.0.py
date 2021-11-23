import random

def jogar():

    N = random.randrange(1,101)
    total_tentativas = 0

    for rodada in range(1, total_tentativas + 1):
        print("tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite um número entre 1 e 100!: ")
        print("Você digitou o número:", chute_str)
        chute = int(chute_str)  # convertendo um valor de str para int

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        maior = chute > N
        menor = chute < N
        acertou = chute == N

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior!")
            elif (menor):
                print("Você errou! O seu chute foi menor!")
            pontos_perdidos = abs(N - chute)
            pontos = pontos - pontos_perdidos

    if (rodada == total_tentativas):
        print("O número secreto era: {}".format(N))
    print("Fim de Jogo")




