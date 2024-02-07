# https://www.acmicpc.net/problem/6416

# 트리인가
# 문제
# 트리는 굉장히 잘 알려진 자료 구조이다. 트리를 만족하는 자료 구조는 비어 있거나(노드의 개수가 0개), 노드의 개수가 1개 이상이고 방향 간선이 존재하며 다음과 같은 조건을 만족해야 한다. 이때, 노드 u에서 노드 v로 가는 간선이 존재하면 간선을 u에 대해서는 '나가는 간선', v에 대해서는 '들어오는 간선'이라고 하자.

# 들어오는 간선이 하나도 없는 단 하나의 노드가 존재한다. 이를 루트(root) 노드라고 부른다.
# 루트 노드를 제외한 모든 노드는 반드시 단 하나의 들어오는 간선이 존재한다.
# 루트에서 다른 노드로 가는 경로는 반드시 가능하며, 유일하다. 이는 루트를 제외한 모든 노드에 성립해야 한다.
# 아래의 그림을 보자. 원은 노드, 화살표는 간선을 의미하며, 화살표의 방향이 노드 u에서 노드 v로 향하는 경우 이는 이 간선이 u에서 나가는 간선이며 v로 들어오는 간선이다. 3개의 그림 중 앞의 2개는 트리지만 뒤의 1개는 트리가 아니다.



# 당신은 간선의 정보들을 받아서 해당 케이스가 트리인지를 판별해야 한다.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있으며, 입력의 끝에는 두 개의 음의 정수가 주어진다.

# 각 테스트 케이스는 여러 개의 정수쌍으로 이루어져 있으며, 테스트 케이스의 끝에는 두 개의 0이 주어진다.

# 각 정수쌍 u, v에 대해서 이는 노드 u에서 노드 v로 가는 간선이 존재함을 의미한다. u와 v는 0보다 크다.

# 출력
# 각 테스트 케이스에 대해서, 테스트 케이스의 번호가 k일 때(k는 1부터 시작하며, 1씩 증가한다) 트리일 경우 "Case k is a tree."를, 트리가 아닐 경우 "Case k is not a tree."를 출력한다.

def is_tree(edges):
    if not edges:  # 간선이 없으면 트리로 간주
        return True
    nodes = set()
    in_degree = {}
    for u, v in edges:
        nodes.add(u)
        nodes.add(v)
        if v in in_degree:  # 노드 v에 두 개 이상의 들어오는 간선이 있으면 트리가 아님
            return False
        in_degree[v] = in_degree.get(v, 0) + 1

    root_nodes = nodes - set(in_degree.keys())
    if len(root_nodes) != 1:  # 루트 노드가 하나가 아니면 트리가 아님
        return False

    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for u, v in edges:
            if u == node:
                dfs(v)

    root_node = root_nodes.pop()
    dfs(root_node)

    return len(visited) == len(nodes)  # 모든 노드가 방문되었는지 확인

case_number = 1
edges = []
while True:
    try:
        line = input()
        if line == "-1 -1":  # 음의 정수 쌍을 입력받으면 프로그램 종료
            break
        pairs = map(int, line.split())
        for u, v in zip(pairs, pairs):
            if u == 0 and v == 0:  # 0 0을 입력받으면 하나의 테스트 케이스 종료
                if is_tree(edges):
                    print(f"Case {case_number} is a tree.")
                else:
                    print(f"Case {case_number} is not a tree.")
                case_number += 1
                edges = []  # 다음 테스트 케이스를 위해 edges 초기화
                continue
            edges.append((u, v))
    except EOFError:  # 입력이 끝나면 반복문 종료
        break