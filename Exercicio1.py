#Faça um programa que peça uma nota, entre zero e dez. 
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

num = float(input("Entre com um número de 0 até 10, será que você acerta?:"))

while num > 10:
    print ("Você errou:")
    print ("tente novamente")
    num = float(input("Entre com um número de 0 até 10, será que você acerta?:"))
print ("Acertou")
