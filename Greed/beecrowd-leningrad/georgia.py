def gergovia():
    while True:
        n = int(input())  # Lê o número de casas (moradores)
        if n == 0:        # Condição de parada
            break
        a = list(map(int, input().split()))  # Lista de compras (+) e vendas (-) de vinho
        trabalho = 0  # Total de esforço de transporte
        saldo = 0     # Saldo acumulado de vinho até o momento
        for i in range(n):
            saldo += a[i]              # Atualiza o saldo com a casa atual
            trabalho += abs(saldo)    # Adiciona o esforço necessário para equilibrar o saldo
        print(trabalho)  # Exibe o total de trabalho necessário para a instância

# Executa a função
gergovia()
