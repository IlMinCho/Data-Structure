# https://www.acmicpc.net/problem/21944

# 문제 추천 시스템 version2
# 문제
# tony9402는 최근 깃헙에 코딩테스트 대비 문제를 직접 뽑아서 "문제 번호, 난이도, 알고리즘 분류"로 정리해놨다.

# 깃헙을 이용하여 공부하시는 분들을 위해 새로운 기능을 추가해보려고 한다.

# 만들려고 하는 명령어는 총 3가지가 있다. 아래 표는 각 명령어에 대한 설명이다.

# recommend 
# $G$ 
# $x$ 	
#  
# $x$가 1인 경우 추천 문제 리스트에서 알고리즘 분류가 
# $G$인 문제 중 가장 어려운 문제 번호를 출력한다.

# 조건을 만족하는 문제가 여러 개라면 그 중 문제 번호가 큰 것으로 출력한다.

#  
# $x$가 -1인 경우 추천 문제 리스트에서 알고리즘 분류가 
# $G$인 문제 중 가장 쉬운 문제 번호를 출력한다.

# 조건을 만족하는 문제가 여러 개라면 그 중 문제 번호가 작은 것으로 출력한다.

# 해당 명령어는 해당 그룹 
# $G$에 문제 번호가 한 개 이상이 있을 경우에만 주어진다.

# recommend2 
# $x$ 	
#  
# $x$가 1인 경우 추천 문제 리스트에서 알고리즘 분류 상관없이 가장 어려운 문제 번호를 출력한다.

# 조건을 만족하는 문제가 여러 개라면 그 중 문제 번호가 큰 것으로 출력한다.

#  
# $x$가 -1인 경우 추천 문제 리스트에서 알고리즘 분류 상관없이 가장 쉬운 문제 번호를 출력한다.

# 조건을 만족하는 문제가 여러 개라면 그 중 문제 번호가 작은 것으로 출력한다.

# recommend3 
# $x$ 
# $L$ 	
#  
# $x$가 1인 경우 추천 문제 리스트에서 알고리즘 분류 상관없이 난이도 
# $L$보다 크거나 같은 문제 중 가장 쉬운 문제 번호를 출력한다.

# 조건을 만족하는 문제가 여러 개라면 그 중 문제 번호가 작은 것으로 출력한다. 만약 조건을 만족하는 문제 번호가 없다면 -1을 출력한다.

#  
# $x$가 -1인 경우 추천 문제 리스트에서 알고리즘 분류 상관없이 난이도 
# $L$보다 작은 문제 중 가장 어려운 문제 번호를 출력한다.

# 조건을 만족하는 문제가 여러 개라면 그 중 문제 번호가 큰 것으로 출력한다. 만약 조건을 만족하는 문제 번호가 없다면 -1을 출력한다.

# add 
# $P$ 
# $L$ 
# $G$ 	추천 문제 리스트에 난이도가 
# $L$이고 알고리즘 분류가 
# $G$인 문제 번호 
# $P$를 추가한다. (추천 문제 리스트에 없는 문제 번호 
# $P$만 입력으로 주어진다. 이전에 추천 문제 리스트에 있던 문제 번호가 다른 난이도와 다른 알고리즘 분류로 다시 들어 올 수 있다.)
# solved 
# $P$ 	추천 문제 리스트에서 문제 번호 
# $P$를 제거한다. (추천 문제 리스트에 있는 문제 번호 
# $P$만 입력으로 주어진다.)
# 명령어 recommend, recommend2, recommend3는 추천 문제 리스트에 문제가 하나 이상 있을 때만 주어진다.

# 명령어 solved는 추천 문제 리스트에 문제 번호가 하나 이상 있을 때만 주어진다.

# 위 명령어들을 수행하는 추천 시스템을 만들어보자.

# 입력
# 첫 번째 줄에 추천 문제 리스트에 있는 문제의 개수 
# $N$가 주어진다.

# 두 번째 줄부터 
# $N + 1$ 줄까지 문제 번호 
# $P$와 난이도 
# $L$, 알고리즘 분류 
# $G$가 공백으로 구분되어 주어진다.

#  
# $N + 2$줄은 입력될 명령문의 개수 
# $M$이 주어진다.

# 그 다음줄부터 
# $M$개의 위에서 설명한 명령문이 입력된다.

# 출력
# recommend, recommend2, recommend3 명령이 주어질 때마다 문제 번호를 한 줄씩 출력한다. 주어지는 recommend, recommend2, recommend3 명령어의 총 개수는 최소 1개 이상이다.

# 제한
#  
# $1 \le N, P \le 100,000$ 
#  
# $1 \le M \le 10,000$ 
#  
# $1 \le L, G \le 100$, 
# $L$와 
# $G$은 자연수
#  
# $x = \pm 1$ 

import sys
import heapq
 
