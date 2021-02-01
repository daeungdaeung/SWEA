# -*- coding: utf-8 -*-
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    number_arr = [] # 입력을 받는 리스트
    result = [] # 출력할 때 사용할 리스트
    for i in range(N):
        number_arr.append(input().split())
    # 90도, 180도, 270도 회전
    # 회전후 생성된 것을 또 90도 회전하면 된다.
    # 270도 까지니까 반복문 3번은 고정이다.
    # 기존 배열에 회전된 배열을 집어넣으면 반복문으로 해결 가능!
    for i in range(3):
        rotate_number_arr = []
        for col in range(N):
            new_row = [] # 회전된 한 행을 받기위한 리스트
            for row in range(N-1, -1, -1): # 역으로 받아와야 회전된 형태를 취할 수 있음
                new_row.append(number_arr[row][col])
            rotate_number_arr.append(new_row)
        result.append(rotate_number_arr)
        # shallow copy 안하면, rotate_number_arr처럼 계속 바뀔듯...
        # 귀찮아서 실험은 안해볼건데, 예측은
        # 아래 코드 실행후 다시 첫줄로 가서 rotate_number_arr = []이다.
        # 따라서 number_arr도 []를 가리키게 될 것... (아마도)
        number_arr = rotate_number_arr[:]
    # 여기서부터는 리스트에 담긴 숫자들을 출력형식에 맞게 만들기 위해서
    # 리스트를 문자열로 바꿀거다. ex) ['7', '4', '1'] -> '741'
    # in place로 변경
    for i in range(3):
        for j in range(N):
            result[i][j] = ''.join(result[i][j])
    # 출력 형식에 맞게 출력 하자
    print('#{}'.format(test_case))
    for i in range(N):
        print('{} {} {}'.format(result[0][i], result[1][i], result[2][i]))
    
