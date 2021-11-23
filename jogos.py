
import forca
import jogoadivinhacaofor


print("***********************************************")
print("*************ESCOLHA O SEU JOGO!***************")
print("***********************************************")

print("(1) JOGO DA FORCA (2) JOGO DA ADIVINHAÇÃO")

jogo = int(input("Qual jogo você quer jogar?: "))

if(jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando adivinhação")
    jogoadivinhacaofor.jogar()