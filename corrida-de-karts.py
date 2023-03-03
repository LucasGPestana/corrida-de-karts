import random

tempos = dict()
media_corredores = dict()
info_melhor_volta_pessoal = dict()

def calcularMediaDeTempos(voltas_tempo):
    
    media_tempos = sum(voltas_tempo) / 10

    return media_tempos

def verificarMelhorVoltaPessoal(corredor):

    # Não está funcionando

    voltas = sorted(tempos_volta, key=tempos_volta.get)
    
    print(f"A melhor volta de {corredor} foi na {voltas[0]}, com {tempos_volta[voltas[0]]}s")

def verificarRanking():    

    pos = 1             

    corredores = sorted(media_corredores, key=media_corredores.get, reverse=False)

    print("RANKING")
    
    for corredor in corredores:
        print(f"{pos}. {corredor} - {media_corredores[corredor]}")
        pos += 1

for index in range(6):
    
    tempos_volta = dict()
    
    nome_corredor = input("Digite o nome do corredor: ")

    for volta in range(1, 11, 1):
        
        # tempo_volta = float(input(f"Digite o tempo, em segundos, da volta {volta}: "))
        tempo_volta = random.choice(range(1, 121))              # Para testes
        tempos_volta[volta] = tempo_volta
    
    tempos[nome_corredor] = tempos_volta

    media_corredor = calcularMediaDeTempos(tempos_volta.values())

    media_corredores[nome_corredor] = media_corredor

    verificarMelhorVoltaPessoal(nome_corredor)

# for corredor in tempos.keys():           # Teste com o random
    # print(corredor, " = ", tempos[corredor])

# for corredor in tempos.keys():              # Teste com o random
    
    # print(corredor, " = ", media_corredores[corredor])

verificarRanking()



