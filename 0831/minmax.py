import sys
sys.stdin = open('test.txt', 'r')
T = int(input())
for tc in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = A[-1] - A[0]
    print("#{} {}".format(tc+1, B))