from collections import defaultdict
input = sys.stdin.readline
class Algorithm():
    def __init__(self,num):
        self.num = num
        self.min_heap = []
        self.max_heap = []
    def insert(self,pb_num,diff):
        heapq.heappush(self.min_heap,(diff,pb_num))
        heapq.heappush(self.max_heap,(-diff,-pb_num))
    def find_heap(self,flag):
        result = []
        if flag > 0:
            if self.max_heap:
                while (-self.max_heap[0][1] not in number_set) or number_algo[-self.max_heap[0][1]][0] != self.num or number_algo[-self.max_heap[0][1]][1] != -self.max_heap[0][0]:
                    heapq.heappop(self.max_heap)
                    if not self.max_heap:
                        break
            if self.max_heap:
                result = [-self.max_heap[0][0],-self.max_heap[0][1]]
        else:
            if self.min_heap:
                while (self.min_heap[0][1] not in number_set) or number_algo[self.min_heap[0][1]][0] != self.num or number_algo[self.min_heap[0][1]][1] != self.min_heap[0][0]:
                    heapq.heappop(self.min_heap)
                    if not self.min_heap:
                        break
            if self.min_heap:
                result = self.min_heap[0]
        return result
 
 
class Difficulty():
    def __init__(self,num):
        self.num = num
        self.min_heap = []
        self.max_heap = []
 
    def insert(self,pb_num):
        heapq.heappush(self.min_heap,pb_num)
        heapq.heappush(self.max_heap,-pb_num)
    def find_heap(self,x):
        result = []
        if x > 0:
            if self.min_heap:
                while self.min_heap[0] not in number_set or (number_algo[self.min_heap[0]][1]) != self.num:
                    heapq.heappop(self.min_heap)
                    if not self.min_heap:
                        break
            if self.min_heap:
                result = self.min_heap[0]
 
        else:
            if self.max_heap:
                while -self.max_heap[0] not in number_set or (number_algo[-self.max_heap[0]][1]) != self.num:
                    heapq.heappop(self.max_heap)
                    if not self.max_heap:
                        break
            if self.max_heap:
                result = -self.max_heap[0]
        return result
 
 
N = int(input())
algo_set = set()
diff_set = set()
algo_dict = {}
diff_dict = {}
number_algo = {}
number_set = set()
for _ in range(N):
    number,dif,algo = map(int,input().split())
    if algo not in algo_set:
        algo_dict[algo] = Algorithm(algo)
        algo_set.add(algo)
    if dif not in diff_set:
        diff_dict[dif] = Difficulty(dif)
        diff_set.add(dif)
    algo_dict[algo].insert(number,dif)
    diff_dict[dif].insert(number)
    number_algo[number] = [algo,dif]
    number_set.add(number)
 
 
M = int(input())
 
for i in range(M):
    command,*arg = input().split()
    if command == 'recommend':
        G,x = map(int,arg)
        print(algo_dict[G].find_heap(x)[1])
    elif command == 'recommend2':
        x = int(arg[0])
        diff_check = 0 if x == 1 else float('inf')
        pb_num_check = -1
        for algo_num in algo_dict:
            ch = algo_dict[algo_num].find_heap(x)
            if not ch: continue
            if x == 1:
                if ch[0] >diff_check:
                    diff_check = ch[0]
                    pb_num_check = ch[1]
                elif ch[0] == diff_check:
                    if pb_num_check < ch[1]:
                        pb_num_check = ch[1]
            else:
                if ch[0] < diff_check:
                    diff_check = ch[0]
                    pb_num_check = ch[1]
                elif ch[0] == diff_check:
                    if pb_num_check > ch[1]:
                        pb_num_check = ch[1]
        print(pb_num_check)
    elif command == 'recommend3':
        flag,L_num = map(int,arg)
        result = -1
        if flag == -1:
            L_num = L_num + flag
        while 0<=L_num<=100:
            if L_num in diff_set:
                ch = diff_dict[L_num].find_heap(flag)
                if not ch:
                    L_num = L_num + flag
                    continue
                result = ch
                print(ch)
                break
            L_num = L_num + flag
        if result == -1:
            print(-1)
 
    elif command == 'solved':
        pb_num = int(arg[0])
        number_set.remove(pb_num)
        del number_algo[pb_num]
    else:
        pb_num,diff_num,algo_num = map(int,arg)
        if algo_num not in algo_set:
            algo_dict[algo_num] = Algorithm(algo_num)
            algo_set.add(algo_num)
        if diff_num not in diff_set:
            diff_dict[diff_num] = Difficulty(diff_num)
            diff_set.add(diff_num)
        algo_dict[algo_num].insert(pb_num,diff_num)
        diff_dict[diff_num].insert(pb_num)
        number_algo[pb_num] = [algo_num,diff_num]
        number_set.add(pb_num)