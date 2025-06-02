instancia = 1

while True:
    N, T = map(int, input().split())
    if N == 0:
        break

    brinquedos = []
    for _ in range(N):
        duracao, pontuacao = map(int, input().split())
        brinquedos.append((duracao, pontuacao))

    dp = [0] * (T + 1)

    for duracao, pontuacao in brinquedos:
        for t in range(T, duracao - 1, -1):
            dp[t] = max(dp[t], dp[t - duracao] + pontuacao)

    print(f"Instancia {instancia}")
    print(dp[T])
    print()
    instancia += 1
