import sys
sys.stdin = open('test.txt', 'r')
T = int(input())
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(arr)
a = []
for i in range(1 << n):
    line = []
    for j in range(n + 1):
        if i & (1 << j):
            line.append(arr[j])
    a.append(line)
for tc in range(T):
    N, K = map(int, input().split())
    cnt = 0
    for k in range(len(a)):
        sum_1 = 0

        if len(a[k]) == N:
            for l in range(len(a[k])):
                sum_1 = sum_1 + a[k][l]
            if sum_1 == K:
                cnt = cnt + 1
    print("#{} {}".format(tc + 1, cnt))