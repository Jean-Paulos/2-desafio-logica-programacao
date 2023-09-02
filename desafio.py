
import random

def saldoVitoria (vitoria, derrota):
    winRate = vitoria - derrota
    return winRate

winRate = saldoVitoria(random.randint(1, 101), random.randint(1, 101))

def avaliadorDeRank(winRate):
    if winRate < 10:
        rank = "Ferro"
        return rank
    elif winRate >= 11 and winRate <= 20:
        rank = "Bronze"
        return rank
    elif winRate >= 21 and winRate <= 50:
        rank = "Prata"
        return rank
    elif winRate >= 51 and winRate <= 80:
        rank = "Ouro"
        return rank
    elif winRate >= 81 and winRate <= 90:
        rank = "Diamante"
        return rank
    elif winRate >= 91 and winRate <= 100:
        rank = "Lendário"
        return rank
    elif winRate >= 101:
        rank = "Imortal"
        return rank

rank = avaliadorDeRank(winRate)

print(f"O Herói tem saldo de {winRate} está no nível de {rank}")
