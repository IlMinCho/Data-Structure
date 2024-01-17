# https://www.acmicpc.net/problem/2504

# 괄호의 값
# 문제
# 4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열이란 다음과 같이 정의된다.

# 한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다.
# 만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다.
# X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.
# 예를 들어 ‘(()[[]])’나 ‘(())[][]’ 는 올바른 괄호열이지만 ‘([)]’ 나 ‘(()()[]’ 은 모두 올바른 괄호열이 아니다. 우리는 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다.

# ‘()’ 인 괄호열의 값은 2이다.
# ‘[]’ 인 괄호열의 값은 3이다.
# ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
# ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
# 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
# 예를 들어 ‘(()[[]])([])’ 의 괄호값을 구해보자. ‘()[[]]’ 의 괄호값이 2 + 3×3=11 이므로 ‘(()[[]])’의 괄호값은 2×11=22 이다. 그리고 ‘([])’의 값은 2×3=6 이므로 전체 괄호열의 값은 22 + 6 = 28 이다.

# 여러분이 풀어야 할 문제는 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력하는 것이다.

# 입력
# 첫째 줄에 괄호열을 나타내는 문자열(스트링)이 주어진다. 단 그 길이는 1 이상, 30 이하이다.

# 출력
# 첫째 줄에 그 괄호열의 값을 나타내는 정수를 출력한다. 만일 입력이 올바르지 못한 괄호열이면 반드시 0을 출력해야 한다.

def calculate_bracket_value(bracket_string):
    stack = []
    for char in bracket_string:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if not stack:
                return 0  # 스택이 비어있으면 올바르지 않은 괄호열

            temp = 0
            while stack and isinstance(stack[-1], int):
                temp += stack.pop()
            
            if stack and ((char == ')' and stack[-1] == '(') or (char == ']' and stack[-1] == '[')):
                stack.pop()  # 여는 괄호 제거
                value = 2 if char == ')' else 3
                stack.append(value if temp == 0 else temp * value)
            else:
                return 0  # 여는 괄호와 닫는 괄호의 짝이 맞지 않음

    if any(isinstance(item, str) for item in stack):
        return 0  # 올바르지 않은 괄호열
    return sum(stack)

def main():
    bracket_string = input()
    print(calculate_bracket_value(bracket_string))

if __name__ == "__main__":
    main()