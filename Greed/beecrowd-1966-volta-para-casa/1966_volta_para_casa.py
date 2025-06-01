def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    B = int(data[1])

    volumes = list(map(int, data[2:2+N]))
    prices = list(map(int, data[2+N:]))

    # lista de tuplas (preço/volume, volume, preço)
    items = sorted([(prices[i] / volumes[i], volumes[i], prices[i]) for i in range(N)])

    total_volume = 0
    for pv_ratio, v, p in items:
        if B >= p:
            total_volume += v
            B -= p
        else:
            # compra fração proporcional
            total_volume += v * (B / p)
            B = 0
            break

    # agora determinar a maior base possível
    # queremos o maior k tal que 1 + 2 + ... + k = k*(k+1)//2 <= total_volume
    # resolução por busca binária
    left, right = 0, int(2e5)
    best_k = 0
    while left <= right:
        mid = (left + right) // 2
        needed = mid * (mid + 1) // 2
        if needed <= total_volume:
            best_k = mid
            left = mid + 1
        else:
            right = mid - 1

    print(best_k)

main()
