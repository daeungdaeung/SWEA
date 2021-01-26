# -*- coding: utf-8 -*-
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
answer = list(range(1, 10))
for test_case in range(1, T + 1):
    possible = True
    sdocu = []
    for i in range(9):
        sdocu.append(list(map(int, input().split())))
    # horizontal 방향으로 스도쿠가 성립하는지 확인
    for row in sdocu:
        if sorted(row) != answer: # 스도쿠 미 성립시 for 문 종료
            possible = False
            break
    if not possible: # 스도쿠가 성립하지 않았을 경우 다음 단계로
        print('#{} {}'.format(test_case, 0))
        continue
    # vertical 방향으로 스도쿠가 성립하는지 확인
    for col in range(9):
        tmp = []
        for row in range(9):
            tmp.append(sdocu[row][col])
        if sorted(tmp) != answer:
            possible = False
            break
    if not possible:
        print('#{} {}'.format(test_case, 0))
        continue
    # square 안에서 스도쿠가 성립하는지 확인
    # (0, 0), (0, 3), ... (6, 6) -> 기준점을 잡음
    for row_ref in range(0, 9, 3):
        for col_ref in range(0, 9, 3):
            # 기준점 설정이 완료되면 기준점을 중심으로 square 안에 9개의
            # 숫자를 보고 스도쿠가 성립하는지 판별하면됨
            square_elem_list = []
            for i in range(0, 3):
                for j in range(0, 3):
                    square_elem_list.append(sdocu[row_ref+i][col_ref+j])
            if sorted(square_elem_list) != answer:
                possible = False
                break
        if possible == False:
            break
    if not possible:
        print('#{} {}'.format(test_case, 0))
    else:
        print('#{} {}'.format(test_case, 1))
                    
