# https://www.acmicpc.net/problem/21939

# 문제 추천 시스템 Version 1

# 문제
# tony9402는 최근 깃헙에 코딩테스트 대비 문제를 직접 뽑아서 "문제 번호, 난이도"로 정리해놨다.

# 깃헙을 이용하여 공부하시는 분들을 위해 새로운 기능을 추가해보려고 한다.

# 만들려고 하는 명령어는 총 3가지가 있다. 아래 표는 각 명령어에 대한 설명이다.

# recommend 
# $x$ 	
#  
# $x$가 1인 경우 추천 문제 리스트에서 가장 어려운 문제의 번호를 출력한다.

# 만약 가장 어려운 문제가 여러 개라면 문제 번호가 큰 것으로 출력한다.

#  
# $x$가 -1인 경우 추천 문제 리스트에서 가장 쉬운 문제의 번호를 출력한다.

# 만약 가장 쉬운 문제가 여러 개라면 문제 번호가 작은 것으로 출력한다.

# add 
# $P$ 
# $L$ 	추천 문제 리스트에 난이도가 
# $L$인 문제 번호 
# $P$를 추가한다. (추천 문제 리스트에 없는 문제 번호 
# $P$만 입력으로 주어진다. 이전에 추천 문제 리스트에 있던 문제 번호가 다른 난이도로 다시 들어 올 수 있다.)
# solved 
# $P$ 	추천 문제 리스트에서 문제 번호 
# $P$를 제거한다. (추천 문제 리스트에 있는 문제 번호 
# $P$만 입력으로 주어진다.)
# 명령어 recommend는 추천 문제 리스트에 문제가 하나 이상 있을 때만 주어진다.

# 명령어 solved는 추천 문제 리스트에 문제 번호가 하나 이상 있을 때만 주어진다.

# 위 명령어들을 수행하는 추천 시스템을 만들어보자.

# 입력
# 첫 번째 줄에 추천 문제 리스트에 있는 문제의 개수 
# $N$ 가 주어진다.

# 두 번째 줄부터 
# $N + 1$ 줄까지 문제 번호 
# $P$와 난이도 
# $L$가 공백으로 구분되어 주어진다.

#  
# $N + 2$줄은 입력될 명령문의 개수 
# $M$이 주어진다.

# 그 다음줄부터 
# $M$개의 위에서 설명한 명령문이 입력된다.

# 출력
# recommend 명령이 주어질 때마다 문제 번호를 한 줄씩 출력한다. 최소 한번의 recommend 명령어가 들어온다.

# 제한
# $1 \le N, P \le 100,000$  
# $1 \le M \le 10,000$ 
# $1 \le L \le 100$, 
# $L$은 자연수
# $x = \pm 1$ 
import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

N = int(input())
mx_heap = []
mn_heap = []
sol = {}

for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(mx_heap, (-L, -P))
    heapq.heappush(mn_heap, (L, P))
    sol[P] = True

M = int(input())
for _ in range(M):
    op = input().split()

    if op[0] == 'recommend':
        x = int(op[1])
        if x == 1:
            while not sol[-mx_heap[0][1]]: heapq.heappop(mx_heap)
            print(-mx_heap[0][1])
        else :
            while not sol[mn_heap[0][1]]: heapq.heappop(mn_heap)
            print(mn_heap[0][1])
    elif op[0] == 'add':
        P, L = int(op[1]), int(op[2])
        while not sol[-mx_heap[0][1]]: heapq.heappop(mx_heap)
        while not sol[mn_heap[0][1]]: heapq.heappop(mn_heap)

        sol[P] = True
        heapq.heappush(mx_heap, (-L, -P))
        heapq.heappush(mn_heap, (L, P))
    else : # solved
        P = int(op[1])
        sol[P] = False