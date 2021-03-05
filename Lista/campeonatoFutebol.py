import random

#       [ NOME , JOGOS , VITORIAS, PONTOS , GOLS ]
def criarTimes( lista_nomes ):
    tabela = [
        [ "", 0, 0, 0, 0 ],
        [ "", 0, 0, 0, 0 ],
        [ "", 0, 0, 0, 0 ],
        [ "", 0, 0, 0, 0 ],
        [ "", 0, 0, 0, 0 ],
        [ "", 0, 0, 0, 0 ],
        [ "", 0, 0, 0, 0 ],
        [ "", 0, 0, 0, 0 ],
        [ "", 0, 0, 0, 0 ],
        [ "", 0, 0, 0, 0 ]
    ]

    for numero in range(10):
        tabela[numero][0] = lista_nomes[numero]

    return tabela


# Imprime todos os times do campeonato
def imprime( times ):
    print( "|     NOMES     | JOGOS | VITORIAS | PONTOS | GOLS |" )
    for time in times:
        print(f'| {time[0].center(13)} | {str(time[1]).center(5)} | {str(time[2]).center(8)} | {str(time[3]).center(6)} | {str(time[4]).center(4)} |')


# Cria uma partida entre 2 times
def partida( timeA, timeB, times ):
    partida = [
        [      timeA[0]       ,        timeB[0]      ],
        [ random.randint(0, 4), random.randint(0, 4) ]
    ]

    if ( partida[1][0] > partida[1][1] ):
        # adicionar vitoria +1 e pontos +3
        timeA[2] += 1
        timeA[3] += 3
    elif ( partida[1][0] < partida[1][1] ):
        # adicionar vitoria +1 e pontos +3
        timeB[2] += 1
        timeB[3] += 3
    else:
        # se der empate pontos +1
        timeA[3] += 1
        timeB[3] += 1
    
    timeA[4] += partida[1][0]
    timeB[4] += partida[1][1]
    timeA[1] += 1
    timeB[1] += 1

    # Para cada time na lista de times do campeonato
    for time in times:
        if ( time[0] == timeA[0] ):
            time = timeA
        elif ( time[0] == timeB[0] ):
            time = timeB


def ganhador(times):
    maior_pontos = 0
    ganhadores = []

    for time in times:
        if (time[3] > maior_pontos):
            maior_pontos = time[3]
            ganhadores = []
            ganhadores.append( time[0] )
        elif( time[3] == maior_pontos ):
            ganhadores.append( time[0] )

    if ( len(ganhadores) > 1 ):
        vitorias = 0
        ganhadores = []
        for time in times:
            if (time[2] > vitorias):
                vitorias = time[2]
                ganhadores = []
                ganhadores.append( time[0] )
            elif( time[2] == vitorias ):
                ganhadores.append( time[0] )

    if ( len(ganhadores) > 1 ):
        gols = 0
        ganhadores = []
        for time in times:
            if (time[4] > gols):
                gols = time[4]
                ganhadores = []
                ganhadores.append( time[0] )
            elif( time[4] == gols ):
                ganhadores.append( time[0] )

    if ( len(ganhadores) == 1):
        print( f'Ganhador do Campeonato: {ganhadores[0]}' )
    else:
        print("Ganhadores do Campeonato:")
        for time in ganhadores:
            print(time)


times = criarTimes([ 
    "SaoPaulo",
    "Palmeiras",
    "Santos",
    "Corinthians",
    "Grêmio",
    "Internacional",
    "Flamengo",
    "Vasco",
    "Fluminense",
    "Botafogo"
])

# Campeonato
for time in times:
    for oponente in times:
        if ( time[0] != oponente[0] ):
            partida( time, oponente, times )

imprime( times )

ganhador( times )