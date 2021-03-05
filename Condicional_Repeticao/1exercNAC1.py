# Solicitacao de dados para o usuario
n1 = int(input("Digite a quantidade total de camisetas e polos vendidas: "))
n2 = int(input("Digite a quantidade total de calças e camisas vendidas: "))
n3 = int(input("Digite a quantidade total de jaquetas e agasalhos vendidas: "))
n4 = int(input("Digite a quantidade total de ternos e sobretudos vendidos: "))

# Salario fixo do vendedor
salFixo = 500

# Salario variavel do vendedor
priCat = n1 * (4 / 100 * salFixo)
segCat = n2 * (5.5 / 100 * salFixo)
terCat = n3 * (7 / 100 * salFixo)
quaCat = n4 * (8.5 / 100 * salFixo)

# Valor total do salario do vendedor
salFinal = salFixo + priCat + segCat + terCat + quaCat

# Imprimindo o salario do vendedor
print("O salario do vendedor foi de R$", salFinal)