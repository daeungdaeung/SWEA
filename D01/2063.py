T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
sorted_list = sorted(list(map(int, input().split(' '))))
print(sorted_list[len(sorted_list)//2])