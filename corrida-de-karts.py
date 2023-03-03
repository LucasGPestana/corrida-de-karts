import random

tempos = dict()
media_corredores = dict()


def calcularMediaDeTempos(voltas_tempo):
    
    media_tempos = sum(voltas_tempo) / 10

    return media_tempos

def verificarMelhorVolta():

    # Não está funcionando

    for volta in range(0, 10, 1):
        for corredor in tempos.keys():
            for corredor2 in tempos.keys():
              if corredor != corredor2 and tempos[corredor][volta] < tempos[corredor2][volta]: 
                  menor_tempo = tempos[corredor][volta]
                  corredor_menor_tempo = corredor
                  volta_menor_tempo = volta + 1 

    return [volta_menor_tempo, corredor_menor_tempo, menor_tempo]

def verificarRanking():

    # Não está funcionando

    ranking = dict()            
    posicoes = list()           # Para evitar a sobrescrição de itens pela referência
    pos = 1                     

    for corredor in tempos.keys():
        ranking.fromkeys([pos, corredor], media_corredores[corredor])
        posicoes.append([pos, corredor, media_corredores[corredor]])
        pos += 1
    
    for pos, corredor, media in ranking.items():
      for pos2, corredor2, media2 in ranking.items():
        if corredor != corredor2 and pos > pos2 and media >= media2:
          posicoes[pos2] = [pos2 + 1, corredor, media] 
          posicoes[pos] = [pos + 1, corredor2, media2]

    return posicoes


for index in range(6):
    
    tempos_volta = list()
    
    nome_corredor = input("Digite o nome do corredor: ")

    for volta in range(10):
        
        # tempo_volta = float(input(f"Digite o tempo da volta {volta + 1}: "))
        tempo_volta = random.choice(range(1, 121))              # Para testes
        tempos_volta.append(tempo_volta)
    
    tempos[nome_corredor] = tempos_volta

for corredor in tempos.keys():           # Teste com o random
    print(corredor, " = ", tempos[corredor])

for corredor in tempos.keys():
    
    media_corredor = calcularMediaDeTempos(tempos[corredor])

    info_melhor_volta = verificarMelhorVolta()

    media_corredores[corredor] = media_corredor


for corredor in tempos.keys():              # Teste com o random
    
    print(corredor, " = ", media_corredores[corredor])

ranking = verificarRanking()

print("Ranking")

print(ranking)

print(f"Melhor Volta: {info_melhor_volta[1]}, feito na volta {info_melhor_volta[0]}, com {info_melhor_volta[2]}s")



