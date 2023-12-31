def lomuto_partition(n, l, r):
    p = n[l]
    s = l
    for i in range(l + 1, r + 1):
        if n[i] < p:
            s += 1
            n[s], n[i] = n[i], n[s]

    n[l], n[s] = n[s], n[l]
    return s

n = [7, 2, 8, 14, 4, 12, 5]
print(lomuto_partition(n, 0, len(n) - 1))
