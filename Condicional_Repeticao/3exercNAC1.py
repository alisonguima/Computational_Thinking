# Solicitando ao usuário dois números inteiros positivos e fazendo a validação
numA = int(input("Digite um número inteiro positivo: "))
while(numA <= 0):
    numA = int(input("Erro! Digite um número inteiro positivo: "))

numB = int(input("Digite outro número inteiro positivo: "))
while(numB <= 0):
    numB = int(input("Erro! Digite um número inteiro positivo: "))

# Verificando qual é o maior número entre numA e numB
if(numA > numB):
    maior = numA
else:
    maior = numB

# Calculando o menor múltiplo comum entre numA e numB
while (maior % numA != 0 or maior % numB != 0):
    maior = maior + 1

# Imprimindo o menor múltiplo comum entre numA e numB
print("O menor múltiplo comum é ", maior)