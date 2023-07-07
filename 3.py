n, m, q = [int(el) for el in input().split()]
lab = []
for i in range(n):
    a = input().split()
    lab.append([int(el) for el in a])
for i in range(q):
    x, y, k = [int(el) for el in input().split()]
    ch = lab[x - 1][y - 1]
    ans = 0
    for j in range(len(lab[x - 1])):
        if abs(lab[x - 1][j] - ch) <= k and j != y - 1:
            ans += 1
    for j in range(n):
        if abs(lab[j][y - 1] - ch) <= k and j != x - 1:
            ans += 1
    print(ans)
