# https://www.acmicpc.net/problem/14425

# 문자열 집합
# 문제
# 총 N개의 문자열로 이루어진 집합 S가 주어진다.

# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다. 

# 다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.

# 다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.

# 입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.

# 출력
# 첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.

import sys

def process_strings():
    # 집합 S를 생성하고 초기화합니다.
    S = set()

    # 문자열의 개수 N과 M을 입력 받습니다.
    N, M = map(int, sys.stdin.readline().split())

    # 집합 S에 포함되어 있는 문자열들을 입력 받아서 집합에 저장합니다.
    for _ in range(N):
        string = sys.stdin.readline().strip()
        S.add(string)

    # 검사해야 하는 문자열들을 입력 받아서 집합 S에 포함되어 있는지 확인하고 개수를 세줍니다.
    count = 0
    for _ in range(M):
        string_to_check = sys.stdin.readline().strip()
        if string_to_check in S:
            count += 1

    # 결과를 출력합니다.
    print(count)

if __name__ == "__main__":
    process_strings()


# def count_strings_in_set(N, M, set_strings, check_strings):
#     # 집합 S에 문자열 저장
#     S = set(set_strings)

#     # S에 포함된 문자열 수 세기
#     count = 0
#     for string in check_strings:
#         if string in S:
#             count += 1

#     return count

# def main():
#     # N과 M 입력받기
#     N, M = map(int, input().split())

#     # 집합 S에 포함될 문자열들 입력받기
#     set_strings = [input() for i in range(N)]

#     # 검사할 문자열들 입력받기
#     check_strings = [input() for i in range(M)]

#     # 결과 출력
#     result = count_strings_in_set(N, M, set_strings, check_strings)
#     print(f"{result}")

# if __name__ == "__main__":
#     main()
    
# def main():
#     # N과 M 입력받기
#     N, M = map(int, input().split())

#     # 집합 S에 포함될 문자열들 입력받기
#     S = set()
#     for _ in range(N):
#         S.add(input())

#     # 검사할 문자열들 입력받고, 집합 S에 포함된 문자열 수 세기
#     count = 0
#     for _ in range(M):
#         if input() in S:
#             count += 1

#     # 결과 출력
#     print(count)

# if __name__ == "__main__":
#     main()