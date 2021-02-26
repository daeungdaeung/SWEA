def f(p, q):
    len_p = len(p)
    len_q = len(q)
    # 두 단어의 길이가 같은 경우
    if len_p == len_q:
        # 아예 똑같지 않는한 둘 사이에는 무조건 다른 단어가 존재한다.
        return 'Y'
    # 두 단어의 길이가 다른 경우
    # 1. p가 더 긴 경우
    elif len_p > len_q:
        # 이 경우는 무조건 둘 사이에 다른 단어가 존재
        # ex) aa, b 사이에는 ab, ac, ..., az, aaa, ... 등이 올 수 있다.
        return 'Y'
    # 2. q가 더 긴 경
    else:
        # 길이 차이가 2 이상일때
        if len_q - len_p > 1:
            return 'Y'
        # 길이 차이가 1 일때
        else:
            for i in range(len_p):
                if p[i] != q[i]:
                    return 'Y'
            else:
                if q[i+1] != 'a':
                    return 'Y'
                else:
                    return 'N'


T = int(input())
for tc in range(1, T+1):
    p = input().strip()
    q = input().strip()

    print('#{} {}'.format(tc, f(p, q)))