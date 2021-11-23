print("**********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("**********************************")

numero_secreto = 43
total_de_tentativas = 3
rodada = 1

#Laço de repetição
while(rodada <= total_de_tentativas): #Condição de entrada
    print("tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número: ")
    print("Você digitou o número:", chute_str)
    chute = int(chute_str) #convertendo um valor de str para int

    # variáveis booleanas = True ou False
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto


    if (acertou):
        print("Você acertou o número secreto!")
    else:
        if(maior):
            print("Você errou! O número digitado é maior que o número secreto!")
        elif (menor):
            print("Você errou! O número digitado é menor que o número secreto!")

    rodada = rodada + 1

print("Fim de Jogo")