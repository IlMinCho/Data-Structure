# https://www.acmicpc.net/problem/21942

# 부품대여장
# 문제
# 송훈이는 로봇 동아리 회원이다. 로봇 동아리에서 필요한 부품이 있을 경우 자유롭게 빌려서 쓰고 다시 돌려놓으면 된다.

# 하지만 부품 정리를 하다가 부품 관리가 너무 힘들어져 새로운 시스템을 도입하려고 한다.

# 부품을 빌려갈 경우 부품 대여장에 정보를 반드시 작성해야한다. 또한 빌려간 부품을 반납 할 경우에도 부품 대여장에 정보를 작성해야한다.

# 또한 대여기간을 정하고 대여기간을 넘길 경우 1분당 벌금을 부여하도록 하는 시스템이다.

# 만약 대여기간이 5분, 1분당 벌금이 5원이라 했을 때 대여한 시각이 2021년 1월 1일 1시 5분이라면 2021년 1월 1일 1시 10분까지 반납해야한다.

# 2021년 1월 1일 1시 14분에 반납을 했다면 4분 늦었기 때문에 벌금을 20원을 내야한다.

# 부품 대여장에 쓰는 형식은 아래와 같다.

# yyyy-MM-dd hh:mm [부품 이름] [동아리 회원 닉네임]
# 아래는 예시를 위한 부품 대여장에 작성된 정보이다. 대여기간이 5분, 벌금은 1원이라 가정하자.

# 2021-01-01 09:12 arduino tony9402
# 2021-01-01 09:13 monitor chansol
# 2021-01-01 09:18 arduino tony9402
# 2021-01-01 09:18 monitor chansol
# 위의 정보를 정리하면 아래와 같다.

# tony9402가 2021년 1월 1일 오전 9시 12분에 arduino를 빌렸다.
# chansol이 2021년 1월 1일 오전 9시 13분에 monitor를 빌렸다.
# tony9402가 2021년 1월 1일 오전 9시 18분에 arduino를 반납했다.
# chansol이 2021년 1월 1일 오전 9시 18분에 monitor를 반납했다.
# tony9402는 1분 늦게 반납했기 때문에 벌금 1원을 내야한다.

# 부품을 대여할 때 지켜야 하는 조건이 있다.

# 한 사람이 같은 종류의 부품을 두개 이상 대여하고 있는 상태일 수 없다.
# 한 사람이 같은 시각에 서로 다른 종류의 부품들을 대여하는 것이 가능하다.
# 같은 사람이더라도, 대여 기간은 부품마다 별도로 적용된다.
# 입력
# 첫 번째 줄에 부품 대여장에 작성된 정보의 개수 
# $N$, 대여기간 
# $L$, 벌금 
# $F$이 공백으로 구분되어 주어진다.

# 대여기간 형식은 DDD/hh:mm으로 DDD는 일, hh는 시간, mm은 분을 의미한다. (000/00:00 는 주어지지 않는다.)

# 두 번째 줄부터 
# $N + 1$번째 줄까지 시간순으로 부품 대여장에 작성한 정보 (시각, 부품 이름 
# $P$, 회원 닉네임 
# $M$)이 공백으로 구분되어 주어진다.

# 빌린 시각의 형식은 yyyy-MM-dd hh:mm으로 yyyy는 연도, MM는 월, dd는 일, hh는 시간, mm는 분을 의미한다. 이 문제에서 들어오는 연도는 항상 2021년도이다.

# 부품 이름 
# $P$는 알파벳 소문자로만 이루어져 있다. 즉, 부품 이름에 공백이 없다.

# 회원 닉네임 
# $M$은 알파벳 소문자와 숫자
# $(0$ ~ 
# $9)$로만 이루어져있다. 즉, 회원 닉네임에 공백이 없다.

# 출력
# 벌금을 내야하는 사람들을 사전순으로 동아리 회원 닉네임 
# $M$와 내야하는 벌금을 한 줄씩 출력한다.

# 만약 벌금을 내야하는 사람들이 없는 경우는 -1을 출력한다.

# 제한
#  
# $2 \le N \le 80,000$, 
# $N$은 짝수
#  
# $0 \le DDD \le 200$ 
#  
# $1 \le MM \le 12$ 
#  
# $0 \le hh \le 23$ 
#  
# $0 \le mm \le 59$ 
#  
# $1 \le F \le 4,000$ 
#  
# $5 \le |P|, |M| \le 20$ 
# 부품을 반납하지 않은 사람은 없다.

import sys

# def input():
#     return sys.stdin.readline().rstrip()

def calculate_days_per_month():
    month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days = [0]
    for month, day in month_days.items():
        days.append(days[-1] + day)
    return days

def change_str(_str, month_days):
    date, time, item, person = _str.split()
    _, month, day = map(int, date.split('-')) # 연도는 처리하지 않습니다.
    hour, minute = map(int, time.split(':'))
    # 월과 일을 기반으로 한 총 분을 계산합니다.
    return person, item, (month_days[month-1] + day - 1) * 24 * 60 + hour * 60 + minute

def solution(info, deadline_time, F):
    dic = {}
    people = {} # 벌금을 내야 하는 사람들을 추적합니다.
    month_days = calculate_days_per_month()
    for data in info:
        person, item, time = change_str(data, month_days)
        if person not in dic:
            dic[person] = {}
        if item in dic[person]:
            # 반납 시간에서 대여 시간을 뺍니다.
            result = time - dic[person].pop(item)
            if result > deadline_time:
                if person not in people:
                    people[person] = 0
                people[person] += (result - deadline_time) * F
        else:
            dic[person][item] = time # 새로운 대여를 기록합니다.
    
    if people:
        for person in sorted(people.keys()):
            print(f'{person} {people[person]}')
    else:
        print(-1)

def main():
    N, L, F = input().split()
    N, F = int(N), int(F)
    day, time = L.split('/')
    day = int(day)
    hour, minute = map(int, time.split(':'))
    deadline_time = day * 24 * 60 + hour * 60 + minute # 대여 기간을 분으로 환산합니다.
    info = [input() for _ in range(N)] # 대여 정보를 입력받습니다.
    
    solution(info, deadline_time, F)

if __name__ == "__main__":
    main()