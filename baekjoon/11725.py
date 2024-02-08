# https://www.acmicpc.net/problem/11725

# 트리의 부모찾기
# 문제
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
from collections import defaultdict, deque
import sys

# sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 늘림

# def dfs(current_node, parent):
#     # 현재 노드의 부모 노드를 기록
#     parent_node[current_node] = parent
#     for next_node in tree[current_node]:
#         if next_node != parent:  # 방문하지 않은 노드인 경우 탐색
#             dfs(next_node, current_node)

# N = int(input())  # 노드의 개수 입력
# tree = defaultdict(list)  # 각 노드의 연결 상태를 저장할 딕셔너리
# parent_node = [0] * (N + 1)  # 각 노드의 부모 노드 번호를 저장할 리스트

# # 트리 구성
# for _ in range(N - 1):
#     a, b = map(int, input().split())
#     tree[a].append(b)
#     tree[b].append(a)

# dfs(1, 0)  # 루트 노드부터 탐색 시작

# # 부모 노드 출력
# for i in range(2, N + 1):
#     print(parent_node[i])

input = sys.stdin.readline

N = int(input())
tree = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 각 노드의 부모 노드를 저장할 리스트
parent_node = [0] * (N + 1)

def bfs():
    queue = deque([1])  # 루트 노드부터 시작
    while queue:
        current_node = queue.popleft()
        for next_node in tree[current_node]:
            if parent_node[next_node] == 0:  # 아직 방문하지 않은 노드인 경우
                parent_node[next_node] = current_node  # 현재 노드를 부모로 설정
                queue.append(next_node)

bfs()  # BFS 실행

# 부모 노드 출력
for i in range(2, N + 1):
    print(parent_node[i])
