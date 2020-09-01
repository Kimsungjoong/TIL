import sys
sys.stdin = open('test.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = int(input())
    c = [0] * 12
    for i in range(N):
        c[num % 10] += 1
        num = num // 10
    max_card = 0
    max_num = 0
    for i in range(len(c)-1, -1, -1):
        if c[i] > max_card:
            max_card = c[i]
            max_num = i
    print("#{} {} {}".format(tc, max_num, max_card))