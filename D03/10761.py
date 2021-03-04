import collections

T = int(input())
for tc in range(1, T+1):
    tmp = list(input().split())
    N = int(tmp[0])
    data = tmp[1:]

    A_data = collections.deque([])  # 모든 데이터를 저장 -> Blue 또는 Orange가 버튼을 누르는 순서
    B_data = collections.deque([])  # Blue가 눌러야하는 버튼 저장
    O_data = collections.deque([])  # Orange가 눌러야하는 버튼 저장

    for i in range(0, N*2, 2):
        if data[i] == 'B':
            B_data.append(int(data[i+1]))
        else:
            O_data.append(int(data[i+1]))
        A_data.append((data[i], data[i+1]))

    B_position = 1
    O_position = 1
    B_idx = 0
    O_idx = 0
    A_idx = 0
    len_B_data = len(B_data)
    len_O_data = len(O_data)
    len_A_data = len(A_data)
    time = 0
    # 전체 데이터를 순회하였으면, while문 종료
    while A_idx < len_A_data:
        # while문이 한번 도는 것은 단위시간이 지남을 의미
        # 버튼을 누르면 bt가 True
        bt = False
        # B_idx가 B_data 크기를 벗어나면 아무것도 실행하지 않음
        if B_idx < len_B_data:
            # B의 위치(B_position)가 눌러야하는 버튼 위치보다 작은 경우 -> +1
            if B_data[B_idx] - B_position > 0:
                B_position += 1
            elif B_data[B_idx] - B_position < 0:
                B_position -= 1
            else:  # B의 위치가 눌러야하는 버튼 위치일 경우
                # 현재 Blue가 버튼을 눌러야하는 차례라면
                if A_data[A_idx][0] == 'B':
                    # 버튼을 누르면 다음에 어떤 버튼을 눌러야하는지 알아야한다.
                    # 버튼을 눌렀음을 알려주는 bt
                    bt = True
                    # 블루 차례이므로 Blue가 버튼을 누르고 다음에 눌러야 하는 버튼 idx로 이동
                    B_idx += 1
                # Blue가 버튼을 누르는 차례가 아니라면 아무것도 수행 X
        if O_idx < len_O_data:
            if O_data[O_idx] > O_position:
                O_position += 1
            elif O_data[O_idx] < O_position:
                O_position -= 1
            else:
                if A_data[A_idx][0] == 'O':
                    bt = True
                    O_idx += 1
        if bt:
            A_idx += 1
        time += 1

    print('#{} {}'.format(tc, time))
