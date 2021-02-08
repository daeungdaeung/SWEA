T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    all_set = {str(i) for i in range(0, 10)}
    my_set = set()
    cnt = 0
    idx = 1
    while all_set != my_set:
        # 숫자를 문자로 바꿔서 비교
        my_set = my_set | set(str(N*idx))
        idx += 1
        cnt += 1
    print('#{} {}'.format(test_case, cnt*N))
