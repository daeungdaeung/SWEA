T = int(input())
for tc in range(1, T+1):
    s = input().strip()
    dic = {}
    for char in s:
        dic[char] = dic.get(char, 0) + 1

    s_list = []
    for k, v in dic.items():
        if v % 2:
            s_list.append(k)
    if s_list:
        s_list.sort()
        result = ''.join(s_list)
    else:
        result = 'Good'
    print('#{} {}'.format(tc, result))