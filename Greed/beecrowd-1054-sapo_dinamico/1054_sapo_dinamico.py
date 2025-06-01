def can_cross(stones, D, max_jump):
    stones = [('B', 0)] + sorted(stones, key=lambda x: x[1]) + [('B', D)]
    positions = [s[1] for s in stones]
    types = [s[0] for s in stones]
    n = len(stones)
    used = [False] * n

    # Ida
    i = 0
    while i < n - 1:
        best = -1
        for j in range(i + 1, n):
            if positions[j] - positions[i] > max_jump:
                break
            best = j
        if best == -1:
            return False
        if types[best] == 'S':
            used[best] = True
        i = best

    # Volta
    i = n - 1
    while i > 0:
        best = -1
        for j in range(i - 1, -1, -1):
            if positions[i] - positions[j] > max_jump:
                break
            if types[j] == 'S' and used[j]:
                continue
            best = j
            break
        if best == -1:
            return False
        if types[best] == 'S':
            used[best] = True
        i = best

    return i == 0

def binary_search(stones, D):
    low, high = 1, D
    result = D
    while low <= high:
        mid = (low + high) // 2
        if can_cross(stones, D, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

def main():
    T = int(input())
    for case_num in range(1, T + 1):
        N, D = map(int, input().split())
        stones = []
        parts = input().split()
        for part in parts:
            kind, dist = part.split('-', 1)
            stones.append((kind, int(dist)))
        answer = binary_search(stones, D)
        print(f"Case {case_num}: {answer}")

if __name__ == "__main__":
    main()
