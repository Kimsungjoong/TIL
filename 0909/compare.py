T = int(input())
for tc in range(T):
    p = input()
    t = input()
    M = len(p)
    N = len(t)

    def BruteForce(p, t):
        i = 0
        j = 0
        while j < M and i < N:
            if t[i] != p[j]:
                i = i - j
                j = -1
            i = i + 1
            j = j + 1
        if j == M :
            return 1
        else:
            return 0
    print("#{} {}".format(tc+1, BruteForce(p, t)))