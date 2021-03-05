# Função que verifica se o ano é bissexto
def verificarMes( algum_mes, algum_ano ):
    ultimo_dia_do_mes = 0
    ano_bissexto = False

    if algum_ano % 4 == 0 and algum_ano % 100 == 0:
        if algum_ano % 400 == 0:
            ano_bissexto = True
        else:
            ano_bissexto = False
    elif algum_ano % 4 == 0:
        ano_bissexto = True

    if algum_mes == 4 or algum_mes == 6 or algum_mes == 9 or algum_mes == 11:
        ultimo_dia_do_mes = 30
    elif algum_mes == 2:
        if ano_bissexto == True:
            ultimo_dia_do_mes = 29
        else:
            ultimo_dia_do_mes = 28
    else:
        ultimo_dia_do_mes = 31
    
    return ultimo_dia_do_mes

# Função que verifica qual o menor dia
def menor_dia(diaA, mesA, anoA,diaB, mesB, anoB):
    dataA = diaA, mesA, anoA
    dataB = diaB, mesB, anoB

    if dataA[2] < dataB[2]:
        menor = dataA
    elif dataA[2] == dataB[2]:
        if dataA[1] < dataB[1]:
            menor = dataA
        elif dataA[1] == dataB[1]:
            if dataA[0] < dataB[0]:
                menor = dataA
            elif dataA[0] > dataB[0]:
                menor = dataB
            else:
                menor = 0
        else:
            menor = dataB
    else: 
        menor = dataB

    return menor


# Função que verifica qual o maior dia
def maior_dia(diaA, mesA, anoA,diaB, mesB, anoB):
    dataA = diaA, mesA, anoA
    dataB = diaB, mesB, anoB

    if dataA[2] > dataB[2]:
        maior = dataA
    elif dataA[2] == dataB[2]:
        if dataA[1] > dataB[1]:
            maior = dataA
        elif dataA[1] == dataB[1]:
            if dataA[0] > dataB[0]:
                maior = dataA
            elif dataA[0] < dataB[0]:
                maior = dataB
            else:
                maior = 0
        else:
            maior = dataB
    else: 
        maior = dataB

    return maior

# Exercício 1
def diaFuturo( dia, mes, ano, quantidade ):
    ultimo_dia = verificarMes( mes, ano )

    for contador in range( quantidade ):
        dia += 1 
        if dia == ultimo_dia:
            dia = 0
            mes += 1
            if mes == 13:
                mes = 1
                ano += 1
            ultimo_dia = verificarMes( mes, ano )

    return dia, mes, ano

# Exercício 2
def diaPassado( dia, mes, ano, quantidade):
    ultimo_dia = verificarMes(mes, ano)

    for contador in range( quantidade ):
        dia -= 1 
        if dia == 0:
            mes -= 1
            ultimo_dia = verificarMes( mes, ano )
            dia = ultimo_dia
            if mes == 0:
                mes = 12
                ano -= 1

    return dia, mes, ano

# Exercício 3
def calcula_dia(diaA, mesA, anoA, diaB, mesB, anoB):
    menor = menor_dia(diaA, mesA, anoA, diaB, mesB, anoB) 
    maior = maior_dia(diaA, mesA, anoA, diaB, mesB, anoB) 
    
    contador = 0

    if menor == maior:
        contador = 0
    else:

        dia = menor[0]
        mes = menor[1]
        ano = menor[2]

        ultimo_dia = verificarMes(menor[1], menor[2])

        while dia != maior[0] or mes != maior[1]  or ano != maior[2]:
            dia += 1
            contador += 1
            if dia > ultimo_dia:
                dia = 1
                mes += 1
                if mes == 13:
                    mes = 1
                    ano += 1 
                ultimo_dia = verificarMes(mes, ano)
            
    return contador


# Exercício 4
def conta_vogais(string):
    totalVogais = 0
    for palavra in string:
        for letra in palavra:
            if letra in 'AEIOU' or letra in 'aeiou':
                totalVogais += 1
    
    return totalVogais

# Exercício 5
def inverte(string):
    # armazena = ""
    # pos = -1
    # while -len(palavra) <= pos:
    #     armazena = armazena + palavra[pos]
    #     pos = pos - 1
    # return armazena
    
    return string[::-1]

# Teste Exercício 1
# dataFuturo = diaFuturo(5, 6, 2020, 2000)
# print(dataFuturo[0], '/', dataFuturo[1], '/', dataFuturo[2])

# Teste Exercício 2
# dataPassado = diaPassado(26, 5, 2020, 1850)
# print(dataPassado[0], '/', dataPassado[1], '/', dataPassado[2])

# Teste Exercício 3
# print(calcula_dia(23, 1, 1999, 10, 12, 2020), "dia(s).")

# Teste Exercício 4
# print("Total de vogais: ",conta_vogais("JabUtIcabA"))

# Teste Exercício 5
# print(inverte("Marrocos"))

# Alteração