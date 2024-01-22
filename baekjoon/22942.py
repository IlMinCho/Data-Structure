# https://www.acmicpc.net/problem/22942

# 데이터 체커
# 문제
# 원 이동하기 2 문제를 만들고 만든 데이터가 문제의 조건에 맞는지 확인하는 코드를 작성해야한다.

# 해당 문제의 데이터는 아래 조건들을 만족해야한다.

# 모든 원의 중심 좌표는 
# $x$축 위에 존재해야 한다.
#  
# $N$개의 원 중 임의의 두 원을 선택했을 때, 교점이 존재하지 않아야 한다. 즉, 하나의 원이 다른 원 안에 존재하거나 외부에 존재한다.
# 데이터 형식은 원의 개수 
# $N$이랑 각 원의 중심 
# $x$좌표, 원의 반지름 
# $r$만 주어진다. 따라서, 2번 조건을 만족하는지만 확인하면 된다.

# 주어진 데이터가 해당 조건을 만족하는지 확인해보자.

# 입력
# 첫 번째 줄에는 원의 개수 
# $N$이 주어진다.

# 두 번째 줄부터 
# $N+1$번째 줄까지 원의 중심 
# $x$좌표, 원의 반지름 
# $r$이 공백으로 구분되어 주어진다.

# 출력
# 데이터가 조건에 맞는다면 YES, 조건에 만족하지 않는다면 NO를 출력한다.

# 제한
#  
# $2 ≤ N ≤ 200,000$ 
#  
# $-1,000,000 ≤ x ≤ 1,000,000$ 
#  
# $1 ≤ r ≤ 10,000$ 
#  
# $x, r$은 정수
import sys

def check_circle(x1, r1, x2, r2):
    d = abs(x1 - x2)
    if d > r1 + r2:
        return "OUT"
    elif d < abs(r1 - r2):
        return "IN"
    else:
        return "NO"

def process_circles(N, circles):
    stack1 = []
    stack2 = []
    checker = ''
    
    for circle1 in circles:
        if checker == "NO":
            continue
        if not stack1:
            stack1.append(circle1)
        else:
            while stack1:
                circle2 = stack1.pop()
                checker = check_circle(circle1[0], circle1[1], circle2[0], circle2[1])
                if checker == "OUT":
                    stack2.append(circle2)
                elif checker == "IN":
                    if circle1[1] > circle2[1]:
                        stack2.append(circle1)
                    else:
                        stack2.append(circle2)
                else:
                    break
            if checker != "NO":
                while stack2:
                    stack1.append(stack2.pop())
    
    return checker if checker == "NO" else "YES"

def main():
    N = int(sys.stdin.readline())
    circles = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(process_circles(N, circles))

if __name__ == "__main__":
    main()