def dfs(month, all):
    global money
    if month >= 13:
        money = min(all, money)
        return


    pay_mon = prices[1]
    pay_day = prices[0] * plan[month]
    if pay_mon > pay_day:  # 한달 요금 vs 하루 요금
        need = pay_day
    else:
        need = pay_mon

    dfs(month+1, all+need)
    dfs(month+3, all+prices[2])


T = int(input())

for tc in range(1, T+1):
    prices = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))

    money = 1e+10
    dfs(1, 0)
    if money < prices[3]:
        result = money
    else:
        result = prices[3]

    print('#{} {}'.format(tc, result))