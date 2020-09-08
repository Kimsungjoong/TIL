T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int,input().split()))
    data.sort()
    A = []
    for i in range(5):
        A.append(data[-1])
        A.append((data[0]))
        data.pop()
        data.pop(0)
    print("#{}".format(tc+1), *A)