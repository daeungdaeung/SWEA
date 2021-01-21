T = int(input())

for i in range(T):

    summation = 0
    for num in list(map(int, input().split(' '))):
        if num % 2:
            summation += num

    print('#{} {}'.format(i+1, summation))