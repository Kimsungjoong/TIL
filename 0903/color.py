import sys
sys.stdin = open('test.txt', 'r')
T = int(input())
for tc in range(T):
    N = int(input())
    data = [[0 for i in range(10)]for _ in range(10)]
    cnt = 0
    cnt_1 = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        if color == 1:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    if data[i][j] == 0:
                        data[i][j] = 1
                    elif data[i][j] == 2:
                        data[i][j] = 3
                        cnt = cnt + 1
        else:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    if data[i][j] == 0:
                        data[i][j] = 2
                    elif data[i][j] == 1:
                        data[i][j] = 3
                        cnt_1 = cnt_1 + 1
    print("#{} {}".format(tc+1, cnt + cnt_1))