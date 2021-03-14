# itertools의 combination을 이용할거냐...
# 조합 함수 구현으로...
def comb(n, r):
    for i in range(len(n)):
        if r == 1:
            yield [n[i]]
        else:
            for nex in comb(n[i+1:], r-1):
                yield [n[i]] + nex

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    R = N // 2
    synergy = [list(map(int, input().split())) for _ in range(N)]

    n = list(range(N))
    # b_material 구하기
    a_materials = list(comb(n, R))
    b_materials = []
    for a_tmp in a_materials:
        tmp = n[:]
        for elem in a_tmp:
            tmp.remove(elem)
        b_materials.append(tmp)

    min_v = 1e+10
    # synergy 계산
    for i in range(len(a_materials)):
        a_synergy = list(comb(a_materials[i], 2))  # 2개씩 뽑아서 시너지를 구해야한다.
        b_synergy = list(comb(b_materials[i], 2))
        a_flavor = 0
        b_flavor = 0
        # 각 재료들을 가지고 맛 구하기
        for j in range(len(a_synergy)):
            a_flavor += synergy[a_synergy[j][0]][a_synergy[j][1]] + synergy[a_synergy[j][1]][a_synergy[j][0]]
            b_flavor += synergy[b_synergy[j][0]][b_synergy[j][1]] + synergy[b_synergy[j][1]][b_synergy[j][0]]

        if abs(a_flavor - b_flavor) < min_v:
            min_v = abs(a_flavor - b_flavor)

    print('#{} {}'.format(tc, min_v))