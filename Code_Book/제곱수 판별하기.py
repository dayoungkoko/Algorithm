def solution(n) :
    return 1 if (n**0.5).is_integer() else 2

'''
programmers 코딩테스트 입문 lv.0 제곱수 판별하기
제곱수라면 1을 아니라면 2를 return

풀이 : 
math.sqrt() 대신 0.5승을 사용할 수도 있다.
is_integer()을 통해 정수면 True, 아니라면 False를 반환
참고로 12.0도 float형이어도 True를 반환한다

ex :
n = 144
result = 1

n = 976
result = 2
'''
