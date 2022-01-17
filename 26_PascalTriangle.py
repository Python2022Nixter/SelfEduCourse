N = 7
P = []

for i in range(N):
    P.append([])
    for j in range(i + 1):
        if j == 0 or j == i:
            P[i].append(1)
        else:
            P[i].append(P[i - 1][j - 1] + P[i - 1][j])

for i in P:
    p = "  " * (N - len(i))
    print(f"{p}{i}")