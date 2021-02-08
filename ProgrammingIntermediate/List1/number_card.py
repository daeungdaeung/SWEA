T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num_card = int(input())
    numbers = list(map(int, list(input())))
    # 카드에 적힌 숫자의 출현 횟수를 저장
    counts = [0] * 10

    for num in numbers:
        counts[num] += 1

    max_val = -1e+10
    val = -1
    for idx, num in enumerate(counts):
        # 기존 숫자의 출현횟수보다 크거나 같은 경우
        # 이경우에 크거나 같다고 했으므로
        # 출현횟수가 같은 경우, 더 큰 숫자가 저장된다.
        if max_val <= num:
            max_val = num
            val = idx

    print('#{} {} {}'.format(test_case, val, max_val))