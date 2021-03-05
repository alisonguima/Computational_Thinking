# Solicitação de dados ao usuário
qtdAulaSem = int (input("Digite a quantidade de aulas semanais: "))
valHrAula = float(input("Digite o valor da hora-aula: "))

# Calculo do salário base
salBase = qtdAulaSem * 4.5 * valHrAula

# Calculo do descanso semanal remunerado
dsr = salBase * 1/6

# Calculo da hora-atividade
hrAtiv = 5/100 * (salBase + dsr)

# Calculo do salario mensal
salMensal = salBase + dsr + hrAtiv

# Impressão dos calculos a cima
print("O salário base é de R$", salBase)
print("O descanso semanal remunerado é de R$", dsr)
print("A hora-atividade é de R$", hrAtiv)
print("O salário mensal é de R$", salMensal)