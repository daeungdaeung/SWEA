T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    print('#{}'.format(test_case))
    N = int(input())
    # i 가 N의 크기를 반복문으로
    for i in range(1, N+1):
        if i == 1:
            cur_row = [1]
            print(' '.join(list(map(str, cur_row))))
            pre_row = cur_row
            cur_row = []
            continue
        for j in range(i):
            # 첫번째
            if j == 0:
                cur_row.append(1)
            elif j == i-1:
                cur_row.append(1)
            else:
                # 가장 중요한 부분
                cur_row.append(pre_row[j-1] + pre_row[j])
        # 가장 중요한 돌리려면 pre_row => 바로 전 row
        pre_row = cur_row
        print(' '.join(list(map(str, cur_row))))
        cur_row = []

    # ///////////////////////////////////////////////////////////////////////////////////