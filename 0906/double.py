import sys
sys.stdin = open('test.txt', 'r')
T = int(input())
for tc in range(T):
    P, Pa, Pb = map(int,input().split())
    end_A, key_A, start_A = P, Pa, 1
    cnt = 0
    while start_A <= end_A:
        cnt = cnt + 1
        middle_A = (start_A + end_A) // 2
        if middle_A == key_A:
            break
        elif middle_A > key_A:
            end_A = middle_A
        else:
            start_A = middle_A
    end_B, key_B, start_B = P, Pb, 1
    cnt_B = 0
    while start_B <= end_B:
        cnt_B = cnt_B + 1
        middle_B = (start_B + end_B) // 2
        if middle_B == key_B:
            break
        elif middle_B > key_B:
            end_B = middle_B
        else:
            start_B = middle_B

    if cnt > cnt_B:
        cnt = 'B'
    elif cnt < cnt_B:
        cnt = 'A'
    else:
        cnt = 0
    print("#{} {}".format(tc+1,cnt))
