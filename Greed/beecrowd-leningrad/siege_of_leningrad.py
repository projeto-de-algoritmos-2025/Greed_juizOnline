import heapq
import math
import sys

def siege_of_leningrad():
    instancia = sys.stdin.read().strip().split('\n')
    idx = 0

    while idx < len(instancia):
        if not instancia[idx]:
            idx += 1
            continue

        parts = instancia[idx].split()
        if len(parts) < 4:
            break
        N, M, K = map(int, parts[:3])
        P = float(parts[3])
        idx += 1

        grafo = [[] for _ in range(N + 1)]
        for _ in range(M):
            u, v = map(int, instancia[idx].split())
            grafo[u].append(v)
            grafo[v].append(u)
            idx += 1

        sniper_data = list(map(int, instancia[idx].split()))
        A = sniper_data[0]
        snipers = [0] * (N + 1)
        for pos in sniper_data[1:]:
            snipers[pos] += 1
        idx += 1

        origem, destino = map(int, instancia[idx].split())
        idx += 1

        heap = [(snipers[origem], origem)]
        visited = [math.inf] * (N + 1)
        visited[origem] = snipers[origem]

        while heap:
            tiros, u = heapq.heappop(heap)
            if tiros > visited[u]:
                continue
            for v in grafo[u]:
                novo_tiros = tiros + snipers[v]
                if novo_tiros < visited[v]:
                    visited[v] = novo_tiros
                    heapq.heappush(heap, (novo_tiros, v))

        min_tiros = visited[destino]

        if min_tiros > K:
            print("0.000")
        else:
            prob = P ** min_tiros
            print("{:.3f}".format(prob))

siege_of_leningrad()
