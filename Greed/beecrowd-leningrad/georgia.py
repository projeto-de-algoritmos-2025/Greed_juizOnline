def resolve_missao(armas, vida_total, limite_balas):
    dp = [0] * (limite_balas + 1)  # dp[i] = máximo dano com i balas

    for balas, poder in armas:
        dano_total = balas * poder
        # Percorre de trás para frente (0/1 knapsack)
        for b in range(limite_balas, balas - 1, -1):
            dp[b] = max(dp[b], dp[b - balas] + dano_total)

    return max(dp) >= vida_total


def main():
    while True:
        try:
            entrada = input().strip()
            if not entrada:
                continue
            QA = int(entrada)
            if QA == 0:
                break

            armas = []
            for _ in range(QA):
                balas, poder = map(int, input().split())
                armas.append((balas, poder))

            QM = int(input())
            vida_total = 0
            for _ in range(QM):
                nome, qtd = input().split()
                qtd = int(qtd)
                if nome == "Ganados":
                    vida_total += qtd * 50
                elif nome == "Colmillos":
                    vida_total += qtd * 60
                elif nome == "Zealot":
                    vida_total += qtd * 75
                elif nome == "Garrador":
                    vida_total += qtd * 100
                elif nome == "LasPlagas":
                    vida_total += qtd * 120
                elif nome == "Regenerador":
                    vida_total += qtd * 150
                elif nome == "ElGigante":
                    vida_total += qtd * 200
                elif nome == "Dr.Salvador":
                    vida_total += qtd * 250

            QB = int(input())

            if resolve_missao(armas, vida_total, QB):
                print("Missao completada com sucesso")
            else:
                print("You Are Dead")

        except EOFError:
            break

# Executa
main()
