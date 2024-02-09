# https://www.acmicpc.net/problem/1991

# 트리순회
# 문제
# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.


# 예를 들어 위와 같은 이진 트리가 입력되면,

# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
# 가 된다.

# 입력
# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

# 출력
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(nodes, val, left, right):
    if val not in nodes:
        nodes[val] = Node(val)
    if left != '.':
        nodes[val].left = Node(left)
        nodes[left] = nodes[val].left
    if right != '.':
        nodes[val].right = Node(right)
        nodes[right] = nodes[val].right
    return nodes

def preorder(node, path=[]):
    if node:
        path.append(node.val)
        preorder(node.left, path)
        preorder(node.right, path)
    return path

def inorder(node, path=[]):
    if node:
        inorder(node.left, path)
        path.append(node.val)
        inorder(node.right, path)
    return path

def postorder(node, path=[]):
    if node:
        postorder(node.left, path)
        postorder(node.right, path)
        path.append(node.val)
    return path

def main():
    N = int(input())
    nodes = {}

    for _ in range(N):
        val, left, right = input().split()
        nodes = insert(nodes, val, left, right)

    root = nodes['A']  # 루트 노드는 항상 'A'
    preorder_result = preorder(root, [])
    inorder_result = inorder(root, [])
    postorder_result = postorder(root, [])

    print("".join(preorder_result))
    print("".join(inorder_result))
    print("".join(postorder_result))

if __name__ == "__main__":
    main()
