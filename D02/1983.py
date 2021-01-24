# -*- coding: utf-8 -*-
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, k = list(map(int, input().split()))
    score_k = 0 # k 번째 학생 점수 -> 전체 학생들 점수 정렬 후 k 번째 학생 점수 찾을 때 활용하려고 저장
    all_scores = []
    for student in range(N):
        scores = list(map(int, input().split()))
        all_scores.append(scores[0]*0.35 + scores[1]*0.4 + scores[2]*0.2)
        if student == k-1:
            score_k = scores[0]*0.35 + scores[1]*0.4 + scores[2]*0.2
    sorted_all_scores = sorted(all_scores)
    k_idx = sorted_all_scores.index(score_k)
    if k_idx/N >= 0.9:
        grade = 'A+'
    elif k_idx/N >= 0.8:
        grade = 'A0'
    elif k_idx/N >= 0.7:
        grade = 'A-'
    elif k_idx/N >= 0.6:
        grade = 'B+'
    elif k_idx/N >= 0.5:
        grade = 'B0'
    elif k_idx/N >= 0.4:
        grade = 'B-'
    elif k_idx/N >= 0.3:
        grade = 'C+'
    elif k_idx/N >= 0.2:
        grade = 'C0'
    elif k_idx/N >= 0.1:
        grade = 'C-'
    else:
        grade = 'D0'
    print('#{} {}'.format(test_case, grade))
    # ///////////////////////////////////////////////////////////////////////////////////