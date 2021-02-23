# -*- coding: utf-8 -*-
T = int(input())
# 이 문제는 곱셈과 나눗셈의 순서를 잘 지켜야 한다...
# 인터넷상에서 한창 떠돌던 문제 -> 8/2*4의 정답이 1 과 16으로 나뉘던 문제이다.
# 비슷한 맥락을 가지고 있는 문
for test_case in range(1, T + 1):
    D, L, N = map(int, input().split())
    damage = int(D*N + D*L*N*(N-1)/200)

    print('#{} {}'.format(test_case, damage))
