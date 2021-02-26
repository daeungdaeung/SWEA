T = int(input())
for tc in range(1, T+1):
    s = input().strip()

    dic = {
        'p': 'q',
        'q': 'p',
        'b': 'd',
        'd': 'b',
    }

    result = ''
    for i in range(len(s)-1, -1, -1):
        result += dic[s[i]]

    print('#{} {}'.format(tc, result))