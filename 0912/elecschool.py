T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    data = list(map(int, input().split()))
    # k는 한번에 갈 수 있는 거리, N은 버스 정류장 갯수, M은 충전기 갯수
    start = 0
    cnt = 0
    end = start + K
    while end < N and end != start:
        if end in data:
            start = end
            end = start + K
            cnt += 1
        elif end not in data:
            end -= 1
    if end == start:
        cnt = 0
    print("#{} {}".format(tc, cnt))