import sys
sys.stdin = open('test.txt', 'r')
T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    data = list(map(int,input().split()))
    line = []
    for i in range(len(data)-M+1):
        A = 0
        for j in range(M):
            A = A + data[i+j]
        line.append(A)
    line.sort()
    print("#{} {}".format(tc+1, line[-1]-line[0]))