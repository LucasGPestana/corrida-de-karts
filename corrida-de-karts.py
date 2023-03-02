import random

tempos = dict()
info_corredores = list()

def calcularMediaDeTempos(voltas_tempo):
    
    media_tempos = sum(voltas_tempo) / 10

    return media_tempos

def verificarMelhorVolta():

    for volta in range(1, 11, 1):
        for corredor in tempos:
            for corredor2 in tempos:
              if corredor != corredor2 and tempos[corredor] < tempos[corredor2]: 
                  menor_tempo = tempos[corredor]
                  corredor_menor_tempo = nome_corredor
                  volta_menor_tempo = volta

    return [volta_menor_tempo, corredor_menor_tempo, menor_tempo]

def verificarRanking():
    
    ranking = []
    
    for pos in range(6):
         ranking.append(f"{pos + 1}.{info_corredores[pos][0]} - {info_corredores[pos][1]}")
    
    print(ranking)

    for pos in range(6):
        for pos2 in range(6):
                if pos != pos2 and pos > pos2 and info_corredores[pos][1] <= info_corredores[pos2][1]:
                            ranking[pos] = f"{pos2 + 1}.{info_corredores[pos][0]} - {info_corredores[pos][1]}"
                            ranking[pos2] = f"{pos + 1}.{info_corredores[pos2][0]} - {info_corredores[pos2][1]}"
    
    return ranking


for index in range(6):
    
    tempos_volta = list()
    
    nome_corredor = input("Digite o nome do corredor: ")

    for volta in range(10):
        
        # tempo_volta = float(input(f"Digite o tempo da volta {volta + 1}: "))
        tempo_volta = random.choice(range(1, 121))
        tempos_volta.append(tempo_volta)
    
    tempos[nome_corredor] = tempos_volta

for corredor in tempos:
    print(corredor, " = ", tempos[corredor])

for corredor in tempos:
    
    media_corredor = calcularMediaDeTempos(tempos[corredor])

    info_melhor_volta = verificarMelhorVolta()

    info_corredores.append([corredor,media_corredor])


for pos in range(6):
    
    print(info_corredores[pos][0], " = ", info_corredores[pos][1])

ranking = verificarRanking()

print("Ranking")

print(ranking)

print(f"Melhor Volta: {info_melhor_volta[1]}, feito na volta {info_melhor_volta[0]}, com {info_melhor_volta[2]}s")





