T = int(input())
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
for test_case in range(1, T + 1):
    s = input()
    all_bit = ''
    origin_s = ''
    for char in s:
        # 해당 문자의 2진수 값을 구하는 과정
        bi = bin(alpha.find(char))[2:]
        bi = (6-len(bi))*'0' + bi
        # 바이너리 변환 후 24bit로 변환
        all_bit += bi
    # 총 3개의 문자 이므로 3번 반복문 사용
    num_char = int(len(all_bit) / 8)
    for i in range(num_char):
        # 8bit binary to decimal
        decimal = int('0b' + all_bit[8*i:8*(i+1)], 2)
        # decimal to ascii 
        origin_char = chr(decimal)
        origin_s += origin_char
    print('#{} {}'.format(test_case, origin_s))