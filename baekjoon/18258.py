# https://www.acmicpc.net/problem/18258

# Queue2
# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여섯 가지이다.

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

import sys
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def push(self, x):
        self.queue.append(x)
    
    def pop(self):
        if self.queue:
            return self.queue.popleft()
        return -1
    
    def size(self):
        return len(self.queue)
    
    def empty(self):
        return 1 if not self.queue else 0
    
    def front(self):
        return self.queue[0] if self.queue else -1
    
    def back(self):
        return self.queue[-1] if self.queue else -1

def process_commands(commands):
    q = Queue()
    for command in commands:
        if command.startswith("push"):
            _, x = command.split()
            q.push(int(x))
        elif command == "pop":
            print(q.pop())
        elif command == "size":
            print(q.size())
        elif command == "empty":
            print(q.empty())
        elif command == "front":
            print(q.front())
        elif command == "back":
            print(q.back())

def main():
    input_lines = sys.stdin.readlines()
    commands = [line.strip() for line in input_lines[1:]] 
    process_commands(commands)

if __name__ == "__main__":
    main()


